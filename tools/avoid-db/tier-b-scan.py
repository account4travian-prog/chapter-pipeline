#!/usr/bin/env python3
"""tier-b-scan.py — Avoid Database Tier B tripwire sweep + Tier D watchlist counters.

Ratified by the author 2026-10-14 (trial: ch.15-17). Registry: ~/workspace/prose-avoid-db/DATABASE.md
Detectors are aligned with the calibration run (calibration/detector-counts.md)
so trial numbers stay comparable with the control-corpus rates (validated
2026-10-14: C61 statistics reproduce the calibration exactly on ch.1/ch.14;
C33 within 2 hits on ch.14 — regex edge cases). A hit is a
flag for a recorded disposition (fixed / cleared-with-reason) — never a fail.

Usage: tier-b-scan.py <draft.md> [--json]
Output: per-candidate hit counts, hits per 1k words, and hit lines for disposition.
"""
import re, sys, json, math
from pathlib import Path

TIER_B = [
    ("C04", "Unearned knowledge frame", re.compile(r"the way [A-Z][a-z]+ would have")),
    ("C12", "Unspecified micro-phrases", re.compile(r"\bfluent\b|back raw|down small|awake in the \w+|held it (carefully|gently|tightly)", re.I)),
    ("C51-note", "Recap inventory (see sentence check below)", None),
    ("C52", "Style-word cluster", re.compile(r"\b(delve|delves|delved|delving|intricate|pivotal|showcase|showcases|showcased|underscore|underscores|underscored|tapestry|tapestries|realm|realms|meticulous|meticulously)\b", re.I)),
    ("C53", "Significance-inflation vocabulary", re.compile(r"\b(pivotal|enduring|transformative|testament|legacy)\b", re.I)),
    ("C55", "Vague attribution", re.compile(r"experts (say|agree)|many (say|believe)|it is widely known|observers note", re.I)),
    ("C58", "Copula avoidance", re.compile(r"\b(serves as|stands as|boasts|features|represents)\b", re.I)),
    ("C59", "Negative parallelism", re.compile(r"not (a|an|the) \w+, but|it (wasn't|was not) about", re.I)),
    ("C60", "Trailing -ing significance tail", re.compile(r",\s*(highlighting|reflecting|underscoring|symbolising|symbolizing)\b", re.I)),
    ("C73", "Abstract scenery nouns", re.compile(r"\b(tapestry|landscape|realm)\b", re.I)),
    ("C74", "Symbolic-significance verbs", re.compile(r"\b(mirrors|mirrored|represents|represented|symbolise|symbolises|symbolised|symbolize|symbolizes|symbolized)\b", re.I)),
    ("C03", "Maxim frames", re.compile(r"was the \w+est \w+|the \w+ (he|she) had, not the \w+ (he|she) wanted|\bis the \w+ \w+ing\b", re.I)),
    ("C41", "Unanchored interpretive simile", re.compile(r"\b(read|reads|felt|feels|looked|looks|sounded|sounds) (like|as if) (a |an |the )?\w+(tion|ness|ity|ance|ence|ment)\b", re.I)),
    ("C09", "Moral/clever labels", re.compile(r"\b(honest|dishonest|cheap|earned|real|dirty|clean) (version|explanation|death|answer|work)\b|hadn't earned|died the \w+|failed at the \w+", re.I)),
    ("C39", "Expectation frame (flag >=3/chapter)", re.compile(r"\b(He|She) had (expected|thought|assumed|imagined)\b")),
    ("C11", "Announced pivot markers", re.compile(r"\bno longer\b|\bfirst time\b|this was different|was a (second|third|fourth) thing", re.I)),
    ("C05", "Withheld specification", re.compile(r"(didn't|did not|wouldn't|would not) (think|name|say)\b|what (that|it) meant", re.I)),
    ("C56", "Qualifier stacking list", re.compile(r"\b(arguably|notably|importantly|seemed|almost)\b|it is worth noting|in many ways|to some extent|a kind of", re.I)),
    ("C20", "Body-beat cluster", re.compile(r"\b(breath|breaths|breathed|breathing|throat|pulse|stomach|jaw|jaws|thumbnail|exhale|exhaled|fingers)\b", re.I)),
    ("C24", "Thesis vocabulary (gloss check)", re.compile(r"what it meant|the point|the lesson|was the (whole )?(job|rule|reason|thing)\b", re.I)),
    ("C35", "Specification litany", re.compile(r"\bno \w+[.,]\s*no \w+|\bNo \w+\. No \w+\.")),
    ("C37", "Tricolon, syndetic form", re.compile(r"\w+,\s*\w+,\s*and\s+\w+")),
]
STAKE_NOUNS = {"job","rent","money","loan","charges","permission","file","copy","career"}
IMAGE_WORDS = ["door","death","dark","hold"]
CONSTRAINT = re.compile(r"\b(record|records|retained|retention|allocation|permission|approved|scope|field|reference)s?\b", re.I)
STANDALONE = re.compile(r"^\s*\W{0,3}(Yes|No|Right|Okay|All right|I know|I understand)\.?\W{0,3}\s*$")
QUOTE = re.compile(r"[“\"]([^”\"]+)[”\"]")

