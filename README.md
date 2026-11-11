# Yohji Yamamoto US: initiative benchmarks

Shared workspace for the brand and community workstream. We benchmark initiatives that comparable brands ran in the US, with New York as the priority, to learn what Yohji Yamamoto could do to build its brand, community and digital presence there.

**This repository is public.** Put only public-source research here. Client documents, internal files and personal data stay out.

## Where to start

1. Read `docs/goal.md` for the goal and the question each brand must help answer.
2. Read `docs/framework.md` for the seven initiative families, the eight attributes and the rating scale.
3. Follow `docs/process.md` to add your brand.
4. Use `prompts/brand_research_prompt.md` to run the research for a brand.
5. Slides and client documents are in the team SharePoint. The link is in `docs/links.md`.

## Structure

```
README.md
docs/
  goal.md                        Goal and the question to answer
  framework.md                   Initiative families, attributes, rating scale
  process.md                     How to contribute, evidence rules, merge steps
  links.md                       Link to the team SharePoint (slides and client documents)
prompts/
  brand_research_prompt.md       Prompt to research one brand
data/
  brands.csv                     One row per brand: footprint, status, caveats, sources
  brand_scores.csv               Draft brand-level ratings on six criteria
  initiatives_all.csv            Generated merge of all brand files (do not edit)
brands/
  _template/                     Copy this folder to start a new brand
  <brand-slug>/
    README.md                    Brand card: footprint, positioning, ratings, takeaways, gaps, sources
    initiatives.csv              One row per initiative
scripts/
  check_initiatives.py           Validates the brand files
  merge_initiatives.py           Builds data/initiatives_all.csv
```

## Brand folders and owners

One folder per brand under `brands/`. Comme des Garcons and Dover Street Market have separate folders. Priority brands and who covers them (put your name in the Owner column when you claim a brand):

| Brand | Folder | Owner | Initiatives now |
| --- | --- | --- | --- |
| Rick Owens | `brands/rick-owens/` | To claim | 3 |
| Issey Miyake | `brands/issey-miyake/` | To claim | 1 |
| Dries Van Noten | `brands/dries-van-noten/` | To claim | 3 |
| Comme Des Garcons | `brands/comme-des-garcons/` | Loic | 15 |
| Gentle Monster | `brands/gentle-monster/` | Loic | 15 |

## Current state

75 initiatives across 16 brands, pre-filled from pages opened in full unless a row says "Snippet only". Transferability ratings are still empty and need a team decision. Brand ratings in `data/brand_scores.csv` are drafts.

## Commands

```
python3 scripts/check_initiatives.py
python3 scripts/merge_initiatives.py
```
