"""
   qradarzoldaxlib.py

   Description: This library provides functionalities to interact with the QRadar API.
   It offers tools for reading configuration files, preparing headers, making GET and PUT requests,
   and fetching application IDs.

   Copyright 2023 Pascal Weber (zoldax) / Abakus Sécurité

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""


import requests
import json
import urllib3
import logging
import os
from typing import Union
from typing import Optional

# Constants for Default Configuration Values
DEFAULT_VERSION = "15.0"
DEFAULT_ACCEPT = "application/json"
CONFIG_FILE = "config.txt"

# Desactivate warning ssl
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set up logging
LOG_FILENAME = 'error.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def read_config(filename: str = CONFIG_FILE) -> dict:
    """
    Reads the configuration from a specified JSON file.

    This function attempts to open and read a JSON configuration file.
    If the file does not exist, or a JSON decoding error occurs, it logs
    the error and returns an empty dictionary. For other unexpected errors,
    it logs the error message and also returns an empty dictionary.

    :param filename: The name of the configuration file to read. Defaults to 'config.txt'.
    :type filename: str

    :return: A dictionary containing the configuration data if successful,
             otherwise an empty dictionary.
    :rtype: dict

    Example:
    --------
    >>> config_data = read_config('config.txt')
    >>> print(config_data)
    {'key': 'value'}
    """
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} does not exist")

        with open(filename, 'r') as file:
            config_data = json.load(file)
            return config_data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error reading configuration file {filename} : {e}")
        print(f"Error reading configuration file {filename} : {e}")
    except Exception as e:
        logger.error(f"Unexpected error occurred while reading {filename} : {e}")
        print(f"Unexpected error occurred while reading {filename} : {e}")
    return {}

config = {**read_config()}

def get_qradar_headers() -> dict:
    """
    Prepare headers for QRadar HTTP request.
    :return: dict containing headers
    """
    return {
        "SEC": config['auth'],
        "Version": config.get('Version', "15.0"),
        "Accept": config.get('Accept', "application/json")
    }

def get_verify_option() -> Union[bool, str]:
    """
    Returns the appropriate value for the 'verify' parameter in requests.
    This could be a boolean (True/False) or a string path to a custom certificate.
    """
    # If verify_ssl is explicitly set to False, return False immediately.
    if config.get('verify_ssl') == False:
        return False

    # If verify_ssl is set to True and ssl_cert_path exists in the config and isn't None or empty string, return its value.
    if config.get('verify_ssl') == 'True' and config.get('ssl_cert_path') != 'None':
        return config['ssl_cert_path']

    # In all other cases, return False.
    return False

def make_request(url: str, method: str = "GET", params: Optional[dict] = None) -> dict:
    """
    Make a request (GET/PUT) to the specified URL.
    :param url: URL to make the request to
    :param method: HTTP method ("GET" or "PUT")
    :param params: Parameters to be sent with the request
    :return: JSON response as a dict if successful, empty dict otherwise
    """
    if method not in ["GET", "PUT"]:
        logger.error(f"Unsupported HTTP method: {method}")
        return {}

    verify_option = get_verify_option()
    try:
        if method == "GET":
            response = requests.get(url, headers=get_qradar_headers(), params=params, verify=verify_option)
        else:
            response = requests.put(url, headers=get_qradar_headers(), data=params, verify=verify_option)

        response.raise_for_status()
        return response.json()

    except (requests.RequestException, requests.exceptions.HTTPError) as e:
        logger.error(f"Error occurred during request: {e}")
        print(f"Error occurred during request: {e}")
        return {}
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")
        return {}

def get_app_id(app_name: str = "QRadar Use Case Manager") -> str:
    """
    Fetch the application ID for a given app name from QRadar.
    :param app_name: Name of the app to fetch the ID for
    :return: Application ID as a string
    """
    url = f"https://{config['ip_QRadar']}/api/gui_app_framework/application_definitions"
    apps = make_request(url)
    # Add a condition to prevent potential infinite loop
    if not isinstance(apps, list):
        return ""
    for app in apps:
        manifest = app.get("manifest", {})
        if manifest.get("name") == app_name:
            return app.get("application_definition_id", "")
    return ""

def get_system_info() -> dict:
    """
    Fetch the system information from the `/api/system/about` API endpoint in QRadar.

    :return: JSON response as a dict containing system information if successful,
             empty dict otherwise.

    Example:
    --------
    >>> system_info = get_system_info()
    >>> print(system_info)
    {
      "release_name": "7.5.0 UpdatePackage 6",
      "build_version": "2021.6.6.20230519190832",
      "fips_enabled": false,
      "external_version": "7.5.0"
    }
    """
    url = f"https://{config['ip_QRadar']}/api/system/about"
    return make_request(url)

def print_qradar_version():
    """Retrieve and print QRadar system information."""
    system_info = get_system_info()
    print(f"QRadar System Information: {config['ip_QRadar']}")
    print(f"release_name: {system_info['release_name']}")
    print(f"build_version: {system_info['build_version']}")
    print(f"fips_enabled: {system_info['fips_enabled']}")
    print(f"external_version: {system_info['external_version']}")
