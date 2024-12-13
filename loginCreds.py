import json

def _fetchCreds(filePath):
    try: 
        file = open(filePath, 'r')
        data = json.load(file)
        return data

    except FileNotFoundError:
        return 'Error: the file was not found'
        

def getID(filePath = 'Creds.json'):
    return _fetchCreds(filePath)['ID']


def getSecret(filePath = 'Creds.json'):
    return _fetchCreds(filePath)['Secret']