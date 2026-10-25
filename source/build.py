"""Collect all data_*.py files, resolve repeats, sort newest-exam-first and write questions.js."""
import json, re, sys, os, shutil
sys.stdout.reconfigure(encoding="utf-8")
import qb

FILES = ["data_F26a", "data_M26b", "data_F25b", "data_M25b", "data_M25a", "data_F24c", "data_M24c", "data_F24b",
         "data_M24b", "data_F24a", "data_M24a", "data_F23c", "data_F23b", "data_F23a", "data_M22", "data_Q", "data_2021"]
for f in FILES:
    __import__(f)

# newest first
RANK = ["M26b", "F26a", "F25x", "F25b", "M25b", "M25a", "F24c", "M24c", "F24b", "M24b", "F24a", "M24a",
        "F23c", "F23b", "F23a", "M22b2", "M22b1", "Q22b", "Q22a", "M22a", "F21a", "M21c", "M21b", "M21a", "Q21"]
assert set(RANK) == set(qb.SOURCES), set(qb.SOURCES) ^ set(RANK)

for qid, ref in qb.PENDING:
    assert qid in qb.BY_ID, "also() on unknown id " + qid
    qb.BY_ID[qid]["from"].append(ref)

# merge questions whose text is identical (same type and answer)
def norm(s):
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"<[^>]+>", "", s.lower()))
seen, out, merged = {}, [], 0
for q in qb.Q:
    key = (q["t"], norm(q["q"]), json.dumps(q["a"]) if q["t"] != "short" else "")
    if key in seen:
        seen[key]["from"].extend(q["from"]); merged += 1
        continue
    seen[key] = q; out.append(q)

for q in out:
    # de-duplicate source refs and order them newest first
    uniq = []
    for f in q["from"]:
        if not any(u["s"] == f["s"] and u["qn"] == f["qn"] for u in uniq):
            uniq.append({k: v for k, v in f.items() if v is not None})
    uniq.sort(key=lambda f: RANK.index(f["s"]))
    q["from"] = uniq

order = {id(q): i for i, q in enumerate(out)}
out.sort(key=lambda q: (q["ch"], RANK.index(q["from"][0]["s"]), order[id(q)]))


data = {"chapters": {str(k): v for k, v in qb.CHAPTERS.items()}, "sources": qb.SOURCES, "questions": out}
dest = sys.argv[1] if len(sys.argv) > 1 else "."
with open(os.path.join(dest, "questions.js"), "w", encoding="utf-8") as fh:
    fh.write("window.QDATA = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
os.makedirs(os.path.join(dest, "img"), exist_ok=True)
if os.path.isdir("img") and os.path.abspath("img") != os.path.abspath(os.path.join(dest, "img")):
    for f in os.listdir("img"):
        shutil.copy("img/" + f, os.path.join(dest, "img", f))
for q in out:
    if q.get("img"):
        assert os.path.exists(os.path.join(dest, "img", q["img"])), q["img"]

from collections import Counter
print("questions:", len(out), "merged duplicates:", merged, "appearances:", sum(len(q["from"]) for q in out))
print("by chapter:", dict(sorted(Counter(q["ch"] for q in out).items())))
print("by type:", dict(Counter(q["t"] for q in out)))
