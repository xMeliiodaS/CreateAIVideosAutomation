import json


class ConfigProvider:
    @staticmethod
    def load_config_json():
        with open('C:\\Users\\Bahaa\\Desktop\\AI_Projects\\CreateAIVideosAutomation\\'
                  'CreateVideoWithAI\\config.json', 'r') as file:
            return json.load(file)

    @staticmethod
    def load_secret_config_json():
        with open('C:\\Users\\user\\Documents\\GitHub\\CreateAIVideosAutomation\\'
                  'CreateVideoWithAI\\secret.json', 'r') as file:
            return json.load(file)

    @staticmethod
    def load_prompt_config_text():
        with open('C:\\Users\\Bahaa\\Desktop\\AI_Projects\\CreateAIVideosAutomation\\'
                  'CreateVideoWithAI\\src\\prompts\\automation_prompts\\prompts.txt', 'r') as file:
            return json.load(file)
