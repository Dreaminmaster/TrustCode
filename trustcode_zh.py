"""TrustCode 中文版：本地 TOTP 密钥生成器。

运行后会生成一个可导入 Google Authenticator、Microsoft Authenticator、
1Password、Bitwarden 等验证器 App 的密钥和二维码。
"""

from __future__ import annotations

import time
from pathlib import Path

import pyotp
import qrcode

应用名称 = "TrustCode"
默认账号 = "shared-user"
刷新间隔 = 30
验证码位数 = 6


def 生成密钥() -> str:
    """生成随机 Base32 格式的 TOTP 密钥。"""
    return pyotp.random_base32()


def 生成导入链接(密钥: str, 服务名称: str = 应用名称, 账号名称: str = 默认账号) -> str:
    """生成验证器 App 可识别的 otpauth 导入链接。"""
    totp = pyotp.TOTP(密钥, digits=验证码位数, interval=刷新间隔)
    return totp.provisioning_uri(name=账号名称, issuer_name=服务名称)


def 保存二维码(导入链接: str, 输出文件: str = "trustcode_qr_zh.png") -> Path:
    """把导入链接保存为二维码图片。"""
    路径 = Path(输出文件)
    图片 = qrcode.make(导入链接)
    图片.save(路径)
    return 路径


def 剩余秒数() -> int:
    """返回当前验证码距离刷新还剩多少秒。"""
    return 刷新间隔 - (int(time.time()) % 刷新间隔)


def main() -> None:
    密钥 = 生成密钥()
    导入链接 = 生成导入链接(密钥)
    二维码路径 = 保存二维码(导入链接)
    totp = pyotp.TOTP(密钥, digits=验证码位数, interval=刷新间隔)

    print("=" * 60)
    print("TrustCode - 本地 TOTP 密钥生成器")
    print("=" * 60)
    print(f"显示标签：{应用名称}:{默认账号}")
    print("\n密钥：")
    print(密钥)
    print("\n当前验证码：")
    print(totp.now())
    print(f"距离刷新还剩：{剩余秒数()} 秒")
    print("\n验证器导入链接：")
    print(导入链接)
    print(f"\n二维码已保存到：{二维码路径.resolve()}")
    print("\n安全提醒：")
    print("- 不要公开你的密钥。")
    print("- 任何拿到同一个密钥的人都能生成相同验证码。")
    print("- 共享密钥只适合可信任的人之间使用。")


if __name__ == "__main__":
    main()
