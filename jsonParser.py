import json

def jsonParser(filePath):
    try: 
        file = open(filePath, 'r')
        data = json.load(file)
        return data

    except FileNotFoundError:
        print('Error: the file was not found')


filePath = 'API_Resp_Connected_Realms'
parsedData = jsonParser(filePath)
connectedRealms = parsedData['realms']

for realm in connectedRealms:
    print(realm['name'], realm['id'] ) 