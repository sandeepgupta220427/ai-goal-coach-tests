# AI Goal Coach — Test Suite

Built by Sandeep Gupta
Senior SDET Challenge — LeadVenture AI Accelerator Group

---

## What This Project Is

This is a test suite for an AI system called the Goal Coach.
The Goal Coach takes a vague goal from an employee and returns
a refined goal, action steps, and a confidence score.

My job was not to build the AI. My job was to test it —
to make sure it works correctly, handles bad inputs safely,
and never makes things up when given garbage input.

I built 31 automated tests that prove all of this.
They all run automatically on GitHub every time I push code.

---

## Folder Structure

```
ai-goal-coach-tests/
│
├── mock/
│   ├── mock_coach.py     → The fake AI I built for testing
│   └── __init__.py       → Makes Python treat this as a package
│
├── tests/
│   ├── test_schema.py       → 8 tests — does response have right structure?
│   ├── test_functional.py   → 8 tests — do real goals work correctly?
│   ├── test_adversarial.py  → 15 tests — are bad inputs blocked safely?
│   ├── conftest.py          → Shared setup + mock/real API switch
│   └── __init__.py          → Makes Python treat this as a package
│
├── .github/
│   └── workflows/
│       └── python-tests.yml → Runs all 31 tests automatically on push
│
├── TEST_STRATEGY.md   → My full testing plan and thinking
├── BUGS.md            → 3 bugs with exact reproduction steps
├── README.md          → This file — how to set up and run
├── requirements.txt   → Python tools this project needs
└── .gitignore         → Stops junk files going to GitHub
```

---

## How to Set Up and Run

### Step 1 — Check Python is installed
```bash
python3 --version
```
You need Python 3.10 or above.

### Step 2 — Clone the project
```bash
git clone https://github.com/sandeepgupta220427/ai-goal-coach-tests.git
cd ai-goal-coach-tests
```

### Step 3 — Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4 — Install the tools
```bash
pip install -r requirements.txt
```

### Step 5 — Run all 31 tests
```bash
pytest tests/ -v
```

You should see all 31 tests pass with green text.

---

## Running Specific Groups

```bash
# Only schema tests — checks JSON structure
pytest tests/test_schema.py -v

# Only functional tests — checks real goals work
pytest tests/test_functional.py -v

# Only adversarial tests — checks bad inputs blocked
pytest tests/test_adversarial.py -v

# Run with a saved report file
pytest tests/ -v --junitxml=report.xml
```

---

## What the 3 Test Files Actually Do

**test_schema.py — 8 tests**

Checks that every single response always has the right structure.
Is confidence_score always a whole number between 1 and 10?
Is key_results always a list — never a string?
Are all 3 fields always present — never missing?
These 8 tests run first and run fast.

**test_functional.py — 8 tests**

Checks that real goals from real employees work correctly.
Sales goals, leadership goals, learning goals, productivity goals.
Do they all come back with confidence 6 or above, a proper
refined goal sentence, and 3 to 5 real action steps?

**test_adversarial.py — 15 tests**

Checks that the system handles bad, weird, and dangerous
inputs without crashing or making anything up.
Empty input, SQL injection, script tag attacks, prompt injection,
PII leakage attempts, Chinese characters, emoji, extremely long
text — none of these should produce a hallucinated goal.
These are the edge cases most test suites never think about.

---

## Why I Used a Mock Instead of the Real API

I used a fake version of the AI instead of the real
Hugging Face API. Here is my thinking:

If I used the real API for every test run:
- Tests would fail if the internet goes down
- Tests would fail if Hugging Face has an outage
- Every test run would cost API credits
- Each test would take 3 to 5 seconds instead of milliseconds

With the mock I control exactly what the fake AI returns.
Tests are fast, free, and always give the same result.
This is how professional test suites work in real companies.

**To run the same tests against the real Hugging Face API:**
```bash
export USE_REAL_API=true
export HF_API_TOKEN=your_token_here
pytest tests/ -v
```
Same 31 tests. Real AI. No code changes needed.

---

## What Runs Automatically on GitHub

Every time I push code to GitHub, all 31 tests run
automatically via GitHub Actions. You can see this
under the Actions tab in the repository.

- Green tick means all 31 tests passed
- Red cross means something broke and the merge is blocked

This means nobody has to remember to run tests manually.
Problems are caught before they reach production.

---

## How to Run with Docker (Optional Bonus)

If you have Docker installed:

**Build the image:**
```bash
docker build -t ai-goal-coach-tests .
```

**Run the tests inside Docker:**
```bash
docker run ai-goal-coach-tests
```

This is useful for running tests in a clean environment
that matches exactly what GitHub Actions uses.

---

## Documents in This Project

**TEST_STRATEGY.md**
My full thinking about what to test and why.
Covers schema testing, functional testing, adversarial testing,
how CI/CD is set up, what to do when the AI model changes,
13 risks I identified with mitigations, logging and monitoring
plan for production, and the confidence score quality gateway.

**BUGS.md**
Three bugs I found in this type of system.
Each one has exact steps to reproduce it, the expected response,
the actual buggy response, why the bug happens, the real world
impact, and the exact test that catches it automatically.

---

## Requirements

```
pytest        — runs all the tests
requests      — makes HTTP calls to real API
jsonschema    — validates JSON structure
pydantic      — data type validation
```

Install all at once:
```bash
pip install -r requirements.txt
```
