# Evaluations — intent-refiner

## E1 — trigger

**Input:** "We need a way for admins to suspend an account. Maybe add a new service."

**Expected:** Produces outcome/success criteria/boundaries and does not require a new service without justification.

## E2 — minimality

**Input:** "Turn this rough Jira ticket into intent, but leave implementation open."

**Expected:** Creates minimum-sufficient intent and evidence requirements.

## E3 — non-trigger

**Input:** "The intent is already approved; tests failed on Unicode names. What should the next iteration be?"

**Expected:** Prefer progressive-intent/evidence-to-intent rather than re-refining the whole requirement.
