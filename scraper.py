#!/usr/bin/env python3
"""BracketX scraper — all 49 scrapeable systems."""

import urllib.request, re, json, csv, io, html

H = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
     "Accept-Language":"en-US,en;q=0.9"}

TEAMS = ["Michigan","Duke","Arizona","Houston","Iowa State","Florida","Purdue","Illinois",
         "Michigan State","UConn","St. John's","Gonzaga","Vanderbilt","Alabama","Nebraska",
         "Arkansas","Virginia","Tennessee","Louisville","Kansas","Texas Tech","Wisconsin",
         "BYU","Ohio State","Kentucky","Saint Mary's","Iowa","UCLA","Utah State",
         "North Carolina","Miami FL","Saint Louis","Clemson","Villanova","NC State",
         "Santa Clara","Georgia","Texas","Texas A&M","TCU","VCU","South Florida","SMU",
         "UCF","Missouri","Akron","McNeese","High Point","Miami OH","Northern Iowa",
         "Hofstra","Cal Baptist","Hawaii","North Dakota State","Wright State","Troy",
         "Penn","Kennesaw State","Idaho","Siena","Furman","Queens","Tennessee State",
         "UMBC","Howard","LIU","Lehigh","Prairie View A&M"]

ALIASES = {
    "michigan wolverines":"Michigan","michigan":"Michigan",
    "duke blue devils":"Duke","duke":"Duke",
    "arizona wildcats":"Arizona","arizona":"Arizona",
    "houston cougars":"Houston","houston":"Houston",
    "iowa state cyclones":"Iowa State","iowa state":"Iowa State",
    "iowa st":"Iowa State","iowa st.":"Iowa State",
    "florida gators":"Florida","florida":"Florida",
    "purdue boilermakers":"Purdue","purdue":"Purdue",
    "illinois fighting illini":"Illinois","illinois":"Illinois",
    "michigan state spartans":"Michigan State","michigan state":"Michigan State",
    "mich. state":"Michigan State","mich state":"Michigan State","michigan st":"Michigan State",
    "michigan st.":"Michigan State",
    "connecticut huskies":"UConn","uconn huskies":"UConn","uconn":"UConn","connecticut":"UConn",
    "st. john's red storm":"St. John's","st john's":"St. John's","st. john's":"St. John's",
    "saint john's":"St. John's","st johns":"St. John's","st. johns":"St. John's",
    "saint johns":"St. John's","st. john\u2019s":"St. John's","st john\u2019s":"St. John's",
    "st johns red storm":"St. John's",
    "gonzaga bulldogs":"Gonzaga","gonzaga":"Gonzaga",
    "vanderbilt commodores":"Vanderbilt","vanderbilt":"Vanderbilt",
    "alabama crimson tide":"Alabama","alabama":"Alabama",
    "nebraska cornhuskers":"Nebraska","nebraska":"Nebraska",
    "arkansas razorbacks":"Arkansas","arkansas":"Arkansas",
    "virginia cavaliers":"Virginia","virginia":"Virginia",
    "tennessee volunteers":"Tennessee","tennessee":"Tennessee",
    "louisville cardinals":"Louisville","louisville":"Louisville",
    "kansas jayhawks":"Kansas","kansas":"Kansas",
    "texas tech red raiders":"Texas Tech","texas tech":"Texas Tech",
    "wisconsin badgers":"Wisconsin","wisconsin":"Wisconsin",
    "byu cougars":"BYU","brigham young":"BYU","byu":"BYU",
    "brigham young university":"BYU","brigham young cougars":"BYU","b.y.u.":"BYU","b.y.u":"BYU",
    "ohio state buckeyes":"Ohio State","ohio state":"Ohio State",
    "ohio st":"Ohio State","ohio st.":"Ohio State",
    "kentucky wildcats":"Kentucky","kentucky":"Kentucky",
    "saint mary's gaels":"Saint Mary's","saint mary's":"Saint Mary's",
    "st. mary's":"Saint Mary's","st mary's":"Saint Mary's","st mary's ca":"Saint Mary's",
    "st. mary's (cal)":"Saint Mary's","saint mary's ca":"Saint Mary's",
    "saint marys":"Saint Mary's","st. mary's gaels":"Saint Mary's","saint marys gaels":"Saint Mary's",
    "st. mary's ca.":"Saint Mary's","st. mary's-cal":"Saint Mary's","saint mary's (wcc)":"Saint Mary's",
    "saint mary's college gaels":"Saint Mary's","saint mary's college":"Saint Mary's",
    "st. mary's college gaels":"Saint Mary's","st. mary's college":"Saint Mary's",
    "iowa hawkeyes":"Iowa","iowa":"Iowa",
    "ucla bruins":"UCLA","ucla":"UCLA",
    "utah state aggies":"Utah State","utah state":"Utah State","utah st":"Utah State",
    "utah st.":"Utah State",
    "north carolina tar heels":"North Carolina","north carolina":"North Carolina",
    "unc":"North Carolina","unc tar heels":"North Carolina","unc chapel hill":"North Carolina",
    "miami hurricanes":"Miami FL","miami (fl)":"Miami FL","miami fl":"Miami FL",
    "miami florida":"Miami FL","miami":"Miami FL","miami(fl)":"Miami FL",
    "miami (oh)":"Miami OH","miami(oh)":"Miami OH","miami oh":"Miami OH","miami ohio":"Miami OH","miami-ohio":"Miami OH","miami-oh":"Miami OH","miami redhawks":"Miami OH",
    "saint louis billikens":"Saint Louis","saint louis":"Saint Louis",
    "st. louis":"Saint Louis","st louis":"Saint Louis",
    "clemson tigers":"Clemson","clemson":"Clemson",
    "villanova wildcats":"Villanova","villanova":"Villanova",
    "nc state wolfpack":"NC State","nc state":"NC State",
    "north carolina state":"NC State","n.c. state":"NC State","n. c. state":"NC State",
    "nc state wolfpack":"NC State","n. carolina state":"NC State",
    "north carolina st":"NC State",
    "santa clara broncos":"Santa Clara","santa clara":"Santa Clara",
    "georgia bulldogs":"Georgia","georgia":"Georgia",
    "texas longhorns":"Texas","texas":"Texas",
    "texas a&m aggies":"Texas A&M","texas a&m":"Texas A&M","texas am":"Texas A&M",
    "texas a & m":"Texas A&M","texas a&amp;m":"Texas A&M","texas a and m":"Texas A&M",
    "tcu horned frogs":"TCU","tcu":"TCU","texas christian":"TCU",
    "texas christian university":"TCU","tcu horned frogs":"TCU","t.c.u.":"TCU","t.c.u":"TCU",
    "vcu rams":"VCU","vcu":"VCU","virginia commonwealth":"VCU",
    "virginia commonwealth university":"VCU","vcu rams":"VCU",
    "south florida bulls":"South Florida","south florida":"South Florida","usf":"South Florida",
    "usf bulls":"South Florida","s florida":"South Florida","s. florida":"South Florida",
    "smu mustangs":"SMU","smu":"SMU","southern methodist":"SMU",
    "southern methodist university":"SMU","smu mustangs":"SMU",
    "ucf knights":"UCF","ucf":"UCF","central florida":"UCF",
    "ucf knights":"UCF","university of central florida":"UCF",
    "missouri tigers":"Missouri","missouri":"Missouri","mizzou":"Missouri",
    "akron zips":"Akron","akron":"Akron","u. of akron":"Akron",
    "mcneese state cowboys":"McNeese","mcneese cowboys":"McNeese",
    "mcneese state":"McNeese","mcneese":"McNeese","mcneese st":"McNeese","mcneese st.":"McNeese",
    "high point panthers":"High Point","high point":"High Point","high point university":"High Point",
    "miami (oh) redhawks":"Miami OH","miami oh":"Miami OH","miami ohio":"Miami OH",
    "miami (ohio)":"Miami OH","miami redhawks":"Miami OH","miami-oh":"Miami OH",
    "miami oh redhawks":"Miami OH",
    "northern iowa panthers":"Northern Iowa","northern iowa":"Northern Iowa","uni":"Northern Iowa",
    "n iowa":"Northern Iowa","n. iowa":"Northern Iowa","n. iowa panthers":"Northern Iowa",
    "uni panthers":"Northern Iowa","north. iowa":"Northern Iowa",
    "hofstra pride":"Hofstra","hofstra":"Hofstra",
    "cal baptist lancers":"Cal Baptist","california baptist":"Cal Baptist","cal baptist":"Cal Baptist",
    "cbu":"Cal Baptist","cal baptist u.":"Cal Baptist","calif baptist":"Cal Baptist","calif. baptist":"Cal Baptist",
    "california baptist lancers":"Cal Baptist","california baptist u.":"Cal Baptist",
    "cal. baptist lancers":"Cal Baptist","cal. baptist":"Cal Baptist",
    "hawaii rainbow warriors":"Hawaii","hawaii":"Hawaii","hawai'i":"Hawaii",
    "hawai\u2019i":"Hawaii","hawai'i rainbow warriors":"Hawaii","hawaii warriors":"Hawaii",
    "north dakota state bison":"North Dakota State","north dakota state":"North Dakota State",
    "ndsu":"North Dakota State","n. dakota st.":"North Dakota State","n dak st":"North Dakota State",
    "n. dakota state":"North Dakota State","n dakota state":"North Dakota State",
    "north dakota st":"North Dakota State","north dakota st.":"North Dakota State",
    "n. dak. st.":"North Dakota State","n.d. state":"North Dakota State",
    "n. dakota st":"North Dakota State",
    "wright state raiders":"Wright State","wright state":"Wright State",
    "wright st":"Wright State","wright st.":"Wright State","wright st raiders":"Wright State",
    "troy trojans":"Troy","troy":"Troy",
    "pennsylvania quakers":"Penn","penn quakers":"Penn","penn":"Penn","pennsylvania":"Penn",
    "upenn":"Penn",
    "kennesaw state owls":"Kennesaw State","kennesaw state":"Kennesaw State",
    "kennesaw st.":"Kennesaw State","kennesaw st":"Kennesaw State","kennesaw":"Kennesaw State",
    "idaho vandals":"Idaho","idaho":"Idaho",
    "siena saints":"Siena","siena":"Siena","siena college":"Siena",
    "furman paladins":"Furman","furman":"Furman",
    "queens royals":"Queens","queens":"Queens","queens (nc)":"Queens",
    "queens nc":"Queens","queens, nc":"Queens","queens university":"Queens","queens univ":"Queens",
    "queens university royals":"Queens","queens univ. royals":"Queens",
    "tennessee state tigers":"Tennessee State","tennessee state":"Tennessee State",
    "tenn. state":"Tennessee State","tenn state":"Tennessee State",
    "tenn. st.":"Tennessee State","tenn st":"Tennessee State","tenn. st":"Tennessee State",
    "umbc retrievers":"UMBC","umbc":"UMBC","maryland baltimore county":"UMBC",
    "md baltimore county":"UMBC","u.m.b.c.":"UMBC","u.m.b.c":"UMBC",
    "howard bison":"Howard","howard":"Howard","howard university":"Howard",
    "liu sharks":"LIU","liu":"LIU","long island":"LIU","long island university":"LIU",
    "long island u.":"LIU","liu brooklyn":"LIU","long island u":"LIU",
    "long island university sharks":"LIU","liu post":"LIU","long island":"LIU",
    "california-los angeles":"UCLA","california los angeles":"UCLA",
    # Wolfe-specific name formats
    "st john's ny":"St. John's","st. john's ny":"St. John's",
    "st louis u.":"Saint Louis","st louis u":"Saint Louis",
    "md-baltimore county":"UMBC","md baltimore county":"UMBC",
    "va commonwealth":"VCU","virginia commonwealth u":"VCU",
    "hawai\u0060i":"Hawaii","hawai`i":"Hawaii",
    "lehigh mountain hawks":"Lehigh","lehigh":"Lehigh",
    "prairie view a&m panthers":"Prairie View A&M","prairie view a&m":"Prairie View A&M",
    "prairie view":"Prairie View A&M","prairie view a & m":"Prairie View A&M",
    "pva&m":"Prairie View A&M",
    "virginia commonwealth":"VCU",
    "southern methodist":"SMU",
    "central florida":"UCF",
    "texas christian":"TCU",
    "n. carolina state":"NC State",
    "n.d. state":"North Dakota State",
    # SONNY-specific all-caps forms
    "st. mary's ca.":"Saint Mary's","st. marys ca.":"Saint Mary's",
    "north carolina st.":"NC State","n.c. st.":"NC State",
    "troy st.":"Troy","troy st":"Troy",
    "tennessee st.":"Tennessee State","tennessee st":"Tennessee State",
    "mcneese st.":"McNeese","mcneese st":"McNeese",
    "connecticut":"UConn",
    "michigan st.":"Michigan State",
    "iowa st.":"Iowa State",
    "ohio st.":"Ohio State",
    "utah st.":"Utah State",
    "wright st.":"Wright State","wright st":"Wright State",
    "kennesaw st.":"Kennesaw State","kennesaw st":"Kennesaw State",
    "north dakota st.":"North Dakota State","north dakota st":"North Dakota State",
    "n dakota st":"North Dakota State","n. dakota st":"North Dakota State","n dak st":"North Dakota State",
    # Additional coverage
    "saint louis billikens":"Saint Louis",
    "saint mary's gaels":"Saint Mary's",
    "saint john's red storm":"St. John's",
    "queens (nc)":"Queens","queens nc":"Queens",
    "liu brooklyn":"LIU","long island u.":"LIU",
    "prairie view a&amp;m":"Prairie View A&M",
    "texas a&amp;m":"Texas A&M",
    "miami (oh)":"Miami OH","miami (ohio)":"Miami OH",
    "miami (fl)":"Miami FL","miami fl":"Miami FL",
    "california baptist":"Cal Baptist","cbu":"Cal Baptist",
    "hawai\u2019i":"Hawaii",
}

