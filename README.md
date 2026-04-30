<div align="center">

# TrustCode

### Generate one-time trust codes for shared verification

A clean local TOTP toolkit for family trust checks, authenticator-compatible secrets, QR imports, private shared verification, and developer testing.

[English](#english) · [中文](#中文)

</div>

---

<a id="english"></a>

## What is TrustCode?

**TrustCode** is a lightweight local toolkit for generating TOTP secrets that work with common authenticator apps.

Its most relatable use is simple: trusted people can share one secret and compare the current code when identity matters. It can also be used for 2FA testing, QR-code onboarding demos, private group verification, and plugin prototypes.

TrustCode treats TOTP as more than a login feature. It turns any authenticator app into a small real-time trust signal.

---

## Why it is useful

In real life, identity is often checked in messy situations: urgent calls, account changes, payment requests, remote help, private groups, and temporary teams.

A TOTP secret is small, portable, and widely supported. Once imported into an authenticator app, it can produce a fresh code every 30 seconds without a server, account, cloud sync, or network connection.

That makes TrustCode useful for family safety, shared verification, offline identity checks, developer testing, and plugin experiments.

---

## Features

- Local-first secret generation
- No account required
- No cloud storage
- Authenticator-compatible import URI
- QR code export through the Python version
- Default label, no manual service or account input required
- English Python version
- Bilingual README
- Useful for family trust checks, development, prototyping, shared verification, and personal safety

---

## Why service name and account name are optional

The service name and account name are mainly display labels inside authenticator apps.

They do not decide the secret itself. They also do not decide whether two devices generate the same current code.

TrustCode uses a default label:

```text
TrustCode:shared-user
```

This keeps the flow simple: run the tool, save the secret or scan the QR code, and import it into your authenticator app.

---

## Use cases

### Family anti-scam trust check

Trusted family members can share one secret and compare the current code in suspicious or urgent situations.

For example, if someone claims to be a family member and asks for money, account access, verification codes, or urgent help, the current code can act as one extra trust check before taking action.

It should be treated as an additional safety step, not as the only proof of identity.

### 2FA development and testing

Generate test secrets and QR codes for login systems, authenticator onboarding, internal tools, demos, and security education.

### Plugin and automation foundation

TrustCode can become the base for a browser extension, Raycast extension, Alfred workflow, Obsidian plugin, VS Code utility, iOS Shortcut, or local desktop widget.

### Private shared verification

Friends, partners, classmates, or small teams can use a shared time-based code as a lightweight identity confirmation method.

### Offline identity check

After the secret is imported, no internet connection is required. As long as both devices have accurate time, both sides can generate matching codes.

---

## Python version

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python trustcode.py
```

The script generates:

- A random TOTP secret
- The current code preview
- An authenticator import URI
- A QR code image

---

## Recommended repository topics

```text
totp authenticator 2fa qrcode security offline verification anti-scam python developer-tools
```

---

## Security notes

TrustCode is a helper tool, not a replacement for official identity verification.

Please remember:

- Never publish your secret.
- Anyone with the same secret can generate the same codes.
- Use shared secrets only with people you trust.
- Do not use this as the only protection for financial, legal, medical, or emergency decisions.
- For high-risk situations, verify through multiple trusted channels.

---

## Roadmap

- Add a polished local browser interface
- Add optional custom labels
- Add local-only encrypted storage
- Add QR export improvements
- Add mobile-friendly PWA mode
- Add browser extension version
- Add simple cards for real-world verification scenarios

---

## Disclaimer

TrustCode is provided for educational, personal, and development purposes.

It does not replace official 2FA systems, emergency services, banking verification, legal identity checks, or professional security tools.

---

<a id="中文"></a>

# 中文说明

## TrustCode是什么？

**TrustCode**是一个轻量的本地TOTP工具，用来生成可以导入常见验证器App的密钥。

它最容易理解的用途是：可信任的人提前共享一个密钥，在需要确认身份时比对当前动态码。它也可以用于双重验证开发测试、二维码导入演示、私人小组确认和插件原型。

TrustCode不只是把TOTP当作登录安全功能，而是把任何验证器App变成一个小型实时信任信号。

---

## 为什么有用？

现实中的身份确认经常发生在混乱场景里：紧急电话、账号变更、付款请求、远程求助、私人群组和临时团队。

TOTP密钥体积小、便于保存，并且被大量验证器App支持。导入验证器App后，它可以在没有服务器、没有账号、没有云同步、没有网络的情况下，每30秒生成新的验证码。

这让TrustCode适合家庭安全、共享验证、离线身份确认、开发测试和插件实验。

---

## 功能特点

- 本地优先
- 不需要注册账号
- 不需要云端存储
- 支持验证器App导入链接
- Python版本支持二维码导出
- 默认标签，不需要手动输入服务名称和账号名称
- 提供英文Python版本
- README默认英文并提供中文说明
- 适合家庭信任确认、开发测试、原型设计、共享验证和个人安全场景

---

## 为什么可以去掉服务名称和账号名称？

服务名称和账号名称主要是验证器App里的显示标签。

它们不决定密钥本身，也不决定两台设备是否能生成相同的当前验证码。

TrustCode默认使用：

```text
TrustCode:shared-user
```

这样用户不需要输入额外信息，直接运行工具、保存密钥或扫描二维码即可。

---

## 使用场景

### 家庭反诈骗信任确认

可信任的家人可以共享一个密钥，在可疑或紧急场景下比对当前动态码。

比如有人冒充亲属、朋友、客服、警察或平台工作人员，并要求转账、提供验证码、登录账户时，可以先要求对方说出当前动态码。

它应被看作额外安全步骤，而不是唯一身份依据。

### 双重验证开发测试

生成测试用密钥和二维码，用于登录系统、验证器导入流程、内部工具、演示项目和安全教育。

### 插件和自动化基础

TrustCode后续可以扩展成浏览器插件、Raycast插件、Alfred工作流、Obsidian插件、VS Code小工具、iOS快捷指令或本地桌面小组件。

### 私人共享验证

朋友、情侣、同学、小团队可以使用同一个动态码作为轻量身份确认方式。

### 离线身份确认

导入密钥后，不需要网络。只要双方手机时间准确，就能生成相同的动态码。

---

## Python版本

安装依赖：

```bash
pip install -r requirements.txt
```

运行：

```bash
python trustcode.py
```

脚本会生成：

- 随机TOTP密钥
- 当前验证码预览
- 验证器导入链接
- 二维码图片

---

## 安全提醒

TrustCode是辅助工具，不能替代官方身份认证。

请注意：

- 不要公开你的密钥。
- 任何拿到同一个密钥的人都能生成相同验证码。
- 只应与可信任的人共享密钥。
- 不要把它作为金融、法律、医疗或紧急情况的唯一判断依据。
- 高风险场景下，应通过多个可靠渠道确认。

---

## 后续计划

- 增加更精致的本地网页界面
- 支持可选自定义标签
- 增加本地加密保存
- 优化二维码导出
- 增加手机PWA模式
- 增加浏览器插件版本
- 增加面向现实验证场景的简单提示卡片

---

## 免责声明

TrustCode仅用于教育、个人和开发测试目的。

它不能替代官方双重验证系统、紧急服务、银行验证、法律身份认证或专业安全工具。
