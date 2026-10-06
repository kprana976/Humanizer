# Patterns to remove, and what to do instead

Evidence tiers: **measured** = a corpus study counted it; **listed** = editors or tool authors list it as a habit, no frequency study opened. No single item proves anything; detectors and readers weigh many together.

## Words and phrases

| Pattern | Tier | Instead |
| --- | --- | --- |
| delve into | measured (28x baseline in PubMed abstracts) | look at, dig into, or cut |
| underscore (verb) | measured (10.9x) | show, stress, confirm |
| showcase / showcasing | measured (10.2x) | show, present |
| intricate / intricacies | measured | complex, detailed, "the details" |
| meticulous / meticulously | measured | careful, thorough |
| boasts a | measured | has |
| pivotal, crucial | measured | important, key; or say why it matters; often delete and keep the fact |
| potential, findings | measured (small gaps) | possible, could; results |
| additionally, suggest, strategy | measured, weak alone | also, and; show; plan |
| Moreover, Furthermore, In addition | listed + heavy-connector finding | and, but, so, or start the next sentence |
| tapestry, testament, multifaceted, myriad, landscape (abstract), foster, garner, seamless, robust (figurative), vibrant | listed | the concrete thing: "a mix of", "shows", "many", "encourage", "get", "smooth" |
| plays a crucial role, it is important to note, in today's fast-paced world, let's dive in | listed | cut; state the fact |
| serves as, stands as, features | listed | is, has |

Synonym swapping fails: whole meaning clusters shift together, so replacing "delve" with "explore" in the same vague sentence changes the word, not the pattern. Fix the claim: make it specific or delete it.

The word list is a moving target. After the "delve" findings, usage dropped on arXiv while other words rose. Do not treat the list as complete; treat vagueness, inflation and uniformity as the real targets.

## Structure

- Every paragraph the same shape (claim, support, restate). Vary it; some paragraphs are one line.
- Explicit connector on every sentence. Humans use implicit links or none.
- Restating the point in the next sentence, and a closing paragraph that summarizes the body. Strongest cues in expert-reader studies (redundancy, repetition, coherence-thread).
- Rule of three lists and "not only X but also Y" templates. Use the number of items there actually are.
- Stock sections ("Challenges", "Future Prospects") and balanced "some critics argue" surveys that never land. State a view if the author has one.
- Generic claims with no context-specific detail ("plays a vital role in healthcare"). Replace with a name, number, place, or example from the user's material.

## Formatting and symbols

- Em dashes as a tic (up to 9 per 1,000 words in some models; 0 in others). Use commas, periods or parentheses; keep them only if the user's own writing uses them.
- Bold on every bullet label, title-case headings, emoji in headings or bullets, curly quotes in plain-text venues.
- Chatbot residue: "As an AI language model", knowledge-cutoff notes, unfilled template blanks, offers of further help, invalid DOIs, uncited "experts". Remove; verify every citation exists.
- Invisible or look-alike characters: not an AI habit, and detectors treat them as evasion. Remove, never add.

## What human writing tends to do (tendencies, not a recipe)

| Dimension | AI tendency | Human tendency |
| --- | --- | --- |
| Rhythm | even sentence shape throughout | plain sentences next to odd ones; length varies |
| Specificity | general terminology | concrete names, numbers, places |
| Verbs | single formal verbs | about 5x more phrasal verbs, twice the diversity |
| Register | longer, formal, objective | shorter, informal, analogies, leans to a conclusion |
| Tone | formal, direct | more emotional, subjective, personal |
| Cohesion | explicit connectors | implicit links, sometimes none |
| Errors | near zero | occasional (more at lower proficiency) |

Two cautions. Rough writing is not automatically "human" to a detector, and polished writing is not automatically AI. Professionally edited human text can also score as AI. So match the author's real voice rather than aiming at a generic "human" style.

## Rewrite examples

Vague, inflated:
> The platform's seamless integration capabilities showcase its pivotal role in the evolving landscape of data management.

Specific (if the user supplied the facts):
> The platform connects to Postgres and S3 without extra config, which is the main reason we picked it.

Connector-heavy:
> Moreover, the results were significant. Furthermore, they were consistent across groups. Additionally, the effect persisted.

Plain:
> The results were significant, held across all three groups, and were still there at six months.

Template closing:
> In conclusion, it is clear that sleep plays a crucial role in overall well-being.

Cut it, or end on the actual last finding:
> Sleep under six hours was the strongest predictor of missed work in this sample.