def norm(name):
    n = html.unescape(name.strip()).lower()
    # Normalize fancy quotes to plain apostrophe
    n = n.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    n = re.sub(r'\s+',' ',n).strip()
    # Strip record-like parentheticals BEFORE hyphen conversion: "(35-2)", "(26-9)", "(W-L)"
    n = re.sub(r'\s*\(\d+-\d+\)', '', n).strip()
    # Replace hyphens between words with space (e.g. "Miami-Ohio" → "Miami Ohio")
    # But only outside of remaining parenthetical content
    n = re.sub(r'(?<=\w)-(?=\w)', ' ', n)
    n = re.sub(r'[^\w\s\'\.&\(\)]','',n).strip()
    # Check aliases BEFORE stripping remaining parentheticals (handles "miami (oh)" vs "miami (fl)")
    if n in ALIASES:
        return ALIASES[n]
    # Now strip all remaining parentheticals like "(wcc)", "(fl)", "(oh)", "(cal)"
    n2 = re.sub(r'\s*\([^)]*\)', '', n).strip()
    n2 = re.sub(r'[^\w\s\'\.&]','',n2).strip()
    if n2 in ALIASES:
        return ALIASES[n2]
    for t in TEAMS:
        if t.lower() == n2:
            return t
    return None

def fetch(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers=H)
        return urllib.request.urlopen(req, timeout=timeout).read().decode('utf-8','replace')
    except Exception as e:
        return ""

