# Week 15 quizzes — source

| Job | Question files | Builds | Images |
|---|---|---|---|
| `vs` | `q_vs_v1.py`, `q_vs_v2.py` | `Vascular_Disease_Quiz_V1.html`, `Vascular_Disease_Image_Quiz_V2.html` | V1 6, V2 all 18 |

Rebuild: `python3 build.py vs write` (one file: `python3 build.py vs:q_vs_v2 write`; omit `write` to audit answer lengths).
Per-item length ranks: `python3 lens.py q_vs_v1`. Contact sheet of images: `python3 vsheet.py out.jpg Key1 Key2 …`.

`build.py`, `lens.py`, `vsheet.py` and the loader in `images.py` are copied from `Week 14/notes/Quiz/_source/`.
Images come from `../../assets/vasc-surg/` (lecture slides) and AMBOSS. **No UWorld images.**
Masked giveaways: "LA Thrombus" label (left atrial CT), "Arteries"/"Clot" labels (SMA CT), "Common Femoral Artery Occlusion"
label (angiogram), stray panel letters on the popliteal angiogram and post-thrombotic photo. Captions name the view, never the diagnosis.
V1 and V2 cover different angles; the app reshuffles choices at runtime.
