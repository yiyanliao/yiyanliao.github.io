"""Fetch Google Scholar profile metrics and write them to source/_data/scholar.json.

Runs weekly in CI (see .github/workflows/scholar.yml). Google Scholar has no public
API and blocks datacenter IPs intermittently, so this script fails *gracefully*: on
any error, or if it gets an empty result, it leaves the existing JSON untouched so the
badge keeps showing the last known values instead of dropping to zero.
"""
import datetime
import json
import pathlib
import sys

AUTHOR_ID = "9DUJUoQAAAAJ"
OUT = pathlib.Path("source/_data/scholar.json")


def main() -> int:
    try:
        from scholarly import scholarly

        author = scholarly.search_author_id(AUTHOR_ID)
        author = scholarly.fill(author, sections=["indices"])
        citations = int(author.get("citedby", 0) or 0)
        if citations <= 0:
            print("Scholar returned no citations; keeping existing file.")
            return 0
        data = {
            "citations": citations,
            "hindex": int(author.get("hindex", 0) or 0),
            "i10index": int(author.get("i10index", 0) or 0),
            "updated": datetime.date.today().isoformat(),
        }
    except Exception as exc:  # noqa: BLE001 — never fail the workflow on scrape errors
        print(f"Scholar fetch failed, keeping existing file: {exc}")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print("Updated scholar.json:", data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
