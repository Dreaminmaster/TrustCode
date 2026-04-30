"""TrustCode: an offline TOTP secret generator.

This script creates a random TOTP secret and an authenticator-compatible
import URI. It uses pyotp instead of a custom cryptographic implementation.
"""

from __future__ import annotations

import time
from pathlib import Path

import pyotp
import qrcode

APP_NAME = "TrustCode"
DEFAULT_ACCOUNT = "shared-user"
DEFAULT_INTERVAL = 30
DEFAULT_DIGITS = 6


def create_secret() -> str:
    """Create a random Base32 TOTP secret."""
    return pyotp.random_base32()


def create_uri(secret: str, issuer: str = APP_NAME, account: str = DEFAULT_ACCOUNT) -> str:
    """Create an otpauth URI for authenticator apps."""
    totp = pyotp.TOTP(secret, digits=DEFAULT_DIGITS, interval=DEFAULT_INTERVAL)
    return totp.provisioning_uri(name=account, issuer_name=issuer)


def save_qr(uri: str, output: str = "trustcode_qr.png") -> Path:
    """Save the authenticator import URI as a QR code image."""
    path = Path(output)
    image = qrcode.make(uri)
    image.save(path)
    return path


def seconds_left() -> int:
    """Return seconds before the current code refreshes."""
    return DEFAULT_INTERVAL - (int(time.time()) % DEFAULT_INTERVAL)


def main() -> None:
    secret = create_secret()
    uri = create_uri(secret)
    qr_path = save_qr(uri)
    totp = pyotp.TOTP(secret, digits=DEFAULT_DIGITS, interval=DEFAULT_INTERVAL)

    print("=" * 60)
    print("TrustCode - Offline TOTP Secret Generator")
    print("=" * 60)
    print(f"Label: {APP_NAME}:{DEFAULT_ACCOUNT}")
    print("\nSecret:")
    print(secret)
    print("\nCurrent code:")
    print(totp.now())
    print(f"Refreshes in: {seconds_left()} seconds")
    print("\nAuthenticator URI:")
    print(uri)
    print(f"\nQR code saved to: {qr_path.resolve()}")
    print("\nSecurity reminder:")
    print("- Keep the secret private.")
    print("- Anyone with this secret can generate the same codes.")
    print("- Use shared secrets only with people you trust.")


if __name__ == "__main__":
    main()
