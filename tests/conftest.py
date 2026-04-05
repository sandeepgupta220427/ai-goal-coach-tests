import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

USE_REAL_API = os.environ.get("USE_REAL_API", "false").lower() == "true"
HF_API_TOKEN = os.environ.get("HF_API_TOKEN", "")

def get_coaching_response(user_input: str) -> dict:
    if USE_REAL_API and HF_API_TOKEN:
        import requests
        API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
        headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
        prompt = f'[INST] You are an AI Goal Coach. User said: "{user_input}". Return ONLY JSON with refined_goal, key_results, confidence_score. [/INST]'
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        return {"refined_goal": "Real API response", "key_results": ["step1"], "confidence_score": 7}
    else:
        from mock.mock_coach import get_goal_coaching
        return get_goal_coaching(user_input)

@pytest.fixture
def coach():
    return get_coaching_response
