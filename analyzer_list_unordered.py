import pandas as pd
import time
#import matplotlib.pyplot as plt
#import numpy as np

# Set variables to store call times and counters
current_call_count = 0
peak_call_count = 0
current_call_start_times = []
current_call_end_times = []
peak_call_start_times = []
peak_call_end_times = []

#plotter_list = []

# Input CDR csv
file_name = input("Enter your file name: ")

start = time.time()

# Read CSV into pandas dataframe and sort calls by start time (dateTimeOrigination column)
cdr_df = pd.read_csv(file_name)
cdr_df = cdr_df.sort_values(by='dateTimeOrigination')

# Iterate through all dataframe rows sequentially
for index, row in cdr_df.iterrows():
    # Add current call end time (dateTimeDisconnect column) to list of end times
    current_call_end_times.append(row[1])
    
    # Sort list of end times in ascending order (earliest to latest disconnect)
    current_call_end_times.sort()
    
    # Add current call start time to a list (these were already ordered sequentially when the dataframe was sorted)
    current_call_start_times.append(row[0])

    # Loop through list of ordered call end times
    for _ in current_call_end_times:
        # Check current dataframe row start time against the earliest call end time (stored in position 0 in the ordered list)
        # If the start time is before the earliest call end time, break the loop. Otherwise, delete that end time and start time
        # from their respective lists
        if row[0] <= current_call_end_times[0]: break
        del current_call_end_times[0]
        del current_call_start_times[0]

    # Set the current_call_count variable to the length of the current_call_end_times list (number of currently active calls).
    current_call_count = len(current_call_end_times)

    #plotter_list.append(current_call_count)

    # If the current call count variable is greater than the peak call count variable (which starts at 0), 
    # set the peak call count to current call count.

    if current_call_count > peak_call_count:
        peak_call_count = current_call_count

        # Set peak call start and end times to the respective "current" lists so we can preserve the peak as the iteration continues.
        peak_call_end_times = current_call_end_times[:]
        peak_call_start_times = current_call_start_times[:]

# Print peak call count total, the last item in the peak call start times list (the latest activated call), and the first item in the
# end call times list (the earliest disconnect time) to determine the "slice" representing the peak.
print(f"There were {peak_call_count} calls between {time.ctime(peak_call_start_times[-1])} and {time.ctime(peak_call_end_times[0])}.")
print((time.time()-start))


#plt.plot(plotter_list)
#plt.show()
#x = np.arange(len(plotter_list))
#plt.bar(x,plotter_list)
#print(plotter_list)
#plt.ylabel('Active Calls')
#plt.xlabel('Time')
#plt.show()