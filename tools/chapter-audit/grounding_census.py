#!/usr/bin/env python3
"""Scene-grounding census — Tier M Class 9 candidate generator.

Council Session 4 (2026-09-30): machine-generated grounding receipt per scene.
Marks E (embodied verbs), A (ambient/sensory registered by the body),
X (instrument-mediated: screen/log/terminal action — NEVER counts as grounding),
C (cognition). Code/log fenced blocks supply no grounding credit.

Usage: grounding_census.py <candidate.md> [--lexicon-version]
Output: JSON receipt to stdout, SHA-256 of the candidate in the header.

This is a CANDIDATE GENERATOR (Tier M), not a prose verdict. Hard/soft hits
are named by the receipt; disposition is Tier O (fix / intentional stillness /
false positive). Thresholds must be calibrated on accepted ch.1-6 before
adoption and never used as a cross-chapter quality score.
"""
import hashlib
import json
import re
import sys
from datetime import date

LEXICON_VERSION = "1.0"
LEXICON_DATE = "2026-09-30"

# Embodied verbs: the viewpoint body moves, touches, handles, or physically acts.
E_VERBS = {
    "woke", "wake", "wakes", "waking", "sat", "sit", "sitting", "stood", "stand",
    "standing", "walked", "walk", "walking", "carried", "carry", "carrying",
    "poured", "pour", "pouring", "picked", "pick", "picked up", "opened", "open",
    "opening", "closed", "close", "turned", "turn", "reached", "reach", "reaching",
    "felt", "feel", "grabbed", "grab", "set", "put", "placed", "lifted", "lift",
    "pushed", "push", "pulled", "pull", "stepped", "step", "knelt", "leaned",
    "lean", "stretched", "stretch", "rubbed", "rub", "shook", "shake", "nodded",
    "nod", "held", "hold", "holding", "dropped", "drop", "caught", "throw",
    "threw", "tossed", "slid", "slide", "climbed", "climb", "descended", "rose",
    "rise", "fell", "fall", "breath", "breathed", "sighed", "sigh", "yawned",
    "swallowed", "chewed", "drank", "drink", "drinking", "ate", "eat", "sipped",
    "sip", "dressed", "undressed", "washed", "showered", "brushed", "shaved",
    "kicked", "kick", "kicking", "stomped", "paced", "pacing", "wandered",
    "hurried", "rushed", "ran", "run", "jogged", "crouched", "crawl", "crawled",
    "draped", "wrapped", "unwrapped", "folded", "unfolded", "tucked", "dug",
    "scraped", "tapped", "rapped", "knocked", "wiped", "dried", "wrung",
    "squeezed", "pinched", "scratched", "massaged", "pressed", "press",
}
# Sensory registered BY THE BODY (not on-screen content).
A_TOKENS = {
    "cold", "warm", "hot", "chilly", "freezing", "cool", "bright", "dark",
    "dim", "glare", "loud", "quiet", "silent", "hum", "humming", "buzz",
    "rattle", "rattling", "creak", "creaking", "thump", "thud", "drip",
    "smell", "smelled", "scent", "aroma", "stink", "taste", "tasted",
    "bitter", "sweet", "sour", "salty", "ache", "ached", "aching", "sore",
    "stiff", "numb", "tingling", "dizzy", "nausea", "shiver", "shivered",
    "sweat", "sweating", "goosebumps", "rough", "smooth", "soft", "hard",
    "sharp", "dull", "heavy", "light", "damp", "wet", "dry", "sticky",
    "gritty", "oily", "furnace", "draft", "breeze", "wind", "sunlight",
    "moonlight", "steam", "smoke", "dust",
}
# Instrument-mediated: procedural screen/log/terminal action. NEVER grounding.
X_VERBS = {
    "read", "reading", "typed", "type", "typing", "clicked", "click",
    "scrolled", "scroll", "scrolling", "dashboard", "monitor", "monitors",
    "screen", "screens", "log", "logs", "logged", "terminal", "console",
    "keyboard", "mouse", "cursor", "tab", "window", "browser", "query",
    "queried", "grep", "grepped", "ssh", "ping", "traceroute", "dashboard",
    "queue", "job", "jobs", "notebook", "spreadsheet", "code", "coded",
    "script", "ran", "run", "execute", "executed", "compiled", "built",
    "deployed", "ssh'd", "tailed", "watched", "stared",
}
# Cognition markers (for distribution reporting, not grounding).
C_VERBS = {
    "thought", "think", "thinking", "wondered", "wonder", "realized",
    "realize", "decided", "decide", "knew", "know", "remembered",
    "remember", "forgot", "understood", "understand", "figured",
    "suspected", "suspect", "considered", "consider", "meant", "mean",
    "felt", "doubted", "doubt", "guessed", "guess", "concluded",
    "noticed", "notice", "recognized", "recognize",
}

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"“])")
FENCE = re.compile(r"^```")
DATELINE = re.compile(r"^\*([A-Z][a-z]+day, [A-Z][a-z]+ \d+(?:, \d{4})?, [\d:]+ [ap]\.m\.)\*$")


