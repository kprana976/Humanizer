# Humanizer

`humanizer-skills/` is a Claude skill that edits text to remove the patterns AI detectors and experienced readers key on, without changing facts.

- `SKILL.md`: workflow, constraints, honest limits
- `scripts/audit.py`: stdlib-only pattern and rhythm audit (`python3 scripts/audit.py draft.txt`)
- `references/`: pattern tables with evidence tiers, and an evidence summary

No edit guarantees a detector score. See `references/evidence.md`.
