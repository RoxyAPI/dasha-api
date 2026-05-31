"""
Dasha API example: current Vimshottari Dasha (Mahadasha, Antardasha, Pratyantardasha)
Docs: https://roxyapi.com/api-reference
"""
import os
from roxy_sdk import create_roxy

roxy = create_roxy(os.environ["ROXY_API_KEY"])

# Step 1: geocode the birth city to get latitude, longitude, timezone
loc = roxy.location.search_cities(q="New Delhi")
city = loc["cities"][0]

# Step 2: get the current dasha periods (Mahadasha, Antardasha, Pratyantardasha) with remaining time
dasha = roxy.vedic_astrology.get_current_dasha(
    date="1990-07-04",
    time="10:12:00",
    latitude=city["latitude"],
    longitude=city["longitude"],
    timezone=city["timezone"],
)

mahadasha = dasha["mahadasha"]
antardasha = dasha["antardasha"]
pratyantardasha = dasha["pratyantardasha"]
r = dasha["remainingInMahadasha"]

print("--- Current Vimshottari Dasha ---")
print(f"Birth nakshatra: {dasha['nakshatraName']} (lord {dasha['nakshatraLord']})")
print(f"Mahadasha:       {mahadasha['planet']}  {mahadasha['startDate']} to {mahadasha['endDate']}")
print(f"Antardasha:      {antardasha['planet']} under {antardasha['mahadashaLord']}")
print(f"Pratyantardasha: {pratyantardasha['planet']} under {pratyantardasha['antardashaLord']}")
print(f"Remaining in Mahadasha: {r['years']}y {r['months']}m {r['days']}d")
