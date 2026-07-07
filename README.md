# wxauto

`wxauto` 是一个基于 Windows UIAutomation 的微信桌面端自动化库，用于操作微信客户端、读取聊天内容、发送消息，以及构建简单的自动化处理流程。

这个仓库当前保存的是 `wxauto 3.9` 归档版本源码，适合学习桌面自动化、研究微信 PC 客户端交互逻辑

## 项目特性

- 支持连接和操作 Windows 微信客户端
- 支持发送文本消息和打字机模式消息
- 支持读取聊天记录与消息对象处理
- 支持监听指定会话并自动处理新消息
- 支持好友申请处理、消息转发、群相关操作
- 提供文档示例与基础测试代码

## 运行环境

本项目主要面向 Windows 环境。

| 项目 | 要求 |
| --- | --- |
| 操作系统 | Windows 10 / 11 / Server 2016+ |
| 微信客户端 | 微信 PC 3.9.x |
| Python | 3.8 - 3.15 |

## 安装依赖

建议先创建虚拟环境，再安装依赖：

```bash
pip install -e .
```

如果只想安装运行依赖，也可以按 `pyproject.toml` 中的声明手动安装：

```bash
pip install tenacity pywin32 pyperclip pillow psutil colorama comtypes
```

## 快速开始

### 1. 初始化微信实例

```python
from wxauto import WeChat

wx = WeChat()
```

### 2. 发送消息

```python
from wxauto import WeChat

wx = WeChat()
wx.SendMsg("你好，这是一条测试消息", who="张三")
```

### 3. 读取当前聊天窗口消息

```python
from wxauto import WeChat

wx = WeChat()
msgs = wx.GetAllMessage()

for msg in msgs:
    print(msg)
```

### 4. 监听并处理新消息

```python
from wxauto import WeChat

wx = WeChat()

def on_message(msg, chat):
    print(f"收到来自 {chat} 的消息: {msg}")

wx.AddListenChat(nickname="张三", callback=on_message)
wx.KeepRunning()
```

## 常见能力

结合仓库中的示例与源码，项目通常可用于以下场景：

- 自动发送单聊或群聊消息
- 监听指定联系人或群聊的新消息
- 提取聊天内容做记录或转发
- 自动处理图片、视频等消息附件
- 处理好友申请与基础群管理动作

更完整的示例可参考：

- `docs/example.md`
- `docs/class/`
- `tests/test_send_many_msg.py`

## 目录结构

```text
wxauto/
├─ wxauto/           # 核心库代码
├─ docs/             # 文档与示例
├─ tests/            # 测试与演示代码
├─ pyproject.toml    # 项目配置与依赖声明
└─ README.md         # 项目说明
```

## 开发说明

- 项目名称：`wxauto`
- 当前版本：`39.2.1`
- 主要入口：
  - `wxauto.WeChat`
  - `wxauto.utils`

如果你准备做二次开发，建议优先阅读以下文件：

- `wxauto/wxauto.py`
- `wxauto/utils.py`
- `wxauto/elements.py`

## 注意事项

- 本项目依赖 Windows 图形界面与 UIAutomation，通常无法在无桌面环境中正常工作
- 微信客户端版本差异可能影响控件定位与自动化稳定性
- 运行自动化脚本时，建议保持微信窗口状态稳定，避免频繁切换界面
- 部分功能与微信客户端行为强相关，升级客户端后可能需要重新适配

