#!/usr/bin/env python3
"""Audit a text for patterns associated with AI-generated prose.

Usage: audit.py [file]   (reads stdin if no file is given)
       audit.py --json [file]

Stdlib only. This is a style audit, not a detector: it counts known tells and
reports rhythm statistics. A clean result does not guarantee any detector score.
"""
import json
import re
import statistics
import sys

# Measured in corpus studies (Kobak 2024, Kousha 2025, Yakura 2024, Juzek 2024-26).
MEASURED_WORDS = [
    "delve", "delves", "delving", "underscore", "underscores", "underscoring",
    "showcase", "showcases", "showcasing", "intricate", "intricacies",
    "meticulous", "meticulously", "boast", "boasts", "pivotal", "crucial",
]
# Listed by editors (Wikipedia guide, blader/humanizer); not frequency-tested here.
LISTED_WORDS = [
    "tapestry", "testament", "multifaceted", "myriad", "foster", "fostering",
    "garner", "seamless", "seamlessly", "vibrant", "utilize", "utilise",
    "leverage", "comprehensive", "landscape", "realm", "navigate", "elevate",
    "unlock", "harness", "embark", "paramount", "holistic", "robust",
]
LISTED_PHRASES = [
    "plays a crucial role", "plays a vital role", "plays a pivotal role",
    "it is important to note", "it's important to note", "it is worth noting",
    "in today's fast-paced world", "in today's digital age", "in the realm of",
    "let's dive in", "let's delve", "serves as", "stands as", "a testament to",
    "not only", "in conclusion", "in summary", "to summarize", "overall,",
    "some critics argue", "future prospects", "ever-evolving", "game-changer",
    "rich tapestry", "navigating the", "at the end of the day",
]
RESIDUE = [
    "as an ai", "as a language model", "i hope this helps", "feel free to",
    "let me know if", "knowledge cutoff", "i cannot browse", "certainly!",
    "great question", "[insert", "[your name]", "lorem ipsum",
]
CONNECTORS = [
    "moreover", "furthermore", "in addition", "additionally", "consequently",
    "nevertheless", "nonetheless", "thus", "hence", "therefore",
]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
BOLD_LABEL = re.compile(r"^\s*(?:[-*]|\d+\.)\s+\*\*[^*]+\*\*\s*:", re.M)
SUSPICIOUS_CHARS = {
    "​": "zero-width space", "‌": "zero-width non-joiner",
    "‍": "zero-width joiner", "⁠": "word joiner",
    "﻿": "BOM / zero-width no-break space", " ": "non-breaking space",
}


def words_of(text):
    return re.findall(r"[A-Za-z][A-Za-z'’-]*", text)


def sentences_of(text):
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?])[\"')\]]*\s+(?=[A-Z\"'(\[])", text)
    return [p for p in (s.strip() for s in parts) if len(words_of(p)) >= 1]


def count_terms(text, terms):
    low = text.lower()
    out = {}
    for t in terms:
        pat = r"(?<![a-z])" + re.escape(t) + (r"" if t.endswith(",") else r"(?![a-z])")
        n = len(re.findall(pat, low))
        if n:
            out[t] = n
    return out


