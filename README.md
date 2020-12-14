Cisco Call Manager - CDR File Peak Time Analysis script

Script processess ~2 million CDR rows in ~100 seconds on an i5. Script is single-threaded. I don't recommend attempting to multi-thread it...

Basic Instructions
1. Download cdr from https://cucmaddress/car application (no CMR needed)
2. To speed up processing, trim file to only dateTimeOrigination and dateTimeDisconnect columns.
3. Copy CDR .csv file to folder with script. 
4. Run analyzer_list_unordered.py
5. Input the filename.
6. Wait...

Output provides peak call volume and time of peak (IE: 20 calls between 12:01 PM and 12:02 PM, although most likely 12:01 and 12:01 due to the way it calculates overlapping calls)