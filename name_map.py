"""
Strict exact-match team name normalization for all 68 tournament teams.
No partial matching. Every variant must be listed explicitly.
"""

TEAM_ALIASES = {
    # DUKE
    "duke": "Duke", "duke blue devils": "Duke", "duke 1": "Duke",
    
    # MICHIGAN  
    "michigan": "Michigan", "michigan wolverines": "Michigan", "michigan 1": "Michigan",
    
    # ARIZONA
    "arizona": "Arizona", "arizona wildcats": "Arizona", "arizona 1": "Arizona",
    
    # FLORIDA
    "florida": "Florida", "florida gators": "Florida", "florida 1": "Florida",
    
    # UCONN
    "uconn": "UConn", "connecticut": "UConn", "uconn huskies": "UConn", "connecticut huskies": "UConn",
    
    # HOUSTON
    "houston": "Houston", "houston cougars": "Houston", "houston 2": "Houston",
    
    # IOWA STATE
    "iowa state": "Iowa State", "iowa st": "Iowa State", "iowa st.": "Iowa State", 
    "iowa state cyclones": "Iowa State", "iowa st. 2": "Iowa State", "iowa st 2": "Iowa State",
    
    # PURDUE
    "purdue": "Purdue", "purdue boilermakers": "Purdue", "purdue 2": "Purdue",
    
    # MICHIGAN STATE
    "michigan state": "Michigan State", "michigan st": "Michigan State", "michigan st.": "Michigan State",
    "michigan state spartans": "Michigan State", "michigan st. 3": "Michigan State", "michigan st 3": "Michigan State",
    
    # ILLINOIS
    "illinois": "Illinois", "illinois fighting illini": "Illinois", "illinois 3": "Illinois",
    
    # GONZAGA
    "gonzaga": "Gonzaga", "gonzaga bulldogs": "Gonzaga",
    
    # VIRGINIA
    "virginia": "Virginia", "virginia cavaliers": "Virginia",
    
    # ALABAMA
    "alabama": "Alabama", "alabama crimson tide": "Alabama",
    
    # KANSAS
    "kansas": "Kansas", "kansas jayhawks": "Kansas",
    
    # NEBRASKA
    "nebraska": "Nebraska", "nebraska cornhuskers": "Nebraska",
    
    # ARKANSAS
    "arkansas": "Arkansas", "arkansas razorbacks": "Arkansas",
    
    # ST. JOHN'S
    "st. john's": "St. John's", "saint john's": "St. John's", "st john's": "St. John's",
    "saint johns": "St. John's", "st. john's red storm": "St. John's",
    "st john's (ny)": "St. John's", "saint john's (ny)": "St. John's",
    "st. john's (ny)": "St. John's", "st. johns": "St. John's",
    
    # TEXAS TECH
    "texas tech": "Texas Tech", "texas tech red raiders": "Texas Tech",
    
    # VANDERBILT
    "vanderbilt": "Vanderbilt", "vanderbilt commodores": "Vanderbilt",
    
    # WISCONSIN
    "wisconsin": "Wisconsin", "wisconsin badgers": "Wisconsin",
    
    # LOUISVILLE
    "louisville": "Louisville", "louisville cardinals": "Louisville",
    
    # NORTH CAROLINA
    "north carolina": "North Carolina", "north carolina tar heels": "North Carolina", "unc": "North Carolina",
    "n. carolina": "North Carolina", "n carolina": "North Carolina",
    
    # TENNESSEE
    "tennessee": "Tennessee", "tennessee volunteers": "Tennessee",
    
    # BYU
    "byu": "BYU", "brigham young": "BYU", "byu cougars": "BYU", "brigham young cougars": "BYU",
    
    # KENTUCKY
    "kentucky": "Kentucky", "kentucky wildcats": "Kentucky",
    
    # SAINT MARY'S
    "saint mary's": "Saint Mary's", "st. mary's": "Saint Mary's", "st mary's": "Saint Mary's",
    "saint mary's college": "Saint Mary's", "st. mary's ca": "Saint Mary's",
    "st mary's ca": "Saint Mary's", "saint mary's ca": "Saint Mary's",
    "saint mary's gaels": "Saint Mary's", "st. mary's college": "Saint Mary's",
    "st mary's, cal.": "Saint Mary's",
    "saint mary's college gaels": "Saint Mary's", "saint mary's (ca)": "Saint Mary's",
    "saint marys": "Saint Mary's", "st marys": "Saint Mary's",
    "saint mary\u2019s": "Saint Mary's", "saint mary\u2019s college": "Saint Mary's",
    "saint mary\u2019s gaels": "Saint Mary's", "saint mary\u2019s (ca)": "Saint Mary's",
    
    # MIAMI FL
    "miami fl": "Miami FL", "miami (fl)": "Miami FL", "miami hurricanes": "Miami FL",
    "miami fl 7": "Miami FL",
    
    # UCLA
    "ucla": "UCLA", "ucla bruins": "UCLA", "california-los angeles": "UCLA",
    
    # CLEMSON
    "clemson": "Clemson", "clemson tigers": "Clemson",
    
    # VILLANOVA
    "villanova": "Villanova", "villanova wildcats": "Villanova",
    
    # OHIO STATE
    "ohio state": "Ohio State", "ohio st": "Ohio State", "ohio st.": "Ohio State",
    "ohio state buckeyes": "Ohio State",
    
    # GEORGIA
    "georgia": "Georgia", "georgia bulldogs": "Georgia",
    
    # TCU
    "tcu": "TCU", "texas christian": "TCU", "tcu horned frogs": "TCU",
    
    # IOWA
    "iowa": "Iowa", "iowa hawkeyes": "Iowa",
    
    # SAINT LOUIS
    "saint louis": "Saint Louis", "st. louis": "Saint Louis", "st louis": "Saint Louis",
    "saint louis billikens": "Saint Louis",
    
    # UTAH STATE
    "utah state": "Utah State", "utah st": "Utah State", "utah st.": "Utah State",
    "utah state aggies": "Utah State",
    
    # UCF
    "ucf": "UCF", "central florida": "UCF", "ucf knights": "UCF",
    
    # MISSOURI
    "missouri": "Missouri", "missouri tigers": "Missouri",
    
    # SANTA CLARA
    "santa clara": "Santa Clara", "santa clara broncos": "Santa Clara",
    
    # TEXAS A&M
    "texas a&m": "Texas A&M", "texas am": "Texas A&M", "texas a&m aggies": "Texas A&M",
    
    # SOUTH FLORIDA
    "south florida": "South Florida", "s. florida": "South Florida", "usf": "South Florida",
    "south florida bulls": "South Florida", "south florida 11": "South Florida",
    "s florida": "South Florida",
    
    # VCU
    "vcu": "VCU", "virginia commonwealth": "VCU", "vcu rams": "VCU",
    "va commonwealth": "VCU",
    
    # NC STATE
    "nc state": "NC State", "north carolina state": "NC State", "north carolina st.": "NC State",
    "n.c. state": "NC State", "nc state wolfpack": "NC State", "n carolina st.": "NC State",
    "n. carolina st.": "NC State",
    
    # TEXAS
    "texas": "Texas", "texas longhorns": "Texas",
    
    # SMU
    "smu": "SMU", "southern methodist": "SMU", "smu mustangs": "SMU",
    "southern meth.": "SMU", "southern methodist 11": "SMU",
    
    # MIAMI OH
    "miami oh": "Miami OH", "miami (oh)": "Miami OH", "miami ohio": "Miami OH",
    "miami (oh) redhawks": "Miami OH", "miami oh 11": "Miami OH",
    "miami redhawks": "Miami OH",
    
    # NORTHERN IOWA
    "northern iowa": "Northern Iowa", "n. iowa": "Northern Iowa", "uni": "Northern Iowa",
    "northern iowa panthers": "Northern Iowa",
    
    # MCNEESE
    "mcneese": "McNeese", "mcneese st": "McNeese", "mcneese st.": "McNeese",
    "mcneese state": "McNeese", "mcneese cowboys": "McNeese",
    
    # HIGH POINT
    "high point": "High Point", "high point panthers": "High Point",
    
    # AKRON
    "akron": "Akron", "akron zips": "Akron",
    
    # HOFSTRA
    "hofstra": "Hofstra", "hofstra pride": "Hofstra",
    
    # TROY
    "troy": "Troy", "troy trojans": "Troy", "troy st.": "Troy",
    
    # HAWAII
    "hawaii": "Hawaii", "hawai'i": "Hawaii", "hawaii rainbow warriors": "Hawaii",
    "hawai'i rainbow warriors": "Hawaii",
    
    # PENN
    "penn": "Penn", "pennsylvania": "Penn", "pennsylvania quakers": "Penn",
    
    # NORTH DAKOTA STATE
    "north dakota state": "North Dakota State", "north dakota st": "North Dakota State",
    "n dakota st": "North Dakota State", "n. dakota st.": "North Dakota State",
    "north dakota state bison": "North Dakota State", "north dakota st.": "North Dakota State",
    "n dakota st.": "North Dakota State", "n. dakota st": "North Dakota State",
    
    # WRIGHT STATE
    "wright state": "Wright State", "wright st": "Wright State", "wright st.": "Wright State",
    
    # KENNESAW STATE
    "kennesaw state": "Kennesaw State", "kennesaw st": "Kennesaw State", 
    "kennesaw": "Kennesaw State", "kennesaw state owls": "Kennesaw State",
    "kennesaw st.": "Kennesaw State",
    
    # FURMAN
    "furman": "Furman", "furman paladins": "Furman",
    
    # IDAHO
    "idaho": "Idaho", "idaho vandals": "Idaho",
    
    # TENNESSEE STATE
    "tennessee state": "Tennessee State", "tennessee st": "Tennessee State",
    "tennessee st.": "Tennessee State", "tennessee state tigers": "Tennessee State",
    "tenn. st.": "Tennessee State",
    
    # QUEENS
    "queens": "Queens", "queens university": "Queens", "queens (nc)": "Queens",
    "queens university royals": "Queens", "queens nc": "Queens",
    "queens (nc) royals": "Queens", "queens royals": "Queens", "queens univ": "Queens",
    
    # SIENA
    "siena": "Siena", "siena saints": "Siena",
    
    # LIU
    "liu": "LIU", "long island": "LIU", "long island university": "LIU",
    "liu sharks": "LIU", "liu brooklyn": "LIU", "long island sharks": "LIU",
    
    # HOWARD
    "howard": "Howard", "howard bison": "Howard", "howard u.": "Howard",
    
    # UMBC
    "umbc": "UMBC", "maryland-baltimore co.": "UMBC", "md-baltimore": "UMBC",
    "umbc retrievers": "UMBC",
    
    # LEHIGH
    "lehigh": "Lehigh", "lehigh mountain hawks": "Lehigh",
    
    # PRAIRIE VIEW A&M
    "prairie view a&m": "Prairie View A&M", "prairie view": "Prairie View A&M",
    "pv a&m": "Prairie View A&M", "prairie view a&m panthers": "Prairie View A&M",
}

