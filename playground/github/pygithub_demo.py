import time

from github import Github  # https://github.com/PyGithub/PyGithub
import json
import os

g = Github(open(os.path.expanduser("~/.github_token")).read())

start_1 = time.perf_counter()
get_starred = list(g.get_user().get_starred())
end_1 = time.perf_counter()
print(f'{end_1 - start_1}', len(get_starred))

# 警告：github.PaginatedList.PaginatedList 非常慢，疑似顺序请求。

start_2 = time.perf_counter()
starred = []
for idx, repo in enumerate(get_starred):

    print(f'Processing... ${idx + 1}')
    # I find stars some of my own repositories, and I don't think
    # I actually did that; artefact of prior GitHub practices?
    if repo.owner.login != "wdpm":
        data = {
            "name": repo.name,
            "owner": repo.owner.login,
            "full_name": repo.full_name,
            "clone_url": repo.clone_url,
        }
        if repo.owner.name:
            data["owner_name"] = repo.owner.name
        if repo.owner.email:
            data["owner_email"] = repo.owner.email
        if repo.owner.avatar_url:
            data["owner_avatar_url"] = repo.owner.avatar_url
        if repo.description:
            data["description"] = repo.description
        if repo.homepage:
            data["homepage"] = repo.homepage

        # topics = repo.get_topics()  # removing this speeds up the program
        # if len(topics) != 0:
        #     data["topics"] = topics

        starred.append(data)

end_2 = time.perf_counter()
print(f'Use time(seconds): {end_2 - start_2}')

with open("pygithub_starred.json", encoding='utf-8', mode="w") as f:
    f.write(json.dumps(starred, ensure_ascii=False, indent=2))
