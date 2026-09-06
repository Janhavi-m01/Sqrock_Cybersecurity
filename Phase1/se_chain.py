"""
se_chain.py — Security Engineering Chain Simulator
Final Cybersecurity Internship Project

Modules:
1. OSINT-style fictional profile
2. Phishing URL risk scoring
3. Security-awareness email simulation
4. Incident-response workflow

All examples are fictional and intended for defensive training.
"""

import re
import json
import datetime
from urllib.parse import urlparse


# ============================================================
# MODULE 1 — OSINT PROFILE SIMULATION
# ============================================================

def fictional_profile(username):
    profile = {
        "username": username,
        "name": "Alex Morgan",
        "company": "ExampleCorp",
        "location": "Training Environment",
        "public_repos": 12,
        "top_langs": {
            "Python": 5,
            "JavaScript": 3,
            "HTML": 2
        },
        "bio": "Software developer — fictional training profile"
    }

    print("\n=== OSINT PROFILE ===")
    print(json.dumps(profile, indent=2))

    return profile


# ============================================================
# MODULE 2 — PHISHING URL SCORER
# ============================================================

KEYWORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "bank",
    "paypal"
]


def phish_score(url):
    parsed = urlparse(url)

    score = 0

    if parsed.scheme != "https":
        score += 30

    for keyword in KEYWORDS:
        if keyword in parsed.netloc.lower():
            score += 20

    if parsed.netloc.count(".") > 3:
        score += 25

    if re.search(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
        parsed.netloc
    ):
        score += 40

    return min(score, 100)


# ============================================================
# MODULE 3 — SECURITY AWARENESS SIMULATION
# ============================================================

def awareness_template(profile):

    return f"""
=== SECURITY AWARENESS SIMULATION ===

Target Profile:
Name     : {profile['name']}
Company  : {profile['company']}
Location : {profile['location']}

This is a FICTIONAL training example.

Subject: Security Awareness Training Example

Hi {profile['name']},

This simulated message demonstrates common phishing indicators.

Indicators to look for:
- Urgent account-related language
- Requests to verify information
- Suspicious links
- Pressure to act quickly

Training Link:
https://lab.internal/awareness-test

ACTION:
Do not enter real credentials into simulated or suspicious pages.
Report suspicious messages through the organization's security process.

=== END SIMULATION ===
"""


# ============================================================
# MODULE 4 — INCIDENT RESPONSE
# ============================================================

def ir_response(incident):

    print("\n=== INCIDENT RESPONSE TRIGGERED ===")

    print(f"Time     : {datetime.datetime.now()}")
    print(f"Type     : {incident['type']}")
    print(f"Severity : {incident['severity']}")
    print(f"User     : {incident['user']}")

    actions = []

    if incident["severity"] in ("HIGH", "CRITICAL"):
        actions.extend([
            "Lock affected user account",
            "Revoke active sessions",
            "Notify SOC team",
            "Preserve relevant security logs"
        ])

    elif incident["severity"] == "MEDIUM":
        actions.extend([
            "Increase monitoring",
            "Review authentication activity",
            "Force password reset if required"
        ])

    else:
        actions.extend([
            "Monitor account activity",
            "Review relevant logs"
        ])

    if incident["type"] == "phishing":
        actions.extend([
            "Quarantine suspicious email",
            "Block malicious indicators",
            "Review related messages"
        ])

    print("\nActions Taken:")

    for action in actions:
        print(f"  [x] {action}")

    report = {
        "incident": incident,
        "actions": actions,
        "timestamp": str(datetime.datetime.now())
    }

    with open("ir_report.json", "w") as file:
        json.dump(report, file, indent=2)

    print("\n[+] IR report saved: ir_report.json")


# ============================================================
# MENU
# ============================================================

def menu():

    print("\n==============================================")
    print("       SECURITY ENGINEERING CHAIN")
    print("       FINAL INTERNSHIP PROJECT")
    print("==============================================")

    print("\nAvailable Modules:")
    print("[osint]     Run fictional OSINT profile")
    print("[phish]     Score a URL for phishing indicators")
    print("[template]  Generate awareness simulation")
    print("[ir]        Trigger incident response")
    print("[exit]      Quit")

    last_profile = None

    while True:

        choice = input("\nSelect module: ").strip().lower()

        # ---------------- OSINT ----------------
        if choice == "osint":

            username = input(
                "Enter fictional training username: "
            ).strip()

            if not username:
                username = "training_user"

            last_profile = fictional_profile(username)

        # ---------------- PHISH ----------------
        elif choice == "phish":

            url = input(
                "Enter URL to score: "
            ).strip()

            score = phish_score(url)

            print(f"\nPhishing Risk Score: {score}%")

            if score >= 70:
                print("Risk Level: HIGH")
            elif score >= 40:
                print("Risk Level: MEDIUM")
            else:
                print("Risk Level: LOW")

        # ---------------- TEMPLATE ----------------
        elif choice == "template":

            if last_profile is None:
                last_profile = fictional_profile(
                    "training_user"
                )

            print(
                awareness_template(last_profile)
            )

        # ---------------- IR ----------------
        elif choice == "ir":

            incident = {
                "type": "phishing",
                "severity": "HIGH",
                "user": "training_user"
            }

            ir_response(incident)

        # ---------------- EXIT ----------------
        elif choice == "exit":

            print("\nSecurity simulation completed.")
            print("Goodbye.")

            break

        else:

            print(
                "Invalid choice. "
                "Use osint, phish, template, ir, or exit."
            )


if __name__ == "__main__":
    menu()