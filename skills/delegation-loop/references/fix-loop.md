# Fix Loop

A wrong result is fixed in the playbook so the next run does not repeat it. Enter here directly when an existing skill or agent gave a wrong result; skip the gate and the interview.

## 1. Describe

Write exactly what went wrong: which output, which part, what it said, what it should have said.

## 2. Diagnose the layer

| Layer | Signs |
|-------|-------|
| Process | A step is missing, in the wrong order, or a decision's rule was never written down |
| Toolbox | Something was rebuilt that already exists, or a saved file is outdated or wrong |
| Proof | No check would have caught the mistake |

Has this happened before? It has when `notes.md` records it or your partner says so.

Tell your partner the layer and why in two sentences. A failure can sit in two layers, for example a made-up number is a process gap (no rule on where numbers come from) and a proof gap (no check that traces them). Name both and fix both.

## 3. Smallest durable fix

- Change only the failed layer. Never rewrite the whole playbook.
- Process → add or reorder the step, or write the decision as "If X, then Y".
- Toolbox → replace the outdated file, or point the step at the file it ignored.
- Proof → add the check that would have failed, as a script when it is mechanical.
- The same mistake twice → an explicit rule that blocks it, ideally a check that fails, not a softer reminder.
- The fix needs a rule only your partner can set (for example whether a calculated metric counts as sourced) → apply the safest rule now and ask the question in your report.
- `notes.md` or `references/INDEX.md` missing → create them as `skill-template.md` describes.

## 4. Log

Add one line at the top of `skills/<job>/notes.md`, under the heading:

```
- 2026-10-31 | proof | CTR 3.2% not in the export | added check-numbers.py to Done when
```

Format: date | layer | what went wrong | what changed. Newest first.

## 5. Rerun and compare

Rerun the same job from scratch with the same input. Show before and after side by side, with the proof report. The fix counts only when the after run passes.

The original input is not available → build a made-up input that reproduces the failure, show before and after on it, say the real rerun is still owed, and tell your partner not to use the real output until it is done.

## 6. Close

- `CHANGELOG.md` line and `python3 scripts/validate.py`.
- Fewer than five checks in `## Done when` → offer a Phase 3 pass (`proof.md`) as the next step.
- The skill has no routing row → propose one; do not add it unasked.

## Monthly

Read `notes.md` once a month. Several lines in the same layer mean that layer needs a bigger rework, or that part of the job is a candidate for the next skill.

## If you cannot write files

Print the full changed file, the exact path, and tell your partner to replace the old copy.