def audit(text):
    words = words_of(text)
    sents = sentences_of(text)
    lens = [len(words_of(s)) for s in sents]
    n_words = len(words)
    r = {"words": n_words, "sentences": len(sents)}

    if len(lens) >= 2:
        mean = statistics.mean(lens)
        sd = statistics.pstdev(lens)
        r["sentence_len"] = {
            "mean": round(mean, 1), "stdev": round(sd, 1),
            "cv": round(sd / mean, 2) if mean else 0.0,
            "min": min(lens), "max": max(lens),
        }
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    plens = [len(words_of(p)) for p in paras]
    if len(plens) >= 3:
        pm = statistics.mean(plens)
        r["paragraph_len_cv"] = round(statistics.pstdev(plens) / pm, 2) if pm else 0.0

    r["residue"] = count_terms(text, RESIDUE)
    r["measured_words"] = count_terms(text, MEASURED_WORDS)
    r["listed_words"] = count_terms(text, LISTED_WORDS)
    r["listed_phrases"] = count_terms(text, LISTED_PHRASES)
    conn = count_terms(text, CONNECTORS)
    r["connectors"] = conn
    r["connector_per_sentence"] = round(sum(conn.values()) / len(sents), 2) if sents else 0.0
    dashes = text.count("—")
    r["em_dashes"] = dashes
    r["em_dashes_per_1000w"] = round(1000 * dashes / n_words, 1) if n_words else 0.0
    r["emoji"] = len(EMOJI.findall(text))
    r["bold_label_bullets"] = len(BOLD_LABEL.findall(text))
    r["curly_quotes"] = sum(text.count(c) for c in "“”‘’")
    r["suspicious_chars"] = {
        name: text.count(ch) for ch, name in SUSPICIOUS_CHARS.items() if text.count(ch)
    }
    # Sentences opening with the same word, a cheap uniformity check.
    starts = [words_of(s)[0].lower() for s in sents if words_of(s)]
    if starts:
        top = max(set(starts), key=starts.count)
        r["most_common_opener"] = {"word": top, "share": round(starts.count(top) / len(starts), 2)}
    return r


def flags(r):
    f = []
    for key, label in [("residue", "Chatbot residue"), ("measured_words", "Measured AI-favored words"),
                       ("listed_phrases", "Template phrases"), ("listed_words", "Listed AI-favored words")]:
        if r[key]:
            f.append(f"{label}: " + ", ".join(f"{k} x{v}" for k, v in r[key].items()))
    if r["connector_per_sentence"] >= 0.15:
        f.append(f"Heavy connectors ({r['connector_per_sentence']} per sentence): use and/but/so or none.")
    if r["em_dashes_per_1000w"] >= 3:
        f.append(f"Em dashes at {r['em_dashes_per_1000w']}/1000 words: cut unless they are your habit.")
    if r["emoji"]:
        f.append(f"Emoji: {r['emoji']}")
    if r["bold_label_bullets"] >= 2:
        f.append(f"Bold-label bullets: {r['bold_label_bullets']}")
    if r["suspicious_chars"]:
        f.append("Invisible/odd characters present (remove; detectors read these as evasion): "
                 + ", ".join(f"{k} x{v}" for k, v in r["suspicious_chars"].items()))
    sl = r.get("sentence_len")
    if sl and r["sentences"] >= 8 and sl["cv"] < 0.40:
        f.append(f"Even rhythm: sentence-length CV {sl['cv']} (rough rule: below ~0.40 reads uniform).")
    op = r.get("most_common_opener")
    if op and r["sentences"] >= 8 and op["share"] >= 0.25:
        f.append(f"Repetitive openers: '{op['word']}' starts {int(op['share']*100)}% of sentences.")
    return f


def main(argv):
    as_json = "--json" in argv
    args = [a for a in argv if a != "--json"]
    text = open(args[0], encoding="utf-8").read() if args else sys.stdin.read()
    r = audit(text)
    fl = flags(r)
    if as_json:
        print(json.dumps({"stats": r, "flags": fl}, indent=2))
    else:
        print(f"Words: {r['words']}  Sentences: {r['sentences']}")
        if "sentence_len" in r:
            s = r["sentence_len"]
            print(f"Sentence length: mean {s['mean']}, stdev {s['stdev']}, CV {s['cv']}, range {s['min']}-{s['max']}")
        if "paragraph_len_cv" in r:
            print(f"Paragraph length CV: {r['paragraph_len_cv']}")
        print(f"Em dashes: {r['em_dashes']} ({r['em_dashes_per_1000w']}/1000w)  Emoji: {r['emoji']}  "
              f"Bold-label bullets: {r['bold_label_bullets']}  Curly quotes: {r['curly_quotes']}")
        print("\nFlags:" if fl else "\nNo flags.")
        for line in fl:
            print(f"  - {line}")
        if r["words"] < 300:
            print("\nShort text (under ~300 words): any detector score on it is unreliable either way.")
        print("\nNote: a style audit, not a detector. A clean result guarantees nothing.")
    return 1 if fl else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
