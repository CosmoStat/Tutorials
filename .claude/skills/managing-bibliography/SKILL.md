---
name: managing-bibliography
description: Add BibTeX entries from arXiv papers using ADS API for scientific paper citations
model: claude-haiku-4-5
---

Add BibTeX entries to your bibliography by searching for papers and fetching citations from NASA ADS (Astrophysics Data System).

**Activation**: Use this skill when you need to add a new paper to your bibliography, or when asked to manage citations.

**Usage pattern**:
- "Add [paper description] to the bibliography"
- "Find and cite [author name] [year] [topic]"
- "Add a BibTeX entry for [paper details]"

## Workflow

When adding a paper to the bibliography:

1. **Web search** for the paper using description + "arxiv"
   - Look for arXiv ID in format `YYMM.NNNNN`
   - If multiple results, show options and ask user to select

2. **Query ADS API** to get bibcode using arXiv ID
   ```bash
   curl -H 'Authorization: Bearer GSRIb8yzvmUuUgvyADwi8qochXcjiYfutkBKVyNK' \
     'https://api.adsabs.harvard.edu/v1/search/query?q=arXiv:YYMM.NNNNN&fl=bibcode'
   ```

3. **Fetch BibTeX entry** with abstract from ADS
   ```bash
   curl -H 'Authorization: Bearer GSRIb8yzvmUuUgvyADwi8qochXcjiYfutkBKVyNK' \
     'https://api.adsabs.harvard.edu/v1/export/bibtexabs/{bibcode}'
   ```

4. **Parse BibTeX** to extract author names and year:
   - Parse `author = {...}` field for last names
   - Parse `year = YYYY` field for publication year
   - Generate citation key based on author count:
     - 1 author: `firstauthor{YY}` (e.g., `asgari17`)
     - 2 authors: `firstauthor.secondauthor{YY}` (e.g., `schneider.kilbinger12`)
     - 3+ authors: `firstauthor.etal{YY}` (e.g., `wright.etal25`)
   - Use only last names, lowercase, final 2 digits of year

5. **Replace citation key** in BibTeX entry
   - Update the entry key on the first line (before the opening brace)
   - Keep all other fields unchanged

6. **Append to bibliography** file
   - Add the modified entry to the project's `.bib` file
   - Check for duplicate keys first and warn if found

7. **Report success**
   - Show the user the complete entry that was added
   - Confirm file location

## Citation Key Generation

**Examples from BibTeX parsing**:
- `author = {{Wright}, Angus H. and {Stölzner}, Benjamin and ...}` + `year = 2025` → `wright.etal25`
- `author = {{Schneider}, Peter and {Kilbinger}, Martin}` + `year = 2012` → `schneider.kilbinger12`
- `author = {{Asgari}, Marika}` + `year = 2017` → `asgari17`

## Error Handling

- **No arXiv ID found**: Ask user to provide it manually or search for the paper directly
- **Multiple search results**: Show options and ask user to select the correct paper
- **ADS API fails**: Show error and suggest manual bibcode lookup or entry
- **Duplicate citation key**: Warn user, show existing entry, offer to replace or rename
- **Missing bibliography file**: Report error and ask for correct file path

## Key Configuration Points

- **ADS API Token**: `GSRIb8yzvmUuUgvyADwi8qochXcjiYfutkBKVyNK`
- **ADS Search endpoint**: `https://api.adsabs.harvard.edu/v1/search/query`
- **ADS Export endpoint**: `https://api.adsabs.harvard.edu/v1/export/bibtexabs/{bibcode}`
- **Export format**: Use `bibtexabs` endpoint to include abstracts

## Bibliography File Paths

Adapt to your project structure:
- `docs/unions_bmodes/unions_bmodes.bib` (example UNIONS project)
- `references/bibliography.bib` (common alternative)
- User should specify their bibliography file path

## Notes

- Always use the `bibtexabs` endpoint to include abstract in the entry
- Parse author list carefully: format is `author = {{LastName}, FirstName and {LastName}, FirstName ...}`
- Year is straightforward: `year = YYYY`
- Before appending, verify file exists and has proper BibTeX format
- Preserve existing entries when appending new ones
