"""Short Password Auth (3 attempts, policy enforced)

Policy:
- Minimum length: 8 characters
- At least 1 uppercase letter
- At least 1 lowercase letter
- At least 1 digit
- At least 1 special character (!@#$%^&*())
"""

#Password Authentication System with Policy Enforcement

import re, sys
pwd = input("Password: ")

USER_DB = {"username": "StrongPass!23", "admin": "Admin@1234"}
SPECIALS = "!@#$%^&*()"


def validate_password(p: str):
    """Return (is_valid, missing_requirements_list)."""
    checks = {
        "≥8 chars": len(p) >= 8,
        "uppercase": re.search(r"[A-Z]", p),
        "lowercase": re.search(r"[a-z]", p),
        "digit": re.search(r"\d", p),
        "special (!@#$%^&*())": any(ch in SPECIALS for ch in p),
    }
    missing = [name for name, ok in checks.items() if not ok]
    return len(missing) == 0, missing


def authenticate(u: str, p: str) -> bool:
    return USER_DB.get(u) == p


def main():
    print("Welcome! You have 3 attempts.\nPassword policy: ≥8, upper, lower, digit, special (!@#$%^&*())")
    for attempt in range(1, 4):
        print(f"\nAttempt {attempt}/3")
        u = input("Username: ").strip()
        p = input("Password: ")

        if not u:
            print("Username cannot be empty.")
            continue

        ok, missing = validate_password(p)
        if not ok:
            print("Password needs:", ", ".join(missing))
            continue

        if authenticate(u, p):
            print(f"Login successful. Welcome, {u}!")
            return
        print("Invalid username or password.")

    print("\nToo many failed attempts. Access denied.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Bye!")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


