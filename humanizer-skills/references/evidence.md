# Evidence summary and limits

Condensed from a research report dated 2026-10-06. Items marked (preprint) are not peer reviewed. Most studies tested ChatGPT-family text; newer models may differ. Detector products change often, so any number here may be out of date. The original report lists full citations; the key sources are below.

## Three detector types

1. **Statistical scoring** (perplexity, burstiness, curvature: DetectGPT, Fast-DetectGPT, Binoculars). Low surprise means likely AI. Fails on constrained human writing: false positive rates of 61% to 81% on granted patent claims (preprint). Binoculars flagged the US Constitution as machine-generated.
2. **Trained classifiers** (Turnitin, GPTZero, Pangram, Originality.ai, Copyleaks). Strong in-domain, weak out of distribution. RAID benchmark (6M+ generations, 11 attacks): easily fooled by adversarial attacks, sampling changes and unseen models. Recursive paraphrasing erodes detection (Sadasivan et al.). OpenAI retired its own classifier in 2023: it caught 26% of AI text and flagged 9% of human text.
3. **Watermarks.** Planted at generation time and checkable only by whoever holds the scheme. Turnitin and GPTZero cannot see one. No public documentation that Claude output carries a watermark; unproven either way. Detectors flag style, not a mark.

## Accuracy, independent results

| Study | Finding |
| --- | --- |
| Liang et al. 2023 | 7 detectors, 91 TOEFL essays: 61.22% average false positive rate; 97.8% flagged by at least one. Prompting for richer vocabulary cut it to 11.77%; rewriting AI essays in a literary style cut detection from 100% to 13% |
| Weber-Wulff et al. 2023 | 14 tools "neither accurate nor reliable"; worse after obfuscation or machine translation |
| Liu et al. 2024 | AI text rephrased with Wordtune: Originality.ai caught 100%, ZeroGPT 88%, Turnitin 30% |
| Hadra et al. 2026 | Turnitin accuracy 0.61, Originality 0.69 on mixed EFL/professional/AI/hybrid text; poor on hybrid |
| Park et al. 2026 (preprint) | 13 detectors, 135,389 manuscript pairs: false positives on human text from 0% to 100% depending on detector; professional editing shifts scores unpredictably |
| Jiang et al. 2024 | Counterexample: near-perfect accuracy on GRE essays in one controlled, in-domain setting |

## Humans are not a better fallback

Lecturers spotted 57% of AI excerpts (Fiedler 2025); teachers could not tell ChatGPT from student essays and were overconfident (Fleckenstein 2024); untrained readers were at chance (Clark 2021). Exception: five heavy ChatGPT users by majority vote misclassified 1 of 300 articles (Russell 2025), relying on the same vocabulary and formality patterns listed in `patterns.md`.

## Why the vocabulary shows up

Best-supported explanation: human-preference training; raters prefer text with these words (Juzek and Ward 2025). People also pick the words up (Yakura 2024), and some were rising before 2022 (Matsui 2025). So "uses delve" is weak evidence of AI on its own.

## Implications for this skill

- Removing patterns improves the text and lowers risk. It does not guarantee a score.
- Short text (under ~300 words), lists, code and formulaic genres are unreliable to score in both directions.
- The honest protection for a real author is process evidence (drafts, version history) and disclosure where required.
- Non-native writers are over-flagged. Do not "fix" their voice into a generic one; simplify nothing that is theirs.

## Key sources

Turnitin AI detection FAQ; GPTZero support and "Inside GPTZero"; Pangram "how it works"; OpenAI classifier retirement notice; Mitchell et al. (DetectGPT); Bao et al. (Fast-DetectGPT); Hans et al. (Binoculars, arXiv 2401.12070); Kirchenbauer et al. (arXiv 2301.10226, 2306.04634); Sadasivan et al. (arXiv 2303.11156); Dugan et al. (RAID, arXiv 2405.07940); Liang et al. 2023 (arXiv 2304.02819); Kobak et al. (arXiv 2406.07016); Kousha et al. 2025; Yakura et al. 2024; Juzek and Ward 2024/2025; The Last Fingerprint (arXiv 2603.27006, preprint). Wikipedia's "Signs of AI writing" was read only through two secondary summaries.
