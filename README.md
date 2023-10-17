# todo-dashboard

> 这是一个早期的想法，未确定是否有进一步的开发打算。

Aim to manage GitHub repos and stars, Douban books, or manual plans.

## 初步设计

模块划分

- github star 和 github repo 管理

- 本地git repo status可视化。提醒及时提交

- 豆瓣书单 想读 已读 在读 管理

技术选型

- pywebview作为前端

数据持久化

- 用户配置，使用简单json文件读写，simplejson，tinydb。

- 常规数据缓存，sqlite。找一个API设计好一点的python client