def strip_fences(lines):
    """Remove fenced code/log blocks — they supply no grounding credit."""
    out, in_fence, removed = [], False, 0
    for ln in lines:
        if FENCE.match(ln.strip()):
            in_fence = not in_fence
            removed += 1
            continue
        if in_fence:
            removed += 1
            continue
        out.append(ln)
    return out, removed


def classify(sent):
    low = sent.lower()
    words = set(re.findall(r"[a-z']+", low))
    e = bool(words & E_VERBS)
    a = bool(words & A_TOKENS)
    x = bool(words & X_VERBS)
    c = bool(words & C_VERBS)
    return {"E": e, "A": a, "X": x, "C": c}


def census(path):
    raw = open(path, encoding="utf-8").read()
    sha = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    lines = raw.splitlines()
    # Skip the header block (before the first dateline).
    start = 0
    for i, ln in enumerate(lines):
        if DATELINE.match(ln.strip()):
            start = i
            break
    body, removed = strip_fences(lines[start:])
    # Split into scenes on datelines.
    scenes, cur = [], {"dateline": None, "lines": []}
    for ln in body:
        m = DATELINE.match(ln.strip())
        if m:
            if cur["dateline"] or cur["lines"]:
                scenes.append(cur)
            cur = {"dateline": m.group(1), "lines": []}
        else:
            cur["lines"].append(ln)
    if cur["dateline"] or cur["lines"]:
        scenes.append(cur)

    receipt_scenes = []
    for idx, sc in enumerate(scenes, 1):
        text = "\n".join(sc["lines"])
        text_nospace = re.sub(r"\s+", " ", text).strip()
        sents = [s.strip() for s in SENT_SPLIT.split(text_nospace) if s.strip()]
        marks = [classify(s) for s in sents]
        e_n = sum(1 for m in marks if m["E"])
        a_n = sum(1 for m in marks if m["A"])
        x_n = sum(1 for m in marks if m["X"])
        c_n = sum(1 for m in marks if m["C"])
        grounded = [m["E"] or m["A"] for m in marks]
        # Longest ungrounded run.
        longest, run, run_at, best_at = 0, 0, 0, 0
        for i, g in enumerate(grounded):
            if not g:
                if run == 0:
                    run_at = i
                run += 1
                if run > longest:
                    longest, best_at = run, run_at
            else:
                run = 0
        trace = [s for s, m in zip(sents, marks) if m["E"] or m["A"]][:6]
        words = len(re.findall(r"[A-Za-z']+", text_nospace))
        receipt_scenes.append({
            "scene": idx,
            "dateline": sc["dateline"],
            "words": words,
            "sentences": len(sents),
            "E_sentences": e_n,
            "A_sentences": a_n,
            "X_sentences": x_n,
            "C_sentences": c_n,
            "longest_ungrounded_run": longest,
            "longest_ungrounded_run_start_sentence": best_at + 1 if longest else None,
            "body_trace_quoted": trace,
        })
    return {
        "tool": "grounding_census.py",
        "lexicon_version": LEXICON_VERSION,
        "lexicon_date": LEXICON_DATE,
        "council": "Session 4, 2026-09-30 — Class 9 Tier M",
        "candidate_sha256": sha,
        "candidate": path.split("/")[-1],
        "fenced_lines_excluded": removed,
        "scenes": receipt_scenes,
        "disclaimer": "Candidate generator only. X never counts as grounding. "
                      "Thresholds uncalibrated — calibrate once on accepted "
                      "ch.1-6 before adoption; never a cross-chapter score.",
    }


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0 if len(sys.argv) > 1 else 1)
    if sys.argv[1] == "--lexicon-version":
        print(f"{LEXICON_VERSION} ({LEXICON_DATE})")
        sys.exit(0)
    print(json.dumps(census(sys.argv[1]), indent=2))
