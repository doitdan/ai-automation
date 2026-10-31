# Toolbox

The toolbox fills itself on the first good run and pays off on the second.

## When to save

Right after your partner approves a result. Not before.

One exception: a rule file taken from a primary source (law, platform policy) is written before the first run, because the first run needs it.

## What to save

| Kind | Example | Where |
|------|---------|-------|
| Mechanical step as a script | pulling numbers out of an export | `scripts/<verb-noun>.py` with a small test |
| Template with placeholders | the email skeleton | `references/<name>-template.md` |
| Reference data | price list, link list, product names | `references/<name>.md`, or `knowledge/` when another skill needs it |
| Approved example | an output your partner sent as-is | `references/examples/<YYYY-MM-DD>-<label>.md` |
| Rule file | tone, format, banned words | `references/RULE.md`, or `knowledge/rules/` when shared |
| Repeated sub-prompt | a prompt reused inside a step | `references/<name>-prompt.md` |

## What not to save

- One-off outputs.
- Passwords, API keys, tokens, customer personal data.
- Client-confidential data: client names, recipients, account IDs, real results. The whole team installs this repo. Save an approved example with made-up names and numbers (업체 A, rounded fake figures), and keep the real client list where the team already keeps it; the skill points to that location.
- Drafts your partner has not approved.

## How to save

1. Save under a descriptive name. No dates or version numbers in tool names (`numbers-pull.py`, not `numbers-pull-v2.py`). Examples are the one exception: they carry the date they were approved.
2. Replace job-specific parts with `[bracketed placeholders]`. Keep one filled example directly below.
3. Edit the step in `SKILL.md` that uses it: name the file, when to use it, and when not to.
4. Add one row to `references/INDEX.md` for every saved file, scripts included (`../scripts/numbers-pull.py`). Create the index if it is missing.
5. A script gets a small test beside it (`scripts/test_<name>.py`). Run it with `python3 -m unittest discover -s scripts -p 'test_*.py'` from the skill folder.
6. A file two or more skills need goes to `knowledge/` with a row in `knowledge/INDEX.md`. Point to it; never copy it.

`references/INDEX.md`:

```markdown
# Files

| File | Purpose | Added |
|------|---------|-------|
| `client-update-template.md` | Email skeleton with placeholders | 2026-10-31 |
```

## Second run

Rerun the whole job from scratch, then report:

- saved files that were used
- anything rebuilt from nothing, each with "save next: <file name>"

## Upkeep

- One file per purpose. A new version replaces the old file; it never sits beside it.
- Two files with similar names doing different things → rename one so they cannot be confused.
- Once a month, delete files `INDEX.md` lists but no step uses.
