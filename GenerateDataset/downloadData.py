from github import Github
from datetime import datetime
import time
import os

ACCESS_TOKEN = "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"
g = Github(ACCESS_TOKEN)

end_time = time.time()
start_time =  end_time - 86400



for i in range(3):
    start_time_str = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
    end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')

    query = f"language:python created:{start_time_str}..{end_time_str}";
    

    result = g.search_repositories(query)

    end_time -= 86400
    start_time -= 86400

    

    for repository in result:
        print(repository.name)
        os.system(f"git clone {repository.clone_url} repos/{repository.owner.login}/{repository.name}")
        
    
    

  
