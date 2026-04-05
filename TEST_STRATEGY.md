# TEST_STRATEGY.md — AI Goal Coach

## 1. What We Test
- Schema validation (all 3 fields always present)
- Functional/happy path (real goals return good responses)
- Adversarial inputs (empty, SQL injection, XSS, gibberish)
- Security (no hallucination for unsafe inputs)
- Regression (tests catch model drift)

## 2. CI/CD Structure
- pytest runs on every pull request
- Any failure blocks the merge
- JUnit XML report generated for dashboards

## 3. Regression Strategy
- Golden dataset of 10-20 known inputs maintained
- Schema tests catch any field changes immediately
- Confidence score range tests catch model drift

## 4. Major Risks & Mitigations
| Risk | Mitigation |
|------|-----------|
| AI hallucinates for nonsense input | Adversarial tests + confidence threshold |
| Schema changes without notice | Schema validation on every CI run |
| Prompt injection bypasses guardrails | Dedicated injection test cases |
| Model API goes down | Mock/stub used locally |

## 5. Logging & Observability
- Log every input, response time, confidence score
- Alert if confidence=0 rate exceeds 5%
- Alert if response time exceeds 5 seconds
- Track score distribution over time
