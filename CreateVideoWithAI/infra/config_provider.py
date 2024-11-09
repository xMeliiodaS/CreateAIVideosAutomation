import json

class ConfigProvider:
    @staticmethod
    def load_config_json():
        with open('C:\\Users\\user\\PycharmProjects\\CreateVideoWithAI\\config.json', 'r') as file:
            return json.load(file)
