---
name: humanizer-skills
description: Edit text so it stops reading like generic AI output (fewer detector-flagged patterns, more specific and varied prose) without changing facts. Use when the user asks to humanize, de-AI, or rewrite text to sound natural, pass or lower an AI-detector score, or audit a draft for AI tells. Includes an audit script that measures the patterns.
---

# Humanizer

Rewrite text so the patterns that detectors and experienced readers key on are gone and the writing is more specific, uneven and direct. Facts stay the same.

## Read this first: what this can and cannot do

Be blunt with the user about this when it matters.

- No edit guarantees a detector result. Detectors disagree with each other (false positive rates on human text range from 0% to 100% across 13 detectors in one preprint), and vendors update them. Never promise "0% AI".
- What does work is removing the real signals: low-surprise word choice, uniform rhythm, template phrases, vague claims, connector-heavy structure. Those edits also make the text better.
- Never invent facts, quotes, numbers, anecdotes or sources to sound human. If the text needs specifics it lacks, ask the user for them.
- Do not use character tricks (look-alike Unicode letters, zero-width characters, odd spacing). Detectors treat them as evasion (GPTZero has a dedicated "Shield" for it), and they corrupt the text.
- If the user must disclose AI use (school, journal, employer), say so once. Turnitin explicitly tries to detect text run through "humanizers".
- If the text is the user's own writing and flagged falsely, the better advice is process evidence: drafts, version history, notes. Non-native English writers get flagged far more often (61% average false positive rate on TOEFL essays across 7 detectors).

## Workflow

1. **Get inputs.** The text, the audience and venue, and ideally 1 to 3 samples of the user's own writing to match. If the text has no concrete detail (names, numbers, places, examples), ask for some before rewriting.
2. **Audit.** Save the text to a file and run:
   `python3 scripts/audit.py draft.txt`
   (or pipe it via stdin). Note the hit counts and the rhythm numbers. This is the "before" score.
3. **Rewrite in passes**, in this order (details and word tables in `references/patterns.md`):
   1. Cut residue and filler: "As an AI", "it is important to note", "in today's fast-paced world", closing summaries that restate the body, offers to help further.
   2. Fix words by fixing the claim. Do not swap "delve" for "explore" and keep the vague sentence; either state the concrete fact or delete the sentence. Synonym swapping changes the word, not the pattern.
   3. Strip connector scaffolding: most "Moreover / Furthermore / In addition" go. Use and, but, so, or start the next sentence.
   4. Make the rhythm uneven on purpose: a 4-word sentence after two long ones; sometimes a fragment. Do not make it random; each short sentence should carry a point.
   5. Prefer plain, everyday verbs and phrasal verbs (find out, set up, put off) over single formal verbs (ascertain, establish, utilize).
   6. Add the author's stance where one exists: an opinion, a doubt, a conclusion. Balanced surveys that never land read as AI.
   7. Formatting: remove bold on every label, title-case headings, emoji bullets, em dashes used as a tic, curly quotes in plain-text venues. Prose beats bullets unless the content is a list.
   8. Stop when the point is made. Cut redundancy and restated points; they are among the strongest cues experienced readers cite.
4. **Re-audit** with the script. Aim for: zero hits in residue and listed phrases, a low connector count, em dashes at or near zero unless the user's own samples use them, and sentence-length variation (the script reports a coefficient of variation; human prose is typically well above AI-uniform text, but treat it as a rough check, not a target to game).
5. **Report.** Give the rewritten text, then a short change log and the before/after audit numbers. State remaining risks plainly: short text (under about 300 words) is unreliable to score either way; formulaic genres (legal, patents, lab reports) look low-surprise even when human; no tool result is proof.

## Constraints while rewriting

- Preserve meaning, facts, names, numbers, citations and the requested tone. Keep technical terms that are the correct term.
- Do not downgrade correct grammar into errors. Occasional natural slips are a human trait, but injecting typos is a gimmick and hurts the reader. Only match errors or quirks that are in the user's own samples.
- Keep contractions in informal writing; keep register appropriate in formal writing. Formal does not mean AI, and "human" does not mean sloppy.
- Match the user's voice when samples exist: sentence length, vocabulary, punctuation habits, how they open and close.
- Do not add content to hit a length. Shorter is usually better.

## Before and after

AI-like:
> In today's fast-paced world, effective communication plays a crucial role in fostering strong teams. Moreover, it is important to note that regular meetings can significantly enhance collaboration.

Rewritten (only valid if the user supplied the facts):
> Our team stopped missing deadlines after we moved standup to 9:15. I think people were just awake by then.

What changed: filler opener removed, vague claim replaced by a specific, a small hedge ("I think") where the author is unsure, no announcement of importance.

If the user did not supply a fact, the honest rewrite is shorter, not invented:
> Regular meetings help teams collaborate, but only if people show up awake.

## Files

- `scripts/audit.py`: pattern and rhythm audit (stdlib only, no network).
- `references/patterns.md`: word and phrase tables with evidence tier, structural patterns, human tendencies.
- `references/evidence.md`: what detectors measure, accuracy findings, and sources.
