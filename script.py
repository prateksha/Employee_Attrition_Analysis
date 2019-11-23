import pandas as pd
# from datetime import datetime, date
import glob

in_time = pd.read_csv("hr-analytics-case-study/in_time.csv")
out_time = pd.read_csv("hr-analytics-case-study/out_time.csv")

in_time.rename(columns = {"Unnamed: 0": "EmployeeID"}, inplace = True) 
out_time.rename(columns = {"Unnamed: 0": "EmployeeID"}, inplace = True) 

for i in range(1,262):
    in_time.iloc[:,i] =  pd.to_datetime(in_time.iloc[:,i]).dt.time
    out_time.iloc[:,i] = pd.to_datetime(out_time.iloc[:,i]).dt.time
    
in_time = in_time.dropna(axis=1, how="all")
out_time = out_time.dropna(axis=1, how="all")

joined_timings = pd.merge(in_time, out_time, on='EmployeeID')

for i in range(1,250):
    for j in range(0, 4410):
        emp_in = joined_timings.iloc[j,i]
        emp_out = joined_timings.iloc[j,i+249]
        print("row = " + str(j) + "col = " + str(i))
#         diff = emp_out - emp_in
        diff_h = (emp_out.hour - emp_in.hour)*60*60
        diff_m = (emp_out.minute - emp_in.minute)*60
        diff_s = emp_out.second - emp_in.second
        joined_timings.iloc[j,i] = (diff_h+diff_m+diff_s)
    joined_timings.drop(joined_timings.columns[i+249], axis=1, inplace=True)
    
joined_timings.to_csv( "combined_csv.csv")