import sys
import os
import requests
import json

def main():
    check_image()


def check_image():
    tmp = requests.get("http://100.71.71.71:5000/v2/" + sys.argv[1] + "/tags/list")
    req = tmp.json()
    #print(req)
    if (tmp.status_code == 404):
        print("1")
        return 1
    else:
        if req["name"] == sys.argv[1] and sys.argv[2] in req["tags"]:
            print("0")
            return 0
        else:
            #raise Exception("Image with tag " + sys.argv[1] + " does not exist in Docker Registry with IP: " + sys.argv[1])
            print("1")
            return 1


if __name__=='__main__':
    main()