# Also handle "Miami" alone - context needed, but in tournament it's Miami FL
# We'll add it as Miami FL since that's the more prominent tournament team
TEAM_ALIASES["miami"] = "Miami FL"

import re

def normalize_team(name):
    """Strict exact-match normalization. No partial matching."""
    if not name or str(name).strip() == '' or str(name) == 'None':
        return None
    
    name = str(name).strip()
    
    # Remove record in parens like "(32-2)" or "(31-3)"
    name = re.sub(r'\s*\([\d]+-[\d]+\)', '', name)
    
    # Remove newline content
    name = name.split('\n')[0].strip()
    
    # Remove emoji
    name = re.sub(r'[🏀📉🤕🔒✅]', '', name).strip()
    
    # Remove trailing seed numbers like "Duke 1", "Houston 2", "South Florida 11"
    name = re.sub(r'\s+\d+$', '', name).strip()
    
    # Remove leading rank numbers like "1. Duke Blue Devils"
    name = re.sub(r'^\d+\.?\s*', '', name).strip()
    
    # Remove " seed," type text
    name = re.sub(r'\s*\d+\s*seed.*', '', name, flags=re.IGNORECASE).strip()
    
    clean = name.lower().strip()
    
    if clean in TEAM_ALIASES:
        return TEAM_ALIASES[clean]
    
    return None  # Not a tournament team - strict matching only

