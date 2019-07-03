from watson import Watson
from issue import Insert_issue

watson = Watson()
insert_issue = Insert_issue()

context = {
    'timezone': 'America/Sao_Paulo'
}

while True:
    userinput = input("Sua mensagem: ")
    response = watson.message(userinput,context)
    if userinput == "abort":
        break
    print("BOT: " + response["output"]["text"][0])
    if response['context'] != context:
        context = response['context']
    if 'issue_name' in response['context']:
        insert_issue.create_issue(response['context'].pop('username',None), response['context'].pop('password',None), \
            response['context'].pop('repo',None), response['context'].pop('issue_name',None))