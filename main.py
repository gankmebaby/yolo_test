import os
import shutil
import json

here = os.getcwd()
print(here)
work_path = here
count = 0
for file in os.listdir(work_path):
    count += 1
    print(file, count)
for rt, dirs, files in os.walk(work_path):
    print(rt)
print('main')
print('ok')
