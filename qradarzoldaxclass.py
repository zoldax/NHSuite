#qradarzoldaxclass.py

"""
   qradarzoldaxclass.py

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

import csv
import re
import json
import argparse
import ipaddress
import qradarzoldaxlib
import os
from datetime import datetime
from typing import Union

class QRadarNetworkHierarchy:
    """
    A class to manage and interact with the QRadar Network Hierarchy by Pascal Weber (zoldax)

    QRadar Network Hierarchy is a logical representation of a network's structure.
    This class provides utilities to validate, fetch, import, and backup the hierarchy.

    Attributes:
    -----------
    base_url : str
        The base URL for the QRadar API.

    Methods:
    --------
    valid_location_format(loc: str) -> bool:
        Validates if a given string is in the correct latitude and longitude format.

    valid_country_code_format(code: str) -> bool:
        Validates if the provided country code is in the correct two-letter format.

    valid_group_format(group: str) -> bool:
        Validates the format of a given group string.

    format_location(location_str: str) -> dict:
        Converts a location string into a dictionary format.

    valid_cidr_format(cidr: str) -> bool:
        Validates if a given string is in the correct CIDR format.

    valid_network_name_format(name: str) -> bool:
        Validate the network name format. Allowed characters: Alphanumerics, -, _""

    fetch_network_hierarchy() -> list:
        Fetches the QRadar Network Hierarchy from the API.

    write_network_hierarchy_to_csv(filename: str) -> int:
        Fetches QRadar Network Hierarchy and writes it to a CSV file.

    import_csv_to_qradar(csv_filename: str) -> Union[bool, int]:
        Imports data from a CSV file into QRadar using the API.

    check_domain() -> None:
        Fetches and displays domain information from QRadar.

    backup_current_hierarchy() -> bool:
        Backs up the current QRadar Network Hierarchy to a CSV file.
    """

    def __init__(self):
        """
        Initialize the QRadarNetworkHierarchy object with the base URL.
        """
        self.config = self._read_config()
        self.base_url = f"https://{self.config['ip_QRadar']}"

    @staticmethod
    def _read_config() -> dict:
        """
        Reads the configuration from the config.txt file.

        Returns:
        --------
        dict : Configuration as a dictionary.
        """
        try:
            with open('config.txt', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception("config.txt not found.")
        except json.JSONDecodeError:
            raise Exception("Failed to decode JSON from config.txt.")

    # Validation Functions

    @staticmethod
    def valid_location_format(loc: str) -> bool:
        """Validate if the provided string is in the correct lat,long format."""
        pattern = r'^(-?\d+(\.\d+)?),\s*(-?\d+(\.\d+)?)$'
        match = re.match(pattern, loc)
        if not match:
            return False
        lat, _, lon, _ = match.groups()
        lat, lon = float(lat), float(lon)

        # Check latitude is between -90 and 90
        if not (-90 <= lat <= 90):
            return False

        # Check longitude is between -180 and 180
        if not (-180 <= lon <= 180):
            return False

        return True



        #return -90 <= lat <= 90 and -180 <= lon <= 180

    @staticmethod
    def valid_country_code_format(code: str) -> bool:
        """Validate if the provided country code is in the correct format."""
        return bool(re.match(r"^[A-Z]{2}$", code))

    @staticmethod
    def valid_group_format(group: str) -> bool:
        """Validate the group format. Allowed characters: Alphanumerics, ., -, _"""
        return bool(re.match(r'^[A-Za-z0-9\.\-_]+$', group))

    @staticmethod
    def format_location(location_str: str) -> dict:
        """Convert location string (long,lat) to dictionary format."""
        ### Have to change the order like the API, long first then lat """Convert location string (lat,long) to dictionary format."""
        lat, lon = map(float, location_str.split(','))
        return {"type": "Point", "coordinates": [lon, lat]}

    @staticmethod
    def valid_cidr_format(cidr: str) -> bool:
        """Validate if the provided string is in correct CIDR format."""
        # Check basic format using regex
        if not re.match(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/(\d{1,2})$", cidr):
            return False

        # Use ipaddress to validate the correctness of the IP address and prefix
        try:
            ipaddress.ip_network(cidr)
            return True
        except ValueError:
            return False

    @staticmethod
    def valid_network_name_format(name: str) -> bool:
        """Validate the network name format. Allowed characters: Alphanumerics, -, _"""
        return bool(re.match(r'^[A-Za-z0-9\-_]+$', name))

    # Functions for NH

    def fetch_network_hierarchy(self):
        """Fetch the QRadar Network Hierarchy."""
        url = f"{self.base_url}/api/config/network_hierarchy/networks"

        # Assume qradarzoldaxlib.make_request can potentially raise exceptions on its own
        try:
            hierarchy_data = qradarzoldaxlib.make_request(url, "GET")

            # Check if the data is not a list, which means something unexpected happened
            if not isinstance(hierarchy_data, list):
                message = f"Unexpected data format received: {hierarchy_data}"
                qradarzoldaxlib.logger.error(message)
                raise ValueError(message)

            return hierarchy_data

        except Exception as e:
            # We can either raise the exception again or handle it gracefully
            qradarzoldaxlib.logger.error(f"Error fetching QRadar Network Hierarchy: {str(e)}")
            return []

    def write_network_hierarchy_to_csv(self, filename="network_hierarchy.csv"):
        """
        Fetch QRadar Network Hierarchy and write it to a CSV file.

        :param filename: The name of the output CSV file.
        :return: Number of lines written.
        """
        hierarchy_data = self.fetch_network_hierarchy()

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            columns = ["id", "group", "name", "cidr", "description", "domain_id", "location", "country_code"]
            writer.writerow(columns)

            for entry in hierarchy_data:
                location = entry.get("location", {})
                location_str = 'N/A'
                if location.get("type") == "Point" and len(location.get("coordinates", [])) == 2:
                    location_str = f"{location['coordinates'][1]},{location['coordinates'][0]}"
                    ## Warning / zoldax : Have to change the order , as QRadar API give the longitude first then the latitude
                entry["location"] = location_str
                data = [entry.get(key, 'N/A') for key in columns]
                writer.writerow(data)

            return len(hierarchy_data) + 1

    def import_csv_to_qradar(self, csv_filename: str) -> Union[bool, int]:
        """
        Import data from the given CSV file to QRadar via the API.
        """

        # Expected Network Hierarchy header for the CSV file
        expected_header = ["id", "group", "name", "cidr", "description", "domain_id", "location", "country_code"]

        if 'safety' in qradarzoldaxlib.config and qradarzoldaxlib.config['safety'].lower() != "off":
            backup_success = self.backup_current_hierarchy()
        else:
            print("Safety parameter is off, no backup from server")
            qradarzoldaxlib.logger.error("Safety parameter is off, no backup from server")

            if not backup_success:
                qradarzoldaxlib.logger.error("Backup failed. Aborting the import process for safety.")
                return False

        url = f"{self.base_url}/api/config/network_hierarchy/staged_networks"
        network_hierarchy_data = []

        try:
            with open(csv_filename, 'r', newline='', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)

                # Check if the header matches the expected header
                if reader.fieldnames != expected_header:
                    print("Header is not correct, must be id,group,name,cidr,description,domain_id,location,country_code.")
                    qradarzoldaxlib.logger.error("Header is not correct, must be id,group,name,cidr,description,domain_id,location,country_code.")
                    return False

                for row in reader:
                    try:
                        network_obj = {
                            "id": int(row["id"]),
                            "description": row["description"],
                            "domain_id": int(row["domain_id"]),
                        }

                        name_val = row.get("name", "").strip()
                        if not self.valid_network_name_format(row["name"]):
                            print(f"Invalid network name {row['name']} for id {row['id']}.")
                            print("A network name may only contain letters, numbers, '-', or '_'")
                            qradarzoldaxlib.logger.error(f"Invalid network name {row['name']} for id {row['id']} - aborting import.")
                            qradarzoldaxlib.logger.error("A network name may only contain letters, numbers, '-', or '_'.")
                        else:
                            network_obj["name"] = name_val

                        if not self.valid_cidr_format(row["cidr"]):
                            print(f"Invalid cidr {row['cidr']} for id {row['id']}.")
                            qradarzoldaxlib.logger.error(f"Invalid cidr {row['cidr']} for id {row['id']} - abort import.")
                        else:
                            cidr_val = row.get("cidr", "").strip()
                            network_obj["cidr"] = cidr_val

                        if not self.valid_group_format(row["group"]):
                            print(f"Invalid group name {row['group']} for id {row['id']}.")
                            print("A group name may only contain letters, numbers, '.', '-', or '_'.")
                            qradarzoldaxlib.logger.error(f"Invalid group name {row['group']} for id {row['id']} - abort import -.")
                            qradarzoldaxlib.logger.error("A group name may only contain letters, numbers, '.', '-', or '_'.")
                        else:
                            group_val = row.get("group", "").strip()
                            network_obj["group"] = group_val

                        location_val = row.get("location", "").strip()
                        if location_val and location_val != "N/A":
                            if self.valid_location_format(location_val):
                                formatted_location = self.format_location(location_val)
                                network_obj["location"] = formatted_location
                            else:
                                print(f"Invalid location format {location_val} for id {row['id']} - import continue - but value set to null.")
                                qradarzoldaxlib.logger.error(f"Invalid location format {location_val} for id {row['id']} - import continue - but value set to null.")

                        country_code_val = row.get("country_code", "").strip()
                        if country_code_val and country_code_val != "N/A":
                            if self.valid_country_code_format(country_code_val):
                                network_obj["country_code"] = country_code_val
                            else:
                                print(f"Invalid country code {country_code_val} for id {row['id']} - import continue - but value set to null.")
                                qradarzoldaxlib.logger.error(f"Invalid country code {country_code_val} for id {row['id']} - import continue - but value set to null.")

                        network_hierarchy_data.append(network_obj)

                    except KeyError as ke:
                        missing_column = ke.args[0]
                        qradarzoldaxlib.logger.error(f"Missing value for column '{missing_column}' in row {reader.line_num}.")
                        return False
                    except ValueError as ve:  # This is to catch any int conversion errors
                        qradarzoldaxlib.logger.error(f"Invalid value in row {reader.line_num}: {ve}")
                        return False
                    except Exception as e:
                        qradarzoldaxlib.logger.error(f"Problems with the data from your file {e}")
                        return False

            response = qradarzoldaxlib.make_request(url, "PUT", params=json.dumps(network_hierarchy_data))
            if response:
                return len(network_hierarchy_data)
            else:
                qradarzoldaxlib.logger.error(f"Failed to import data from {csv_filename} incorrect format (no data) or incorrect data")
                print(f"Failed to import data from {csv_filename} incorrect format (no data) or incorrect data")
                return False

        except FileNotFoundError:
            qradarzoldaxlib.logger.error(f"File {csv_filename} not found.")
            return False
        except csv.Error:
            qradarzoldaxlib.logger.error(f"Error reading CSV file {csv_filename}.")
            return False
        except Exception as e:
            qradarzoldaxlib.logger.error(f"An unexpected error occurred: {e}")
            return False

    def check_domain(self):
        """
        Fetch and display the domain information from QRadar.
        """
        url = f"{self.base_url}/api/config/domain_management/domains"
        domain_data = qradarzoldaxlib.make_request(url, "GET")

        if not isinstance(domain_data, list):
            qradarzoldaxlib.logger.error(f"Unexpected data format received: {domain_data}")
            return

        for domain in domain_data:
            domain_id = domain.get("id", 'N/A')
            if domain_id == 0:
                domain_name = "DEFAULT_DOMAIN"
            else:
                domain_name = domain.get("name", 'N/A') or 'N/A'
            domain_description = domain.get("description", 'N/A') or 'N/A'
            print(f"Domain ID: {domain_id}, Domain Name: {domain_name}, Description: {domain_description}")

    def backup_current_hierarchy(self) -> bool:
        """
        Create a backup of the current network hierarchy.
        """
        try:
            if not os.path.exists('safety'):
                os.mkdir('safety')

            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            backup_filename = f"safety/backup-before-import-NH-{qradarzoldaxlib.config['ip_QRadar']}-{timestamp}.csv"
            print(f"Safety parameter is on, actual Network Hierarchy backuped in {backup_filename} before import")

            self.write_network_hierarchy_to_csv(backup_filename)
            return True

        except Exception as e:
            qradarzoldaxlib.logger.warning(f"Failed to create a backup due to the following error: {e}")
            return False
