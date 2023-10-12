# ⚙️ QRadar Interaction Library: Error Logging

### 🖋️ Author
- **Pascal Weber (zoldax)**

## 🚫 Errors Logged in `qradarzoldaxlib`
The library, `qradarzoldaxlib.py`, offers functionalities for interaction with the QRadar API. Below is a breakdown of potential errors that may be logged:

### 1. 📑 `read_config` Function

This function reads configuration data from a JSON file.

#### Error Scenarios:

- **🚫 File Not Found**:
    ```
    Error reading configuration file [filename] : [filename] does not exist
    ```

- **🔣 JSON Decoding Error**:
    ```
    Error reading configuration file [filename] : [specific JSON decoding error message]
    ```

- **❗ Unexpected Errors**:
    ```
    Unexpected error occurred while reading [filename] : [error details]
    ```

### 2. 🌐 `make_request` Function

This function sends an HTTP request (either GET or PUT) to a specified URL.

#### Error Scenarios:

- **❌ Unsupported HTTP Method**:
    ```
    Unsupported HTTP method: [method]
    ```

- **⚠️ Request Exception or HTTP Error**:
    ```
    Error occurred during request: [error details]
    ```

- **❗ Unexpected Errors**:
    ```
    An unexpected error occurred: [error details]
    ```

### 3. 🆔 `get_app_id` Function

This function fetches the application ID for a given app name from QRadar.

#### Note:
If the function fails to fetch applications from the QRadar API, no specific error message is logged, but the function returns an empty string.

## 🚫 Errors Logged in `qradarzoldaxclass.py`

### 📢 Errors

- **Configuration Reading 📚**
    - `config.txt not found.`
    - `Failed to decode JSON from config.txt.`
  
- **Network Hierarchy Fetching 🌐**
    - `Unexpected data format received: {hierarchy_data}`

- **CSV Import to QRadar 📤**
    - 🚫 `Backup failed. Aborting the import process for safety.`
        - When: The safety mode is ON, and backup of the current network hierarchy fails.
        - Location: Method `import_csv_to_qradar`.

    - ❌ `Invalid cidr {row['cidr']} for id {row['id']} - abort import.`
        - When: The provided CIDR in the CSV is invalid.
        - Location: Method `import_csv_to_qradar`.

    - ❌ `Invalid group name {row['group']} for id {row['id']} - abort import -.`
        - When: The provided group name in the CSV is invalid.
        - Location: Method `import_csv_to_qradar`.

    - ⚠️ `Invalid location format {location_val} for id {row['id']} - import continue - but value set to null.`
        - When: The provided location format in the CSV is invalid.
        - Location: Method `import_csv_to_qradar`.

    - ⚠️ `Invalid country code {country_code_val} for id {row['id']} - import continue - but value set to null.`
        - When: The provided country code in the CSV is invalid.
        - Location: Method `import_csv_to_qradar`.

    - 🚫 `Failed to import data from {csv_filename}`
        - When: There's an error while making a request to import the data.
        - Location: Method `import_csv_to_qradar`.

    - ❗ `File {csv_filename} not found.`
        - When: The specified CSV file for import is not found.
        - Location: Method `import_csv_to_qradar`.

    - ❗ `Error reading CSV file {csv_filename}.`
        - When: There's an error reading the CSV file.
        - Location: Method `import_csv_to_qradar`.

    - 🚫 `An unexpected error occurred: {e}`
        - When: Any unexpected error occurs.
        - Location: Method `import_csv_to_qradar`.

- **Domain Information Checking 🌍**
    - `Unexpected data format received: {domain_data}`

- **Backup of Current Network Hierarchy 💾**
    - `Failed to create a backup due to the following error: {e}`

