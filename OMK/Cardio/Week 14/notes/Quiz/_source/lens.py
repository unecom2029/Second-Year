import sys, importlib
for mod in sys.argv[1:]:
    Q=importlib.import_module(mod).Q
    print('==',mod)
    for i,q in enumerate(Q,1):
        if all(len(c.split())<=4 for c in q['choices']): continue
        L=[len(c) for c in q['choices']]; k=q['key']
        rank=sorted(L,reverse=True).index(L[k])+1
        print(f"{i:2} rank{rank} key={L[k]} others={[l for j,l in enumerate(L) if j!=k]}  | {q['choices'][k][:60]}")
