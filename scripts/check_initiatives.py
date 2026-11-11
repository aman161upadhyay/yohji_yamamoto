"""Validate the per-brand files brands/<brand>/initiatives.csv.

Usage: python3 scripts/check_initiatives.py
Checks the header, the allowed values for family and evidence status,
unique ids and the presence of a source URL on every row.
"""
import csv
import glob
import os
import sys

HEADER = [
    "id", "brand", "initiative", "family", "city", "dates", "what_happened",
    "objective", "audience", "partners", "physical_digital_bridge",
    "investment", "results_and_next_move", "transferability_1to3",
    "source_url", "source_date", "evidence_status",
]
FAMILIES = {
    "One-off in-store experience",
    "Recurring experience",
    "Omnichannel set-up",
    "Activation",
    "Digital influence",
    "Collaboration",
    "Community and loyalty",
}
EVIDENCE = {"Opened in full", "Snippet only", "Unverified"}

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
files = sorted(glob.glob(os.path.join(root, "brands", "*", "initiatives.csv")))
errors = []
seen_ids = set()
count = 0

for path in files:
    name = os.path.basename(path)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != HEADER:
            errors.append("%s: header does not match the template" % name)
            continue
        for n, row in enumerate(reader, 2):
            count += 1
            where = "%s line %d" % (name, n)
            if not row["id"]:
                errors.append(where + ": missing id")
            elif row["id"] in seen_ids:
                errors.append(where + ": duplicate id " + row["id"])
            seen_ids.add(row["id"])
            if row["family"] not in FAMILIES:
                errors.append(where + ": unknown family '%s'" % row["family"])
            if row["evidence_status"] not in EVIDENCE:
                errors.append(where + ": unknown evidence status '%s'" % row["evidence_status"])
            if not row["source_url"].startswith("http"):
                errors.append(where + ": source_url must be a link")
            t = row["transferability_1to3"]
            if t and t not in {"1", "2", "3"}:
                errors.append(where + ": transferability must be 1, 2 or 3")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("OK: %d initiatives in %d files" % (count, len(files)))
