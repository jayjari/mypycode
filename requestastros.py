#!/usr/bin/python3
  
#using the requests library
import requests

# API is a constant so capitalize it:
MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    #make a Request
    resp = requests.get(MAJORTOM)

    pyj = resp.json()

    astrocosmo = pyj.get("people")

    for spaceperson in astrocosmo:
        print(spaceperson["name"])

if __name__ == "__main__":
    main()
    #parse out the Json we stripped off response
    #display selected data on screen - names of the people in space
