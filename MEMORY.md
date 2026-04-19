# bracketx — Project Memory

**Last updated:** 2026-04-19
**Repo:** https://github.com/chrisdell88/bracketx
**Live:** single-page HTML (bracketx.html / index.html)

## Session start protocol
1. `cd ~/Projects/bracketx`
2. `git pull` (auto via hook)
3. Read this file
4. `git log --oneline -10` for recent context

## Current state (post-tournament)
Tournament is **over** — Michigan won the 2026 NCAA Championship. Dashboard is now a completed retrospective + interactive archive.

- `bracketx.html` = production dashboard, single-file React-via-CDN (no build step, React.createElement, not JSX)
- 48 composite ranking systems live in the data (up from 39 in original spec)
- 68/68 team coverage across all systems after F4 fixes
- X-Score v6 is the latest computation (`xscore_v6.json`); v5 still referenced as fallback
- Data arrays (R, SR, CR, BRACKET) inlined in `bracketx.html`

## Tabs (all shipped)
- **RANKINGS** — horizontal scroll table, 48 systems, color-coded tiers, 10+ rank-diff highlights, hover tooltips, RATINGS KEY modal
- **BRACKET** — interactive 63-pick simulator, R64 → Championship, X-Spread + win%, PREVIEW head-to-head popup
- **MATCHUPS** — all 32 R64 cards with region borders, X-Spread, KenPom comparison, EDGE badges
- **FUTURES** — bracket-path probability sim; now includes **retrospective with actual results** (fec2eed)
- **SIMULATE** — 10K-run Monte Carlo, visual bracket shape with connectors
- **METHODOLOGY** — explains X-Score, spread formula (Δ × 8.3)
- **TRACKER / TICKER** — live results tracker through championship, 64 games

## Recent work arc
1. Final Four prep: E8 results, F4 matchups, ticker updates (e82de56)
2. Mobile responsive polish (04477db)
3. F4 X-score refresh — 43→48 systems, VERSUS fix (Illinois 81→7), SRAT to 68/68, Dunkel added
4. CPROG removed entirely (14e0831)
5. QRI column re-ranked from raw scores, 62/68 matched (1ced049)
6. F4 full data update: 12 systems fixed to 68/68 (e3d879e)
7. Championship: Michigan wins, 48 systems, ticker + tracker complete (42c4192)
8. Ratings Key date audit + Futures retrospective with actuals (fec2eed)
9. WIP save: logos (bracketx-logo.png, apple-touch-icon, og-image, favicon-512), SYSTEMS.md doc, rankings data (d47562d)
10. MEMORY.md stub committed for cross-device sync (8828047)

## Where we left off (2026-04-19)
- Tournament complete, retrospective in place
- Logos + favicons + og-image added to repo (WIP commit d47562d) — **verify they're wired into `<head>` of index.html / bracketx.html**
- `SYSTEMS.md` added as documentation of all 48 ranking systems
- `new_ranks.json`, `raw_ratings.json`, `scraped_ranks.json`, `r_array_v63.js` are WIP data files from the F4/championship update pipeline
- `scraper.py` + `name_map.py` (282 aliases) handle the refresh pipeline
- No open bugs flagged; last functional change was Futures retrospective

## Critical rules (from CLAUDE.md)
- **NEVER full-rewrite** bracketx.html — surgical edits only
- All backgrounds explicit dark (`#0d1117` / `#0e1218`) — never `transparent`
- All data is real/verified — never estimate
- Color scheme: bg `#0d1117`, cyan `#00d4ff`, green `#00e676`, red `#ff4444`, gold `#ffd600`, orange `#ff6b35`
- Fonts: Outfit 900 (logo), DM Mono (data)
- X-Spread formula: X-Score differential × 8.3, to nearest tenth

## Key files
| File | Purpose |
|---|---|
| `bracketx.html` | Main dashboard (inline React + data) |
| `index.html` | Entry point |
| `xscore_v6.json` | Latest X-Score computation |
| `xscore_v5.json` | Prior X-Score (fallback reference) |
| `dashboard_data_v5.js` | JS arrays (has OLD unfixed Dolphin — prefer R_fixed/SR_fixed) |
| `scraper.py` | Ranking system scraper |
| `name_map.py` | 282-alias team name normalization |
| `SYSTEMS.md` | Documentation of all 48 systems |
| `CNAME` | Custom domain config |

## Next likely tasks
- Verify logo/favicon/og-image meta tags are wired in HTML `<head>`
- Final design polish pass now that tournament is over
- Possible 2027 prep: archive current dashboard, set up refresh pipeline
