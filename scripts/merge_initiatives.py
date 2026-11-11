"""Merge every per-brand file in brands/<brand>/initiatives.csv into data/initiatives_all.csv.

Usage: python3 scripts/merge_initiatives.py
Run scripts/check_initiatives.py first. Folders that start with an underscore
(the template) are skipped. Never edit initiatives_all.csv by hand.
"""
import csv
import glob
import os

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
files = sorted(glob.glob(os.path.join(root, "brands", "*", "initiatives.csv")))
rows = []
header = None

for path in files:
    if os.path.basename(os.path.dirname(path)).startswith("_"):
        continue
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        rows.extend(reader)

rows.sort(key=lambda r: (r["brand"], r["id"]))
out = os.path.join(root, "data", "initiatives_all.csv")
with open(out, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(rows)
print("Wrote %d rows to data/initiatives_all.csv" % len(rows))
