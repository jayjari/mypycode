#!/usr/bin/python3
"""Author: Jayesh Jariwala | Python Training """

# python has not json support

import json
import urllib.request
import csv
import os
import pprint

import requests
import paramiko

def getlistdata():
    student_lists = open("studentlist.csv")
    reader = csv.reader(student_lists)
    return reader

def listrecord():
    readerdata = getlistdata()
    for row in readerdata:
        print("{: >15} {: >5} {: >10}".format(*row))
    
def listtable():
    readerdata = getlistdata()
    for row in readerdata:
        print("Student Name: " + str(row[0]))
        print("Studnet Number: " + str(row[1]))
        print("Student Group: " + str(row[2]) + "\n")

def cmdissue(sshsession, commandtoissue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(commandtoissue)
    return ssh_stdout.read()

def sshtouser():
    # listtable()
    # getuser = int(input("Enter number of user: "))
    # from jrprogrammer import cmdissue
    # ssh student@pyapi-206-bchd
    print("SSH to User Not working Yet")

    SVRS = [{'ip':'10.10.2.3', 'un':'bender'}, {'ip':'10.10.2.4', 'un':'fry'}]
    CMDLIST = ['touch sshworked.txt', 'touch sshworked2.txt', 'uptime']
    
    # harvest RSA key
    myprivkey = paramiko.RSAKey.from_private_key_file('/home/student/.ssh/id_rsa')
    
    for server in SVRS:
        # init connection to remote machine    
        sshsession = paramiko.SSHClient()
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshsession.connect(hostname=server['ip'], username=server['un'], pkey=myprivkey)
                                                          
        # touch two files
        # get uptime of server
        for commandtoissue in CMDLIST:
            with open("serverresult.log", "a") as svrlog:
                print(cmdissue(sshsession, commandtoissue), file=svrlog)
            
        # close the connection
        sshsession.close()

def jsonastros():
    with open("astros.json", "r") as astrodata:
        astrostring = astrodata.read()
        
    # print("This is the NON string : " + astrostring)
    astrostringdecoded = json.loads(astrostring)
    # print("This is the JSONstring : " + str(astrostringdecoded))
    # print(astrostringdecoded['message'])
    
    numpeeps = astrostringdecoded['number']
    print("\nThe number of astros is: " + str(numpeeps))
    
    peeps = astrostringdecoded['people']
    print("The astro peep list is: " + str(peeps))
    
    x = 0
    for person in peeps:
        print(str(x) + ". " + str(person["name"]) + " is on " + str(person["craft"]))
        x=x+1

def jsonastrosURL():
    resp = urllib.request.urlopen("http://api.open-notify.org/astros.json")

    jstring = resp.read()

    pyj = json.loads(jstring)

    astrocosmo = pyj.get("people")

    print("\n This will print just names of ASTRO retrieved for JSON URL")
    for spaceperson in astrocosmo:
        print(spaceperson["name"])

def NASAjson():
    APIURL = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key="
    
    with open("nasa.key", "r") as keydata:
        key = keydata.read()
        APIURL = APIURL + str(key)
    # print("Compiled URL: " + str(APIURL))

    resp = requests.get(APIURL)
    nasajson = resp.json()

    # print(nasajson)
    # pprint.pprint(nasajson)

    for neo in nasajson["near_earth_objects"]:
        if neo["is_potentially_hazardous_asteroid"]:
            print("NEO NAME : " + str(neo["name"]) + "  *** NEARBY, ROCKET TO MARS NOW ****")
        else:
            print("NEO NAME : " + str(neo["name"]) + "  It's Faraway")

def D2LshowInstructions():
    print('''
RPG Game
========
Commands:
  go [directions]
  get [item]
  ''')

def D2LshowStatus():
    print('-----------------')
    print('You are in the ' + currentRoom)

    print('Inventory : ' + str(inventory))

    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print('------------------')

def D2Ldrawhouse():
    global hallitem
    global dineitem
    global kitcitem

    horzline= "|-------------|"
    verline = "|             |"
    space   = "  "
    hallline= verline
    dineline= verline
    kitcline= verline
    
    if currentRoom == 'Hall':
        hallline = "|     YOU     |"
    elif currentRoom == 'Dining Room':
        dineline= "|     YOU     |"
    elif currentRoom == 'Kitchen':
        kitcline= "|     YOU     |"
        
    try:
        if rooms['Hall']['item'] != 'key':
            nothing=nothing
    except:
        hallitem = verline

    try:
        if rooms['Dining Room']['item'] != 'potion':
            nothing=nothing
    except:
        dineitem = verline

    try:
        if rooms['Kitchen']['item'] != 'monster':
            nothing=nothing
    except:
        kitcitem = verline
        
    print(horzline + space + horzline)
    print(hallline + space + dineline)
    print("|    HALL     |" + space + "|   DINING    |")
    print(hallitem + space + dineitem)
    print(horzline + space + horzline)
    
    print(" ")
    
    print(horzline)
    print(kitcline)
    print("|   KITCHEN   |")
    print(kitcitem)
    print(horzline)
          
def Day2Lab():
    global inventory
    inventory = []

    global rooms
    rooms = { 'Hall':{'south':'Kitchen', 'east':'Dining Room', 'item':'key'},
              'Kitchen':{'north':'Hall', 'item':'monster'},
              'Dining Room':{'west':'Hall', 'south':'Garden', 'item':'potion'},
              'Garden':{'north':'Dining Room'} }

    global currentRoom
    currentRoom = 'Hall'

    global hallitem
    hallitem = "|     KEY     |"
    global dineitem
    dineitem = "|   POTION    |"
    global kitcitem
    kitcitem = "|   MONSTER   |"

    D2LshowInstructions()

    while True:
        D2Ldrawhouse()
        D2LshowStatus()

        global move
        move = ''
        while move == '':
            move = input('>')

        move = move.lower().split()

        if move[0] == 'go':
            if move[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[1]]
            else:
                print('You can\'t go that way!')
    
        if move[0] == 'get':
            if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                inventory += [move[1]]
                print(move[1] + 'got !')
                del rooms[currentRoom]['item']
            else:
                print('Can\'t get ' + move[1] + '!')

        if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
            print('A monster has got you... GAME OVER!')
            # break

        if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
            print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
            break
            

while True:
    print("\n 1. Print Student List as table from CSV")
    print(" 2. Print Student List as records from CSV")
    print(" 3. JSON ASTROS from file")
    print(" 4. JSON ASTROS from URL")
    print(" 5. NASA JSON")
    print(" 6. ROOMS - Day 2 Lab")
    print(" 7. SSH to user")
    print(" 0. Exit")
    selection = input("\nEnter your selection: ")
    selection = int(selection)
    if selection == 1:
        listrecord()
    elif selection == 2:
        listtable()
    elif selection == 3:
        jsonastros()
    elif selection == 4:
        jsonastrosURL()
    elif selection == 5:
        NASAjson()
    elif selection == 6:
        Day2Lab()
    elif selection == 7:
        sshtouser()
    elif selection == 0:
        print("Exiting... bye")
        break
    else:
        print("You did not enter a valid entry!")
        continue


