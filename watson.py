from ibm_watson import AssistantV1
import json

class Watson:
    def __init__(self):
        self.assistant = AssistantV1(
    iam_apikey='BG_afJLnGZhPiXcisACErbLpoRNHipA6RaeyFqotguP9',
    url='https://gateway.watsonplatform.net/assistant/api',
    version='2018-07-10')

    def message(self, message, context):
        content = self.assistant.message(
            workspace_id="ea4c42ba-73c5-43f1-beb9-07b6677f7b7a",
            input={
                'text': message
            },
            context = context
        ).get_result()
        return content


    #print(len(response['context']))
    #print(json.dumps(response['intents'][0]['intent']))