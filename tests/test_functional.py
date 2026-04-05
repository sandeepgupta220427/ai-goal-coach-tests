# tests/test_functional.py
# These tests check that REAL, valid, normal user goals work correctly.
# This is called the "happy path" — things working as expected.

from mock.mock_coach import get_goal_coaching


class TestFunctional:

    def test_sales_goal_returns_high_confidence(self):
        """A real sales-related goal should get a confidence score of 6 or above"""
        result = get_goal_coaching("I want to improve my sales performance")
        assert result["confidence_score"] >= 6, \
            f"Expected confidence >= 6, got {result['confidence_score']}"

    def test_sales_goal_returns_non_empty_refined_goal(self):
        """A real goal must produce a refined goal string, not None or empty"""
        result = get_goal_coaching("I want to improve my sales performance")
        assert result["refined_goal"] is not None
        assert len(result["refined_goal"]) > 10, "Refined goal is too short"

    def test_leadership_goal_works(self):
        """Leadership goal should return correct structure with high confidence"""
        result = get_goal_coaching("I want to become a better team leader")
        assert result["confidence_score"] >= 6
        assert len(result["key_results"]) >= 3

    def test_learning_goal_works(self):
        """A learning/skill goal should be handled successfully"""
        result = get_goal_coaching("I want to learn data analysis")
        assert result["confidence_score"] >= 6
        assert result["refined_goal"] is not None

    def test_productivity_goal_works(self):
        """Productivity improvement goal should return proper response"""
        result = get_goal_coaching("I want to improve my productivity at work")
        assert result["confidence_score"] >= 6

    def test_refined_goal_is_a_string(self):
        """refined_goal must be a proper string for valid inputs"""
        result = get_goal_coaching("I want to get better at public speaking")
        assert isinstance(result["refined_goal"], str)

    def test_key_results_are_all_strings(self):
        """Every single item in key_results must be a string"""
        result = get_goal_coaching("I want to improve my time management")
        for item in result["key_results"]:
            assert isinstance(item, str), f"Key result is not a string: {item}"

    def test_key_results_are_not_empty_strings(self):
        """No key result should be an empty or blank string"""
        result = get_goal_coaching("I want to build better habits")
        for item in result["key_results"]:
            assert item.strip() != "", "Found an empty key result"
