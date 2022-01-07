from flask import Flask, Blueprint, request
from services.BotService import BotService

webhook = Blueprint('webhook',__name__)

@webhook.route("/webhooks", methods=["POST"])
def hello_world():
    data = request.get_json()
    print(data)
    if(data["status"] == "RECEIVED"):
        BotService.handleMessage(**data)
    return "OK"