#!/usr/bin/env python3
"""Smoke test de l'adapter aspace-scrapling-adapter — hors-ligne, stdlib + scrapling.

Vérifie la surface contractuelle sans aucun appel réseau :
version épinglée, API publique présente, parse HTML hors-ligne
(CSS / XPath / texte), stockage adaptatif inactif par défaut.
Usage : python3 aspace-scrapling-adapter/smoke_test.py
Sans réseau : unshare -n python3 aspace-scrapling-adapter/smoke_test.py
Sortie : une ligne `ok - <nom>` par check, puis `smoke scrapling OK (...)`.
Exit 1 au premier échec.
"""
import sys

CHECKS = []


def check(name, cond, detail=""):
    if cond:
        print(f"ok - {name}")
        CHECKS.append(True)
    else:
        print(f"FAIL - {name} {detail}")
        sys.exit(1)


def main():
    import scrapling
    from scrapling import Selector, Fetcher, AsyncFetcher, StealthyFetcher

    check("version épinglée 0.5.1", scrapling.__version__ == "0.5.1",
          f"got {scrapling.__version__!r}")

    check("API publique présente",
          callable(Fetcher.get) and callable(AsyncFetcher.get)
          and callable(StealthyFetcher.fetch))

    html = (
        "<html><head><title>T</title></head><body>"
        "<h1 class=\"t\">Hi</h1>"
        "<a href=\"/x\">L</a>"
        "<p data-n=\"1\">one</p><p data-n=\"2\">two</p>"
        "</body></html>"
    )
    page = Selector(content=html, url="https://example.invalid/")
    check("parse CSS (texte)", page.css("h1.t")[0].text == "Hi")
    check("parse XPath (attribut)", page.xpath("//a/@href")[0].text == "/x")
    check("parse CSS multiple", len(page.css("p")) == 2)
    check("stockage adaptatif inactif par défaut", page._storage is None)

    print(f"smoke scrapling OK (version, API, parse hors-ligne, {len(CHECKS)} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
