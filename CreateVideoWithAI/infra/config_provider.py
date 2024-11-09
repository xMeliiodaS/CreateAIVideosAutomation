import json


class ConfigProvider:
    @staticmethod
    def load_config_json():
        with open('C:\\Users\\user\\Documents\\GitHub\\CreateAIVideosAutomation\\'
                  'CreateVideoWithAI\\config.json', 'r') as file:
            return json.load(file)
