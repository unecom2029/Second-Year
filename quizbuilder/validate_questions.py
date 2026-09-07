#!/usr/bin/env python3
"""Check an AI-generated question batch against the UWorld house style before you paste it
into the quiz builder. Usage:  python3 validate_questions.py batch.json"""
import json, re, sys

def main(path):
    d = json.load(open(path, encoding='utf-8'))
    qs = d.get('questions', [])
    print("%s  |  name=%r  |  %d questions\n" % (path, d.get('name'), len(qs)))
    fails = 0
    for i, q in enumerate(qs, 1):
        s, ch, cor = q.get('stem',''), q.get('choices',[]), q.get('correct')
        we = q.get('wrongExplanations', {})
        exp, eli5 = q.get('explanation',''), q.get('eli5','')
        txt = [re.sub(r'^[A-H]\.\s*', '', c) for c in ch]
        msgs = []
        def chk(cond, msg):
            if not cond: msgs.append(msg)

        # --- JSON contract (breaks the app if wrong) ---
        chk(isinstance(cor, int) and 0 <= cor < len(ch), "'correct' is not a valid 0-based index")
        chk(4 <= len(ch) <= 8, "option count %d outside 4-8" % len(ch))
        chk(all(c.startswith("ABCDEFGH"[j] + ". ") for j, c in enumerate(ch)),
            "choice letter prefixes are not sequential A, B, C...")
        if isinstance(cor, int) and 0 <= cor < len(ch):
            want = {str(j) for j in range(len(ch)) if j != cor}
            chk(set(we) == want, "wrongExplanations keys %s should be %s "
                "(key by CHOICE INDEX, skipping the correct one)"
                % (sorted(we, key=lambda x:int(x) if x.isdigit() else 99), sorted(want, key=int)))
        chk(all(str(v).strip() for v in we.values()), "an entry in wrongExplanations is empty")

        # --- UWorld house style ---
        ordered = re.search(r'^[A-H]\.\s*(C\d|T\d|L\d|S\d|Phase|\d)', ch[0]) if ch else None
        chk(ordered or sorted(txt, key=str.lower) == txt,
            "options not alphabetized -> should be: " + " | ".join(sorted(txt, key=str.lower)))
        chk(re.search(r'\bdue to\b', s) or s.startswith(("An investigator", "Researchers",
            "A clinical trial", "An epidemiologic")), "opener does not use 'due to'")
        chk("because of" not in s, "uses NBME 'because of' instead of 'due to'")
        chk(s.rstrip().endswith("?"), "stem does not end with the lead-in question")
        chk("Educational objective:" in exp, "explanation has no 'Educational objective:' line")
        if "Educational objective:" in exp:
            w = len(exp.split("Educational objective:")[1].split())
            chk(25 <= w <= 70, "educational objective is %d words (target 30-50)" % w)
        chk("->" in exp or "→" in exp, "explanation has no arrow mechanism chain")
        chk(len(re.findall(r'[.!?]', eli5)) <= 3, "eli5 is longer than 3 sentences")
        chk(not re.search(r'\b(shown|photograph|image below|figure|the arrow|curve labeled)\b', s, re.I),
            "stem references an image (this app is text-only)")
        chk(not re.search(r'\b(all of the above|none of the above)\b', " ".join(txt), re.I),
            "option set contains all/none of the above")
        wc = len(s.split())
        chk(45 <= wc <= 200, "stem is %d words (UWorld median 111, p10 72, p90 151)" % wc)

        status = "OK  " if not msgs else "FAIL"
        print("%s item %-3d %d options, key=%s, stem=%d words"
              % (status, i, len(ch), "ABCDEFGH"[cor] if isinstance(cor,int) and cor<len(ch) else "?", wc))
        for m in msgs:
            print("       - " + m)
        fails += bool(msgs)

    keys = "".join("ABCDEFGH"[q['correct']] for q in qs
                   if isinstance(q.get('correct'), int) and q['correct'] < 8)
    print("\nanswer key: %s" % (" ".join(keys) or "n/a"))
    if keys:
        top = max(set(keys), key=keys.count)
        if keys.count(top) > len(keys) / 2:
            print("  warning: '%s' is the key for %d of %d items - skewed"
                  % (top, keys.count(top), len(keys)))
        run = max(len(r) for r in re.findall(r'(.)\1*', keys))
        if run >= 4:
            print("  warning: same letter correct for %d consecutive items" % run)
    print("\n%d of %d items passed." % (len(qs) - fails, len(qs)))
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "batch.json"))
