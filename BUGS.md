# BUGS.md — AI Goal Coach Simulated Bug Report

## BUG-001: Empty Input Produces a Refined Goal
**Severity:** Critical
**Steps:** Call endpoint with input ""
**Expected:** refined_goal=null, confidence_score=0
**Actual:** Returns a valid refined goal (hallucination)
**Test:** test_adversarial.py → test_empty_string_gives_zero_confidence

## BUG-002: confidence_score Returned as Float
**Severity:** High
**Steps:** Call endpoint with any valid goal
**Expected:** confidence_score=8 (integer)
**Actual:** confidence_score=7.5 (float — wrong type)
**Test:** test_schema.py → test_confidence_score_is_integer

## BUG-003: SQL Injection Not Blocked
**Severity:** Critical
**Steps:** Call endpoint with "'; DROP TABLE goals; --"
**Expected:** refined_goal=null, confidence_score<=3
**Actual:** Returns a refined goal containing the injection string
**Test:** test_adversarial.py → test_sql_injection_is_blocked
