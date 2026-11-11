# How to contribute

## Add a brand

1. Pick a brand from `data/brands.csv` or propose a new one.
2. Create a branch named `brand/<brand-slug>`.
3. Copy the folder `brands/_template/` to `brands/<brand-slug>/` if your brand has no folder yet.
4. Research the brand with `prompts/brand_research_prompt.md` and fill one row per initiative. Aim for 10 to 20 initiatives and choose depth over breadth.
5. Fill the brand card in `brands/<brand-slug>/README.md` (footprint, positioning, ratings, three takeaways, gaps, sources) and update the brand's row in `data/brands.csv`.
6. Run `python3 scripts/check_initiatives.py`. Fix every error it reports.
7. Run `python3 scripts/merge_initiatives.py` and commit the regenerated `data/initiatives_all.csv`.
8. Open a pull request. A teammate reviews the sources before merging.

One folder per brand avoids merge conflicts. Never edit `data/initiatives_all.csv` by hand.

## Evidence rules

- Prefer primary sources (brand site, press releases, official social accounts), then trade press (WWD, Business of Fashion, Modern Retail, Retail Dive, FashionUnited).
- Open each page in full before using it. A search snippet alone does not count.
- Set `evidence_status` to Opened in full, Snippet only or Unverified.
- Keep facts, inferences and unknowns apart. Write "Not found" when you cannot find a figure and never estimate one.
- Give each fact its source date and flag sources more than three years old.
- Paraphrase sources and quote at most 15 words from any one page.

## Allowed values

- `family`: One-off in-store experience, Recurring experience, Omnichannel set-up, Activation, Digital influence, Collaboration, Community and loyalty
- `evidence_status`: Opened in full, Snippet only, Unverified
- `transferability_1to3`: 1, 2, 3 or empty until the team rates it

## Public repository rules

Do not commit client documents, internal planning files, interview notes with named individuals, credentials or personal data. When in doubt, keep it out and ask the team.
