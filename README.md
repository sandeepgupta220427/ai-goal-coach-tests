# AI Goal Coach — Test Suite

A comprehensive automated test suite for the AI Goal Coach system.

## Project Structure
```
ai-goal-coach-tests/
├── mock/
│   └── mock_coach.py
├── tests/
│   ├── conftest.py
│   ├── test_schema.py
│   ├── test_functional.py
│   └── test_adversarial.py
├── TEST_STRATEGY.md
├── BUGS.md
├── requirements.txt
└── README.md
```

## Setup
pip install -r requirements.txt

## Run Tests
pytest tests/ -v

## 🐳 Running with Docker (Optional)

Build the Docker image:
```bash
docker build -t ai-goal-coach-tests .
```

Run the tests inside Docker:
```bash
docker run ai-goal-coach-tests
```
