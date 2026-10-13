# Niger (NE) — législation en Markdown

Part of [LawCodex](https://github.com/LawCodex): the legislation of every country as plain Markdown in git.

**Minimal repository: basic constitutional texts of the Republic of Niger** (in French, the official language),
from official websites of the Presidency and of the Government.

Retrieved 2026-10-13.

<!-- COUNTS -->
| Directory | Files |
|---|---|
| `constitution/` | 2 |
| **Total** | **2** |
<!-- /COUNTS -->

## Contents

```
constitution/charte-de-la-refondation-2025.md   Charte de la Refondation, promulgated 26 March 2025 (with the promulgation decree)
constitution/constitution-2010.md               Constitution of the Seventh Republic, 25 November 2010
```

Constitutional context (stated factually): on 26 July 2023 the military took power; the Conseil national pour la
sauvegarde de la patrie (CNSP) suspended the Constitution of 25 November 2010 by ordonnance n° 2023-01 of 28 July
2023 and organised the public authorities by ordonnance n° 2023-02. Following the Assises nationales pour la
Refondation (February 2025), the *Charte de la Refondation* was promulgated by décret n° 2025-160/P/CNSP of 26 March
2025 (Journal officiel of 31 March 2025). Under its article 78 the Charter has constitutional value and repeals
ordonnance n° 2023-02; its preamble records the end of the Seventh Republic; article 73 sets the duration of the
Refondation period at 60 months from promulgation, adjustable. The 2010 Constitution is kept for reference with
`status: unknown` and an explanatory note.

The Charter comes from a scan of the Journal officiel and was OCRed (tesseract, French): expect recognition errors
(e.g. "Chapitre JE" for "Chapitre II", "Ja" for "la"). The 2010 Constitution PDF has a text layer.

## Sources

| Document | URL |
|---|---|
| Charte de la Refondation (JO of 31 March 2025) — Présidence de la République, "Textes officiels" | https://www.presidence.ne/pages/textes-officiels → https://www.presidence.ne/uploads/20260716_072647_charte-de-la-refondation-2025.pdf |
| Constitution of 25 November 2010 — Gouvernement du Niger, "Textes fondamentaux" | https://www.gouv.ne/index.php/textes-fondamentaux/constitution-de-la-7eme-republique |

## Not covered / known gaps

* **No ordinary legislation.** No official online collection of Nigerien laws and ordinances could be reached: the
  Secrétariat général du Gouvernement / Journal officiel website (sgg.gouv.ne) did not answer and has no Internet
  Archive captures; the Assemblée nationale (dissolved in July 2023) site only had speeches and reports.
  Since 2023, legislation takes the form of ordinances of the CNSP / President.
* The gouv.ne site also offers the Code électoral and the Charte des partis politiques of the Seventh Republic
  period; they were not included (political parties were dissolved by ordonnance n° 2025-06 of 26 March 2025,
  printed in the same Journal officiel issue, which is not included either).

## Copyright

Official texts of the Republic of Niger, published on government websites without stated reuse restrictions. The
Markdown conversion is provided as is; the authoritative text is the one published in the Journal officiel de la
République du Niger.

## Regenerating

```sh
python3 scripts/ne_fetch.py    # downloads the two PDFs to ../_raw/ne/ and writes the Markdown (needs tesseract + fra)
python3 scripts/ne_readme.py   # updates the counts table
```
