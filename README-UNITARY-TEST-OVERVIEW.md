# 📘 Unitary Tests Overview NHSuite for QRadar

### ✍️ Author: Pascal Weber (zoldax)

## 📋 Table of Contents
- [🔧 Preparation](#preparation)
- [🛠 Config Errors](#config-errors)
- [🌐 API Errors](#api-errors)
- [📥 Import Errors](#import-errors)
- [📤 Export Testing and Errors](#export-testing-and-errors)
- [🔍 check-domain Testing and Errors](#check-domain-testing-and-errors)
- [🔎 check-version Testing and Errors](#check-version-testing-and-errors)

## 🔧 Preparation

| Test Name          | Test Option | Expected Output | Setup Command  |
|--------------------|-------------|-----------------|----------------|
| Removing error.log | -h          | usage:          | rm error.log   |

## 🛠 Config Errors

| Test Name                           | Test Option       | Expected Output                   | Setup Command                                   |
|-------------------------------------|-------------------|-----------------------------------|-------------------------------------------------|
| Checking correct config return      | --check-version   | QRadar System Information         |                                                 |
| Missing config.txt file             | --check-version   | Error reading configuration file  | rm config.txt                                   |
| No Read Access to Config File       | --check-version   | Permission denied                 | chmod 100 config.txt                            |
| Comma missing in json config.txt    | --check-version   | Error reading configuration file  | cp config/config.suppress.comma.txt config.txt  |

## 🌐 API Errors

| Test Name                                                    | Test Option       | Expected Output                                      | Setup Command                                   |
|--------------------------------------------------------------|-------------------|------------------------------------------------------|-------------------------------------------------|
| QRadar Target Host Not Available                             | --check-version   | Max retries exceeded with url                        | cp config/config.bad.ip.txt config.txt          |
| Wrong Key in Config File (HTTP 401)                          | --check-version   | 401 Client Error                                     | cp config/config.wrong.key.txt config.txt       |
| Wrong API Version in Config File (HTTP 422)                  | --check-version   | 422 Client Error                                     | cp config/config.wrong.api.txt config.txt       |
| Wrong Accept String in API (HTTP 406)                        | --check-version   | 406 Client Error                                     | cp config/config.wrong.accept.txt config.txt    |
| Wrong verify_ssl String in API (set automatically to false)  | --check-version   | QRadar System Information                            | cp config/config.wrong.verify.txt config.txt    |
| Wrong ssl_cert_path (File or Chain) in API                   | --check-version   | Could not find a suitable TLS CA certificate bundle  | cp config/config.wrong.ssl.path.txt config.txt  |

## 📥 Import Errors

| Test Name                                                      | Test Option                           | Expected Output                      | Setup Command                                   |
|----------------------------------------------------------------|---------------------------------------|--------------------------------------|-------------------------------------------------|
| Checking correct import return                                 | -i test/network-hierarchy.csv         | lines imported successfully          |                                                 |
| Checking correct return safety on                              | -i test/network-hierarchy.csv         | Safety parameter is on               |                                                 |
| Checking correct return safety off                             | -i test/network-hierarchy.csv         | Safety parameter is off              | cp config/config.safety.off.txt config.txt      |
| Missing File Name for Importing                                | -i                                    | expected one argument                |                                                 |
| Incorrect File Structure for Importing (No Headers)            | -i test/nh_noheaders.csv              | Header is not correct, must be...    |                                                 |
| Incorrect File Structure for Importing (Wrong Headers)         | -i test/nh_wrongheaders.csv           | Header is not correct, must be...    |                                                 |
| Incorrect File Structure for Importing (Just the Headers)      | -i test/nh_justheaders.csv            | no data                              |                                                 |
| Incorrect File Structure for Importing (id blank or string)    | -i test/nh_idstring.csv               | invalid literal for int() with...    |                                                 |
| Incorrect File Structure for Importing (group blank or string) | -i test/nh_groupinvcar.csv            | A group name may only contain ...    |                                                 |
| Incorrect File Structure for Importing (name blank or string)  | -i test/nh_nameinvalid.csv            | A network name may only contain...   |                                                 |
| Incorrect File Structure for Importing (cidr)                  | -i test/nh_invalidcidr.csv            | Invalid cidr                         |                                                 |
| Incorrect File Structure for Importing (Number out of range)   | -i test/nh_domainidoutrange.csv       | invalid literal for int() with...    |                                                 |
| Incorrect File Structure for Importing (domain id blank)       | -i test/nh_domainidstring.csv         | invalid literal for int() with...    |                                                 |
| Incorrect File Structure for Importing (GPS coordinates)       | -i test/nh_gpsinvalid.csv             | Invalid location format              |                                                 |
| Incorrect File Structure for Importing (invalid country code)  | -i test/nh_countrycodeinvalid.csv     | Invalid country code                 |                                                 |

## 📤 Export Testing and Errors

| Test Name                                          | Test Option   | Expected Output                   | Setup Command                          |
|----------------------------------------------------|---------------|-----------------------------------|----------------------------------------|
| Successful export with -e                          | -e            | lines exported successfully       |                                        |
| Successful export with -e <file.csv> file          | -e file.csv   | lines exported successfully       | rm -f file.csv                         |
| Export with -e failed due to no connection         | -e            | No data exported                  | cp config/config.bad.ip.txt config.txt |

## 🔍 check-domain Testing and Errors

| Test Name                         | Test Option      | Expected Output     | Setup Command |
|-----------------------------------|------------------|---------------------|---------------|
| Checking correct check-version    | --check-domain   | DEFAULT_DOMAIN      |               |

## 🔎 check-version Testing and Errors

| Test Name                         | Test Option      | Expected Output           | Setup Command |
|-----------------------------------|------------------|---------------------------|---------------|
| Checking correct check-version    | --check-version  | QRadar System Information |               |

