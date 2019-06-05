#!/usr/bin/python3
"""Author: Jayesh Jariwala | Learning JSON in Python Lab 6"""

# python has not json support

import json

def main():
    ## create a blob of data to work with
    hitchhikers = [{"name":"Zaphod Beeblebrox", "species":"Betelgeusian"}, {"name":"Arthur Dent", "species":"Human"}]

    ## display our python data (a list containing two dictionaries)
    print(hitchhikers)

    ## open a new file in write mode
    zfile = open("galaxyguide.json", "w")

    ## use the json library
    ## USAGE: json.dump(input data, file like object) ##
    json.dump(hitchhikers, zfile)

    ## close the file when we are done
    zfile.close()

main()
