# 🛠️NHSuite 🛠for IBM QRadar SIEM

NHSuite allows users to efficiently manage their QRadar Network Hierarchy. Utilizing the provided QRadar API, users can seamlessly export, import, and fetch domain information in a CSV format.

[![License](https://img.shields.io/github/license/zoldax/NHSuite?color=44CC11)](LICENSE)  [![Commit](https://img.shields.io/github/commit-activity/t/zoldax/NHSuite)](https://github.com/zoldax/NHSuite/commits/)  [![Views](https://hits.sh/github.com/zoldax/NHSuite.svg)](https://hits.sh/github.com/zoldax/NHSuite/) [![Last commit](https://img.shields.io/github/last-commit/zoldax/NHSuite/main)](https://github.com/zoldax/NHSuite/commits/main)

---
# Table of Contents
- [🛠️NHSuite](#️nhsuite)
  - [📌 Details](#-details)
  - [📖 Description](#-description)
  - [🛠️Usage](#️usage)
    - [1. Exporting the Network Hierarchy to CSV](#1-exporting-the-network-hierarchy-to-csv)
    - [2. Importing Network Hierarchy from CSV](#2-importing-network-hierarchy-from-csv)
    - [3. Checking Domain Information](#3-checking-domain-information)
    - [3. Checking QRadar System Information](#3-checking-qradar-system-information)
  - [📦 Requirements](#-requirements)
  - [📥 Inputs](#-inputs)
  - [📤 Outputs](#-outputs)
  - [🔑 Functionalities & Key Function](#-functionalities--key-function)
  - [🛠Configuration: `config.txt`](#configuration-configtxt)
    - [1. `ip_QRadar`](#1-ip_qradar)
    - [2. `auth`](#2-auth)
    - [3. `Version`](#3-version)
    - [4. `Accept`](#4-accept)
    - [5. `verify_ssl`](#5-verify_ssl)
    - [6. `ssl_cert_path`](#6-ssl_cert_path)
    - [7. `safety` Parameter](#7-safety-parameter)
  - [🔐 SSL API Connection Support](#-ssl-api-connection-support)
  - [🚫Error Handling](#error-handling)
  - [📝 Notes](#-notes)
  - [📜 Disclaimer](#-disclaimer)
---

## 📌 Details
- **Name**: NHSuite.py
- **Description**: A utility script designed to interface with the QRadar Network Hierarchy. Export, import, and fetch domain functionalities are provided.
- **Author**: Pascal Weber (zoldax) / Abakus Sécurité

## 📖 Description
NHSuite allows users to efficiently manage their QRadar Network Hierarchy. Utilizing the provided QRadar API, users can seamlessly export, import, and check domain-specific hierarchies in a CSV format.

At its heart, the tool aims to help — to offer a more straightforward approach to network hierarchy management, whether you're directly interfacing with QRadar or operating from a remote 🐧 Linux machine. Its functionalities, from error handling to data export, serve the user's needs without pretense.
 
The tool isn't just about functionality—it's about adaptability. In the modern software development world, Continuous Integration and Continuous Deployment (CI/CD) have become foundational principles we saw that every day on the operational field. This ensure network hierarchy updates, backup, and changes to be consistently integrated, tested, and deployed to test environnement before production, and is part of a more global projet on my side.

It's also worth noting that, by hosting the script on GitHub, there's an open invitation for everyone to contribute and improve upon it. It's a collaborative effort, and the real value of the tool will be determined by the community's engagement and feedback 📢 (ideas for example : phpIPAM translation, etc...)
In summary, 🛠 NHSuite 🛠 is a humble attempt to make life a bit easier 🌟.

## 🛠️Usage

For detailed usage and command-line options, execute the script with `-h` or `--help`.

Using NHSuite is straightforward with command-line arguments. Here's a step-by-step guide:

### 1. Exporting the Network Hierarchy to CSV:
To export the current QRadar Network Hierarchy into a CSV, use the `-e` or `--export-file` argument. You can specify the name of the output file. If you don't, it will default to `network_hierarchy.csv`.

**Example**:
```bash
# Export to default file name (network_hierarchy.csv)
python3 NHSuite.py -e

# Export to a specific file name
python3 NHSuite.py -e my_network_data.csv
```

### 2. Importing Network Hierarchy from CSV:

If you have a CSV file with the network hierarchy you'd like to import into QRadar, use the `-i` or `--import-file` argument followed by the file's path.
Before importing a new network hierarchy, it's essential to have a backup of your current setup. This tool has a built-in function to facilitate this if the safety parameter on the config.txt file is set to on.

**Example**:
```bash
# Import from a specific CSV file
python3 NHSuite.py -i path_to_my_network_data.csv
```

### 3. Checking Domain Information:

To retrieve and display domain information from QRadar, utilize the `--check-domain` flag.

**Example**:
```bash
# Fetch and display domain information from QRadar
python3 NHSuite.py --check-domain
```

### 3. Checking QRadar System Information:

To retrieve and display domain information from QRadar, utilize the `--check-version` flag.

**Example**:
```bash
# Display system information from QRadar
python3 NHSuite.py --check-version
```

## 📦 Requirements
- `qradarzoldaxlib`: A library to interact with QRadar's API.
- `qradarzoldaxclass`: Contain NetworkHierarchy class with methods and decorators.

## 📥 Inputs
1. `-e`, `--export-file`: Specify a file name to export the network hierarchy to. Defaults to 'network_hierarchy.csv' if no name is provided.
2. `-i`, `--import-file`: Specify a CSV file to import network hierarchy from.
3. `--check-domain`: Fetch and display domain information from QRadar.

## 📤 Outputs
- CSV File (when exporting) that includes fields such as `id`, `group`, `name`, `cidr`, `description`, `domain_id`, `location`, `country_code`.
- Console prints with domain information when `--check-domain` is used.

## 🛠Configuration: `config.txt` 

The `config.txt` file contains configuration parameters required for the communication with QRadar. Here's an overview of each parameter:

### 1. `ip_QRadar`

This represents the IP address or the domain name of your QRadar instance.

```json
"ip_QRadar": "qradardemo.zoldaxcorp.lan"
```

### 2. `auth`

This is the authentication token which is used to authenticate your requests to the QRadar API.

```json
"auth": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
```

### 3. `Version`

This represents the version of the QRadar API you are targeting.

```json
"Version": "15.0"
```

### 4. `Accept`

This parameter determines the format in which you'd like the response from the QRadar API. Typically, this would be set to `application/json`.

```json
"Accept": "application/json"
```

### 5. `verify_ssl`

This parameter determines whether the SSL certificate validation should be performed when connecting to QRadar.

```json
"verify_ssl": "True"
```

- "True" indicates that SSL verification is enabled.
- "False" indicates that SSL verification is disabled. Note: Disabling SSL verification is not recommended for production environments.

### 6. `ssl_cert_path`

If you have a custom certificate chain for SSL verification, or if the server's certificate chain isn't recognized by the default set of trusted certificate authorities on your system, you can specify a PEM file containing the entire certificate chain. (CA pem file from your PKI for example)

```json
"ssl_cert_path": "/path/to/certchained.pem"
```

- If you don't have a custom certificate chain, or if `verify_ssl` is set to "False", you can set this to "None".

Please ensure that all parameters are properly configured to match your QRadar environment and your preferences.


### 7. `safety` Parameter
```json
"safety": "on"
```

The `safety` parameter is a switch that can be set to either `on` or `off`. It governs whether a backup of the current network hierarchy is made before performing potentially disruptive operations.

#### When set to `on`:

- Before importing or making any changes to the QRadar Network Hierarchy, the tool will first create a backup of the current hierarchy.
- This backup is stored in a directory named `safety`. If this directory doesn't already exist, it will be created.
- The backup filename will follow the format: `backup-before-import-NH-QRadarIP-Timestamp.csv`.
- By having this safety backup, users can restore to a previous state in case of any unintended changes or issues.

#### When set to `off`:

- No backup will be created before making changes.
- Users should be cautious when setting this parameter to `off`, especially in production environments, as it might be harder to revert unintended modifications without a recent backup.

To leverage this feature, ensure you configure the `safety` parameter appropriately in the tool's configuration or command-line arguments.


## 🔐 SSL API Connection Support

For secure communication with the QRadar API, this tool supports SSL verification through two configuration parameters in the `config.txt` file:

### 1. `verify_ssl`

This parameter determines whether SSL certificate validation should be performed.


- `"True"`: This means that the SSL certificate provided by the server will be validated against the certificate authorities available in your environment. If you have a custom certificate authority or the server's certificate chain isn't in the default set of trusted authorities on your system, you need to specify the path to a PEM file containing the entire certificate chain using the `ssl_cert_path` parameter. Remember to use the right name for the QRadar_ip as IP or fqdn depending on how you created the certificate.

- `"False"`: This will bypass any SSL certificate validation. This option is not recommended for production environments due to security concerns, as it makes the connection vulnerable to man-in-the-middle attacks.

### 2. `ssl_cert_path`

If you have a custom certificate chain or if the server's certificate chain isn't recognized by the default set of trusted certificate authorities on your system, you can specify a PEM file containing the entire certificate chain.

## 🚫Error Handling
The tool is equipped to handle errors like invalid CIDR format, invalid group name, issues while parsing 'location' and 'country_code' fields, and any unexpected exceptions. Errors are logged using `qradarzoldaxlib.logger.error` on file `error.log`.

- A description of handled errors is on the [README-ERROR.md](README-ERROR.md) file.
- A Unitary test result of handled errors is on the [README-UNITARY-TEST.md](README-UNITARY-TEST.md) file.
- A Unitary test methodology of handled errors is on the [README-UNITARY-TEST-OVERVIEW.md](README-UNITARY-TEST-OVERVIEW.md) file.
- A Unitary battery test result is on the [README-UNITARY-TEST-RESULTS.txt](README-UNITARY-TEST-RESULTS.txt) file.


For errors related to the API call of QRadar here is the common API error Message : https://www.ibm.com/docs/en/qradar-common?topic=versions-api-error-messages

## 📝 Notes

Always test any modifications in a safe and non production environment. Do backups !

This Python tool, NHSuite, has been developed through countless hours of hard work and dedication. We are pleased to offer it to the community as a free and open-source resource, a testament to our commitment to supporting and enhancing our QRadar community.

Please consult IBM Guidelines for building a Network hierarchy : https://www.ibm.com/docs/en/qradar-on-cloud?topic=hierarchy-guidelines-defining-your-network

## Environment and Prerequisite

The script can work directly on QRadar (Tested on 7.5.X) or on a remote Linux machine (Debian) meeting the requirements (preferred method).

### Working Directly on QRadar

**Qradar > 7.5.0 (Python 3.6 (Use of f-strings))**

The script has been designed with flexibility in mind. For those who have direct access and the required privileges, the script can operate directly on a QRadar system. We have verified its compatibility with QRadar versions 7.5.x. This direct method allows for streamlined integration and quick access to QRadar's features without the need for additional configurations.

However, there are some considerations when working directly on QRadar.

### Working on a Remote Linux Machine (Preferred Method)

For a more isolated and controlled environment, we recommend executing the script on a remote 🐧 Linux machine. Our tests have particularly been positive on Debian-based systems.

This method has several advantages:

- 🏝️ **Isolation:** Running the script remotely ensures that QRadar's primary functions remain undisturbed. There's no risk of unintentionally consuming excessive resources on the QRadar system.
- 🤸 **Flexibility:** A separate Linux machine provides more freedom for customization, debugging, and script optimization. This can be especially beneficial when integrating the script with other tools or systems.
- 🛡️ **Security:** Operating the script remotely can add a layer of security. By limiting direct access to the QRadar system, you can further safeguard against potential threats or mishaps.

#### 📋 Requirements for the Remote Linux Machine:

- **Python Version:** Ensure that Python is installed, preferably a version that supports f-strings (Python 3.6 and above).
- **Network Access:** The remote machine should have network access to QRadar for API calls. Ensure that any firewalls or security groups allow for the necessary communication between the two systems.
- **Required Libraries:** The script might rely on specific Python libraries. These should be installed and kept updated on the remote machine.
- **Authentication:** API authentication details, like tokens or credentials, should be securely managed. Consider using environment variables or secure configuration files.

##### 🧪 Tested on my side on:

- debian Bullseye (11.7)
- Python 3.9.2
- Requests==2.31.0
- urllib3==1.26.5

## 🤝 Contribution

We warmly welcome contributions from everyone! If you have ideas, code, bug fixes, or anything else you'd like to share, please do so. Your insights and expertise can help improve the project for the entire community. Thank you for being a part of our journey! 🌟

## 📜 Disclaimer:

All content is without warranty of any kind. Use at your own risk. I assume no liability for the accuracy, correctness, completeness, usefulness, or any damages.

Q1 LABS, QRADAR and the 'Q' Logo are trademarks or registered trademarks of IBM Corp. All other trademarks are the property of their respective owners. 

IBM, the IBM logo, and ibm.com are trademarks or registered trademarks of International Business Machines Corp., registered in many jurisdictions worldwide. Other product and service names might be trademarks of IBM or other companies.

----------------------------------------------------------
