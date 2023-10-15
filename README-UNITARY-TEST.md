# Unitary Tests NHUtil for IBM QRadar Network Hierarchy 

# Author : Pascal Weber (zoldax)

📝 This document summarizes different unitary tests performed with the NHUtil for QRadar tool to catch errors.

## Table of Contents
1. [Config File Errors](#config-file-errors)
2. [API Errors](#api-errors)
3. [Import Errors](#import-errors)

## Config File Errors
- 🚫 **Missing config.txt File**
  - Output: `Error reading configuration file config.txt : config.txt does not exist`
  - Error.log: `[2023-10-13 11:11:08,296] - ERROR - Error reading configuration file config.txt : config.txt does not exist`

- 🚫 **No Read Access to Config File**
  - Output: `Unexpected error occurred while reading config.txt : [Errno 13] Permission denied: 'config.txt'`
  - Error.log: `[2023-10-13 11:15:24,793] - ERROR - Unexpected error occurred while reading config.txt : [Errno 13] Permission denied: 'config.txt'`

- 🚫 **Suppressed ',' in Config File**
  - Output: `Error reading configuration file config.txt : Expecting ',' delimiter: line 8 column 5 (char 225)`
  - Error.log: `[2023-10-13 11:17:04,855] - ERROR - Error reading configuration file config.txt : Expecting ',' delimiter: line 8 column 5 (char 225)`

## API Errors
- 🚫 **Target Not Available**
  - Output: `Error occurred during request: Max retries exceeded`
  - Notes: No data exported.

- 🚫 **Wrong Key in Config File (HTTP 401)**
  - Output: `Error occurred during request: 401 Client Error`
  - Error.log: `[2023-10-13 14:04:48,360] - ERROR - Unexpected data format received: {}`

- 🚫 **Wrong API Version in Config File (HTTP 422)**
  - Output: `Error occurred during request: 422 Client Error`
  - Error.log: `[2023-10-13 14:06:25,235] - ERROR - Unexpected data format received: {}`

- 🚫 **Wrong Accept String in API (HTTP 406)**
  - Output: `Error occurred during request: 406 Client Error`
  - Error.log: `[2023-10-13 14:09:29,279] - ERROR - Unexpected data format received: {}`

- 🚫 **Wrong verify_ssl String in API (HTTP 406)**
  - Output: `Error occurred during request: 406 Client Error`
  - Error.log: `[2023-10-13 14:09:29,279] - ERROR - Unexpected data format received: {}`

- 🚫 **Wrong ssl_cert_path (File or Chain) in API**
  - Output: `Could not find a suitable TLS CA certificate bundle`
  - Error.log: `[2023-10-13 14:23:24,471] - ERROR - Unexpected data format received: {}`

## Import Errors
- 🚫 **Missing File Name for Importing**
  - Output: `Expected one argument`

- 🚫 **Incorrect File Structure for Importing (No Headers)**
  - Output: `Header is not correct, must be id,group,name,cidr,description,domain_id,location,country_code.`
  - Error.log: `10-13 14:42:33,430] - ERROR - Header is not correct, must be id,group,name,cidr,description,domain_id,location,country_code.`

- 🚫 **Incorrect File Structure for Importing (Wrong Headers)**
  - Output: `Header is not correct, must be id,group,name,cidr,description,domain_id,location,country_code.`
  - Error.log: `10-13 14:42:33,430] - ERROR - Header is not correct, must be id,group,name,cidr,description,domain_id,location,country_code.`

- 🚫 **Incorrect File Structure for Importing (Just the Headers) (HTTP 422)**
  - Output: `Data import failed.`
  - Error.log: `[2023-10-13 14:46:41,597] - ERROR - Failed to import data from network_hierarchy.csv`

- 🚫 **Incorrect File Structure for Importing (id blank or string)**
  - Output: `Data import failed.`
  - Error.log: `[2023-10-13 15:09:19,113] - ERROR - An unexpected error occurred: invalid literal for int() with base 10: ''`
  - Error.log: `[2023-10-13 15:10:09,914] - ERROR - An unexpected error occurred: invalid literal for int() with base 10: 'AZEZ'`
  - Error.log: `[2023-10-13 15:10:35,605] - ERROR - An unexpected error occurred: invalid literal for int() with base 10: 'WrongIDtyped'`

- 🚫 **Incorrect File Structure for Importing (group blank or invalid characters in string) (HTTP 422)**
  - Output: `Invalid group name &é"(Net-catchall-10-172-192 for id 1. A group name may only contain letters, numbers, '.', '-', or '_'. Error occurred during request: 422 Client Error: 422 for url: https://192.168.10.146/api/config/network_hierarchy/staged_networks Data import failed.`
  - Error.log: `[2023-10-13 15:52:14,345] - ERROR - Invalid group name &é"(Net-catchall-10-172-192 for id 1 - abort import -.`
  - Error.log: `[2023-10-13 15:52:14,355] - ERROR - Error occurred during request: 422 Client Error: 422 for url: https://192.168.10.146/api/config/network_hierarchy/staged_networks`
  
- 🚫 **Incorrect File Structure for Importing (name blank or invalid characters in string) (HTTP 422)**
  - Output: `Invalid network name &éNet_10_0_0_0 for id 1. A network name may only contain letters, numbers, '-', or '_'. Error occurred during request: 422 Client Error: 422 for url: https://192.168.10.146/api/config/network_hierarchy/staged_networks Data import failed.`
  - Error.log: `[2023-10-13 15:50:52,312] - ERROR - Invalid network name &éNet_10_0_0_0 for id 1 - aborting import.`
  - Error.log: `[2023-10-13 15:50:52,322] - ERROR - Error occurred during request: 422 Client Error: 422 for url: https://192.168.10.146/api/config/network_hierarchy/staged_networks`

- 🚫 **Incorrect File Structure for Importing (cidr) (HTTP 422)**
  - Output: `Invalid cidr 10.0.0.0/99 for id 1. Error occurred during request: 422 Client Error: 422 for url: https://192.168.10.146/api/config/network_hierarchy/staged_networks Data import failed.`
  - Error.log: `[2023-10-13 16:06:07,839] - ERROR - Invalid cidr 10.0.0.0/99 for id 1 - abort import.`

- 🚫 **Incorrect File Structure for Importing (Number out of range for domain id) (HTTP 422)**
  - Output: `Error occurred during request: 422 Client Error: 422 for url: https://192.168.10.146/api/config/network_hierarchy/staged_networks Data import failed.`
  - Error.log: `[2023-10-13 16:10:35,342] - ERROR - Error occurred during request: 422 Client Error: 422 for url: https://192.168.10.146/api/config/network_hierarchy/staged_networks`

- 🚫 **Incorrect File Structure for Importing (domain id blank or string)**
  - Output: `Data import failed.`
  - Error.log: `[2023-10-13 16:13:04,903] - ERROR - An unexpected error occurred: invalid literal for int() with base 10: ''`
  - Error.log: `[2023-10-13 16:14:37,981] - ERROR - An unexpected error occurred: invalid literal for int() with base 10: 'wrongdomainid'`

- 🚫 **Incorrect File Structure for Importing (GPS coordinates)**
  - Output: `Invalid location format 1999,292929 for id 1 - import continues - but value set to null. 25 lines imported successfully!`
  - Error.log: `[2023-10-13 16:16:30,202] - ERROR - Invalid location format 1999,292929 for id 1 - import continues - but value set to null.`

- 🚫 **Incorrect File Structure for Importing (invalid country code)**
  - Output: `Invalid country code LALALAND for id 1 - import continues - but value set to null. 25 lines imported successfully!`
  - Error.log: `[2023-10-13 16:18:52,449] - ERROR - Invalid country code LALALAND for id 1 - import continues - but value set to null.`




