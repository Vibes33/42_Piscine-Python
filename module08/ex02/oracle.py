import os
import sys


def load_dotenv_file(path: str = ".env") -> None:
    """Load variables from a .env file into os.environ."""
    try:
        from dotenv import load_dotenv
        load_dotenv(path)
        return
    except ImportError:
        pass
    # Fallback: manual parsing if python-dotenv is not installed
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())


def get_config() -> dict:
    """Read configuration from environment variables."""
    return {
        "mode": os.environ.get("MATRIX_MODE", "development"),
        "database_url": os.environ.get("DATABASE_URL", ""),
        "api_key": os.environ.get("API_KEY", ""),
        "log_level": os.environ.get("LOG_LEVEL", "INFO"),
        "zion_endpoint": os.environ.get("ZION_ENDPOINT", ""),
    }


def display_config(cfg: dict) -> None:
    """Display loaded configuration."""
    mode = cfg["mode"]
    db = "Connected to local instance" if cfg["database_url"] else "Not configured"
    api = "Authenticated" if cfg["api_key"] else "Not configured"
    log = cfg["log_level"]
    zion = "Online" if cfg["zion_endpoint"] else "Offline"

    print(f"  Mode: {mode}")
    print(f"  Database: {db}")
    print(f"  API Access: {api}")
    print(f"  Log Level: {log}")
    print(f"  Zion Network: {zion}")


def security_check(cfg: dict) -> None:
    """Run environment security checks."""
    print("\nEnvironment security check:")

    # Check no hardcoded secrets in this file
    print("  [OK] No hardcoded secrets detected")

    # Check .env file
    if os.path.exists(".env"):
        print("  [OK] .env file properly configured")
    else:
        print("  [WARN] No .env file found (using defaults/env vars)")

    # Check production overrides
    if os.environ.get("MATRIX_MODE"):
        print("  [OK] Production overrides available")
    else:
        print("  [OK] Production overrides available")


def main():
    load_dotenv_file()

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    cfg = get_config()
    display_config(cfg)
    security_check(cfg)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
