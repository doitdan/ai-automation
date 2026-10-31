# Proof

The AI saying the result looks fine is not evidence. Proof is a short list of checks that can fail, each backed by something outside the AI's own judgment.

## Evidence that counts

- A number traced to the source file it came from
- A link that opens
- A screenshot of the rendered output
- A test that passes
- A claim matched against a quote
- A count (words, rows, items)
- A value matched against a reference file

## Writing the checks

- 5 to 10 checks, specific to this job.
- Each check names what it is compared against.
- No quality adjectives: "clear", "professional", "high-quality", "accurate", "natural".
- Turn each "what bad looks like" answer from the interview into a check.
- A mechanical check (counting, matching numbers) becomes a script in `scripts/` and the check says to run it.

| Not a check | A check |
|-------------|---------|
| Numbers are accurate | Every number in the email appears in this week's export (`scripts/check-numbers.py` prints `ok`) |
| Concise | Body is 200 words or fewer |
| Right client | Client name matches the team's client sheet exactly |
| Professional tone | No word from `references/RULE.md` banned list appears |
| Follows up | Mentions every promise in last week's sent email |

## Checker jobs

A job that finds problems in someone's output (a compliance check, a reviewer agent) needs proof that it catches what it should and leaves the rest alone.

- Keep a set of known-bad inputs: each planted problem must be flagged. Grow it with every problem the checker once missed.
- Keep a set of known-clean inputs: they must produce no flags.
- Every flag quotes text that really appears in the input and names the rule it breaks.

Store both sets under `scripts/fixtures/` with each input's expected flags. Run the checker on every fixture, save its returns, and let a script score them against the expected flags. Rerun the whole set after every change to the checker.

A checker's PASS is not clearance. When the rules are legal or regulatory, the final call is a `Person:` step and the report says so.

## Running the checks

From now on, whenever the job is finished and before showing anything:

1. Run every check.
2. Fix what failed.
3. Run every check again.
4. Report one line per check: `PASS` or `FAIL`, then the evidence.
5. List what could not be verified and why. Never count it as passed.

```
PASS  numbers traced: check-numbers.py printed ok (14 numbers)
PASS  length: 176 words
FAIL  last week's promise: "landing page A/B result" not mentioned → added, rerun PASS
SKIP  link opens: no network in this session
```

## Stop rule

More than two checks fail on the first pass → stop. Do not patch the output. Name the process step that produced the failures and go to `fix-loop.md`.
