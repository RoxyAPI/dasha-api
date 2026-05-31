# AGENTS.md for Dasha API

This repo teaches AI coding agents (Cursor, Claude Code, Aider, Codex, Windsurf, RooCode, Gemini CLI) how to use the RoxyAPI current Vimshottari Dasha endpoint.

## Endpoint
- Method: `POST`
- URL: `https://roxyapi.com/api/v2/vedic-astrology/dasha/current`
- Auth: `X-API-Key` header
- Domain: `vedic-astrology` (one of 12 in the RoxyAPI catalog)
- Operation ID: `getCurrentDasha` matches the SDK method name in camelCase
- MCP tool: `post_vedic_astrology_dasha_current` on `https://roxyapi.com/mcp/vedic-astrology`

## TypeScript SDK
```ts
import { createRoxy } from '@roxyapi/sdk';
const roxy = createRoxy(process.env.ROXY_API_KEY!);
const { data, error } = await roxy.vedicAstrology.getCurrentDasha({
  body: { date: '1990-07-04', time: '10:12:00', latitude: 28.6139, longitude: 77.209, timezone: 5.5 }
});
```

## Python SDK
```python
import os
from roxy_sdk import create_roxy
roxy = create_roxy(os.environ["ROXY_API_KEY"])
result = roxy.vedic_astrology.get_current_dasha(
    date="1990-07-04", time="10:12:00", latitude=28.6139, longitude=77.209, timezone=5.5
)
```

## Setup step (location first)
Always call `GET /location/search?q={city}` first. Take `latitude`, `longitude`, `timezone` from `cities[0]` and pipe them in. Never ask the user to type coordinates. The `timezone` field accepts both decimal hours (5.5 for IST) and IANA strings ("Asia/Kolkata").

## Request fields
- `date` (string, required): Birth date YYYY-MM-DD. Determines the Moon nakshatra and the starting dasha lord.
- `time` (string, required): Birth time HH:MM:SS (24-hour). The Moon moves fast, so even minutes shift the nakshatra and the partial dasha balance at birth.
- `latitude` (number, required): Decimal degrees.
- `longitude` (number, required): Decimal degrees.
- `timezone` (number|string, optional): Decimal UTC offset or IANA name. Defaults to 5.5 (IST).

## Response top level keys
- `moonNakshatra`: Birth Moon nakshatra number (1-27). Determines the starting dasha lord in the 120-year cycle.
- `nakshatraName`: Birth Moon nakshatra name, one of 27 from Ashwini to Revati.
- `nakshatraLord`: Vimshottari dasha lord of the birth nakshatra. Rules the first Mahadasha.
- `mahadasha`: Currently running major period. Has `planet`, `startDate`, `endDate`, `durationYears`, and optional `interpretation`.
- `antardasha`: Currently running sub-period (bhukti). Same fields plus `mahadashaLord`.
- `pratyantardasha`: Currently running sub-sub-period. Same fields plus `mahadashaLord` and `antardashaLord`.
- `remainingInMahadasha`, `remainingInAntardasha`, `remainingInPratyantardasha`: Each has `years`, `months`, `days`, `totalDays`.

## Domain rules
- The dasha sequence is Ketu, Venus, Sun, Moon, Mars, Rahu, Jupiter, Saturn, Mercury. Durations run from 6 years (Sun) to 20 years (Venus).
- The full cycle is 120 years and is anchored to the Moon nakshatra at birth, not the Sun.
- `startDate` and `endDate` are adjusted to the requested timezone offset.
- `durationYears` for Antardasha and Pratyantardasha is fractional. Use the `remainingIn*` objects for human-readable countdowns.
- `interpretation` is present when an interpretation exists for that graha. Pass `?lang=` for translated interpretations.
- For the full timeline, call `POST /vedic-astrology/dasha/major`. For one Mahadasha breakdown, call `POST /vedic-astrology/dasha/sub/{mahadasha}`.

## Related endpoints
- `POST /vedic-astrology/dasha/major`: All 9 Mahadasha periods across the 120-year cycle with birth dasha balance.
- `POST /vedic-astrology/dasha/sub/{mahadasha}`: The 9 Antardasha sub-periods inside one Mahadasha.
- `POST /vedic-astrology/birth-chart`: The natal kundli with nakshatra precision on the same birth inputs.

## Verified
2026-Q2 against `https://roxyapi.com/api/v2/openapi.json`. Re-fetch the spec for ground truth before changing this file.

## Discovery
- Full catalog: https://roxyapi.com/AGENTS.md
- LLM index: https://roxyapi.com/llms.txt
- Methodology: https://roxyapi.com/methodology