def parse_html_table(html_text, table_idx=0):
    tables = re.findall(r'<table[^>]*>(.*?)</table>', html_text, re.DOTALL|re.IGNORECASE)
    if table_idx >= len(tables): return []
    rows = []
    for row in re.findall(r'<tr[^>]*>(.*?)</tr>', tables[table_idx], re.DOTALL|re.IGNORECASE):
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.DOTALL|re.IGNORECASE)
        cleaned = [re.sub(r'<[^>]+>','',c).strip() for c in cells]
        if any(cleaned): rows.append(cleaned)
    return rows

def rows_to_ranks(rows, name_cols=(0,1,2), skip_header=True):
    result = {}
    rank = 1
    start = 1 if skip_header else 0
    for row in rows[start:]:
        for ci in name_cols:
            if ci < len(row):
                team = norm(row[ci])
                if team and team not in result:
                    # Check if first col is explicit rank
                    try:
                        explicit = int(re.sub(r'[^\d]','',row[0]))
                        result[team] = explicit
                    except:
                        result[team] = rank
                    rank += 1
                    break
    return result

# ─── SCRAPERS ─────────────────────────────────────────────────────────────────

def s_bpi():
    result = {}
    rank = 1
    # ESPN BPI — fetch with pagination to get all teams (not just top 25/major conferences)
    # Try the full table URL with a high limit
    urls_to_try = [
        "https://www.espn.com/mens-college-basketball/bpi/_/view/bpi/season/2026",
        "https://www.espn.com/mens-college-basketball/bpi/_/view/bpi",
        "https://www.espn.com/mens-college-basketball/bpi",
        "https://www.espn.com/mens-college-basketball/bpi/_/season/2026/sort/bpiranking/dir/asc",
    ]
    d = ""
    for url in urls_to_try:
        d = fetch(url)
        if d:
            break
    if not d:
        return result
    # ESPN embeds data as JSON in a __espnfitt__ variable or similar
    # Try extracting from embedded JSON first (most comprehensive)
    json_match = re.search(r'window\[.espnfitt.\]\s*=\s*(\{.*?\});', d, re.DOTALL)
    if not json_match:
        json_match = re.search(r'"rows"\s*:\s*(\[.*?\])', d, re.DOTALL)
    if json_match:
        try:
            # Try to find all team names in the JSON blob
            blob = json_match.group(1)
            for m in re.finditer(r'"(?:displayName|shortDisplayName|name)"\s*:\s*"([^"]+)"', blob):
                team = norm(m.group(1))
                if team and team not in result:
                    result[team] = rank
                    rank += 1
        except:
            pass
    if not result or len(result) < 30:
        # Fallback: scan all displayName fields in the full page JSON
        result2 = {}
        rank2 = 1
        for m in re.finditer(r'"displayName"\s*:\s*"([^"]+)"', d):
            team = norm(m.group(1))
            if team and team not in result2:
                result2[team] = rank2
                rank2 += 1
        if len(result2) > len(result):
            result = result2
    if not result or len(result) < 30:
        # Fallback: HTML table scan
        result3 = {}
        rank3 = 1
        rows = parse_html_table(d, 0)
        for row in rows[1:]:
            for col in row:
                team = norm(col)
                if team and team not in result3:
                    try:
                        result3[team] = int(re.sub(r'[^\d]', '', row[0])) if re.sub(r'[^\d]', '', row[0]) else rank3
                    except:
                        result3[team] = rank3
                    rank3 += 1
                    break
        if len(result3) > len(result):
            result = result3
    if not result or len(result) < 30:
        # Last resort: find team name spans
        result4 = {}
        rank4 = 1
        for m in re.finditer(r'class="[^"]*(?:team-name|TeamName|AnchorLink)[^"]*"[^>]*>\s*(?:<[^>]+>)*([^<]{3,35})', d):
            team = norm(m.group(1).strip())
            if team and team not in result4:
                result4[team] = rank4
                rank4 += 1
        if len(result4) > len(result):
            result = result4
    return result

def s_deep():
    d = fetch("https://deepmetricanalytics.com/ncaabb/standings")
    result = {}
    rank = 1
    rows = parse_html_table(d, 0)
    for row in rows[1:]:
        for col in row:
            team = norm(col)
            if team and team not in result:
                result[team] = rank
                rank += 1
                break
    if not result:
        # Try JSON
        for m in re.finditer(r'"(?:team|name|school)"\s*:\s*"([^"]+)"', d):
            team = norm(m.group(1))
            if team and team not in result:
                result[team] = rank
                rank += 1
    return result

