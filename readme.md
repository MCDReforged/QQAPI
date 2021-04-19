# CoolQAPI

> [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 的QQ开发API
>
> 事件功能参考了 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 的插件加载

## 环境要求

### 依赖的Python模块

已存储在 [requirements.txt](requirements.txt) 中, 可以使用 `pip install -r requirements.txt` 安装

## 使用

前往 [release](https://github.com/zhang-anzhi/CoolQAPI/releases) 页面下载最新的release并解压

### 配置QQ机器人

机器人建议使用 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)

如有问题可以在 MCDR 群内讨论或发 Issue

示例配置(请修改QQ号和密码)：

```yaml
account:
  uin: 123123123
  password: 'psasword'
  encrypt: false
  status: 0
  relogin:
    disabled: false
    delay: 3
    interval: 0
    max-times: 0
  use-sso-address: true
heartbeat:
  disabled: false
  interval: 5
message:
  post-format: array
  ignore-invalid-cqcode: false
  force-fragment: false
  fix-url: false
  proxy-rewrite: ''
  report-self-message: false
  remove-reply-at: false
  extra-reply-data: false
output:
  log-level: warn
  debug: false
default-middlewares: &default
  access-token: ''
  filter: ''
  rate-limit:
    enabled: false
    frequency: 1
    bucket: 1
servers:
  - http:
      disabled: false
      host: 127.0.0.1
      port: 5700
      timeout: 5
      middlewares:
        <<: *default
      post:
          - url: '127.0.0.1:5701/post'
  - ws:
      disabled: true
      host: 127.0.0.1
      port: 6700
      middlewares:
        <<: *default
  - ws-reverse:
      disabled: true
      universal: ws://your_websocket_universal.server
      api: ws://your_websocket_api.server
      event: ws://your_websocket_event.server
      reconnect-interval: 3000
      middlewares:
        <<: *default
  - pprof:
      disabled: true
      host: 127.0.0.1
      port: 7700
database:
  leveldb:
    enable: true
```

### 配置MCDR

将 `CoolQAPI-MCDR.py` 和 `CoolQAPI` 文件夹放入MCDR的plugins文件夹

重载MCDR

### 关于多服使用

`QQBridge` 可以将一个机器人接受的信息分发给多个服务器进行处理

这里是进行多个服务器配置的方法 [QQBridge使用文档](doc/QQBridge.md)

## 配置文件

配置文件位于 `CoolQAPI\config.yml`

`post_host`

默认值: `127.0.0.1`

接收转发消息的ip地址

`post_port`

默认值: `5701`

接收转发消息的端口

`post_path`

默认值: `post`

接收转发消息的路径

`api_host`

默认值: `127.0.0.1`

api的ip地址

`api_port`

默认值: `5700`

api的端口

`command_prefix`

默认值: `/`

触发命令事件的消息前缀

## 指令

| Command | Function |
| -| -|
| !!cq update | 检查并自动更新 |

## 开发

请阅读 [开发文档](doc/plugin.md) 了解开发相关内容
