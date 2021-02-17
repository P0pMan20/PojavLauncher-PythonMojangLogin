#mojang auth
import requests
import uuid
import json
import sys

if len(sys.argv) == 3:
    username = sys.argv[1]
    password = sys.argv[2]
else:
    username = "username" #Put username or email here
    password = "password" #Put password here
url = "https://authserver.mojang.com"   
headers = {'Content-Type': 'application/json'}
uuid = str(uuid.uuid4())
selectedVersion = "1.16.5" #Enter version string here ie 1.16.5 or fabric-loader-0.11.1-1.16.5

data = {"agent": { "name" : "Minecraft", "version": 1}, "username": username, "password": password,
"clientToken": uuid, "requestUser": False}


p = requests.post(url + '/authenticate', headers=headers, json=data)
#print(p.json())
pjson = p.json()


output = { "accessToken": pjson['accessToken'],
"clientToken": pjson['clientToken'], 
"profileId":pjson['selectedProfile']['id'],
'username': pjson['selectedProfile']['name'],
"selectedVersion": selectedVersion,
"isMicrosoft": False,
"msaRefreshToken": 0}
#print(output)
try:
    with open('.pojavlauncher/accounts/' + pjson['selectedProfile']['name'] + '.json', 'w+') as f:
        json.dump(output, f)

        

except FileNotFoundError:
    print('Please run this in /var/mobile/Documents and ensure you have ran PojavLauncher and Minecraft once.')
    exit()
print('logged in')
