import os
import sys

with open(sys.argv[1], 'r') as file:
    str_tmp = "ghostgoose"
    data = file.read()
    tmp = sys.argv[2] + ":" + sys.argv[3]
    if sys.argv[2] == "100.71.71.71:5000/db-service":
        data = data.replace("100.71.71.71:5000/db-service:latest", tmp)
    elif sys.argv[2] == "100.71.71.71:5000/init-container":
        data = data.replace("100.71.71.71:5000/init-container:latest", tmp)
    print(data)
         

with open(sys.argv[1], 'w') as file:
    file.write( data )
