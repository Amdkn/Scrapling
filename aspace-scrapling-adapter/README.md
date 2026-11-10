# aspace-scrapling-adapter

Adapter A'Space (seul code A'Space du fork `Amdkn/Scrapling`) pour **Scrapling 0.5.1**,
gel `c5121c7` — bibliothèque Python de web scraping (parse HTML + fetchers HTTP/navigateur).

## Surface (contrat)

Voir `contract.json`. Surface exposée, par ordre de priorité :

1. **`scrapling.Selector(content)`** — parse HTML **hors-ligne** (CSS / XPath / texte).
   Stockage adaptatif désactivé par défaut (`adaptive=False`) : aucun fichier créé.
2. **`scrapling.Fetcher.get(url)`** — requête HTTP explicite de l'utilisateur.
   Jamais invoquée par l'adapter ; jamais invoquée sans URL donnée par l'appelant.
3. **`scrapling.AsyncFetcher` / `scrapling.StealthyFetcher`** — mêmes règles.

## Ce que l'adapter ne fait jamais

- Aucun appel réseau de sa propre initiative (ni fetch, ni vérification de version,
  ni rapport) — la télémétrie est **zéro** (voir `scrapling-TELEMETRY-AUDIT.md`).
- Aucune modification du code amont, aucune copie de fichier amont.
- Aucun secret lu ou écrit.

## Licence — clause de non-approbation (BSD-3-Clause, clause 3)

Le fork `Amdkn/Scrapling` **n'est ni endossé par D4Vinci, ni présenté comme tel**.
Le nom du titulaire du copyright et des contributeurs ne sert pas à endosser
ou promouvoir un produit dérivé sans autorisation écrite préalable.
`LICENSE` amont préservé byte-identique dans le fork.

## Smoke test

```sh
python3 aspace-scrapling-adapter/smoke_test.py
# sans interface réseau :
unshare -n python3 aspace-scrapling-adapter/smoke_test.py
```

Attendu : 6 checks `ok`, puis `smoke scrapling OK (...)`.
