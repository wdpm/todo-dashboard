# Douban 豆瓣

## API libraries

- [ ] [豆坟](https://github.com/doufen-org/tofu)

  用于备份 douban 的浏览器扩展。这个项目的完成度很高，暂时用不到这个项目。
- [ ] ~~[ 同步豆瓣标记条目到 Notion/NeoDB](https://github.com/bambooom/douban-backup)~~

  基于 JS 实现的油猴脚本，先是导出 csv，然后再 notion 新建 database，然后导入 csv。数据同步：
  - 人工 update 导入的 CSV 文件，然后再次写入 notion database。
  - 使用 GitHub Actions 定时从 RSS 信息更新 Notion。缺点是仅有保留最新的 10 条信息，也就是如果在一个更新周期间隔内，
    你标记了超过10条数据记录，那么就会丢数据。

  代码质量一般。应该暂时用不到。
- [ ] ~~[notion_sync_data](https://github.com/Qliangw/notion_sync_data)~~

  基于Python实现。代码质量一般，可以稍微看看API请求部分就可以了，用处不大。
- [ ] [ 用于同步豆瓣读书观影记录到 Notion](https://github.com/lccurious/notion-transfer)