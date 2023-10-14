#!/usr/bin/env python3

"""
   NHSuite.py

   A utility script to export, import and fetch domain from the QRadar Network Hierarchy.

   Requirements:
   - qradarzoldaxlib: A library to interact with QRadar API.
   - qradarzoldaxclass : A library containing my NH Class and methods

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

import argparse
import qradarzoldaxlib
from qradarzoldaxclass import QRadarNetworkHierarchy

# export_data and import_data helper functions to handle exporting and importing 

def export_data(qradar_nh, export_file):
    """Export data to CSV file."""
    try:
        lines_exported = qradar_nh.write_network_hierarchy_to_csv(export_file)
        if lines_exported == 1:  # Only header was exported, meaning no data.
            return "No data exported."
        else:
            return f"{lines_exported} lines exported successfully! (including col headers)"
    except Exception as e:
        return f"Error during export: {e}"

def import_data(qradar_nh, import_file):
    """Import data from CSV file."""
    try:
        lines_imported = qradar_nh.import_csv_to_qradar(import_file)
        if isinstance(lines_imported, int) and lines_imported > 0:
            return f"{lines_imported} lines imported successfully!"
        else:
            return "Data import failed."
    except Exception as e:
        return f"Error during import: {e}"

def main():
    """Main function to handle command-line arguments and execute desired actions."""
    qradar_nh = QRadarNetworkHierarchy()

    parser = argparse.ArgumentParser(description="QRadar Network Hierarchy Suite by Pascal Weber (zoldax) / Abakus Sécurité")
    parser.add_argument('-e', '--export-file', nargs='?', const="network_hierarchy.csv", default=None, metavar="FILENAME", help="Export network hierarchy to a CSV file. If no filename is provided, it will default to 'network_hierarchy.csv'.")
    parser.add_argument('-i', '--import-file', type=str, metavar="IMPORT_FILENAME", help="Import network hierarchy from a CSV file")
    parser.add_argument('--check-domain', action='store_true', help="Fetch and display domain information from QRadar")
    parser.add_argument('--check-version', action='store_true', help="Retrieve and display QRadar current system information")

    args = parser.parse_args()

    if args.export_file:
        print("Please wait... exporting data.")
        print(export_data(qradar_nh, args.export_file))

    elif args.import_file:
        print("Please wait... importing data.")
        print(import_data(qradar_nh, args.import_file))

    elif args.check_domain:
        try:
            qradar_nh.check_domain()
        except Exception as e:
            print(f"Error checking domain: {e}")

    elif args.check_version:
        try:
            qradarzoldaxlib.print_qradar_version()
        except Exception as e:
            print(f"Error checking version: {e}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()


