# STP – System Test Plan | DummyPay

> Draft template for the Product Manager. Complete verified details after product exploration.

## 1. Objective
Verify agreed behavior of DummyPay, a simulated payment system with no real money transfers (per assignment).

## 2. Scope
To be defined from the actual app and the assignment requirements.

## 3. Out of scope
To be agreed with the Product Manager. Do not assume unverified integrations.

## 4. Environments and tools
- Application: https://dummypay.vercel.app/
- Automation: Python, Pytest, Playwright
- Browser(s): To be agreed

## 5. Test strategy
- **Smoke:** short, high-priority checks of critical verified flows.
- **Regression:** wider checks of verified features after changes.
- **Nightly:** optional extended regression when scheduled.
- **Positive and negative:** target 3–5 each per verified screen, per assignment.

## 6. Entry / exit criteria
To be agreed after discovery and with the Product Manager.

## 7. Risks, dependencies and open questions
- Screens and navigation not yet mapped.
- Exact valid/invalid behavior and expected messages not yet verified.
- Test accounts, reset strategy, browsers and data policies still need agreement.

## 8. Deliverables
STP, STD (at least 30 prioritized test cases), POM code, execution reports, GitHub repository.
