from github import Github

class Insert_issue:
    def create_issue(self, username, password, repo, issue_name):
        try:
            g = Github(username, password)
            repo = g.get_repo(repo)  
            return repo.create_issue(title=issue_name)
        except Exception as ex:
            ex.data['message']
    