print("Name map loaded. Testing...")
tests = [
    "Duke", "Duke 1", "Duke Blue Devils", "duke",
    "Florida", "Florida 1", "Florida Gators", "Florida State", "Florida St", "South Florida",
    "Michigan", "Michigan 1", "Michigan State", "Michigan St.", "Michigan St. 3",
    "Miami FL", "Miami (FL)", "Miami (OH)", "Miami OH", "Miami",
    "St. John's", "Saint John's", "St John's (NY)",
    "Iowa State", "Iowa St.", "Iowa St. 2", "Iowa",
    "North Carolina", "NC State", "North Carolina State",
    "Tennessee", "Tennessee State", "Tennessee St",
    "UMBC", "Maryland-Baltimore Co.",
    "Prairie View A&M", "PV A&M",
    "McNeese St.", "McNeese",
    "Duke\n 1 seed, ✅",
]
for t in tests:
    result = normalize_team(t)
    status = "✓" if result else "✗"
    print(f"  {status} '{t}' -> {result}")

# === PATCH: Additional aliases found in audit ===
_EXTRA = {
    # Smart/curly apostrophe variants (Unicode 0x2019)
    "st. john\u2019s": "St. John's",
    "st john\u2019s": "St. John's",
    "saint john\u2019s": "St. John's",
    "st. mary\u2019s": "Saint Mary's",
    "st mary\u2019s": "Saint Mary's",
    "saint mary\u2019s": "Saint Mary's",
    "st mary\u2019s ca": "Saint Mary's",
    "st. mary\u2019s ca": "Saint Mary's",
    # No apostrophe
    "saint marys": "Saint Mary's",
    "st marys": "Saint Mary's",
    "st. marys": "Saint Mary's",
    # LIU Brooklyn
    "liu brooklyn": "LIU",
    "liu_brooklyn": "LIU",
    "long island university sharks": "LIU",
    # Queens NC
    "queens nc": "Queens",
    "queens_nc": "Queens",
    "queens university royals": "Queens",
    # Kennesaw variants
    "kennesaw st.": "Kennesaw State",
    "kennesaw st": "Kennesaw State",
    # McNeese extra
    "mcneese state": "McNeese",
    # North Carolina extra
    "n carolina": "North Carolina",
    "n. carolina": "North Carolina",
}
for k,v in _EXTRA.items():
    TEAM_ALIASES[k] = v

