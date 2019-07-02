from github import Github

def create_issue(username, password, repo, issue_name):
    g = Github(username, password)
    repo = g.get_repo(repo)  
    return repo.create_issue(title=issue_name)
    