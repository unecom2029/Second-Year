"""Per-item answer-length ranks: python3 lens.py q_A1_cycle [more modules]"""
import sys, importlib
for mod in sys.argv[1:]:
    Q = importlib.import_module(mod).Q
    print('==', mod)
    for i, q in enumerate(Q, 1):
        if all(len(c.split()) <= 4 for c in q['choices']): continue
        L = [len(c) for c in q['choices']]; k = q['key']
        rank = sorted(L, reverse=True).index(L[k]) + 1
        flag = ' <-- LONGEST' if L[k] == max(L) and L.count(max(L)) == 1 else (' <-- SHORTEST' if L[k] == min(L) and L.count(min(L)) == 1 else '')
        print(f"{i:2} rank {rank}/{len(L)} key={L[k]} others={sorted(l for j,l in enumerate(L) if j!=k)}{flag}")
