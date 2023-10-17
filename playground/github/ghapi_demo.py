# pip install ghapi
import os
import time

from ghapi.core import GhApi
from ghapi.page import paged, pages


# => api limit of not-login user
# api = GhApi(limit_cb=_f)
# res = api['/repos/{owner}/{repo}'](owner='wdpm', repo='todo-dashboard')
# print(res)
# print(api.limit_rem)
# 51
# Quota remaining: 51 of 60

# => api limit of login user
# github_token = open(os.path.expanduser("~/.github_token")).read()
# api = GhApi(token=github_token)
# res = api['/repos/{owner}/{repo}'](owner='wdpm', repo='todo-dashboard')
# print(res)
# print(api.limit_rem)
# 4999

#  => repo list for org
# docs: https://ghapi.fast.ai/page.html#paged
# github_token = open(os.path.expanduser("~/.github_token")).read()
# api = GhApi(token=github_token)
# repos = paged(api.repos.list_for_org, org='mad-center')
# for page in repos:
#     print(len(page), page[0].name)

# 23 mad-player-experiment

# => get starred repo list
# activity https://ghapi.fast.ai/fullapi.html#activity
# activity.list_repos_starred_by_user(username, sort, direction, per_page, page): List repositories starred by a user
# github_token = open(os.path.expanduser("~/.github_token")).read()
# api = GhApi(token=github_token)
# # starred_page_1 = api.activity.list_repos_starred_by_user("wdpm", "created", "desc", 100, 6)
# # how to determine the last page number?
# starred_page_1 = api.activity.list_repos_starred_by_user("wdpm", "created", "desc", 100, 7)
# print(f'starred_page_1: ', len(starred_page_1))
#
# for idx, item in enumerate(starred_page_1):
#     print(idx, item.full_name)

# web page is 523, Here is 521. Why?

# => repos.list_for_user
github_token = open(os.path.expanduser("~/.github_token")).read()
api = GhApi(token=github_token)
# repos.list_for_user(username, type, sort, direction, per_page, page): List repositories for a user
# sort:
# - all 全部 89
# - owner owner是自己的仓库 84
# - member 作为成员参与的项目 5
start_1 = time.perf_counter()
user_repos_1 = api.repos.list_for_user("wdpm", "all", "updated", "desc", 100, 1)
end_1 = time.perf_counter()
print('TIME: ', end_1 - start_1)
# TIME:  22.5534004000001
print(f'user_repos_1: ', len(user_repos_1))

for idx, item in enumerate(user_repos_1):
    print(idx, item.full_name)
