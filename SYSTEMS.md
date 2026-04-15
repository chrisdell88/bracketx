# BracketX — Definitive Systems Reference

**Source of truth: `_rkSys` array in `bracketx.html` (Ratings Key modal)**
**Last verified: 2026-03-28**

Total: **58 systems** = 46 weighted (T1+T2) + 12 compare/reference (T3)
- 12 systems: user provides manually
- 34 systems: auto-scraped by scraper.py
- 12 systems: T3 compare/reference (user provides when available)

## CRITICAL NOTES
- ALL systems rank 300+ Division I teams nationally. We extract and store only the 68 tournament teams' ranks.
- Dolphin Simulation is flagged in the code only because its scraper returns raw national ranks instead of converting to 1-68 relative rank — this is a scraper bug, not a scale difference.
- All 68 tournament teams MUST be present in every system. No partial coverage accepted.

---

## YOU PROVIDE (12 systems)

### T1 — Efficiency Models (upload after each round)
| Abbr | Full Name | URL |
|------|-----------|-----|
| KP | KenPom Efficiency Ratings | https://kenpom.com |
| BT | BartTorvik T-Rank | https://barttorvik.com |
| EM | Evan Miya BPR | https://evanmiya.com |
| COOP | COOPER Bayesian Elo (Nate Silver) | https://natesilver.net |
| SW | SwishStats Team Ratings | https://swishstats.org |
| HAS | HaslaMetrics | https://haslametrics.com |
| INCC | INCC Stats | https://inccstats.com |
| DEEP | DeepMetrics | https://deepmetricanalytics.com |
| CMBKI | CMBKI+ Composite | https://cfbpredictor.com |

### T2 — No public data endpoint (you provide)
| Abbr | Full Name | URL |
|------|-----------|-----|
| FTN | FTN Power Rankings | https://ftnfantasy.com |
| BARON | Noah Baron's Rankings | https://noahbaron.substack.com |
| DLPHN | Dolphin Simulation | https://dolphinsim.com |

---

## I SCRAPE (34 systems)

### Confirmed working (30)
| Abbr | Full Name | URL | Notes |
|------|-----------|-----|-------|
| BPI | ESPN BPI | https://espn.com/mens-college-basketball/bpi | T1 |
| MASSEY | Massey Ratings | https://masseyratings.com | T2 |
| COLLEY | Colley's Bias Free Matrix | https://colleyrankings.com | T2 — fetches via HTML frame |
| DRAT | DRatings Inference Index | https://dratings.com | T2 |
| VERSUS | Versus Sports Simulator | https://versussportssimulator.com | T2 |
| SIMM | Simmons Ratings | https://simmonsratings.com | T2 — non-standard HTML |
| JENG | James England Rankings | https://rankings.jameseng.land | T2 |
| TALIS | Talisman Red's Ratings | https://talismanred.com | T2 |
| SONNY | Sonny Moore Power Ratings | https://sonnymoorepowerratings.com | T2 |
| WHEEL | WheelusSports | https://rwheelus.github.io | T2 |
| AEI | Adjusted Elo Ratings | https://aeiratings.com | T2 — direct CSV |
| OOSH | Splunty Rankings (OOSH) | https://misteroosh.wixsite.com | T2 |
| WOLFE | Wolfe Ratings | https://wolferatings.com | T2 |
| BCM | BCMoore Rankings | https://ncaa.bcmoorerankings.com | T2 |
| CJB | CJB Ratings | https://cjb-ratings.com | T2 |
| ENTROPY | Entropy System | https://dokterentropy.com | T2 — parser needs finishing |
| DUNK | Dunkel Index | https://dunkelindex.com | T2 pre |
| TMRK | TeamRankings | https://teamrankings.com | T2 pre |
| WAYWD | Bryan Wilson Empirical (Wayward) | https://waywardtrends.com | T2 pre |
| WHTLK | Whitlock Rankings | https://whitlockrankings.com | T2 pre |
| QRI | Quality Rating Index | https://bracket-madness.sbs | T2 pre |
| WHOE | Who Earned It? | https://whoearnedit.com | T2 pre |
| AMSTS | All My Sports Teams Suck | https://allmysportsteamssuck.com | T2 pre |
| OMNI | Omni Rankings | https://omnirankings.com | T2 pre |
| JNG | Job's Nitty Gritty | https://hoopshd.com | T2 pre |
| SRCBB | Sports-Reference | https://sports-reference.com | T2 pre |
| TPR | The Power Rank | https://thepowerrank.com | T2 pre |
| PACK | Packard Power Rankings | https://org.coloradomesa.edu | T2 pre |
| BIHL | Bihl Rankings | https://jeffbihl.com | T2 pre |
| RAMS | RAMS Rating System | https://ramsrating.com | T2 pre |

### Parsers still need to be written (4)
| Abbr | Full Name | URL |
|------|-----------|-----|
| STATSHARP | StatSharp Power Ratings | https://statsharp.com |
| MOOG | Mark Moog Ratings | https://markmoog.com |
| ODDS | Odds Gods Rankings | https://egomaniacsbracket.onrender.com |
| JTHOM | JThom Analytics | https://jthomanalytics.com |

---

## T3 COMPARE / REFERENCE (12 — not weighted in X-Score)
| Abbr | Full Name | URL |
|------|-----------|-----|
| NET | NCAA NET Rankings | https://ncaa.com |
| RPI | RPI | https://warrennolan.com |
| LRMCB | LRMC Bayesian | https://isye.gatech.edu |
| LRMCC | LRMC Classic | https://isye.gatech.edu |
| LRMC-NM | LRMC No-MOV | https://isye.gatech.edu |
| LAURA | Laura Albert (Badger Bracketology) | https://bracketology.engr.wisc.edu |
| CPURE | COOPER Pure Elo | https://natesilver.net |
| CPROG | COOPER Progression | https://natesilver.net |
| SOR | SOR (Strength of Record) | https://espn.com |
| WAB | WAB (Wins Above Bubble) | https://wabwatch.com |
| CMTE | NCAA Committee Rankings | https://ncaa.com |
| SRAT | Sports Ratings | https://sports-ratings.com |

---

## TOTALS
- 12 (you provide) + 34 (I scrape) = **46 weighted systems**
- + 12 T3 compare = **58 total**

---

## TIER WEIGHTS IN X-SCORE
- T1: weight 3x (Evan Miya BPR gets 3.5x)
- T2: weight 1x
- T3: not weighted (compare/reference only)

## CORRECT SL ARRAY (38 systems currently in code — missing: CMBKI, FTN, STATSHARP, MOOG, ODDS, BARON, JTHOM, CJB until data is gathered)
KP, BT, EM, COOP, SW, HAS, INCC, BPI, DEEP (T1=9)
MASSEY, COLLEY, DRAT, VERSUS, SIMM, JENG, TALIS, SONNY, WHEEL, AEI, OOSH, WOLFE, BCM (T2 recent=13)
DUNK, TMRK, WAYWD, WHTLK, QRI, WHOE, AMSTS, OMNI, JNG, SRCBB, TPR, PACK, DLPHN, BIHL, RAMS, ENTROPY (T2 pre+=16)

## AFTER EACH ROUND — UPDATE WORKFLOW
1. You upload 12 manual systems
2. Run `python3 scraper.py` → scraped_ranks.json
3. Merge into SR matrix (68 × 46)
4. Recompute X-Score
5. Update R, BRACKET, TRACKER arrays in bracketx.html
6. Update book spreads via Odds API
7. `git push origin main` → live in ~2 min
Target: ~30 minutes per round
