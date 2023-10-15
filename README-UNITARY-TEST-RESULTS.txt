[2023-10-15 15:27:24] Starting test...
---------------------------------------------------------------------------------------
################################ Preparation ###################################
---------------------------------------------------------------------------------------
Removing error.log [0;32mPASSED[0m
---------------------------------------------------------------------------------------
################################ Config Errors ###################################
---------------------------------------------------------------------------------------
Checking correct config return [0;32mPASSED[0m
Missing config.txt file [0;32mPASSED[0m
No Read Access to Config File [0;32mPASSED[0m
Comma missing in json config.txt file [0;32mPASSED[0m
---------------------------------------------------------------------------------------
################################ API Errors ###################################
---------------------------------------------------------------------------------------
QRadar Target Host Not Available [0;32mPASSED[0m
Wrong Key in Config File (HTTP 401) [0;32mPASSED[0m
Wrong API Version in Config File (HTTP 422) [0;32mPASSED[0m
Wrong Accept String in API (HTTP 406) [0;32mPASSED[0m
Wrong verify_ssl String in API (set automatically value to false) [0;32mPASSED[0m
Wrong ssl_cert_path (File or Chain) in API [0;32mPASSED[0m
---------------------------------------------------------------------------------------
################################ Import Errors ###################################
---------------------------------------------------------------------------------------
Checking correct import return [0;32mPASSED[0m
Checking correct return safety on [0;32mPASSED[0m
Checking correct return safety off [0;32mPASSED[0m
Missing File Name for Importing [0;32mPASSED[0m
Incorrect File Structure for Importing (No Headers) [0;32mPASSED[0m
Incorrect File Structure for Importing (Wrong Headers) [0;32mPASSED[0m
Incorrect File Structure for Importing (Just the Headers) (HTTP 422) [0;32mPASSED[0m
Incorrect File Structure for Importing (id blank or string) [0;32mPASSED[0m
Incorrect File Structure for Importing (group blank or invalid characters in string) (HTTP 422) [0;32mPASSED[0m
Incorrect File Structure for Importing (name blank or invalid characters in string) (HTTP 422) [0;32mPASSED[0m
Incorrect File Structure for Importing (cidr) (HTTP 422) [0;32mPASSED[0m
Incorrect File Structure for Importing (Number out of range for domain id) (HTTP 422) [0;32mPASSED[0m
Incorrect File Structure for Importing (domain id blank or string) [0;32mPASSED[0m
Incorrect File Structure for Importing (GPS coordinates) [0;32mPASSED[0m
Incorrect File Structure for Importing (invalid country code) [0;32mPASSED[0m
---------------------------------------------------------------------------------------
################################ Export Testing Errors ###################################
---------------------------------------------------------------------------------------
Successfull export with -e to create default network_hierarhy.csv file [0;32mPASSED[0m
Successfull export with -e <file.csv> file [0;32mPASSED[0m
Export with -e failed due to no connection [0;32mPASSED[0m
---------------------------------------------------------------------------------------
################################ check-domain Testing and Errors ###################################
---------------------------------------------------------------------------------------
Checking correct check-version return [0;32mPASSED[0m
---------------------------------------------------------------------------------------
################################ check-version Testing and Errors ###################################
---------------------------------------------------------------------------------------
Checking correct check-version return [0;32mPASSED[0m
---------------------------------------------------------------------------------------
                                 TEST SUMMARY                                          
---------------------------------------------------------------------------------------
Total Tests Run: 31
Passed: [0;32m31[0m
Failed: [0;31m0[0m
---------------------------------------------------------------------------------------
[2023-10-15 15:27:36] Test finished...
