import yaml

applicationConfig = open("../resources/application.yml", "r")

data = yaml.safe_load(applicationConfig)

moorseUrl = data["moorse"]["api"]["url"]
moorseIntegration = data["moorse"]["integration"]
moorseToken = data["moorse"]["token"]
port = data["server"]["port"]