def sentences(text):
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    sents = []
    for p in paras:
        for s in re.split(r"(?<=[.!?…])\s+(?=[A-Z0-9“\"])", p.replace("\n", " ")):
            if s.strip(): sents.append(s.strip())
    return paras, sents

def content_words(s):
    return {w for w in re.findall(r"[a-z']+", s.lower()) if len(w) > 3}

def main():
    path = Path(sys.argv[1]); as_json = "--json" in sys.argv
    text = path.read_text(encoding="utf-8")
    words = len(text.split())
    lines = text.splitlines()
    results = {}
    for cid, name, rx in TIER_B:
        if rx is None: continue
        hits = []
        for i, ln in enumerate(lines, 1):
            for _ in rx.finditer(ln): hits.append(i)
        results[cid] = {"name": name, "hits": len(hits), "lines": hits[:20]}
    paras, sents = sentences(text)
    # C51: sentences with >=3 distinct stake nouns (calibration form; copula condition not applied)
    c51 = sum(1 for s in sents if len({w for w in re.findall(r"[a-z]+", s.lower())} & STAKE_NOUNS) >= 3)
    results["C51"] = {"name": "Recap inventory of stakes", "hits": c51, "lines": []}
    # C84: adjacent paragraph pairs sharing an image word
    c84 = 0
    for a, b in zip(paras, paras[1:]):
        wa = {w for w in IMAGE_WORDS if re.search(rf"\b{w}\b", a, re.I)}
        wb = {w for w in IMAGE_WORDS if re.search(rf"\b{w}\b", b, re.I)}
        if wa & wb: c84 += 1
    results["C84"] = {"name": "Metaphor chain (adjacent paragraphs)", "hits": c84, "lines": []}
    # C07: quoted turn vs following narration sentence overlap >=0.7 (approximation: quote vs next sentence in same paragraph flow)
    # C08: echo chains — quoted-segment machinery
    quotes = QUOTE.findall(text)
    def overlap(a, b):
        wa, wb = content_words(a), content_words(b)
        return len(wa & wb) / max(1, min(len(wa), len(wb)))
    c08 = 0; run = 0
    for a, b in zip(quotes, quotes[1:]):
        neg = b.strip().lower().startswith(("no", "not", "never", "it wasn't", "it was not", "i didn't", "we don't"))
        if neg and overlap(a, b) >= 0.6: run += 1
        else:
            if run >= 2: c08 += 1
            run = 0
    if run >= 2: c08 += 1
    results["C08"] = {"name": "Echo-chain dialogue runs (>=3 turns)", "hits": c08, "lines": []}
    # Tier D watchlist
    d = {}
    d["C33"] = len(CONSTRAINT.findall(text))
    d["C31"] = sum(1 for ln in lines if STANDALONE.match(ln))
    qs = [q for q in quotes if q.strip().endswith("?")]
    d["C46"] = {"interrogative": len(qs), "quoted_turns": len(quotes), "share": round(len(qs)/max(1,len(quotes)), 3)}
    lens = [len(s.split()) for s in sents]
    if lens:
        mean = sum(lens)/len(lens); var = sum((x-mean)**2 for x in lens)/len(lens)
        d["C61"] = {"sentences": len(lens), "mean_words": round(mean,2), "stdev": round(math.sqrt(var),2)}
    if as_json:
        print(json.dumps({"file": str(path), "words": words, "tier_b": results, "tier_d": d}, indent=1)); return
    print(f"# Tier B sweep — {path.name} ({words} words)")
    for cid in sorted(results):
        r = results[cid]
        print(f"{cid} {r['name']}: {r['hits']} hits ({r['hits']/words*1000:.2f}/1k)" + (f" lines {r['lines']}" if r['lines'] else ""))
    print(f"# Tier D watchlist")
    print(f"C33 constraint tokens: {d['C33']} ({d['C33']/words*1000:.2f}/1k)")
    print(f"C31 standalone beats: {d['C31']} ({d['C31']/words*1000:.2f}/1k)")
    print(f"C46 interrogative share: {d['C46']['share']} ({d['C46']['interrogative']}/{d['C46']['quoted_turns']} quoted turns)")
    print(f"C61 sentence length: mean {d['C61']['mean_words']} words, stdev {d['C61']['stdev']} (n={d['C61']['sentences']})")

if __name__ == "__main__": main()
