import sys
import os
from datetime import datetime
import re
if(len(sys.argv) < 2):
	tmp_dir = "TMP_"+sys.argv[0]
	os.system(f"mkdir {tmp_dir}")
	start_time = os.path.getctime(tmp_dir)
	os.system(f"rm -rf {tmp_dir}")
	print(start_time)
	sys.exit()

output_file = sys.argv[1]
monitor_path = sys.argv[2]
start_time = sys.argv[3]

arr = [monitor_path]
my_dict = {}

while(len(arr) > 0):
	d = arr.pop(0)
	darr = os.listdir(d)
	for df in darr:
		p = f"{d}/{df}"
		if(not(os.path.islink(p))):
			my_dict[p] = os.path.getctime(p)
			if(os.path.isdir(p)):
				arr.append(p)

filtered_keys = [key for key, value in my_dict.items() if value > float(start_time)]

output_dir = sorted_keys = sorted(filtered_keys, key=lambda x: my_dict[x])

f = open(output_file, "w")
for od in output_dir:
	f.write(od+"  --> "+str(os.path.getsize(od))+"\n")
