# Business Requirement: Challenge spec states refined_goal=String,
# key_results=Array[3-5], confidence_score=Integer(1-10)
# These tests verify the CONTRACT — not our mock implementation

# tests/test_schema.py
# These tests check that the AI response always has the correct structure/shape.
# Think of this like checking a form has all required fields filled in.

from mock.mock_coach import get_goal_coaching


class TestSchema:

    def test_response_has_refined_goal_field(self):
        """Response must always contain the 'refined_goal' key"""
        result = get_goal_coaching("I want to improve my sales skills")
        assert "refined_goal" in result, "Missing field: refined_goal"

    def test_response_has_key_results_field(self):
        """Response must always contain the 'key_results' key"""
        result = get_goal_coaching("I want to improve my sales skills")
        assert "key_results" in result, "Missing field: key_results"

    def test_response_has_confidence_score_field(self):
        """Response must always contain the 'confidence_score' key"""
        result = get_goal_coaching("I want to improve my sales skills")
        assert "confidence_score" in result, "Missing field: confidence_score"

    def test_key_results_is_a_list(self):
        """key_results must be a list/array, not a string or number"""
        result = get_goal_coaching("I want to lead a team")
        assert isinstance(result["key_results"], list), "key_results should be a list"

    def test_key_results_has_between_3_and_5_items(self):
        """For valid goals, key_results must have 3 to 5 items"""
        result = get_goal_coaching("I want to improve my communication skills")
        count = len(result["key_results"])
        assert 3 <= count <= 5, f"Expected 3-5 key results, got {count}"

    def test_confidence_score_is_integer(self):
        """confidence_score must be a whole number (not 8.5, not 'high')"""
        result = get_goal_coaching("I want to get promoted")
        assert isinstance(result["confidence_score"], int), "confidence_score must be int"

    def test_confidence_score_is_between_1_and_10(self):
        """confidence_score must always be between 1 and 10 (inclusive)"""
        result = get_goal_coaching("I want to get promoted")
        score = result["confidence_score"]
        assert 1 <= score <= 10, f"Score {score} is out of range 1-10"

    def test_refined_goal_is_string_or_none(self):
        """refined_goal must be either a string or None — never a number or list"""
        result = get_goal_coaching("I want to improve my writing")
        assert isinstance(result["refined_goal"], (str, type(None))), \
            "refined_goal must be a string or None"
