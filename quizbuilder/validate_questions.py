#!/usr/bin/env python3
"""Check an AI-generated question batch against the UWorld house style before you paste it
into the quiz builder. Usage:  python3 validate_questions.py batch.json"""
import json, re, sys

def main(path):
    d = json.load(open(path, encoding='utf-8'))
    qs = d.get('questions', [])
    print("%s  |  name=%r  |  %d questions\n" % (path, d.get('name'), len(qs)))
    fails = 0
    key_longest = key_shortest = 0
    item_ratios = []
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
        # Exhibits are HTML inside the stem; judge the prose and the figure separately.
        figs = re.findall(r'<figure\b.*?</figure>', s, re.I | re.S)
        prose = re.sub(r'<[^>]+>', ' ', re.sub(r'<figure\b.*?</figure>', ' ', s, flags=re.I | re.S))
        chk(figs or not re.search(r'\b(shown|photograph|image below|the arrow|curve labeled)\b', prose, re.I),
            "stem refers to an image but no <figure> is attached")
        for f in figs:
            chk(re.search(r'<(img|svg)\b', f, re.I), "<figure> has no <img> or <svg> inside it")
            chk(not re.search(r'<script|<foreignObject|\son\w+\s*=|javascript:', f, re.I),
                "figure contains script, foreignObject, or an event attribute")
            chk("class='qfig'" in f or 'class="qfig"' in f, "figure is missing class='qfig'")
            for u in re.findall(r'<img[^>]*\ssrc=[\'"]([^\'"]+)', f, re.I):
                print("   (check by hand) image URL must come from your source content: %s" % u[:100])
        chk(not re.search(r'\b(all of the above|none of the above)\b', " ".join(txt), re.I),
            "option set contains all/none of the above")
        wc = len(prose.split())
        chk(40 <= wc <= 200,
            "stem is %d words (measured corpus: median 100, p10 63, p90 137)" % wc)

        # --- LENGTH CUE: the correct answer must not be the longest option ---
        # Measured in real UWorld items: key/distractor length ratio is 1.00 at the
        # median, and the key is the longest option only 14% of the time (below the
        # 20% expected by chance in a 5-option set). Models default to the opposite.
        if isinstance(cor, int) and 0 <= cor < len(txt) and len(txt) > 1:
            lens = [len(t.split()) for t in txt]
            klen = lens[cor]
            others = [x for j, x in enumerate(lens) if j != cor]
            mx, mn = max(lens), min(lens)
            avg = sum(others) / len(others)
            item_ratios.append(klen / avg if avg else 1.0)
            is_longest = klen == mx and lens.count(mx) == 1
            if is_longest:
                key_longest += 1
                chk(False, "LENGTH CUE: the correct answer is the single LONGEST option "
                    "(%d words vs %.1f avg distractor) - trim the key, or raise two "
                    "distractors to the same specificity" % (klen, avg))
            if klen == mn and lens.count(mn) == 1:
                key_shortest += 1
                chk(False, "LENGTH CUE: the correct answer is the single SHORTEST option "
                    "(%d words vs %.1f avg distractor)" % (klen, avg))
            # over-qualified key even when some distractor is nominally longer
            if not is_longest and avg and klen > 1.3 * avg:
                chk(False, "LENGTH CUE: key is %.2fx the mean distractor length "
                    "(limit 1.30) - the key is over-qualified" % (klen / avg))

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
    if item_ratios:
        n = len(item_ratios)
        avg_ratio = sum(item_ratios) / n
        print("\nlength-cue audit (real UWorld: key is longest ~14%, mean ratio ~1.04)")
        print("  key is the single longest option: %d of %d (%.0f%%)"
              % (key_longest, n, 100.0 * key_longest / n))
        print("  key is the single shortest option: %d of %d (%.0f%%)"
              % (key_shortest, n, 100.0 * key_shortest / n))
        print("  mean key/distractor length ratio: %.2f" % avg_ratio)
        if 100.0 * key_longest / n > 20:
            print("  WARNING: the key is the longest option in over 20% of items - this is "
                  "the machine-written tell. Trim the keys; do not pad the distractors.")
        if avg_ratio > 1.15:
            print("  WARNING: keys run %.0f%% longer than distractors on average - "
                  "over-qualified keys." % ((avg_ratio - 1) * 100))

    print("\n%d of %d items passed." % (len(qs) - fails, len(qs)))
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "batch.json"))
