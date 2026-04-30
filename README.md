<div align="center">

# TrustCode

### Offline TOTP Secret Generator for Shared Verification

A clean local tool for creating authenticator-compatible TOTP secrets, designed for family anti-scam checks, private shared verification, and developer testing.

[English](#english) · [中文](#中文)

</div>

---

<a id="english"></a>

## What is TrustCode?

**TrustCode** is a lightweight local TOTP secret generator.

It creates a secret that can be imported into common authenticator apps such as Google Authenticator, Microsoft Authenticator, 1Password, Bitwarden, and other TOTP-compatible tools.

The project is designed around one simple idea: a shared time-based code can become a low-cost trust check between people who already know and trust each other.

For example, you and your family can store the same secret in your authenticator apps. If someone calls and claims to be you in an emergency, both sides can compare the current 6-digit code before taking action.

---

## Why it exists

Many scams rely on panic, urgency, and impersonation.

Traditional family passwords can be leaked, guessed, recorded, or obtained through social engineering. A time-based verification code changes regularly and can be generated locally by both trusted parties after the secret has been shared.

TrustCode turns a simple authenticator secret into a small shared trust protocol.

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
- Designed for personal safety, shared verification, and development testing

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

### Family anti-scam verification

Share one secret with trusted family members.

When someone claims to be a family member and asks for money, account access, verification codes, or urgent help, ask them to confirm the current code shown in the authenticator app.

If the code does not match, stop and verify through another trusted channel.

### Private shared verification

Friends, partners, classmates, or small teams can use a shared code as a lightweight identity confirmation method.

### Offline identity check

After the secret is imported, no internet connection is required. As long as both devices have accurate time, both sides can generate matching codes.

### Developer testing

Developers can quickly generate TOTP secrets and QR codes for testing 2FA onboarding, login systems, authenticator import flows, and internal demos.

### Plugin foundation

TrustCode can later be extended into browser extensions, Raycast or Alfred workflows, Obsidian plugins, VS Code utilities, iOS Shortcuts, local desktop widgets, or a family safety companion app.

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
totp authenticator 2fa security offline anti-scam verification python
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
- Add clear safety cards for family anti-scam use

---

## Disclaimer

TrustCode is provided for educational, personal, and development purposes.

It does not replace official 2FA systems, emergency services, banking verification, legal identity checks, or professional security tools.

---

<a id="中文"></a>

# 中文说明

## TrustCode是什么？

**TrustCode**是一个轻量的本地TOTP密钥生成器。

它可以生成能够导入Google Authenticator、Microsoft Authenticator、1Password、Bitwarden等验证器App的密钥。

这个项目的核心想法是：一个共同保存的动态验证码，可以成为亲友之间低成本的实时身份确认方式。

例如，你和家人提前保存同一个密钥。以后有人打电话冒充你，说自己遇到紧急情况、需要转账、需要验证码时，家人可以先要求对方说出当前6位动态码。

如果动态码对不上，就应立即停止操作，并通过其他可靠方式确认身份。

---

## 为什么做这个项目？

很多诈骗依赖紧张感、时间压力和身份冒充。

传统的家庭暗号可能被套话、录音、猜到或泄露。基于时间的动态验证码会定期变化，并且在密钥提前共享后，可以由双方在本地生成。

TrustCode把一个普通的验证器密钥变成了一个小型的共享信任机制。

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
- 适合个人安全、亲友验证和开发测试

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

### 家庭反诈骗确认

你可以和可信任的家人共享一个密钥。

当有人冒充亲属、朋友、客服、警察或平台工作人员，并要求转账、提供验证码、登录账户时，可以先要求对方说出当前动态码。

如果验证码不一致，应立即停止沟通，并通过其他方式确认。

### 朋友之间的实时暗号

朋友、情侣、同学、小团队可以使用同一个动态码作为轻量身份确认方式。

### 离线身份确认

导入密钥后，不需要网络。只要双方手机时间准确，就能生成相同的动态码。

### 开发测试工具

开发者可以用它快速生成TOTP密钥、二维码和当前验证码，用来测试登录系统、双重验证流程和验证器导入体验。

### 插件化基础

后续可以扩展成浏览器插件、Raycast插件、Alfred工作流、Obsidian插件、VS Code小工具、iOS快捷指令、本地桌面小组件或家庭安全码App。

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
- 增加给家人看的防诈骗提示卡片

---

## 免责声明

TrustCode仅用于教育、个人和开发测试目的。

它不能替代官方双重验证系统、紧急服务、银行验证、法律身份认证或专业安全工具。