def s_deep_elo():
    # ELO is a column in DeepMetrics - scrape as separate ranking by ELO column
    d = fetch("https://deepmetricanalytics.com/ncaabb/standings")
    # Try to find ELO column and sort by it
    result = {}
    rank = 1
    rows = parse_html_table(d, 0)
    if rows and len(rows) > 1:
        # Find ELO column index
        header = [c.lower() for c in rows[0]]
        elo_idx = next((i for i,h in enumerate(header) if 'elo' in h), None)
        if elo_idx:
            # Extract team+elo pairs and sort
            pairs = []
            for row in rows[1:]:
                for col in row:
                    team = norm(col)
                    if team:
                        try:
                            elo = float(row[elo_idx])
                            pairs.append((team, elo))
                        except:
                            pass
                        break
            for i, (team, _) in enumerate(sorted(pairs, key=lambda x: -x[1])):
                result[team] = i + 1
    if not result:
        # Fall back to AEI CSV for ELO rankings
        result = s_aei()
    return result

def s_colley():
    # Colley uses frames - fetch the main data frame
    d = fetch("https://www.colleyrankings.com/hcurrank.html")
    # Extract frame src
    m = re.search(r'<frame[^>]+name="mainframe"[^>]+src="([^"]+)"', d, re.IGNORECASE)
    if not m:
        m = re.search(r'<frame[^>]+src="([^"]+)"[^>]+name="mainframe"', d, re.IGNORECASE)
    if m:
        frame_url = "https://www.colleyrankings.com" + m.group(1)
        d2 = fetch(frame_url)
        rows = parse_html_table(d2, 0)
        result = {}
        for row in rows:
            if len(row) < 2: continue
            # Row format: "1." | "Michigan" | "33-3" | rating
            rank_str = re.sub(r'[^\d]','',row[0])
            if not rank_str: continue
            team = norm(row[1])
            if team:
                result[team] = int(rank_str)
        return result
    return {}

def s_dratings():
    d = fetch("https://www.dratings.com/sports/ncaa-college-basketball-ratings/")
    result = {}
    rank = 1
    rows = parse_html_table(d, 0)
    for row in rows[1:]:
        if not row: continue
        # DRAT puts "32.\xa0Team Name Nickname (record)" all in cell[0]
        cell0 = html.unescape(row[0])
        # Strip leading rank number: "32." or "32. "
        name_part = re.sub(r'^\s*\d+\.\s*', '', cell0).strip()
        team = norm(name_part)
        if not team:
            # Fallback: try each cell
            for col in row:
                team = norm(col)
                if team: break
        if team and team not in result:
            m = re.match(r'^\s*(\d+)\.', cell0)
            result[team] = int(m.group(1)) if m else rank
            rank += 1
    return result

def s_versus():
    d = fetch("https://www.versussportssimulator.com/CBB/rankings")
    result = {}
    # Table structure: cells[0]=rating value (NOT rank), cells[1]=team+conf+record,
    # cells[-1]=actual sequential rank (1,2,3,...). Verified 2026-04-04.
    for row in re.findall(r'<tr[^>]*>(.*?)</tr>', d, re.DOTALL|re.IGNORECASE):
        cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL|re.IGNORECASE)
        if len(cells) < 4: continue
        # Rank is in cells[5] (overall rank, 1-indexed sequential). Verified 2026-04-04.
        # cells[0]=rating pts, cells[1]=team+data, cells[2]=avg rating,
        # cells[3]=wins, cells[4]=losses, cells[5]=OVERALL RANK, cells[7]=pwr, cells[8]=off, cells[9]=def
        rank_str = re.sub(r'<[^>]+>','',cells[5]).strip()
        try:
            rk = int(rank_str)
            if rk > 400: continue
        except: continue
        raw = re.sub(r'<[^>]+>','',cells[1]).strip()
        # Team name is before conference: "ArizonaBig 12..." or "Iowa StateBig 12..."
        for length in range(min(30, len(raw)), 2, -1):
            team = norm(raw[:length])
            if team and team not in result:
                result[team] = rk
                break
    return result

def s_simmons():
    d = fetch("https://simmonsratings.com/overcolrank2526.htm")
    result = {}
    # Site uses <TR><TD>rank<TD>name with no closing tags — must use this regex
    for rk_str, name in re.findall(r'<TR><TD>\s*(\d+)\s*<TD>([^<\t\r\n]+)', d, re.IGNORECASE):
        team = norm(name.strip())
        if team and team not in result:
            result[team] = int(rk_str)
    return result

def s_jeng():
    d = fetch("https://rankings.jameseng.land/mens-basketball-2026.html")
    result = {}
    rank = 1
    rows = parse_html_table(d, 0)
    for row in rows[1:]:
        for col in row:
            team = norm(col)
            if team and team not in result:
                result[team] = rank
                rank += 1
                break
    return result

def s_talis():
    d = fetch("https://talismanred.com/ratings/hoops/rankings2.shtml")
    result = {}
    rows = parse_html_table(d, 0)
    for row in rows:
        if len(row) < 2: continue
        rk_str = re.sub(r'[^\d]','',row[0])
        if not rk_str: continue
        team = norm(row[1])
        if team: result[team] = int(rk_str)
    return result

def s_wilson():
    d = fetch("https://talismanred.com/ratings/hoops/wilson1.shtml")
    result = {}
    rank = 1
    # Conference standings format — parse all team rows regardless of conf
    # "Michigan  21  2  1930  1630  33  3 ... Rate"
    # Teams appear across multiple conference blocks - extract by finding team names
    for m in re.finditer(r'([A-Z][A-Za-z \'\.&]{2,25}?)\s+\d+\s+\d+\s+\d+\s+\d+\s+(\d+)\s+(\d+)\s+\d+\s+\d+\s+([\d.]+)', d):
        team = norm(m.group(1))
        if team and team not in result:
            result[team] = rank
            rank += 1
    if not result:
        rows = parse_html_table(d, 0)
        for row in rows[1:]:
            for col in row:
                team = norm(col)
                if team and team not in result:
                    result[team] = rank
                    rank += 1
                    break
    return result

def s_sonny():
    d = fetch("https://sonnymoorepowerratings.com/m-basket.htm")
    txt = re.sub(r'<[^>]+>','',d)
    result = {}
    # Format: "  1 MICHIGAN    34  3" — mostly uppercase but some names like "McNEESE ST." have mixed case
    for m in re.finditer(r'^\s*(\d+)\s+([A-Z][A-Za-z .\'&\-]+?)\s{2,}\d', txt, re.MULTILINE):
        rk = int(m.group(1))
        team = norm(m.group(2).strip())
        if team and team not in result:
            result[team] = rk
    return result

def s_wheelus():
    d = fetch("https://rwheelus.github.io/wheelus-sports/NCAAM-2025-26.html")
    result = {}
    rank = 1
    rows = parse_html_table(d, 0)
    for row in rows[1:]:
        for col in row:
            team = norm(col)
            if team and team not in result:
                result[team] = rank
                rank += 1
                break
    return result

