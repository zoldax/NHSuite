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

import csv
import re
import json
import argparse
import ipaddress
import os
import qradarzoldaxlib
from qradarzoldaxclass import QRadarNetworkHierarchy
from datetime import datetime
from typing import Union

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
        lines_exported = qradar_nh.write_network_hierarchy_to_csv(args.export_file)
        print(f"{lines_exported} lines exported successfully! (including col headers)")

    elif args.import_file:
        lines_imported = qradar_nh.import_csv_to_qradar(args.import_file)
        if isinstance(lines_imported, int) and lines_imported > 0:
            print(f"{lines_imported} lines imported successfully!")
        else:
            print("Data import failed.")

    elif args.check_domain:
        qradar_nh.check_domain()

    elif args.check_version:  
        qradarzoldaxlib.print_qradar_version()

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
