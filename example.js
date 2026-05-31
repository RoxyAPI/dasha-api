/**
 * Dasha API example: current Vimshottari Dasha (Mahadasha, Antardasha, Pratyantardasha)
 * Docs: https://roxyapi.com/api-reference
 */
import { createRoxy } from '@roxyapi/sdk';

const roxy = createRoxy(process.env.ROXY_API_KEY);

// Step 1: geocode the birth city to get latitude, longitude, timezone
const { data: loc } = await roxy.location.searchCities({ query: { q: 'New Delhi' } });
const { latitude, longitude, timezone } = loc.cities[0];

// Step 2: get the current dasha periods (Mahadasha, Antardasha, Pratyantardasha) with remaining time
const { data: dasha } = await roxy.vedicAstrology.getCurrentDasha({
  body: { date: '1990-07-04', time: '10:12:00', latitude, longitude, timezone },
});

const { mahadasha, antardasha, pratyantardasha } = dasha;
const r = dasha.remainingInMahadasha;

console.log('--- Current Vimshottari Dasha ---');
console.log(`Birth nakshatra: ${dasha.nakshatraName} (lord ${dasha.nakshatraLord})`);
console.log(`Mahadasha:       ${mahadasha.planet}  ${mahadasha.startDate} to ${mahadasha.endDate}`);
console.log(`Antardasha:      ${antardasha.planet} under ${antardasha.mahadashaLord}`);
console.log(`Pratyantardasha: ${pratyantardasha.planet} under ${pratyantardasha.antardashaLord}`);
console.log(`Remaining in Mahadasha: ${r.years}y ${r.months}m ${r.days}d`);
