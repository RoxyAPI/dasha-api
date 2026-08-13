[![Dasha API](banner.png)](https://roxyapi.com/products/vedic-astrology-api)

# Dasha API

> Vimshottari Dasha API. Current Mahadasha, Antardasha, Pratyantardasha with remaining time, plus the 120 year dasha timeline and nakshatra balance at birth. Roxy Ephemeris, verified against NASA JPL Horizons.

[![Get API Key](https://img.shields.io/badge/Get_API_Key-RoxyAPI-14b8a6?style=for-the-badge&logo=key&logoColor=white)](https://roxyapi.com/pricing)
[![Try Live](https://img.shields.io/badge/Try_API_Live-Free_in_browser-22c55e?style=for-the-badge&logo=swagger&logoColor=white)](https://roxyapi.com/api-reference)
[![Methodology](https://img.shields.io/badge/Methodology-NASA_JPL_verified-f59e0b?style=for-the-badge&logo=nasa&logoColor=white)](https://roxyapi.com/methodology)
[![MCP Server](https://img.shields.io/badge/MCP_Server-Streamable_HTTP-8b5cf6?style=for-the-badge&logo=anthropic&logoColor=white)](https://roxyapi.com/docs/mcp)
[![SDK](https://img.shields.io/badge/SDK-TypeScript_+_Python_+_PHP_+_C%23_+_Go_+_WordPress-3b82f6?style=for-the-badge&logo=npm&logoColor=white)](https://roxyapi.com/docs/sdk)

## What is Dasha API

The Dasha API calculates the current Vimshottari Dasha periods (Mahadasha, Antardasha, Pratyantardasha) for any birth date, time, and location, with remaining time in each period. This dasha calculator API is built for life phase prediction and planetary period analysis. The 120 year dasha system is based on the Moon nakshatra at birth, so the response also returns the birth nakshatra and its lord. Use it to understand current planetary influences, dasha transitions, and timing of events in Vedic astrology. Roxy Ephemeris, verified against NASA JPL Horizons. 12+ spiritual domains in one subscription, Remote MCP server included.

## Why this API

| Property | Value |
|----------|-------|
| Coverage | 12+ spiritual domains in one subscription |
| Calculation | Roxy Ephemeris, verified against NASA JPL Horizons |
| MCP server | `https://roxyapi.com/mcp/vedic-astrology` (Streamable HTTP, no local setup) |
| SDKs | TypeScript on npm `@roxyapi/sdk`, Python on PyPI `roxy-sdk`, PHP on Packagist `roxyapi/sdk`, C# on NuGet `RoxyApi.Sdk`, Go `github.com/RoxyAPI/sdk-go`, WordPress plugin `roxyapi` |
| Pricing | One key, flat per call, from $39/mo |
| Licensing | Personal and commercial use, including closed source apps. No AGPL or GPL entanglement. [Full terms](https://roxyapi.com/policy/license) |
| Last verified | 2026-Q3 |

## Quick start

1. Get a key at [roxyapi.com/pricing](https://roxyapi.com/pricing)
2. Pick a language below
3. Copy the snippet, run, ship

### cURL

```bash
# Step 1: geocode the city
curl -s "https://roxyapi.com/api/v2/location/search?q=New+Delhi" \
  -H "X-API-Key: $ROXY_API_KEY"

# Step 2: call the endpoint with latitude, longitude, and timezone from cities[0]
curl -X POST https://roxyapi.com/api/v2/vedic-astrology/dasha/current \
  -H "X-API-Key: $ROXY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"date":"1990-07-04","time":"10:12:00","latitude":28.6139,"longitude":77.209,"timezone":5.5}'
```

### Python

```python
import os
from roxy_sdk import create_roxy

roxy = create_roxy(os.environ["ROXY_API_KEY"])

# Step 1: geocode the birth city
city = roxy.location.search_cities(q="New Delhi")["cities"][0]

# Step 2: get the current Vimshottari dasha periods
dasha = roxy.vedic_astrology.get_current_dasha(
    date="1990-07-04",
    time="10:12:00",
    latitude=city["latitude"],
    longitude=city["longitude"],
    timezone=city["timezone"],
)

maha = dasha["mahadasha"]
print(f"Nakshatra: {dasha['nakshatraName']} (lord {dasha['nakshatraLord']})")
print(f"Mahadasha: {maha['planet']} {maha['startDate']} to {maha['endDate']}")
print("Remaining in Mahadasha:", dasha["remainingInMahadasha"])
```

### JavaScript (Node)

```js
import { createRoxy } from '@roxyapi/sdk';

const roxy = createRoxy(process.env.ROXY_API_KEY);

// Step 1: geocode the birth city
const { data: loc } = await roxy.location.searchCities({ query: { q: 'New Delhi' } });
const { latitude, longitude, timezone } = loc.cities[0];

// Step 2: get the current Vimshottari dasha periods
const { data: dasha } = await roxy.vedicAstrology.getCurrentDasha({
  body: { date: '1990-07-04', time: '10:12:00', latitude, longitude, timezone },
});

const maha = dasha.mahadasha;
console.log(`Nakshatra: ${dasha.nakshatraName} (lord ${dasha.nakshatraLord})`);
console.log(`Mahadasha: ${maha.planet} ${maha.startDate} to ${maha.endDate}`);
console.log('Remaining in Mahadasha:', dasha.remainingInMahadasha);
```

### TypeScript

```ts
import { createRoxy } from '@roxyapi/sdk';

const roxy = createRoxy(process.env.ROXY_API_KEY!);

// Step 1: geocode the birth city
const { data: loc } = await roxy.location.searchCities({ query: { q: 'New Delhi' } });
const { latitude, longitude, timezone } = loc.cities[0];

// Step 2: get the current Vimshottari dasha periods (Mahadasha, Antardasha, Pratyantardasha)
const { data: dasha } = await roxy.vedicAstrology.getCurrentDasha({
  body: { date: '1990-07-04', time: '10:12:00', latitude, longitude, timezone },
});

const maha = dasha.mahadasha;
console.log(`Nakshatra: ${dasha.nakshatraName} (lord ${dasha.nakshatraLord})`);
console.log(`Mahadasha: ${maha.planet} ${maha.startDate} to ${maha.endDate}`);
console.log('Remaining in Mahadasha:', dasha.remainingInMahadasha);
```

## Request schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `date` | string | yes | Birth date in YYYY-MM-DD format. Determines the Moon nakshatra and the starting dasha lord in the Vimshottari cycle. |
| `time` | string | yes | Birth time in 24-hour HH:MM:SS format. The Moon moves fast, so even minutes shift the nakshatra and the partial dasha balance at birth. |
| `latitude` | number | yes | Birth location latitude in decimal degrees. Example: Delhi 28.6139, Mumbai 19.0760. |
| `longitude` | number | yes | Birth location longitude in decimal degrees. Example: Delhi 77.2090, Mumbai 72.8777. |
| `timezone` | number or string | no | Timezone as decimal hours from UTC (e.g. 5.5 for IST) or IANA name (e.g. "Asia/Kolkata"). IANA strings resolve to DST-correct offset for the given date. Defaults to 5.5 (IST). |

## Response shape

```json
{
  "moonNakshatra": 17,
  "nakshatraName": "Anuradha",
  "nakshatraLord": "Saturn",
  "mahadasha": {
    "planet": "Ketu",
    "startDate": "2023-08-23T10:12:00",
    "endDate": "2030-08-23T10:12:00",
    "durationYears": 7,
    "interpretation": "This period is often spiritually oriented..."
  },
  "antardasha": {
    "planet": "Mars",
    "mahadashaLord": "Ketu",
    "startDate": "2026-02-24T16:24:00",
    "endDate": "2026-07-23T20:12:00",
    "durationYears": 0.408
  },
  "pratyantardasha": {
    "planet": "Ketu",
    "mahadashaLord": "Ketu",
    "antardashaLord": "Mars",
    "startDate": "2026-05-31T09:26:00",
    "endDate": "2026-06-09T02:15:00",
    "durationYears": 0.024
  },
  "remainingInMahadasha": { "years": 4, "months": 2, "days": 23, "totalDays": 1545 },
  "remainingInAntardasha": { "years": 0, "months": 1, "days": 24, "totalDays": 54 },
  "remainingInPratyantardasha": { "years": 0, "months": 0, "days": 9, "totalDays": 9 }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `moonNakshatra` | number | Birth Moon nakshatra number (1-27). This nakshatra determines the starting dasha lord in the Vimshottari 120-year cycle. |
| `nakshatraName` | string | Name of the birth Moon nakshatra (lunar mansion). One of 27 Vedic nakshatras from Ashwini to Revati. |
| `nakshatraLord` | string | Vimshottari dasha lord of the birth nakshatra. This planet rules the first Mahadasha in the native life cycle. |
| `mahadasha` | object | Currently running Mahadasha (major planetary period). Start and end dates are determined by Moon nakshatra at birth. |
| `mahadasha.planet` | string | Ruling graha of this dasha period. One of 9 planets in the Ketu-Venus-Sun-Moon-Mars-Rahu-Jupiter-Saturn-Mercury sequence. |
| `mahadasha.startDate` | string | Start datetime of this dasha period. Adjusted to the requested timezone offset. |
| `mahadasha.endDate` | string | End datetime of this dasha period. Adjusted to the requested timezone offset. |
| `mahadasha.durationYears` | number | Duration in years. Mahadasha durations range from 6 years (Sun) to 20 years (Venus). |
| `mahadasha.interpretation` | string | Vedic interpretation of the planetary period describing themes, karmic lessons, and life areas affected by this graha. |
| `antardasha` | object | Currently running Antardasha (bhukti), the sub-period within a Mahadasha. Adds `mahadashaLord` (parent Mahadasha lord). |
| `pratyantardasha` | object | Currently running Pratyantardasha (sub-sub-period), the third level of the hierarchy for finer event timing. Adds `mahadashaLord` and `antardashaLord`. |
| `remainingInMahadasha` | object | Time remaining in the currently running Mahadasha, as `years`, `months`, `days`, and `totalDays`. |
| `remainingInAntardasha` | object | Time remaining in the currently running Antardasha, as `years`, `months`, `days`, and `totalDays`. |
| `remainingInPratyantardasha` | object | Time remaining in the currently running Pratyantardasha, as `years`, `months`, `days`, and `totalDays`. |

## Common use cases

| Use case | Endpoint flow |
|----------|---------------|
| Current life phase for a birth date and city | Call `/location/search?q={city}` first, take `latitude`, `longitude`, `timezone` from `cities[0]`, POST to `/vedic-astrology/dasha/current` |
| Dasha transition countdown widget | Read `remainingInMahadasha`, `remainingInAntardasha`, and `remainingInPratyantardasha` for a live countdown to the next period change. |
| Full 120 year dasha timeline | Call `/vedic-astrology/dasha/major` for all 9 Mahadasha periods from birth with the birth dasha balance. |
| Antardasha breakdown of a single Mahadasha | Call `/vedic-astrology/dasha/sub/{mahadasha}` for the 9 proportional sub-periods within one Mahadasha. |
| Event timing in Vedic astrology software | Combine current dasha with the natal chart from `/vedic-astrology/birth-chart` for prediction and planetary period analysis. |

## Related endpoints in this domain

- [All Mahadashas (120 year cycle)](https://roxyapi.com/api-reference#tag/Vedic-Astrology/POST/vedic-astrology/dasha/major): The complete Vimshottari timeline, all 9 Mahadasha periods from birth with the birth dasha balance
- [Antardashas for a Mahadasha](https://roxyapi.com/api-reference#tag/Vedic-Astrology/POST/vedic-astrology/dasha/sub/{mahadasha}): The 9 proportional Antardasha sub-periods inside a single Mahadasha
- [Vedic Birth Chart](https://roxyapi.com/api-reference#tag/Vedic-Astrology/POST/vedic-astrology/birth-chart): The natal kundli with nakshatra precision on the same birth inputs

## Use this in your AI agent

Connect Claude, GPT, Gemini, or Cursor to RoxyAPI through the remote MCP server. No Docker. No self hosting. The full MCP tool catalog for this domain is at `https://roxyapi.com/mcp/vedic-astrology`.

```json
{
  "mcpServers": {
    "vedic-astrology": {
      "url": "https://roxyapi.com/mcp/vedic-astrology",
      "headers": { "X-API-Key": "$ROXY_API_KEY" }
    }
  }
}
```

See [docs/mcp](https://roxyapi.com/docs/mcp) for Claude Desktop, Cursor, Windsurf, VS Code, and Claude Code setup.

## For AI coding agents

This repo ships an [AGENTS.md](AGENTS.md) execution playbook. Cursor, Claude Code, Aider, Codex, Windsurf, RooCode, and Gemini CLI will pick it up automatically. Top level overview lives at [roxyapi.com/AGENTS.md](https://roxyapi.com/AGENTS.md).

## Resources

- [Methodology and gold standard tests](https://roxyapi.com/methodology) verified against NASA JPL Horizons
- [Full API reference](https://roxyapi.com/api-reference) interactive Scalar UI
- [TypeScript SDK on npm](https://www.npmjs.com/package/@roxyapi/sdk)
- [Python SDK on PyPI](https://pypi.org/project/roxy-sdk/)
- [PHP SDK on Packagist](https://packagist.org/packages/roxyapi/sdk)
- [C# SDK on NuGet](https://www.nuget.org/packages/RoxyApi.Sdk)
- [Go SDK on pkg.go.dev](https://pkg.go.dev/github.com/RoxyAPI/sdk-go)
- [WordPress plugin](https://wordpress.org/plugins/roxyapi/)
- [llms.txt](https://roxyapi.com/llms.txt) full LLM citation index
- [Top level AGENTS.md](https://roxyapi.com/AGENTS.md)

## Other RoxyAPI samples

[![Kundli API](https://img.shields.io/badge/Kundli_API-RoxyAPI-14b8a6?style=flat-square)](https://github.com/RoxyAPI/kundli-api)
[![KP Astrology API](https://img.shields.io/badge/KP_Astrology_API-RoxyAPI-14b8a6?style=flat-square)](https://github.com/RoxyAPI/kp-astrology-api)
[![Panchang API](https://img.shields.io/badge/Panchang_API-RoxyAPI-14b8a6?style=flat-square)](https://github.com/RoxyAPI/panchang-api)

## License

MIT for this sample repo. See [LICENSE](LICENSE).

**Catalog licensing:** Personal and commercial use, including closed source proprietary apps. No AGPL or GPL entanglement. RoxyAPI APIs and SDKs are safe to embed in commercial products. Full terms at [roxyapi.com/policy/license](https://roxyapi.com/policy/license).

## Contact

- Site: [roxyapi.com](https://roxyapi.com)
- Status: [roxyapi.com/api-reference](https://roxyapi.com/api-reference)