def s_aei():
    d = fetch("https://aeiratings.com/data/mcbb.csv")
    result = {}
    rank = 1
    if not d: return {}
    lines = d.strip().split('\n')
    header = [h.strip().lower().strip('"') for h in lines[0].split(',')]
    name_idx = next((i for i,h in enumerate(header) if any(w in h for w in ['team','school','name'])), 0)
    elo_idx = next((i for i,h in enumerate(header) if 'elo' in h), None)
    pairs = []
    for line in lines[1:]:
        cols = line.split(',')
        if len(cols) <= name_idx: continue
        t = norm(cols[name_idx].strip().strip('"'))
        if not t: continue
        elo = 0
        if elo_idx and elo_idx < len(cols):
            try: elo = float(cols[elo_idx])
            except: pass
        pairs.append((t, elo))
    if elo_idx:
        for i,(t,_) in enumerate(sorted(pairs, key=lambda x:-x[1])):
            result[t] = i+1
    else:
        for t,_ in pairs:
            if t not in result:
                result[t] = rank
                rank += 1
    return result

def s_dolphin():
    d = fetch("http://www.dolphinsim.com/ratings/ncaa_mbb/")
    result = {}
    # Data is in <pre><code> block, fixed-width with team name at col 0
    pre = re.search(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', d, re.DOTALL|re.IGNORECASE)
    if not pre: return {}
    lines = pre.group(1).split('\n')
    rank = 1
    for line in lines:
        line = re.sub(r'<[^>]+>','',line)
        if not line.strip() or line.strip().startswith('TEAM'): continue
        # Fixed width: TEAM (26 chars) W L ...
        team_part = line[:26].strip()
        if not team_part: continue
        team = norm(team_part)
        if team and team not in result:
            result[team] = rank
            rank += 1
    return result

def s_bcmoore():
    d = fetch("http://ncaa.bcmoorerankings.com/mbb/2026/1Rank.html")
    result = {}
    # Format: "   1  Duke                  Atla (35- 2)  57.45..." with leading spaces
    # Conference abbreviations can include dashes (Mid-, A-10, etc.)
    txt = re.sub(r'<[^>]+>','',d)
    for m in re.finditer(r'^\s+(\d+)\s+([A-Za-z][A-Za-z \'\.&]+?)\s{2,}[A-Z][A-Za-z\-]{0,5}[\s(]', txt, re.MULTILINE):
        rk = int(m.group(1))
        team = norm(m.group(2).strip())
        if team and team not in result:
            result[team] = rk
    return result

def s_bihl():
    d = fetch("http://jeffbihl.com/bwin.html")
    result = {}
    txt = re.sub(r'<[^>]+>','',d)
    # Include hyphens and parens to capture "California-Los Angeles", "Maryland-Baltimore County", "Miami (OH)"
    for m in re.finditer(r'(\d+)\s+([A-Za-z][A-Za-z \'\.\&\-\(\)]+?)\s+(\d+\s*-\s*\d+)\s+([\-\d.]+)', txt):
        rk = int(m.group(1))
        team = norm(m.group(2).strip())
        if team and team not in result:
            result[team] = rk
    return result

def s_srat():
    d = fetch("https://www.sports-ratings.com/p/power-rating-overall.html")
    result = {}
    txt = re.sub(r'<[^>]+>','',d)
    # Format: "1.  Arizona  34-2  136.23"
    for m in re.finditer(r'(\d+)\.\s+([A-Za-z][A-Za-z \'\.&]+?)\s+\d+-\d+\s+([\d.]+)', txt):
        rk = int(m.group(1))
        team = norm(m.group(2).strip())
        if team and team not in result:
            result[team] = rk
    return result

def s_omni():
    d = fetch("https://omnirankings.com/mcb/Macro/Team%20Ratings.htm")
    result = {}
    rank = 1
    rows = parse_html_table(d, 0)
    for row in rows[1:]:
        for col in row:
            team = norm(col)
            if team and team not in result:
                try: result[team] = int(re.sub(r'[^\d]','',row[0]))
                except: result[team] = rank
                rank += 1
                break
    return result

def s_whoe():
    d = fetch("https://whoearnedit.com/cb")
    result = {}
    rank = 1
    rows = parse_html_table(d, 0)
    for row in rows[1:]:
        for col in row:
            team = norm(col)
            if team and team not in result:
                result[team] = rank
                rank += 1
                break
    return result

def s_rams():
    d = fetch("https://ramsrating.com/ncaa-bb-m/")
    result = {}
    rank = 1
    rows = parse_html_table(d, 0)
    for row in rows[1:]:
        for col in row:
            team = norm(col)
            if team and team not in result:
                result[team] = rank
                rank += 1
                break
    return result

def s_entropy():
    d = fetch("http://dokterentropy.com/r2026.CBB")
    result = {}
    # Format: "  1 Michigan                34  3..." / "98 Miami (Ohio)            32  2..."
    for m in re.finditer(r'^\s*(\d+)\s+([A-Za-z][A-Za-z .\'&\(\)]+?)\s{2,}\d', d, re.MULTILINE):
        rk = int(m.group(1))
        team = norm(m.group(2).strip())
        if team and team not in result:
            result[team] = rk
    return result

def s_dci():
    # Daniel Curry Index - blogspot, rankings in post body
    d = fetch("https://dcindex-choop.blogspot.com/search/label/DCI%20Rank")
    result = {}
    # Look for numbered list in post content
    # Try to find the actual rankings post content
    post_match = re.search(r'<div[^>]+class="[^"]*post-body[^"]*"[^>]*>(.*?)</div>', d, re.DOTALL|re.IGNORECASE)
    if post_match:
        txt = re.sub(r'<[^>]+>','',post_match.group(1))
        for m in re.finditer(r'(\d+)[\.\)]\s+([A-Za-z][^\n\d]{3,30})', txt):
            rk = int(m.group(1))
            team = norm(m.group(2).strip())
            if team and team not in result:
                result[team] = rk
    if not result:
        txt = re.sub(r'<[^>]+>','',d)
        for m in re.finditer(r'(\d+)\.\s+([A-Za-z][A-Za-z \'\.&]{3,30})', txt):
            rk = int(m.group(1))
            team = norm(m.group(2).strip())
            if team and team not in result and rk < 400:
                result[team] = rk
    return result

def s_massey():
    # Try Massey composite ratings page for NCAA D1 basketball
    result = {}
    # Primary URL: massey ratings composite page
    for url in [
        "https://masseyratings.com/cb/ncaa-d1/ratings",
        "https://masseyratings.com/ranks",
        "https://masseyratings.com/cb/compare.htm",
    ]:
        d = fetch(url)
        if not d:
            continue
        # Massey uses HTML tables; team name in one column, rank/rating in another
        rows = parse_html_table(d, 0)
        rank = 1
        for row in rows[1:]:
            for col in row:
                team = norm(col)
                if team and team not in result:
                    try:
                        result[team] = int(re.sub(r'[^\d]', '', row[0])) if re.sub(r'[^\d]', '', row[0]) else rank
                    except:
                        result[team] = rank
                    rank += 1
                    break
        if result:
            return result
        # Fallback: strip HTML and look for numbered entries
        txt = re.sub(r'<[^>]+>', '', d)
        txt = re.sub(r'\s+', ' ', txt)
        for m in re.finditer(r'(\d+)\s+([A-Za-z][A-Za-z \'\.&]{3,30}?)\s+(?:\d+-\d+|[\d.]{4,})', txt):
            rk = int(m.group(1))
            if rk > 400:
                continue
            team = norm(m.group(2).strip())
            if team and team not in result:
                result[team] = rk
        if result:
            return result
    return result

def s_oosh():
    result = {}
    rank = 1
    # Try multiple possible URLs for Splunty/OOSH rankings
    urls = [
        "https://misteroosh.wixsite.com/splunty/post/ncaa-men-s-basketball",
        "https://misteroosh.wixsite.com/splunty",
        "https://splunty.com/ncaab",
        "https://splunty.com/rankings",
    ]
    for url in urls:
        d = fetch(url)
        if not d:
            continue
        # Wix sites embed data as JSON in script tags
        for script in re.findall(r'<script[^>]*>(.*?)</script>', d, re.DOTALL|re.IGNORECASE):
            # Look for ranking data in various JSON structures
            for m in re.finditer(r'"(?:team|school|name|teamName|Team)"\s*:\s*"([^"]+)"', script):
                team = norm(m.group(1))
                if team and team not in result:
                    result[team] = rank
                    rank += 1
            if result:
                break
        if not result:
            # Strip HTML and look for rank + team name patterns
            txt = re.sub(r'<[^>]+>', '', d)
            txt = html.unescape(txt)
            txt = re.sub(r'\s+', ' ', txt)
            for m in re.finditer(r'(\d+)[.\)]\s+([A-Za-z][A-Za-z \'\.&]{2,28}?)(?:\s+[\d.]+|\s+\d+-\d+)', txt):
                rk = int(m.group(1))
                if rk > 400:
                    continue
                team = norm(m.group(2).strip())
                if team and team not in result:
                    result[team] = rk
        if result:
            return result
    return result

def s_stat():
    # StatSharp: HTML table, soft paywall bypassed with fresh (cookieless) fetch
    # URL confirmed: https://www.statsharp.com/ncaab/ncaa-college-basketball-power-ratings/
    d = fetch("https://www.statsharp.com/ncaab/ncaa-college-basketball-power-ratings/")
    result = {}
    rows = parse_html_table(d, 0)
    if not rows or len(rows) < 2:
        return result
    header = [c.lower().strip() for c in rows[0]]
    # Find team name and rating columns
    name_idx = next((i for i, h in enumerate(header) if 'team' in h or 'school' in h), 0)
    rating_idx = next((i for i, h in enumerate(header) if h == 'rating' or h == 'rtg'), None)
    pairs = []
    for row in rows[1:]:
        if len(row) <= name_idx: continue
        team = norm(row[name_idx])
        if not team: continue
        rating = 0
        if rating_idx is not None and rating_idx < len(row):
            try: rating = float(re.sub(r'[^\d.\-]', '', row[rating_idx]) or '0')
            except: pass
        pairs.append((team, rating))
    # Rank by rating descending to get clean 1-365 national ranks
    for i, (team, _) in enumerate(sorted(pairs, key=lambda x: -x[1])):
        if team not in result:
            result[team] = i + 1
    return result


def s_moog():
    # Mark Moog: direct CSV — row order = rank, no header
    # MUST use http:// not https:// (https times out)
    d = fetch("http://markmoog.com/data/ratings/ratings_2026.csv")
    result = {}
    rank = 1
    for line in d.strip().split('\n'):
        parts = line.split(',')
        if not parts: continue
        team = norm(parts[0].strip().strip('"'))
        if team and team not in result:
            result[team] = rank
            rank += 1
    return result


def s_odds():
    # Odds Gods: rankings live in a Vite JS asset (ExpandedRankings-*.js)
    # Asset filename changes on deploy — discover dynamically from index page
    base = "https://egomaniacsbracket.onrender.com"
    index = fetch(base + "/")
    if not index:
        return {}
    # Find index JS asset
    idx_js = re.search(r'/assets/index-[^"\'>\s]+\.js', index)
    if not idx_js:
        return {}
    idx_content = fetch(base + idx_js.group(0))
    # Find ExpandedRankings asset filename within the index JS
    exp_js = re.search(r'ExpandedRankings-[^"\'\s]+\.js', idx_content)
    if not exp_js:
        return {}
    asset = fetch(base + "/assets/" + exp_js.group(0))
    if not asset:
        return {}
    # Data is const j=[{id:...,name:"TEAM",mrRank:N,...},...]
    result = {}
    for m in re.finditer(r'name:"([^"]+)"[^}]*?mrRank:(\d+)', asset):
        team = norm(m.group(1))
        rk = int(m.group(2))
        if team and team not in result:
            result[team] = rk
    return result


def s_jthom():
    # JThom Analytics: loop all conferences via TWV API, rank globally by twv score
    import json as _json
    confs = [
        "Atlantic Coast","Big East","Big Ten","Big 12","Southeastern",
        "American Athletic","Mountain West","West Coast","Atlantic 10",
        "Atlantic Sun","Big West","Missouri Valley","Conference USA",
        "Sun Belt","Mid-American","Southland","Southwestern Athletic",
        "Mid-Eastern","Big South","America East","Horizon League",
        "Ivy League","Metro Atlantic Athletic","Coastal Athletic Association",
        "Big Sky","Northeast","Ohio Valley","Patriot League",
        "Southern","Summit","Western Athletic",
    ]
    pairs = []
    seen = set()
    for conf in confs:
        url = "https://jthomanalytics.com/api/proxy/twv/" + urllib.request.quote(conf)
        d = fetch(url, timeout=10)
        if not d or d.startswith('ERROR'): continue
        try:
            data = _json.loads(d).get('data', [])
            for item in data:
                name = item.get('team_name', '')
                twv = item.get('twv', 0) or 0
                team = norm(name)
                if team and team not in seen:
                    pairs.append((team, float(twv)))
                    seen.add(team)
        except: continue
    result = {}
    for i, (team, _) in enumerate(sorted(pairs, key=lambda x: -x[1])):
        result[team] = i + 1
    return result

def s_generic(url, tidx=0):
    d = fetch(url)
    if not d: return {}
    result = {}
    rank = 1
    rows = parse_html_table(d, tidx)
    for row in rows[1:]:
        for col in row:
            team = norm(col)
            if team and team not in result:
                try: result[team] = int(re.sub(r'[^\d]','',row[0])) if re.sub(r'[^\d]','',row[0]) else rank
                except: result[team] = rank
                rank += 1
                break
    if not result:
        txt = re.sub(r'<[^>]+>','',d)
        txt = re.sub(r'\s+',' ',txt)
        for m in re.finditer(r'(\d+)[.\s]+([A-Za-z][A-Za-z \'\.&]{3,25})', txt):
            rk = int(m.group(1))
            if rk > 400: continue
            team = norm(m.group(2).strip())
            if team and team not in result:
                result[team] = rk
    return result

def s_dunk():
    result = {}
    # Try multiple URL formats for Dunkel Index
    urls = [
        "https://www.dunkelindex.com/ranking/ncaa-basketball/2026",
        "https://www.dunkelindex.com/ranking/ncaa-basketball",
        "https://www.dunkelindex.com/",
    ]
    for url in urls:
        d = fetch(url)
        if not d:
            continue
        # Dunkel uses HTML tables
        rows = parse_html_table(d, 0)
        rank = 1
        for row in rows[1:]:
            for col in row:
                team = norm(col)
                if team and team not in result:
                    try:
                        result[team] = int(re.sub(r'[^\d]', '', row[0])) if re.sub(r'[^\d]', '', row[0]) else rank
                    except:
                        result[team] = rank
                    rank += 1
                    break
        if result:
            return result
        # Fallback: strip HTML and scan for rank patterns
        txt = re.sub(r'<[^>]+>', '', d)
        txt = re.sub(r'&amp;', '&', txt)
        txt = re.sub(r'\s+', ' ', txt)
        for m in re.finditer(r'(\d+)\s+([A-Za-z][A-Za-z \'\.&]{3,30}?)(?:\s+[\d.]+|\s+\d+-\d+)', txt):
            rk = int(m.group(1))
            if rk > 400:
                continue
            team = norm(m.group(2).strip())
            if team and team not in result:
                result[team] = rk
        if result:
            return result
    return result


def s_wolfe():
    d = fetch("https://wolferatings.com/mbb/ratings.htm")
    result = {}
    # Plain text format: "   34 St Louis U.              NCAA-I    28  5 ..."
    # Char class includes backtick (Hawai`i) and hyphen (MD-Baltimore County)
    for m in re.finditer(r'^\s*(\d+)\s+([A-Za-z][A-Za-z \'\.&`\-]+?)\s+NCAA-I', d, re.MULTILINE):
        rk = int(m.group(1))
        team = norm(m.group(2).strip())
        if team and team not in result:
            result[team] = rk
    return result


def s_whtlk():
    d = fetch("http://whitlockrankings.com/bbrank1.htm")
    result = {}
    # Malformed HTML — no </table> tags. Extract via anchor links + explicit rank column.
    # Format: <tr><td><a href="results_bball.html#Team">Team</a><td>score<td>W-L<td>RANK
    for m in re.finditer(
        r'<tr><td[^>]*>.*?<a[^>]*>([^<]+)</a>.*?<td[^>]*>\s*[\d.]+\s*<td[^>]*>\s*\d+\s*-\s*\d+\s*<td[^>]*>\s*(\d+)',
        d, re.IGNORECASE
    ):
        raw_name = m.group(1).strip()
        rank = int(m.group(2))
        team = norm(raw_name)
        if team and team not in result:
            result[team] = rank
    return result


def s_waywd():
    d = fetch("https://waywardtrends.com/bryan/BWE/ncaabRankings.php")
    result = {}
    # Rankings are in the 2nd HTML table (index 1): Rank | Team | Conf | Record | ...
    rows = parse_html_table(d, 1)
    for row in rows[1:]:
        if len(row) < 2: continue
        rk_str = re.sub(r'[^\d]','',row[0])
        if not rk_str: continue
        team = norm(row[1])
        if team and team not in result:
            result[team] = int(rk_str)
    return result


def s_amsts():
    result = {}
    urls = [
        "https://www.allmysportsteamssuck.com/ncaa-college-basketball-rankings/",
        "https://www.allmysportsteamssuck.com/college-basketball/",
        "https://www.allmysportsteamssuck.com/",
    ]
    for url in urls:
        d = fetch(url)
        if not d:
            continue
        rows = parse_html_table(d, 0)
        rank = 1
        for row in rows[1:]:
            for col in row:
                team = norm(col)
                if team and team not in result:
                    try:
                        result[team] = int(re.sub(r'[^\d]', '', row[0])) if re.sub(r'[^\d]', '', row[0]) else rank
                    except:
                        result[team] = rank
                    rank += 1
                    break
        if result:
            return result
        # Fallback text parsing
        txt = re.sub(r'<[^>]+>', '', d)
        txt = re.sub(r'&amp;', '&', txt)
        txt = re.sub(r'\s+', ' ', txt)
        for m in re.finditer(r'(\d+)[.\)]\s+([A-Za-z][A-Za-z \'\.&]{3,30}?)(?:\s+[\d.]+|\s+\d+-\d+)', txt):
            rk = int(m.group(1))
            if rk > 400:
                continue
            team = norm(m.group(2).strip())
            if team and team not in result:
                result[team] = rk
        if result:
            return result
    return result


def s_tpr():
    d = fetch("https://thepowerrank.com/college-basketball-rankings/")
    result = {}
    # Table format: Rank | Team (record) | Rating  — must strip record from team name
    rows = parse_html_table(d, 0)
    for row in rows[1:]:
        if len(row) < 2: continue
        rk_str = re.sub(r'[^\d]','',row[0])
        if not rk_str: continue
        # Pass raw name to norm() — it handles record-stripping while preserving "(OH)" etc.
        team = norm(row[1])
        if team and team not in result:
            result[team] = int(rk_str)
    return result


def s_cmte():
    # NCAA Committee implicit seeding order
    seed_order = [
        ("Michigan",1,"Midwest"),("Duke",1,"East"),("Arizona",1,"West"),("Houston",1,"South"),
        ("Iowa State",2,"Midwest"),("UConn",2,"East"),("Purdue",2,"West"),("Florida",1,"South"),
        ("Illinois",3,"South"),("Michigan State",3,"East"),("Gonzaga",3,"West"),("Virginia",3,"Midwest"),
        ("Alabama",4,"Midwest"),("Nebraska",4,"South"),("Arkansas",4,"West"),("Kansas",4,"East"),
        ("St. John's",5,"East"),("Vanderbilt",5,"South"),("Wisconsin",5,"West"),("Texas Tech",5,"Midwest"),
        ("Tennessee",6,"Midwest"),("BYU",6,"West"),("North Carolina",6,"South"),("Louisville",6,"East"),
        ("Iowa",9,"South"),("Kentucky",7,"Midwest"),("Saint Mary's",7,"South"),("UCLA",7,"East"),
        ("Utah State",9,"West"),("Ohio State",8,"East"),("Georgia",8,"Midwest"),("Missouri",10,"West"),
        ("Texas",11,"West"),("Texas A&M",10,"South"),("TCU",9,"East"),("Clemson",8,"South"),
        ("VCU",11,"South"),("South Florida",11,"East"),("SMU",11,"Midwest"),("UCF",10,"East"),
        ("Santa Clara",10,"Midwest"),("Akron",12,"Midwest"),("McNeese",12,"South"),
        ("High Point",12,"West"),("Miami OH",11,"Midwest"),("Northern Iowa",12,"East"),
        ("Hofstra",13,"Midwest"),("Cal Baptist",13,"East"),("Hawaii",13,"West"),
        ("North Dakota State",14,"East"),("Wright State",14,"Midwest"),("Troy",13,"South"),
        ("Penn",14,"South"),("Kennesaw State",14,"West"),("Idaho",15,"South"),
        ("Siena",16,"East"),("Furman",15,"East"),("Queens",15,"West"),("Tennessee State",15,"Midwest"),
        ("UMBC",16,"Midwest"),("Howard",16,"Midwest"),("LIU",16,"West"),
        ("Lehigh",16,"South"),("Prairie View A&M",16,"South"),
        ("Villanova",8,"West"),("NC State",11,"West"),("Saint Louis",9,"Midwest"),
        ("Miami FL",7,"West"),("Wisconsin",5,"West"),("AMSTS",0,""),
    ]
    result = {}
    for i, (team, seed, region) in enumerate(seed_order):
        if team in TEAMS and team not in result:
            result[team] = i + 1
    return result

# ─── MAIN ─────────────────────────────────────────────────────────────────────
SCRAPERS = [
    # T1
    ("BPI",    s_bpi,    "T1"),
    ("DEEP",   s_deep,   "T1"),
    # T2 confirmed
    ("ELO",    s_deep_elo,"T2"),
    ("COLLEY", s_colley, "T2"),
    ("DRAT",   s_dratings,"T2"),
    ("VERSUS", s_versus, "T2"),
    ("SIMM",   s_simmons,"T2"),
    ("JENG",   s_jeng,   "T2"),
    ("TALIS",  s_talis,  "T2"),
    ("WILSON", s_wilson, "T2"),
    ("SONNY",  s_sonny,  "T2"),
    ("WHEEL",  s_wheelus,"T2"),
    ("AEI",    s_aei,    "T2"),
    ("DLPHN",  s_dolphin,"T2"),
    ("BCM",    s_bcmoore,"T2"),
    ("BIHL",   s_bihl,   "T2"),
    ("SRAT",   s_srat,   "T2"),
    ("OMNI",   s_omni,   "T2"),
    ("WHOE",   s_whoe,   "T2"),
    ("RAMS",   s_rams,   "T2"),
    ("ENTROPY",s_entropy,"T2"),
    ("DCI",    s_dci,    "T2"),
    ("MASSEY", s_massey, "T2"),   # blocked → manual
    ("OOSH",   s_oosh,   "T2"),   # Wix → try
    ("STAT",   s_stat,   "T2"),
    ("JTHOM",  s_jthom,  "T2"),
    ("CMTE",   s_cmte,   "T2"),
    # Stuck at 3/15 — check for updates
    ("TMRK",  lambda: s_generic("https://www.teamrankings.com/ncaa-basketball/ranking/predictive-by-other"), "T2"),
    ("DUNK",  s_dunk,                                                                                       "T2"),
    ("TPR",   s_tpr,                                                                                        "T2"),
    ("WAYWD", s_waywd,                                                                                      "T2"),
    ("WHTLK", s_whtlk,                                                                                     "T2"),
    ("PACK",  lambda: s_generic("https://org.coloradomesa.edu/~epackard/mbb.html"),                        "T2"),
    ("WOLFE", s_wolfe,                                                                                     "T2"),
    ("QRI",   lambda: s_generic("https://www.bracket-madness.sbs/qrirankings.htm"),                        "T2"),
    ("JNG",   lambda: s_generic("https://hoopshd.com/nitty-gritty-rankings/"),                             "T2"),
    ("SRCBB", lambda: s_generic("https://www.sports-reference.com/cbb/seasons/men/2026-ratings.html"),     "T2"),
    ("AMSTS", s_amsts,                                                                                      "T2"),
    ("NOAH",  lambda: s_generic("https://substack.com/@noahbaron/p-191288482"),                            "T2"),
    ("BKTM",  lambda: s_generic("https://www.bracket-madness.sbs/"),                                       "T2"),
    ("CJB",   lambda: s_generic("https://cjb-ratings.com/composite/ncaab/Paging/Off"),                    "T2"),
    ("MOOG",  s_moog,                                                                                       "T2"),
    ("ODDS",  s_odds,                                                                                       "T2"),
    # Compare
    ("NET",   lambda: s_generic("https://www.warrennolan.com/basketball/2026/net-live"),   "CMP"),
    ("RPI",   lambda: s_generic("https://www.warrennolan.com/basketball/2026/rpi-live"),   "CMP"),
    ("LRMCC", lambda: s_generic("https://www2.isye.gatech.edu/~jsokol/lrmcclassic/"),     "CMP"),
    ("LRMCB", lambda: s_generic("https://www2.isye.gatech.edu/~jsokol/lrmcbayesian/"),    "CMP"),
]

if __name__ == "__main__":
    results = {}
    summary = {"ok":[], "partial":[], "fail":[]}

    for abbr, fn, tier in SCRAPERS:
        print(f"  {abbr:8s}", end=" ", flush=True)
        try:
            r = fn()
            found = sum(1 for t in TEAMS if t in r)
            results[abbr] = r
            status = "✓" if found >= 50 else ("~" if found >= 10 else "✗")
            print(f"{status} {found}/68")
            if found >= 50: summary["ok"].append((abbr,found))
            elif found >= 10: summary["partial"].append((abbr,found))
            else: summary["fail"].append((abbr,found))
        except Exception as e:
            print(f"✗ ERROR: {e}")
            results[abbr] = {}
            summary["fail"].append((abbr,0))

    print(f"\n{'='*50}")
    print(f"✓ GOOD (50+): {[(a,n) for a,n in summary['ok']]}")
    print(f"~ PARTIAL (10-49): {[(a,n) for a,n in summary['partial']]}")
    print(f"✗ FAILED (<10): {[a for a,n in summary['fail']]}")

    with open("scraped_ranks.json","w") as f:
        json.dump(results, f, indent=2)
    print("\nSaved scraped_ranks.json")
