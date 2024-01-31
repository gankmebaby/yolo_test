import os
import shutil
here = os.getcwd()
print(here)
work_path = here
count = 2
for file in os.listdir(work_path):
    count+=1
    print(file)
print(count)
