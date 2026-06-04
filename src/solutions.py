"""
UZCARD Academy — Block 1: Python Basics
Week 01 | Lessons 4–13 Solutions & Quiz Answers
Author: Ibroximjon
"""


# ─────────────────────────────────────────────
# LESSON 4 — Functions & Collections
# ─────────────────────────────────────────────
# Quiz answers:
#   1. 1500 + 2300 + 15000 = 18800
#   2. Approved transactions total

def approved_total(txns):
    """Return total amount of approved transactions."""
    return sum(amount for amount, status in txns if status == "approved")


txns_l4 = [
    (1500, "approved"),
    (2300, "declined"),
    (890,  "approved"),
    (15000, "approved"),
]

if __name__ == "__main__":
    print("Lesson 4:", approved_total(txns_l4))  # 17390


# ─────────────────────────────────────────────
# LESSON 5 — Strings
# ─────────────────────────────────────────────
# Quiz answers:
#   1. ZCA
#   2. Python strings are immutable
#   3. strip()
#   4. "1,500"

def mask_card(card: str) -> str:
    """Return masked card number: first 4 + 8 stars + last 4."""
    return f"{card[:4]}{'*' * 8}{card[-4:]}"


if __name__ == "__main__":
    print("Lesson 5:", mask_card("8600123456781234"))  # 8600********1234


# ─────────────────────────────────────────────
# LESSON 6 — Lists & Sorting
# ─────────────────────────────────────────────
# Quiz answers:
#   1. None
#   2. append adds one element, extend adds each item from an iterable
#   3. [4, 6]
#   4. -1

def top_transactions(txns: list, n: int = 3) -> list:
    """Return top-N transactions by amount (descending)."""
    return sorted(txns, reverse=True)[:n]


txns_l6 = [1500, 2300, 890, 15000, 500, 7200, 3400]

if __name__ == "__main__":
    print("Lesson 6:", *top_transactions(txns_l6))  # 15000 7200 3400


# ─────────────────────────────────────────────
# LESSON 7 — Dicts & Sets
# ─────────────────────────────────────────────
# Quiz answers:
#   1. {} — empty dict
#   2. .get() returns None instead of raising KeyError
#   3. Lists are mutable (unhashable)
#   4. {2, 3}

def unique_currencies(txns: list) -> str:
    """Return sorted comma-separated unique currencies."""
    return ",".join(sorted({t["currency"] for t in txns}))


txns_l7 = [
    {"amount": 1500, "currency": "UZS"},
    {"amount": 50,   "currency": "USD"},
    {"amount": 890,  "currency": "UZS"},
    {"amount": 25,   "currency": "EUR"},
    {"amount": 60,   "currency": "RUB"},
    {"amount": 45,   "currency": "USD"},
]

if __name__ == "__main__":
    print("Lesson 7:", unique_currencies(txns_l7))  # EUR,RUB,USD,UZS


# ─────────────────────────────────────────────
# LESSON 8 — Functions (advanced)
# ─────────────────────────────────────────────
# Quiz answers:
#   1. None (no explicit return)
#   2. Mutable default arguments are shared across all calls
#   3. LEGB: Local → Enclosing → Global → Builtin

def commission(amount: float, rate: float = 0.01) -> float:
    """Calculate commission for a given amount and rate."""
    return amount * rate


if __name__ == "__main__":
    print("Lesson 8:", commission(150000), commission(150000, 0.015))  # 1500.0 2250.0


# ─────────────────────────────────────────────
# LESSON 9 — Lambda & Sorting Objects
# ─────────────────────────────────────────────
# Quiz answers:
#   1. tuple
#   2. *lst unpacks, lst is a single argument
#   3. Multi-line block with return

def top_customers_by_balance(customers: list) -> str:
    """Return customer names sorted by balance descending."""
    return ",".join(
        c["name"] for c in sorted(customers, key=lambda c: c["balance"], reverse=True)
    )


customers_l9 = [
    {"name": "Ali",     "balance": 1500},
    {"name": "Dilnoza", "balance": 23000},
    {"name": "Bobur",   "balance": 890},
]

if __name__ == "__main__":
    print("Lesson 9:", top_customers_by_balance(customers_l9))  # Dilnoza,Ali,Bobur


# ─────────────────────────────────────────────
# LESSON 10 — Virtual Environments
# ─────────────────────────────────────────────
# Quiz answers:
#   1. Isolate project dependencies
#   2. pip freeze writes current versions to a file
#   3. Name collisions, unclear origins
#   4. requirements.txt


# ─────────────────────────────────────────────
# LESSON 11 — File I/O
# ─────────────────────────────────────────────
# Quiz answers:
#   1. with guarantees file is closed even if an error occurs
#   2. 'w' overwrites, 'a' appends
#   3. for line in f:
#   4. utf-8

def parse_transaction_log(text: str) -> int:
    """Parse pipe-separated transaction log and return approved total."""
    total = 0
    for line in text.strip().splitlines():
        _, amount, status = [p.strip() for p in line.split("|")]
        if status == "approved":
            total += int(amount)
    return total


LOG = (
    "Ali | 1500 | approved\n"
    "Bobur | 5000 | declined\n"
    "Ali | 23000 | approved\n"
    "Dilnoza | 890 | approved"
)

if __name__ == "__main__":
    print("Lesson 11:", parse_transaction_log(LOG))  # 25390


# ─────────────────────────────────────────────
# LESSON 12 — JSON
# ─────────────────────────────────────────────
# Quiz answers:
#   1. dumps → string, dump → file
#   2. ensure_ascii=False prevents mangling Cyrillic/Uzbek chars
#   3. datetime is not JSON-serializable by default
#   4. JSON booleans are lowercase: true/false

import json


def max_amount_customer(raw_json: str) -> str:
    """Return the customer name with the highest transaction amount."""
    data = json.loads(raw_json)
    return max(data, key=lambda x: x["amount"])["customer"]


RAW = '[{"customer":"Ali","amount":1500},{"customer":"Bobur","amount":23000},{"customer":"Dilnoza","amount":890}]'

if __name__ == "__main__":
    print("Lesson 12:", max_amount_customer(RAW))  # Bobur


# ─────────────────────────────────────────────
# LESSON 13 — Error Handling
# ─────────────────────────────────────────────
# Quiz answers:
#   1. bare except catches everything including KeyboardInterrupt
#   2. finally always runs — with or without an exception
#   3. raise (bare) re-raises the current exception
#   4. Exception (base class for most built-in exceptions)

def safe_div(a: float, b: float):
    """Divide a by b; return 'error' on ZeroDivisionError."""
    try:
        return a / b
    except ZeroDivisionError:
        return "error"


if __name__ == "__main__":
    print("Lesson 13:", safe_div(10, 2), safe_div(5, 0))  # 5.0 error
