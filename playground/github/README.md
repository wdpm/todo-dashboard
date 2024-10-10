# Github

## API alternatives libraries

> Refer: https://docs.github.com/en/rest/overview/libraries?apiVersion=2022-11-28#python

- ~~gidgethub~~: [brettcannon/gidgethub](https://github.com/brettcannon/gidgethub)

  文档过于简略，没有足够的文档来说明API的使用，放弃。

- ghapi: [fastai/ghapi](https://github.com/fastai/ghapi)

  和Github Rest API文档保持同步，功能实现也很完整。很棒。

- ~~PyGithub~~: [PyGithub/PyGithub](https://github.com/PyGithub/PyGithub)

  性能太差，请求过慢。500个starred，请求了21s。而且 iter遍历是几分钟。还有Read Timeout。

- ~~libsaas~~: [duckboard/libsaas](https://github.com/ducksboard/libsaas)
  
  SaSS 工具库，不合适，抛弃。

- github3.py: [sigmavirus24/github3.py](https://github.com/sigmavirus24/github3.py)

  应该可行。文档也完备。https://github3.readthedocs.io/en/latest/narrative/getting-started.html#using-the-library

- ~~sanction~~: [demianbrecht/sanction](https://github.com/demianbrecht/sanction)

  孵化阶段，功能欠缺，文档欠缺。抛弃。

- ~~agithub~~: [jpaugh/agithub](https://github.com/jpaugh/agithub)

  关注点不集中，不单单是github api。功能文档欠缺。抛弃。

- ~~octohub~~: [turnkeylinux/octohub](https://github.com/turnkeylinux/octohub)

  功能非常有限，文档欠缺。抛弃。

- ~~github-flask~~: [github-flask (Official Website)](http://github-flask.readthedocs.org/)

  github api for flask framework。不合适。

- ~~torngithub~~: [jkeylu/torngithub](https://github.com/jkeylu/torngithub)

  tornado 扩展。不合适。而且功能文档欠缺。

- ~~githubkit~~: [yanyongyu/githubkit](https://github.com/yanyongyu/githubkit)

  不成熟，抛弃。

- ~~octokit.py~~: [khornberg/octokit.py](https://github.com/khornberg/octokit.py)

  孵化早期阶段，一堆TODO。抛弃。

- ~~aiogithubapi~~: https://github.com/ludeeus/aiogithubapi
  
  API 不完善。抛弃。
- gitpython: https://gitpython.readthedocs.io/en/stable/tutorial.html#tutorial-label
 
  管理 Git 本地仓库的python工具库。可能有用。目前处于维护状态。

## documentation

- [Github 官方文档](https://docs.github.com/zh) - 按需粗略阅读一次。以及当作工具书来查询参考。

## github actions

- [lychee-action](https://github.com/lycheeverse/lychee-action) - 检测 md 中的 link 是否可访问，用于一些 awesome-? 的聚合 project。
- [read-file](https://github.com/marketplace/actions/read-file) - 读取 repo 下某一个路径的文件内容，可以用于提取 metadata。
  例如：为 mad-center 创建一个 dashboard，列出所有项目当前的开发状态以及其他信息。

## 管理多个本地 repos

本地一般有很多个 git repos，如果能有一个工具，可以快速检测出所有 git 仓库的当前 state，并输出概要描述信息，
那将非常有帮助，这可以减少记忆的心智负担。

下面是一些调研得到的方案。

> https://myrepos.branchable.com/ 这个网址的 "related software" 章节提供了很多选择。

- [ ] [git-status-all](https://github.com/reednj/git-status-all) - 基于 Ruby，非常简洁。
- [ ] [gr](https://github.com/mixu/gr) - 基于 Node。
- [ ] [~~multi-git-status~~](https://github.com/fboender/multi-git-status)
    - 基本不处理 edge cases，输出信息不正确。不推荐。
- [ ] [git-plus](https://github.com/tkrajina/git-plus)
- [ ] [gita](https://github.com/nosarthur/gita)
- [x] https://stackoverflow.com/a/41274966 - bash script，推荐。
  > `find . -name .git -print -execdir git status \;`