# BracketX — Composite Power Index Dashboard

## PROJECT OVERVIEW
Interactive NCAA Tournament 2026 dashboard. 39 composite ranking systems + 7 compare systems across 68 tournament teams. Single-page HTML app with React (loaded via CDN), rendered on dark background (#0d1117).

## CURRENT STATE
`bracketx.html` is the working dashboard. It renders but has design issues that need fixing. DO NOT rewrite from scratch. Make surgical fixes only.

## CRITICAL RULES
- NEVER do a full rewrite. Only make targeted, surgical changes.
- All backgrounds MUST be explicit dark colors (#0d1117 or #0e1218). Never use "transparent" on containers.
- Before showing any output, verify: syntax OK, dark backgrounds explicit, all features still present.
- All data is real, verified, extracted from source spreadsheets. NEVER estimate or approximate data.

## TECH STACK
- Single HTML file with inline React (loaded via CDN: react 18.2.0, react-dom 18.2.0)
- Uses React.createElement (not JSX) since there's no build step
- Fonts: Outfit (900 weight for BRACKETX logo), DM Mono (data/monospace)
- Color scheme: bg #0d1117, cyan #00d4ff, green #00e676, red #ff4444, gold #ffd600, orange #ff6b35

## DESIGN SPEC (from screenshots)
- Header: "BRACKETX" in Outfit 900 + gold "COMPOSITE POWER INDEX" in DM Mono
- Tabs: RANKINGS, BRACKET, MATCHUPS, FUTURES, METHODOLOGY
- Region pills: ALL, EAST, SOUTH, WEST, MIDWEST (color-coded)
- Rankings table: horizontally scrollable, X# cyan, per-seed colored badges, wide team column, conf·record on one line
- Left border: all cyan (#00d4ff) down entire table
- X-SCORE values: cyan. BEST header: green. WORST header+values: red (#ff4444)
- System columns: T1=cyan, T2=bronze(#c0885a), T3=blue-slate(#8899aa)
- Green/red highlight boxes on system values where rank differs 10+ from X-rank (22% opacity, bright)
- Hover tooltips on every column header showing full system name
- RATINGS KEY button opens modal with all 39 systems by tier

## BRACKET TAB
- Interactive "Build Your BracketX Bracket" simulator
- Round-by-round tabs: R64, R32, S16, E8, Final Four, Championship
- Radio circle picks, independent advancement, 63-pick counter, RESET, champion display
- X-Spread + win % on every game card
- PREVIEW button for head-to-head comparison popup
- Game dates/times on R64 cards

## MATCHUPS TAB
- All 32 R64 matchups as cards with region color borders
- X-Spread + KenPom rank comparison on each card
- Win probability bars
- EDGE badges on high-value matchups

## FUTURES TAB
- Bracket-path probability simulation using X-Scores
- Columns: X#, SD, TEAM, CHAMP%, TITLE%, F4%, E8%, S16%
- Color-coded headers (gold=champ, orange=title, cyan=F4, green=E8)

## DATA
- `bracketx.html` contains all data inline (R, SR, CR arrays + BRACKET)
- `R_fixed.json` / `SR_fixed.json` = corrected data with Dolphin fix
- `xscore_v5.json` = full X-Score computation results
- `dashboard_data_v5.js` = JS arrays (NOTE: has OLD unfixed Dolphin - use R_fixed/SR_fixed instead)
- `name_map.py` = team name normalization (282 aliases)

## SPREAD FORMULA
X-Spread = X-Score differential × 8.3, shown to nearest tenth

## FOOTER
Black background, "BRACKETX" logo + "Chris Dell: Founder"
