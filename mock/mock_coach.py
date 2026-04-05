# mock/mock_coach.py
# FAKE AI Goal Coach — simulates what the real AI would return.

def get_goal_coaching(user_input: str) -> dict:

    # Empty or whitespace input
    if not user_input or not user_input.strip():
        return {"refined_goal": None, "key_results": [], "confidence_score": 0}

    # Very short input
    if len(user_input.strip()) < 5:
        return {"refined_goal": None, "key_results": [], "confidence_score": 1}

    # Numbers-only input is not a goal
    if user_input.strip().isdigit():
        return {"refined_goal": None, "key_results": [], "confidence_score": 2}

    # Adversarial / unsafe / PII / injection patterns
    bad_patterns = [
        "drop table", "select *", "<script>",
        "ignore previous", "forget instructions",
        "ignore your instructions",
        "alert(", "--", "';",
        "personal details", "personal info",
        "other users", "show me your system prompt",
        "reveal", "extract data",
    ]
    lowered = user_input.lower()
    for pattern in bad_patterns:
        if pattern in lowered:
            return {"refined_goal": None, "key_results": [], "confidence_score": 1}

    # Profanity check
    profanity_list = ["badword1", "badword2"]
    for word in profanity_list:
        if word in lowered:
            return {"refined_goal": None, "key_results": [], "confidence_score": 2}

    # Valid goal — return proper structured response
    return {
        "refined_goal": (
            f"By Q3 2025, I will achieve measurable improvement in: "
            f"'{user_input.strip()}' by tracking weekly progress with clear metrics."
        ),
        "key_results": [
            "Complete 1 relevant course or training per month",
            "Track progress weekly using a measurable metric",
            "Get feedback from a mentor or manager every 2 weeks",
            "Achieve a 20% improvement by end of quarter"
        ],
        "confidence_score": 8
    }
