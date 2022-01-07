from utils.LoadYml import moorseUrl, moorseToken, moorseIntegration

import requests
import json

class MoorseMessageAPI:

    def sendMessage(toNumber, message):
        body = {'to': toNumber, 'body': message}
        header = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": moorseToken}
        response = requests.request("POST", moorseUrl + "v2/whatsapp/" + moorseIntegration + "/send-message", json=body, headers=header)
        return json.loads(response.text)