print("Patch applied. New total aliases:", len(TEAM_ALIASES))

# === PATCH 2: Cal Baptist + DRatings format fixes ===
_EXTRA2 = {
    "cal baptist": "Cal Baptist",
    "california baptist": "Cal Baptist",
    "cal baptist lancers": "Cal Baptist",
    "california baptist lancers": "Cal Baptist",
    "cal baptist 13": "Cal Baptist",
    # DRatings full name formats
    "north carolina tar heels": "North Carolina",
    "saint mary's gaels": "Saint Mary's",
    "saint mary\u2019s gaels": "Saint Mary's",
    "brigham young cougars": "BYU",
    "miami hurricanes": "Miami FL",
    "nc state wolfpack": "NC State",
    "northern iowa panthers": "Northern Iowa",
    "mcneese cowboys": "McNeese",
    "mcneese state cowboys": "McNeese",
}
for k,v in _EXTRA2.items():
    TEAM_ALIASES[k] = v
print("Patch 2 applied. Total aliases:", len(TEAM_ALIASES))

# === PATCH 3: Remaining unmapped teams ===
_EXTRA3 = {
    "wright state raiders": "Wright State",
    "penn quakers": "Penn",
    "pennsylvania quakers": "Penn",
    "north carolina state wolfpack": "NC State",
    "unc tar heels": "North Carolina",
    "unc": "North Carolina",
    "hawai\u02bbi": "Hawaii",  # Unicode okina
    # Hawai'i with various apostrophe-like characters
}
for k,v in _EXTRA3.items():
    TEAM_ALIASES[k] = v
# Also handle the Hawai'i with right single quote
TEAM_ALIASES["hawai\u2019i"] = "Hawaii"
TEAM_ALIASES["hawai'i"] = "Hawaii"  # straight apostrophe
print("Patch 3 applied. Total aliases:", len(TEAM_ALIASES))

# === PATCH 4: Final name fixes ===
_EXTRA4 = {
    "miami (fla.)": "Miami FL",
    "u miami (fl)": "Miami FL",
    "miami university (oh)": "Miami OH",
    "miami-ohio": "Miami OH",
    "miami ohio": "Miami OH",
}
for k,v in _EXTRA4.items():
    TEAM_ALIASES[k] = v
print("Patch 4 applied. Total aliases:", len(TEAM_ALIASES))

# === PATCH 5: Final gaps from user ===
_EXTRA5 = {
    "c florida": "UCF",
    "n iowa": "Northern Iowa",
    "tenn st": "Tennessee State",
    "tenn st.": "Tennessee State",
    "maryland baltimore co.": "UMBC",
    "maryland baltimore co": "UMBC",
    "ca baptist": "Cal Baptist",
    "calif baptist": "Cal Baptist",
}
for k,v in _EXTRA5.items():
    TEAM_ALIASES[k] = v
print("Patch 5 applied. Total aliases:", len(TEAM_ALIASES))
