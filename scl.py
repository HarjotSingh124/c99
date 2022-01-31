import os
import sys
import datetime
req_path = input("Enter your path: ")
age = 5
today = datetime.datetime.now()
if not os.path.exists(req_path):
  print("Please provide a valid path")
  sys.exit(1)
if os.path.isfile(req_path):
  print("Please Provide a Directory path")  
  sys.exit(2)
for each_file in os.listdir(req_path):
  each_file_path = os.path.join(req_path, each_file)
  if os.path.isfile(each_file_path):
    file_cre_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
    dif = (today-file_cre_date).days
    if dif>age:
      print(each_file_path, dif)
      os.remove(each_file_path)

