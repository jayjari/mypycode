#!/usr/bin/python3
"""Author: Jayesh Jariwala | Learning JSON in Python Lab 6"""

# python has not json support

import json

def main():
    ## open the file
    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()

    ## display our decoded string
    print(datacenterstring)
    print(type(datacenterstring))
    print("\nThe code above is string data. Python cannot easily work with this data.")
    input("Press Enter to continue\n")

    ## Create the json string
    datacenterdecoded = json.loads(datacenterstring)

    ## This is now a dictionary
    print(type(datacenterdecoded))

    ## display the servers in the datacenter
    print(datacenterdecoded)

    ## display the servers in row3
    print(datacenterdecoded["row3"])

    ## display the second server in row2
    print(datacenterdecoded["row2"][1])

    ## write code to
    ## display the last server in row3
    print(datacenterdecoded["row3"][-1])
                            
main()
