#!/usr/bin/env python3
"""Niger: Charte de la Refondation (26 March 2025) and the Constitution of 25 November 2010
(Seventh Republic), from official websites of the Presidency (presidence.ne) and the Government (gouv.ne).
Usage: python3 ne_fetch.py [--no-download]"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ne_text as T  # noqa

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(os.path.dirname(REPO), "_raw", "ne")
os.environ.setdefault("LC_TESSDATA", os.path.join(RAW, "tessdata"))
os.environ["LC_PSM"] = "3"  # two-column Journal officiel scans
RETRIEVED = os.environ.get("LC_RETRIEVED", "2026-10-13")
CHARTE = "https://www.presidence.ne/uploads/20260716_072647_charte-de-la-refondation-2025.pdf"
CONST = "https://www.gouv.ne/images/textes-fondamentaux/constitution.pdf"


def get(url, name):
    dest = os.path.join(RAW, name)
    if "--no-download" not in sys.argv:
        T.fetch(url, dest, delay=3, check_pdf=True)
    if not T.pdf_ok(dest):
        raise SystemExit("bad pdf " + url)
    return dest


def main():
    # Charte de la Refondation: JO of 31 March 2025 (scan); keep the promulgation decree and the Charter
    pages, ocr = T.pdf_text(get(CHARTE, "charte.pdf"), "fra", tmpdir=RAW)
    lines = T.clean_pages(pages)
    a = [i for i, x in enumerate(lines) if re.match(r"^D[ée]cret n° ?2025-160", x)][-1]  # skip the table of contents
    b = next(i for i, x in enumerate(lines) if i > a and re.match(r"^MINIST[EÈ]RE DE LA D[EÉ]FENSE", x))
    seg = [x for x in lines[a:b] if not re.match(r"^(\d{1,2} mars 2025|JOURNAL OFFICIEL DE LA REPUBLIQUE DU NIGER|\d{4})$", x)]
    body = T.structure(seg, "fr")
    meta = {"title": "Charte de la Refondation", "identifier": "Décret n° 2025-160/P/CNSP du 26 mars 2025 portant promulgation de la Charte de la Refondation",
            "type": "constitution", "jurisdiction": "ne", "language": "fr", "date": "2025-03-26", "status": "in_force",
            "source": CHARTE, "record": "https://www.presidence.ne/pages/textes-officiels",
            "gazette": "Journal officiel de la République du Niger, 31 mars 2025 (numéro spécial)",
            "retrieved": RETRIEVED,
            "note": "Charter with constitutional value (art. 78); text obtained by OCR of the scanned Journal officiel, with the promulgation decree"}
    T.write_md(os.path.join(REPO, "constitution", "charte-de-la-refondation-2025.md"), meta, meta["title"], body)
    print("OK charte", sum(len(x) for x in body), "OCR" if ocr else "")
    # Constitution of 25 November 2010
    pages, ocr = T.pdf_text(get(CONST, "constitution-2010.pdf"), "fra", tmpdir=RAW)
    body = T.structure(T.clean_pages(pages), "fr")
    meta = {"title": "Constitution de la VIIème République", "identifier": "Décret n° 2010-754/PCSRD du 25 novembre 2010",
            "type": "constitution", "jurisdiction": "ne", "language": "fr", "date": "2010-11-25", "status": "unknown",
            "source": CONST, "record": "https://www.gouv.ne/index.php/textes-fondamentaux/constitution-de-la-7eme-republique",
            "retrieved": RETRIEVED,
            "note": ("Suspended by ordonnance n° 2023-01 of 28 July 2023; the Charte de la Refondation of 26 March 2025 "
                     "records the end of the Seventh Republic. Kept for reference")}
    T.write_md(os.path.join(REPO, "constitution", "constitution-2010.md"), meta, meta["title"], body)
    print("OK constitution 2010", sum(len(x) for x in body), "OCR" if ocr else "")


if __name__ == "__main__":
    main()
