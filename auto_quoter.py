from github import Github
from dotenv import load_dotenv
import os


load_dotenv()
MAIL=os.getenv("MAIL")
PASSWORD=os.getenv("PASSWORD")
g=Github(MAIL, PASSWORD)
repos=g.search_repositories(query="language:python")
print(repos)
for repo in g.get_user().get_repos():
    print(repo.name)