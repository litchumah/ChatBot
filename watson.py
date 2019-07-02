from ibm_watson import AssistantV1
import json

assistant = AssistantV1(
    iam_apikey='BG_afJLnGZhPiXcisACErbLpoRNHipA6RaeyFqotguP9',
    url='https://gateway.watsonplatform.net/assistant/api',
    version='2018-07-10')

def message(message):
    content = assistant.message(
        workspace_id="d2d9d556-0fed-41c9-9963-5003ed00746d",
        input={
            'text': message
        }
    ).get_result()
    return content

response = assistant.list_workspaces(headers={'Custom-Header': 'custom_value'})

while True:
    x = input("Sua mensagem: ")
    if x == "abort":
        break
    else:
        print("BOT: " + message(x)["output"]["text"][0])
