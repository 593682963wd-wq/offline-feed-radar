# 离线订阅阅读雷达

保留RSS/Atom条目解析、稳定ID、去重、关键字排序、查询和摘要，输入仅为本地XML文本。

## 使用

Python 3.11+。在本目录建立独立虚拟环境：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python cli.py example.json
.venv/bin/python -m unittest discover -v
```

`example.json`从零编写，仅含虚构输入。可以显式提供自己的同结构JSON文件。输出默认为终端；`--output result.json`使用独占创建，避免覆盖已有结果。CLI失败退出码2。

## 数据与边界

不发现本机账号、不读取环境中的模型密钥、不发送消息、不请求远端数据。只处理调用方明确传入的文件、记录或参数。合成示例不代表任何实际业务结果。不包含原订阅清单、公司资料、HTTP抓取、AI排名或平台发布。

## 发布状态

本项目源码采用 MIT 许可证，见 LICENSE。依赖按各自上游许可使用，安装的依赖/模型/字体/媒体不随此源码目录分发。

## 2026-11-08 候选修订

- 稳定身份使用完整输入SHA256。
- Atom摘要缺失时读content。
- Atom优先alternate链接而非self。
- XML解析和安全异常转换为ValueError/CLI2。

使用包内合成样例复跑；发布集合根目录的 `verify_release.py --project personal-feed-radar` 会依次执行测试和首次使用命令。原有版本的测试计数属于当时记录，本轮汇总以集合验证报告为准。
