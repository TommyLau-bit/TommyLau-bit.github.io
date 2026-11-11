// ── Power: the roster of ways to power an AI data centre ────────────────────
// Tommy, 11 Nov 2026. The grid first, then the machines builders turn to
// when it makes them wait (no "unlock" idea: Tommy, 11 Nov 2026). Every number is sourced and dated; a number that
// could not be sourced is null and shows as n/a. Ratings are never typed in:
// they are worked out from these numbers by the formulas in power-ratings.ts.
import type { Stat } from './power-ratings';

export type Group = { id: string; name: string; tag: string; why: string };
export const GROUPS: Group[] = [
  { id: 'grid', name: 'The grid', tag: 'GRID', why: 'Where every builder starts: no machine to buy and no fuel to find, if the grid will connect you.' },
  { id: 'biggas', name: 'Big gas turbines', tag: 'GAS-L', why: 'When the grid makes you wait, you build your own power station beside the campus.' },
  { id: 'smallgas', name: 'Small gas machines', tag: 'GAS-S', why: 'When the big turbines are sold out, smaller machines come from other factories and other queues.' },
  { id: 'sun', name: 'Solar and batteries', tag: 'SUN', why: 'The fastest power to build, but it cannot carry a winter night.' },
  { id: 'nuclear', name: 'Large nuclear', tag: 'NUC', why: 'Power for every hour of the year: old reactors first, new ones later.' },
  { id: 'micro', name: 'Microreactors', tag: 'MICRO', why: 'A reactor small enough to move by road, if its fuel can be made.' },
];

export type Card = {
  id: string;
  group: string;
  name: string;
  examples?: string | null;
  makers: string[];
  chapters: { slug: string; anchor?: string }[];
  stats: {
    sizeMW: Stat;
    monthsToPower: Stat;
    costPerKW: Stat;
    fuel: Stat;           // fuel and heat rate (display only)
    capacityFactor: Stat; // display only: how often it ran
    elcc: Stat;           // PJM ELCC class rating: the round-the-clock rating reads this
    fuelDays: Stat;
    permitMonths: Stat;
    bottleneck: Stat;     // display only
  };
  role: string;           // one word for the job it does for a data centre (replaces OVR)
  ability: string;
  weakness: string;
  drawing: string;        // aria-label of the cutaway
};

export const CARDS: Card[] = [
 {
  "id": "grid",
  "role": "Default",
  "group": "grid",
  "name": "Grid connection",
  "examples": "Johor and America",
  "makers": [
   "Siemens Energy",
   "Hitachi Energy"
  ],
  "chapters": [
   {
    "slug": "the-queue-not-the-chip",
    "anchor": "why-did-so-many-data-centres-come-to-johor"
   },
   {
    "slug": "america-rations-the-plug",
    "anchor": "which-step-takes-longest-and-why-can-no-rule-hurry-it"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": 389,
    "display": "about 389 MW a load",
    "basis": "Average of the 17 large loads totalling 6,608 MW that had cleared every ERCOT check except approval to energise by 20 August 2026; my division of ERCOT's figures.",
    "source": "ERCOT presentation to the Public Utility Commission of Texas (20 August 2026), as cited in the piece",
    "date": "2026-08-20"
   },
   "monthsToPower": {
    "value": [
     12,
     48
    ],
    "display": "12 months on Green Lane, 36 to 48 before (Johor)",
    "basis": "Time to connect a data centre at 132 or 275 kV in Malaysia: 36 to 48 months before Tenaga's Green Lane Pathway (8 August 2023), 12 months under it, plant included. No equivalent American figure is published for loads.",
    "source": "Tenaga Nasional, Green Lane Pathway, as cited in the piece",
    "date": "2023-08-08"
   },
   "costPerKW": {"value": 505, "display": "about US$500/kW (Tenaga's worked example)", "short": "about US$500/kW to connect (Tenaga example)", "basis": "Tenaga's own worked example of its connection charge for a 40 MW high-voltage customer, not a real project: RM82,257,523 for 40,000 kW, about RM2,056/kW, at about RM4.07 to the US dollar (Bank Negara Malaysia, 11 Nov 2026). The charge is the project cost less 15 years of discounted network revenue, so it varies by site and can be zero. No US utility or regulator publishes a per-kW figure for data centres.", "source": "Tenaga Nasional, Connection Charges Book 2025, Table 7", "url": "https://www.tnb.com.my/assets/files/TNB_Connection_Charges_Book_2025_ENG.pdf", "date": "2025"},
   "capacityFactor": {
    "display": "n/a",
    "basis": "Firm service is a promise to carry the load 'at all times short of an emergency'; no percentage is published. Cut-first tiers state no hours either.",
    "value": null
   },
   "fuelDays": {"value": 0, "display": "0 days", "short": "0 days: power by wire", "basis": "Power comes by wire and nothing is stored on site: the same rule as gas on a pipe. If the grid goes down, so does the site."},
   "permitMonths": {
    "value": null,
    "display": "n/a",
    "basis": "FERC targets 2 to 3 months for the study that lists the upgrades (show cause order, 18 June 2026), but the study is not the wait: the queue for transformers and lines is, and that is already in Speed."
   },
   "bottleneck": {
    "value": null,
    "display": "Transformers: 36 to 60 months",
    "basis": "Lead time for large power transformers, the upgrade no rule can hurry (DOE, July 2024).",
    "source": "US Department of Energy report (July 2024), as cited in the piece",
    "date": "2024-07"
   },
   "fuel": {
    "value": null,
    "display": "Grid mix",
    "basis": "The site buys from the grid; no fuel of its own."
   },
   "elcc": {"value": 99.949, "display": "99.95% of the year with power (US average, 2025)", "short": "99.95% of the year powered", "basis": "Not a PJM firmness rating, which the grid has no class for: the share of 2025 the average US customer had power, from SAIDI of 269.2 minutes including major events; 100 x (1 - 269.2 / 525,600). 2024 was worse, 662.6 minutes (99.87%).", "source": "EIA, Electric Power Annual, Table 11.1, Reliability Metrics of U.S. Distribution System", "url": "https://www.eia.gov/electricity/annual/html/epa_11_01.html", "date": "2025"}
  },
  "ability": "Firm service: the grid promises power at all times short of an emergency.",
  "weakness": "Large transformers are quoted at 36 months, and up to 60.",
  "drawing": "Cutaway of a grid connection: a high-voltage line feeds a substation transformer, shown open with its core, copper windings, oil, bushings and radiators, then through the fence to the data centre, while new projects wait in line for a connection."
 },
 {
  "id": "heavy-sc",
  "role": "Bridge",
  "group": "biggas",
  "name": "Heavy-frame gas turbine, simple cycle",
  "examples": "GE Vernova 7HA, Siemens HL, Mitsubishi JAC",
  "makers": [
   "GE Vernova",
   "Siemens Energy",
   "Mitsubishi Heavy"
  ],
  "chapters": [
   {
    "slug": "the-equipment-queue",
    "anchor": "what-electrical-gear-does-an-ai-data-centre-need-before-it-can-switch-on"
   },
   {
    "slug": "building-your-own-power",
    "anchor": "how-long-is-the-queue-at-ge-vernova"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": 430,
    "display": "430 MW",
    "basis": "One GE Vernova 7HA.03 in simple cycle (maker rating). Siemens SGT6-9000HL 440 MW; Mitsubishi M501JAC 453 MW.",
    "source": "GE Vernova 7HA product pages, as cited in the piece",
    "date": "2026-11-07 (read)"
   },
   "monthsToPower": {
    "value": [
     81,
     92
    ],
    "display": "81 to 92 months",
    "basis": "A heavy slot sold on 28 October 2026 ships in 2032 (63 to 74 months later) and then needs about 18 months on site; my arithmetic from GE Vernova's statements. The piece rounds this to power 'around 2034'.",
    "source": "GE Vernova results call (28 October 2026) and call of 22 July 2026, as cited in the piece",
    "date": "2026-10-28"
   },
   "costPerKW": {
    "value": 1158,
    "display": "US$1,158/kW (2025$)",
    "basis": "EIA's planning cost for a new combustion turbine, industrial frame, 2025 dollars, before its optimism factor. One table for every EIA-based card, so the costs compare like for like.",
    "source": "EIA, Assumptions to the Annual Energy Outlook 2026: Electricity Market Module, Table 3 (base overnight cost)",
    "url": "https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf",
    "date": "2026-04"
   },
   "capacityFactor": {
    "value": 13.6,
    "display": "13.6% (US gas turbines, 2025)",
    "basis": "Actual 2025 capacity factor of all US natural gas combustion turbines (heavy-frame and aeroderivative together). This measures how much they ran by dispatch choice as peakers, not how much they could run; it understates ability.",
    "source": "EIA, Electric Power Monthly, Table 6.07.A, Capacity Factors for Utility Scale Generators Primarily Using Fossil Fuels",
    "url": "https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_a",
    "date": "2026-10-23 (2025 annual, final)"
   },
   "fuelDays": {
    "value": 0,
    "display": "0 days",
    "basis": "Gas on a pipe: no fuel stored on site (spec rule: gas on a pipe = 0 days)."
   },
   "permitMonths": {
    "display": "n/a",
    "basis": "No dated air permit for a heavy-frame simple-cycle plant at a data centre is in the pieces or found in a primary record. Homer City's permit (about 7.5 months) covers combined cycle and aeroderivatives only.",
    "value": null
   },
   "bottleneck": {
    "value": null,
    "display": "122 GW queue, 6.1 years",
    "basis": "GE Vernova gas turbine gigawatts under contract (firm orders plus paid slot reservations) at 30 September 2026, in years of its 20 GW a year output; the three makers together hold about 250 GW.",
    "source": "GE Vernova results release (28 October 2026), as cited in the piece",
    "date": "2026-10-28"
   },
   "fuel": {
    "value": null,
    "display": "Natural gas, 7,884 Btu/kWh",
    "basis": "Maker's rated heat rate of a new GE 7HA.03 in simple cycle (43.3% efficiency). The US fleet's tested 2025 average for all gas turbines is 10,975.",
    "source": "GE Vernova 7HA product pages, as cited in the piece",
    "date": "2026-11-07 (read)"
   },
   "elcc": {
    "value": 59,
    "display": "PJM ELCC 59% (gas CT class)",
    "basis": "PJM's rating of a gas combustion turbine for the 2029/30 capacity auction: the share of each MW it counts as firm. PJM rates turbines by class, not by frame or aeroderivative.",
    "source": "PJM, ELCC Class Ratings for the 2029/2030 Base Residual Auction",
    "date": "2026-08-07",
    "origin": "new"
   }
  },
  "ability": "About 430 MW from one machine at 43 per cent efficiency.",
  "weakness": "A slot sold today ships in 2032; GE Vernova's queue is 6.1 years.",
  "drawing": "Cutaway of a heavy-frame gas turbine in simple cycle: air enters through filters, the compressor squeezes it, gas burns in the combustor, the hot gas spins the turbine stages, which turn the compressor and the generator on one shaft, and the exhaust leaves up the stack."
 },
 {
  "id": "ccgt",
  "role": "Baseload",
  "group": "biggas",
  "name": "Combined-cycle gas plant",
  "examples": "One gas turbine plus a steam turbine",
  "makers": [
   "GE Vernova",
   "Siemens Energy",
   "Mitsubishi Heavy"
  ],
  "chapters": [
   {
    "slug": "the-equipment-queue",
    "anchor": "what-electrical-gear-does-an-ai-data-centre-need-before-it-can-switch-on"
   },
   {
    "slug": "building-your-own-power",
    "anchor": "how-does-a-gas-turbine-turn-gas-into-electricity"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": 640,
    "display": "about 640 MW",
    "basis": "One GE 7HA.03 turbine plus a steam turbine (one-on-one combined cycle), maker figure. Siemens HL 655 MW, Mitsubishi JAC 664 MW one-on-one. Real plants often pair two turbines (EIA's reference plant is 1,227 MW).",
    "source": "GE Vernova 7HA product pages, as cited in the piece",
    "date": "2026-11-07 (read)"
   },
   "monthsToPower": {
    "value": [
     29,
     52
    ],
    "display": "29 to 52 months",
    "basis": "Meta's Hyperion: Louisiana's regulator approved three Entergy gas plants (2,262 MW) in August 2025 for service in 2028 and 2029; my arithmetic from approval month to January 2028 and December 2029.",
    "source": "Louisiana Public Service Commission approval, docket U-37425, as cited in the piece",
    "date": "2025-08"
   },
   "costPerKW": {
    "value": 1032,
    "display": "US$1,032/kW (2025$)",
    "basis": "EIA's planning cost for a new combined cycle, multi-shaft, 2025 dollars, before its optimism factor. One table for every EIA-based card, so the costs compare like for like.",
    "source": "EIA, Assumptions to the Annual Energy Outlook 2026: Electricity Market Module, Table 3 (base overnight cost)",
    "url": "https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf",
    "date": "2026-04"
   },
   "capacityFactor": {
    "value": 58.7,
    "display": "58.7%",
    "basis": "Actual 2025 capacity factor of US natural gas combined-cycle plants; partly set by dispatch choice.",
    "source": "EIA Electric Power Monthly, Tables 6.07.A and 6.07.B (23 October 2026)",
    "url": "https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_a",
    "date": "2026-10-23"
   },
   "fuelDays": {
    "value": 0,
    "display": "0 days",
    "basis": "Gas on a pipe: no fuel stored on site (spec rule: gas on a pipe = 0 days)."
   },
   "permitMonths": {
    "value": 7.5,
    "display": "about 7.5 months (Homer City air permit)",
    "basis": "Pennsylvania DEP air plan approval 32-00457A for Homer City (seven combined-cycle turbines and ten Mitsubishi FT8 aeroderivatives): application received 4 April 2025, approval issued 18 November 2025; about 7.5 months, my arithmetic. By netting against its retired coal boilers, Homer City avoided the federal Prevention of Significant Deterioration review for NOx and CO only; it stays under that review for particulates, sulphuric acid mist and greenhouse gases, and must buy 369 tonnes of VOC credits. A fast case, not a typical one.",
    "source": "Pennsylvania DEP, Technical Review Memo for Plan Approval No. 32-00457A, Homer City Generation LP",
    "url": "https://files.dep.state.pa.us/regionalresources/NWRO/NWROPortalFiles/Homer-City/Air/Final-AQ-Plan-Approval/Tech%20Review%20Memo%20Signed%2020251118.pdf",
    "date": "2025-11-18"
   },
   "bottleneck": {
    "value": null,
    "display": "Same turbine queue",
    "basis": "Mitsubishi Heavy says orders booked in its August 2026 quarter were due between 2028 and 2030; GE Vernova sold slots for 2032.",
    "source": "Mitsubishi Heavy Q&A summary (6 August 2026), as cited in the piece",
    "date": "2026-08-06"
   },
   "fuel": {
    "value": null,
    "display": "Natural gas, 7,535 Btu/kWh",
    "basis": "US fleet average tested heat rate for natural gas combined cycle, 2025 (EIA Electric Power Annual, Table 8.2).",
    "source": "EIA Electric Power Annual, Table 8.2, as cited in the piece",
    "date": "2025 data"
   },
   "elcc": {
    "value": 75,
    "display": "PJM ELCC 75%",
    "basis": "PJM's rating of a combined-cycle gas plant for the 2029/30 capacity auction: the share of each MW counted as firm.",
    "source": "PJM, ELCC class ratings for the 2029/2030 Base Residual Auction",
    "date": "2026-08-07"
   }
  },
  "ability": "Burns about 30 per cent less gas per unit than simple cycle.",
  "weakness": "Same turbine queue; Duke's filed plants cost about US$1,620 to 2,340 per kilowatt.",
  "drawing": "Cutaway of a combined-cycle plant: a gas turbine sends its hot exhaust into a heat recovery boiler, whose tube banks raise steam in a drum; the steam drives a steam turbine and a second generator, and a condenser turns it back to water."
 },
 {
  "id": "aero",
  "role": "Fast start",
  "group": "smallgas",
  "name": "Aeroderivative gas turbine",
  "examples": "GE Vernova LM2500XPRESS, LM6000",
  "makers": [
   "GE Vernova",
   "Mitsubishi Power"
  ],
  "chapters": [
   {
    "slug": "building-your-own-power",
    "anchor": "is-there-a-faster-machine"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": [
     35,
     58
    ],
    "display": "35 to 58 MW",
    "basis": "Output of one aeroderivative: GE Vernova LM2500XPRESS about 35 MW to LM6000 PF+ up to about 58 MW.",
    "source": "GE Vernova product data, as cited in the piece",
    "date": "2026-11"
   },
   "monthsToPower": {
    "value": [
     45,
     56
    ],
    "display": "45 to 56 months",
    "basis": "GE Vernova's CEO: an aeroderivative ships about 24 months before a heavy unit and needs about six months on site. Heavy slots sold in October 2026 ship in 2032, so an aero ordered then ships in 2030 and runs about six months later; my arithmetic.",
    "source": "GE Vernova call (22 July 2026), as cited in the piece",
    "date": "2026-07-22"
   },
   "costPerKW": {
    "value": 2275,
    "display": "US$2,275/kW (2025$)",
    "basis": "EIA's planning cost for a new combustion turbine, aeroderivative, 2025 dollars, before its optimism factor. One table for every EIA-based card, so the costs compare like for like.",
    "source": "EIA, Assumptions to the Annual Energy Outlook 2026: Electricity Market Module, Table 3 (base overnight cost)",
    "url": "https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf",
    "date": "2026-04"
   },
   "capacityFactor": {
    "value": 13.6,
    "display": "13.6% (US gas turbines, 2025)",
    "basis": "Actual 2025 capacity factor of all US natural gas combustion turbines (heavy-frame and aeroderivative together). This measures how much they ran by dispatch choice as peakers, not how much they could run; it understates ability.",
    "source": "EIA, Electric Power Monthly, Table 6.07.A, Capacity Factors for Utility Scale Generators Primarily Using Fossil Fuels",
    "url": "https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_a",
    "date": "2026-10-23 (2025 annual, final)"
   },
   "fuelDays": {
    "value": 0,
    "display": "0 days",
    "basis": "Gas on a pipe: no fuel stored on site (spec rule: gas on a pipe = 0 days)."
   },
   "permitMonths": {
    "value": 7.5,
    "display": "about 7.5 months (Homer City air permit)",
    "basis": "Pennsylvania DEP air plan approval 32-00457A for Homer City (seven combined-cycle turbines and ten Mitsubishi FT8 aeroderivatives): application received 4 April 2025, approval issued 18 November 2025; about 7.5 months, my arithmetic. By netting against its retired coal boilers, Homer City avoided the federal Prevention of Significant Deterioration review for NOx and CO only; it stays under that review for particulates, sulphuric acid mist and greenhouse gases, and must buy 369 tonnes of VOC credits. A fast case, not a typical one.",
    "source": "Pennsylvania DEP, Technical Review Memo for Plan Approval No. 32-00457A, Homer City Generation LP",
    "url": "https://files.dep.state.pa.us/regionalresources/NWRO/NWROPortalFiles/Homer-City/Air/Final-AQ-Plan-Approval/Tech%20Review%20Memo%20Signed%2020251118.pdf",
    "date": "2025-11-18"
   },
   "bottleneck": {
    "value": null,
    "display": "124-unit backlog, about 2.5 years",
    "basis": "GE Vernova aeroderivatives ordered less shipped since 1 January 2025, at 30 September 2026; about two and a half years of its last twelve months' shipments.",
    "source": "GE Vernova 2025 Form 10-K and Form 10-Q to 30 September 2026, as cited in the piece",
    "date": "2026-09-30"
   },
   "fuel": {
    "value": null,
    "display": "Natural gas, 10,975 Btu/kWh",
    "basis": "US fleet average tested heat rate for natural gas combustion turbines, 2025, which the piece applies to simple-cycle turbines including aeroderivatives. New LM6000 PF+ rated up to about 41.3% efficiency.",
    "source": "EIA Electric Power Annual, Table 8.2, as cited in the piece",
    "date": "2025 data"
   },
   "elcc": {
    "value": 59,
    "display": "PJM ELCC 59% (gas CT class)",
    "basis": "PJM's rating of a gas combustion turbine for the 2029/30 capacity auction: the share of each MW it counts as firm. PJM rates turbines by class, not by frame or aeroderivative.",
    "source": "PJM, ELCC Class Ratings for the 2029/2030 Base Residual Auction",
    "date": "2026-08-07",
    "origin": "new"
   }
  },
  "ability": "Ships about 24 months before a heavy unit; six months on site.",
  "weakness": "Burns about 46 per cent more gas than combined cycle; 124-unit backlog.",
  "drawing": "Cutaway of an aeroderivative gas turbine in its enclosure on a skid: a jet-engine core of compressors, an annular combustor and a high-pressure turbine, then a power turbine that drives the generator, with the exhaust leaving up a stack."
 },
 {
  "id": "recip",
  "role": "Modular",
  "group": "smallgas",
  "name": "Reciprocating gas engine",
  "examples": "Wärtsilä, Caterpillar",
  "makers": [
   "Wärtsilä",
   "Caterpillar"
  ],
  "chapters": [
   {
    "slug": "building-your-own-power",
    "anchor": "is-there-a-faster-machine"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": 18.9,
    "display": "18.9 MW an engine",
    "basis": "One Wärtsilä 18V50SG engine, 18,875 kW at 60 Hz (product leaflet). Sold in blocks: the 282 MW order is 15 engines.",
    "source": "Wärtsilä 18V50SG product leaflet, as cited in the piece",
    "date": "2026-11"
   },
   "monthsToPower": {
    "value": [
     27,
     38
    ],
    "display": "27 to 38 months",
    "basis": "Wärtsilä's 282 MW US data-centre order announced 5 October 2026: delivery 2028, fully running 2029; months to full running are my arithmetic (January to December 2029). First power falls between delivery and full running.",
    "source": "Wärtsilä release (5 October 2026), as cited in the piece",
    "date": "2026-10-05"
   },
   "costPerKW": {
    "value": [
     1400,
     1500
    ],
    "display": "US$1,400 to 1,500/kW",
    "basis": "ProPetro's gas engines, nominal dollars, including balance of plant (about US$1.4m to US$1.5m per MW). A builder's figure, not EIA's planning basis.",
    "source": "ProPetro Form 8-K (28 October 2026), as cited in the piece",
    "date": "2026-10-28"
   },
   "capacityFactor": {
    "value": 18.0,
    "display": "18.0% (US gas engines, 2025)",
    "basis": "Actual 2025 capacity factor of US natural gas internal combustion engines; reflects dispatch as peakers, not ability to run.",
    "source": "EIA, Electric Power Monthly, Table 6.07.A, Capacity Factors for Utility Scale Generators Primarily Using Fossil Fuels",
    "url": "https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_a",
    "date": "2026-10-23 (2025 annual, final)"
   },
   "fuelDays": {
    "value": 0,
    "display": "0 days",
    "basis": "Gas on a pipe: no fuel stored on site (spec rule: gas on a pipe = 0 days)."
   },
   "permitMonths": {
    "display": "n/a",
    "basis": "No dated air permit for an engine plant is in the pieces or a primary record found. Texas paused such permits for data-centre infrastructure on 19 October 2026.",
    "value": null
   },
   "bottleneck": {
    "display": "Lead times rising",
    "basis": "Wärtsilä's interim report of 27 October 2026; it gives no number of months.",
    "source": "Wärtsilä interim report (27 October 2026), as cited in the piece",
    "date": "2026-10-27",
    "value": null
   },
   "fuel": {
    "value": null,
    "display": "Natural gas, 8,853 Btu/kWh",
    "basis": "US fleet average tested heat rate for natural gas internal combustion engines, 2025. A new Wärtsilä 18V50SG is rated at 50.0% efficiency.",
    "source": "EIA Electric Power Annual, Table 8.2, as cited in the piece",
    "date": "2025 data"
   },
   "elcc": {"value": 92, "display": "PJM ELCC 92% (Diesel Utility class)", "basis": "Under PJM's rules (Manual 21B), reciprocating internal combustion engines are the Diesel technology type, so a pipeline-gas engine falls in the Diesel Utility class, not the gas turbine class. A class rating, not a measured record for gas engines; a behind-the-meter engine gets none unless offered into PJM's auction.", "source": "PJM, ELCC Class Ratings for the 2029/2030 Base Residual Auction; PJM Manual 21B, Revision 06, section 2.4", "url": "https://www.pjm.com/-/media/DotCom/planning/res-adeq/elcc/29-30-bra-elcc-class-ratings.pdf", "date": "2026-08-07"}
  },
  "ability": "Small 18.9 MW blocks; Wärtsilä's engine reaches full load in two minutes.",
  "weakness": "Lead times keep rising; an October 2026 order runs fully only in 2029.",
  "drawing": "Cutaway of a reciprocating gas engine: on the left, one pair of cylinders in a V, with pistons, connecting rods and the crankshaft, and a turbocharger in the V; on the right, the generating set from the side, engine, flywheel and alternator on a skid."
 },
 {
  "id": "fuelcell",
  "role": "Modular",
  "group": "smallgas",
  "name": "Solid oxide fuel cell",
  "examples": "Bloom Energy",
  "makers": [
   "Bloom Energy"
  ],
  "chapters": [
   {
    "slug": "building-your-own-power",
    "anchor": "is-there-a-faster-machine"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": 10,
    "display": "10 MW (EIA reference plant)",
    "basis": "EIA's reference fuel cell plant size. Bloom's systems are modular, from hundreds of kilowatts to hundreds of megawatts; its 10-K gives no single unit size.",
    "source": "EIA, Assumptions to the Annual Energy Outlook 2026: Electricity Market Module, Table 3",
    "url": "https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf",
    "date": "2026-04"
   },
   "monthsToPower": {
    "value": 3,
    "display": "about 3 months (Bloom's claim)",
    "claim": "Bloom's own claim of about 90 days, not a measured project",
    "basis": "Bloom's own statement that on-site generation can make power available within about 90 days 'in certain project scopes', subject to permitting and site conditions. A company claim, not a measured project. EIA's planning lead time for fuel cells is 3 years.",
    "source": "Bloom Energy, Form 10-K for 2025",
    "url": "https://www.sec.gov/Archives/edgar/data/1664703/000162828026006516/be-20251231.htm",
    "date": "2026-02-09"
   },
   "costPerKW": {
    "value": 7818,
    "display": "US$7,818/kW (2025$)",
    "basis": "EIA's planning cost for a new fuel cells, 10 MW, 2025 dollars, before its optimism factor. One table for every EIA-based card, so the costs compare like for like.",
    "source": "EIA, Assumptions to the Annual Energy Outlook 2026: Electricity Market Module, Table 3 (base overnight cost)",
    "url": "https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf",
    "date": "2026-04"
   },
   "capacityFactor": {
    "display": "n/a",
    "basis": "EIA's Electric Power Monthly capacity factor tables have no fuel cell column; Bloom publishes no fleet capacity factor.",
    "value": null
   },
   "fuelDays": {
    "value": 0,
    "display": "0 days",
    "basis": "Gas on a pipe: no fuel stored on site (spec rule: gas on a pipe = 0 days)."
   },
   "permitMonths": {
    "display": "n/a",
    "basis": "No months published. Bloom's 10-K says air permits are usually needed only for larger installations and New York, New Jersey and North Carolina exempt fuel cells, but that permit times have lengthened.",
    "value": null
   },
   "bottleneck": {
    "value": null,
    "display": "Factory: 2 GW a year",
    "basis": "Bloom's stated factory capacity by the end of 2026, against Oracle's intent to procure up to 2.8 GW alone.",
    "source": "Bloom Energy 2025 Form 10-K, as cited in the piece",
    "date": "2026-02-09"
   },
   "fuel": {
    "value": null,
    "display": "Natural gas, 6,469 Btu/kWh",
    "basis": "EIA planning heat rate for a new fuel cell plant.",
    "source": "EIA, Assumptions to the Annual Energy Outlook 2026: Electricity Market Module, Table 3",
    "url": "https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf",
    "date": "2026-04"
   },
   "elcc": {"value": 99.9, "display": "about 99.9% available (Bloom's fleet figure)", "short": "99.9% available", "claim": "Bloom's own fleet availability, not a grid operator's rating", "basis": "PJM has no fuel cell class: a fuel cell would fall in its Other Unlimited Resource Class, which gets a rating per resource, not a class rating. Bloom's 10-K: fleet availability about 99.9% for all non-redundant installations since 2020. Availability, not PJM's peak firmness, so not strictly comparable.", "source": "Bloom Energy, Form 10-K for 2025", "url": "https://www.sec.gov/Archives/edgar/data/1664703/000162828026006516/be-20251231.htm", "date": "2026-02-09"}
  },
  "ability": "No flame: New York, New Jersey and North Carolina give fuel cells air-permit exemptions.",
  "weakness": "EIA's planning cost is US$7,818 per kilowatt, the highest gas machine here.",
  "drawing": "Cutaway of a solid oxide fuel cell: on the left, a magnified stack of thin cells, each a fuel layer, a ceramic electrolyte and an air layer, between metal plates; on the right, the fuel cell server with its power modules and an inverter. There is no flame."
 },
 {
  "id": "fleet",
  "role": "Stopgap",
  "group": "smallgas",
  "name": "Rented power fleet",
  "examples": "Solaris Energy Infrastructure",
  "makers": [
   "Solaris Energy Infrastructure",
   "ProPetro"
  ],
  "chapters": [
   {
    "slug": "building-your-own-power",
    "anchor": "is-there-a-faster-machine"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": 29,
    "display": "about 29 MW a turbine",
    "basis": "Seven turbines bought by Solaris in the fourth quarter of 2026 provide 'over 200 MW'; my division, so a floor.",
    "source": "Solaris Energy Infrastructure, Form 10-Q to 30 September 2026",
    "url": "https://www.sec.gov/Archives/edgar/data/1697500/000162828026071604/sei-20260930.htm",
    "date": "2026-11-06"
   },
   "monthsToPower": {
    "value": [
     2,
     5
    ],
    "display": "2 to 5 months",
    "basis": "Solaris's 10-Q (filed 6 November 2026): seven turbines it has secured, over 200 MW, start running from the first quarter of 2027, 2 to 5 months later. My arithmetic; no order-to-power time is published.",
    "source": "Solaris Energy Infrastructure, Form 10-Q to 30 September 2026",
    "url": "https://www.sec.gov/Archives/edgar/data/1697500/000162828026071604/sei-20260930.htm",
    "date": "2026-11-06"
   },
   "costPerKW": {"value": 815, "display": "under US$815/kW (turbines only)", "short": "under US$815/kW (turbines only)", "basis": "Solaris paid about US$163.0m for seven turbines providing 'over 200 MW'; my division, so a ceiling. Turbine purchase price only, bought from private parties after the quarter: not an installed or new-build cost, and the fleet is rented to the user, not bought.", "source": "Solaris Energy Infrastructure, Form 10-Q to 30 September 2026", "url": "https://www.sec.gov/Archives/edgar/data/1697500/000162828026071604/sei-20260930.htm", "date": "2026-11-06"},
   "capacityFactor": {
    "display": "n/a",
    "basis": "No fleet capacity factor published.",
    "value": null
   },
   "fuelDays": {
    "value": 0,
    "display": "0 days",
    "basis": "Gas on a pipe: no fuel stored on site (spec rule: gas on a pipe = 0 days)."
   },
   "permitMonths": {
    "display": "n/a",
    "basis": "No permit time published for rented fleets.",
    "value": null
   },
   "bottleneck": {
    "value": null,
    "display": "3.2 GW already contracted",
    "basis": "Solaris capacity under long-term contracts (release of 4 November 2026): the fast lane is booked too.",
    "source": "Solaris Energy Infrastructure release (4 November 2026), as cited in the piece",
    "date": "2026-11-04"
   },
   "fuel": {
    "value": null,
    "display": "Natural gas",
    "basis": "Gas turbines it owns and rents out."
   },
   "elcc": {
    "value": 59,
    "display": "PJM ELCC 59% (gas CT class)",
    "basis": "PJM's rating of a gas combustion turbine for the 2029/30 capacity auction: the share of each MW it counts as firm. PJM rates turbines by class, not by frame or aeroderivative.",
    "source": "PJM, ELCC Class Ratings for the 2029/2030 Base Residual Auction",
    "date": "2026-08-07",
    "origin": "new"
   }
  },
  "ability": "Over 200 MW of bought turbines due to run from early 2027.",
  "weakness": "Its fleet is already booked: 3.2 GW under long-term contracts.",
  "drawing": "Cutaway of a rented power fleet: two gas turbines, each on a road trailer with its generator and exhaust stack, fed by one gas line and cabled together to the campus."
 },
 {
  "id": "solar",
  "role": "Daytime",
  "group": "sun",
  "name": "Utility solar farm",
  "examples": null,
  "makers": [
   "Intersect Power (developer)"
  ],
  "chapters": [
   {
    "slug": "solar-and-batteries",
    "anchor": "how-much-of-the-year-does-a-solar-farm-actually-produce"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": 150,
    "display": "150 MW (EIA reference plant)",
    "basis": "EIA's reference single-axis tracking solar plant, 150 MW AC, the same plant its cost figure is for. The biggest built for AI so far, Google and Intersect's Quantum in Texas, is 640 MW.",
    "source": "EIA / Sargent & Lundy, Capital Cost and Performance Characteristic Estimates for Utility Scale Electric Power Generating Technologies",
    "url": "https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2025.pdf",
    "date": "2024-01"
   },
   "monthsToPower": {
    "value": 24,
    "display": "24 months (EIA build time, before any grid queue)",
    "basis": "EIA modelling lead time for solar PV with tracking; excludes the interconnection queue.",
    "source": "EIA, Assumptions to the Annual Energy Outlook 2026, Electricity Market Module, Table 3",
    "url": "https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf",
    "date": "2026-04"
   },
   "costPerKW": {
    "value": 1484,
    "display": "US$1,484/kW (2025$)",
    "basis": "EIA's planning cost for a new solar PV with single-axis tracking, 2025 dollars, before its optimism factor. One table for every EIA-based card, so the costs compare like for like.",
    "source": "EIA, Assumptions to the Annual Energy Outlook 2026: Electricity Market Module, Table 3 (base overnight cost)",
    "url": "https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf",
    "date": "2026-04"
   },
   "capacityFactor": {
    "value": 24.0,
    "display": "24.0% (13.1% in December)",
    "basis": "US utility solar capacity factor, 2025; 31.9% in June and July, 13.1% in December.",
    "source": "EIA Electric Power Monthly, Table 6.07.B (23 October 2026)",
    "url": "https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_b",
    "date": "2026-10-23"
   },
   "fuelDays": {
    "display": "No purchased fuel",
    "basis": "Spec rule: solar has no purchased fuel (Fuel rating 99).",
    "value": Infinity
   },
   "permitMonths": {
    "display": "n/a",
    "basis": "No permit or interconnection-study time for solar is in the pieces or a primary record found.",
    "value": null
   },
   "bottleneck": {
    "value": null,
    "display": "14 MW per firm MW",
    "basis": "Megawatts of tracking solar needed for one firm megawatt on PJM's 2029/30 rating; the piece's arithmetic.",
    "source": "PJM ELCC ratings, piece's arithmetic",
    "date": "2026-08-07"
   },
   "fuel": {
    "value": null,
    "display": "None purchased",
    "basis": "No fuel bought."
   },
   "elcc": {
    "value": 7,
    "display": "PJM ELCC 7%",
    "basis": "PJM's rating of tracking solar for the 2029/30 auction (fixed solar 6%), down from 14% for 2025/26.",
    "source": "PJM, ELCC class ratings for the 2029/2030 Base Residual Auction",
    "date": "2026-08-07"
   }
  },
  "ability": "EIA's planning build time is two years, and there is no fuel to buy.",
  "weakness": "PJM counts tracking solar as 7 per cent of a firm megawatt.",
  "drawing": "Cutaway of a solar farm: rows of panels on single-axis trackers that follow the sun across the sky, an inverter, and an inset of one panel cut through to show the glass, silicon cells and backing."
 },
 {
  "id": "battery",
  "role": "Buffer",
  "group": "sun",
  "name": "Battery storage, grid scale",
  "examples": null,
  "makers": [
   "Intersect Power (developer)"
  ],
  "chapters": [
   {
    "slug": "solar-and-batteries",
    "anchor": "what-can-a-battery-cover-and-what-cant-it"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": 150,
    "display": "150 MW (4 hours, 600 MWh)",
    "basis": "EIA's reference lithium-ion battery: 150 MW, 600 MWh.",
    "source": "EIA / Sargent & Lundy, Capital Cost and Performance Characteristic Estimates for Utility Scale Electric Power Generating Technologies (study for AEO2025)",
    "url": "https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2025.pdf",
    "date": "2024-01-10"
   },
   "monthsToPower": {
    "value": 12,
    "display": "12 months (EIA build time, before any grid queue)",
    "basis": "EIA modelling lead time for four-hour lithium-ion battery storage; excludes the interconnection queue.",
    "source": "EIA, Assumptions to the Annual Energy Outlook 2026, Electricity Market Module, Table 3",
    "url": "https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf",
    "date": "2026-04"
   },
   "costPerKW": {
    "value": 1521,
    "display": "US$1,521/kW (2025$)",
    "basis": "EIA's planning cost for a new four-hour battery storage, 2025 dollars, before its optimism factor. One table for every EIA-based card, so the costs compare like for like.",
    "source": "EIA, Assumptions to the Annual Energy Outlook 2026: Electricity Market Module, Table 3 (base overnight cost)",
    "url": "https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf",
    "date": "2026-04"
   },
   "capacityFactor": {
    "display": "n/a",
    "basis": "Capacity factor does not describe a battery; see the PJM ELCC rating.",
    "value": null
   },
   "fuelDays": {
    "value": 0.167,
    "display": "4 hours (0.17 days)",
    "basis": "Duration of the standard grid battery, 4 hours, divided by 24 (spec rule).",
    "source": "Piece, citing EIA's planning model"
   },
   "permitMonths": {
    "display": "n/a",
    "basis": "No permit or interconnection-study time for batteries is in the pieces or found in a primary record.",
    "value": null
   },
   "bottleneck": {
    "value": null,
    "display": "Rating falls to 23% by 2035/36",
    "basis": "PJM's preliminary, non-binding four-hour battery rating for 2035/36, from 57% for 2029/30: each new battery counts for less.",
    "source": "PJM preliminary ELCC ratings (4 September 2026)",
    "date": "2026-09-04"
   },
   "fuel": {
    "value": null,
    "display": "Stored power",
    "basis": "Stores electricity made elsewhere; burns nothing."
   },
   "elcc": {
    "value": 57,
    "display": "PJM ELCC 57%",
    "basis": "PJM's rating of a four-hour battery for the 2029/30 auction; preliminary ratings fall to 42% for 2030/31, 23% by 2035/36 and 19% by 2042/43.",
    "source": "PJM, ELCC class ratings for the 2029/2030 Base Residual Auction",
    "date": "2026-08-07"
   }
  },
  "ability": "Builds in one year on EIA's planning assumptions.",
  "weakness": "PJM's preliminary rating falls from 57 to 23 per cent by 2035/36.",
  "drawing": "Cutaway of a grid battery: a container opened to show racks of battery modules and a cooling unit, then an inverter and a transformer that connect it to the grid."
 },
 {
  "id": "restart",
  "role": "Baseload",
  "group": "nuclear",
  "name": "Reactor restart",
  "examples": "Crane, Palisades, Duane Arnold",
  "makers": [
   "Constellation",
   "Holtec",
   "NextEra Energy"
  ],
  "chapters": [
   {
    "slug": "nuclear-for-ai",
    "anchor": "how-does-a-closed-reactor-come-back-to-life"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": [
     615,
     835
    ],
    "display": "615 to 835 MW",
    "basis": "The three US restarts: Crane 835 MW, Palisades about 800 MW, Duane Arnold 615 MW.",
    "source": "Owners' releases and NRC, as cited in the piece",
    "date": "2026-11-07"
   },
   "monthsToPower": {
    "value": [
     34,
     39
    ],
    "display": "34 to 39 months",
    "basis": "Crane: from Constellation's announcement and Microsoft contract (20 September 2024) to power in the second half of 2027; my arithmetic. Palisades, further along, has no date since its fuel loading stopped.",
    "source": "Constellation (20 September 2024, 6 August 2026), as cited in the piece",
    "date": "2026-08-06"
   },
   "costPerKW": {
    "value": 1900,
    "display": "about US$1,900/kW",
    "basis": "Crane: about US$1.6 billion invested over 835 MW, nominal dollars, my arithmetic. Palisades about US$2,275 (US$1.52bn DOE loan ceiling plus US$300m from Michigan, over 800 MW) and Duane Arnold up to about US$3,100 are funding ceilings, not costs.",
    "source": "Constellation, Holtec and NextEra, as cited in the piece",
    "date": "2026"
   },
   "capacityFactor": {
    "value": 91.1,
    "display": "91.1%",
    "basis": "US nuclear fleet capacity factor, 2025.",
    "source": "EIA Electric Power Monthly, Table 6.07.B (23 October 2026)",
    "url": "https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_b",
    "date": "2026-10-23"
   },
   "fuelDays": {
    "value": [
     548,
     730
    ],
    "display": "18 to 24 months",
    "basis": "Days between refuelling outages of a large water-cooled reactor, 18 to 24 months converted at 30.4 days a month.",
    "source": "Piece"
   },
   "permitMonths": {
    "value": 30,
    "display": "about 30 months",
    "basis": "Palisades' NRC restart path, first filing 1 February 2023 to approval 24 July 2025. Crane: filed November 2024, NRC target decision 4 March 2027 (about 28 months).",
    "source": "NRC, as cited in the piece",
    "date": "2025-07-24"
   },
   "bottleneck": {
    "value": null,
    "display": "Only three candidates",
    "basis": "Only three closed US reactors have restart applications; the grid place and repairs set each date (Palisades has none since fuel loading stopped).",
    "source": "NRC, as cited in the piece",
    "date": "2026-11-07"
   },
   "fuel": {
    "value": null,
    "display": "Uranium, ~5% LEU",
    "basis": "Ordinary reactor fuel."
   },
   "elcc": {
    "value": 96,
    "display": "PJM ELCC 96%",
    "basis": "PJM's rating of nuclear for the 2029/30 auction.",
    "source": "PJM, ELCC class ratings for the 2029/2030 Base Residual Auction",
    "date": "2026-08-07"
   }
  },
  "ability": "Crane costs about US$1,900 per kilowatt and runs on ordinary fuel.",
  "weakness": "Only three restarts exist, and Palisades has no date since fuel loading stopped.",
  "drawing": "Cutaway of a large water-cooled reactor plant: inside the containment, the reactor core, the pressuriser and a steam generator; steam goes to the turbine hall with its turbines, generator and condenser, and a cooling tower beside it."
 },
 {
  "id": "uprate",
  "role": "Top-up",
  "group": "nuclear",
  "name": "Reactor uprate",
  "examples": null,
  "makers": [
   "Constellation",
   "Vistra"
  ],
  "chapters": [
   {
    "slug": "nuclear-for-ai",
    "anchor": "what-is-an-uprate-and-why-is-it-the-cheapest-new-nuclear-megawatt"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": 78,
    "display": "about 78 MW an uprate",
    "basis": "NRC's list of expected applications: 31 uprates adding about 2,421 MW from late 2026 to 2032; my division. Historic average: 8,030 MW over 172 uprates, about 47 MW.",
    "source": "NRC expected applications list (8 September 2026), as cited in the piece",
    "date": "2026-09-08"
   },
   "monthsToPower": {
    "value": 26,
    "display": "up to 26 months (target, first MW)",
    "basis": "Google's 890 MW deal with Constellation, signed 6 October 2026: Constellation's first megawatts by 2028, i.e. within 26 months at most; the last before the end of 2032.",
    "source": "Constellation and Google (6 October 2026), as cited in the piece",
    "date": "2026-10-06"
   },
   "costPerKW": {
    "value": 4800,
    "display": "about US$4,800/kW",
    "basis": "Google's uprates at Constellation: more than US$4.3bn over 890 MW, nominal dollars, the piece's arithmetic. Byron and Braidwood: about US$5,100.",
    "source": "Constellation (6 October 2026), as cited in the piece",
    "date": "2026-10-06"
   },
   "capacityFactor": {
    "value": 91.1,
    "display": "91.1%",
    "basis": "US nuclear fleet capacity factor, 2025.",
    "source": "EIA Electric Power Monthly, Table 6.07.B (23 October 2026)",
    "url": "https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_b",
    "date": "2026-10-23"
   },
   "fuelDays": {
    "value": [
     548,
     730
    ],
    "display": "18 to 24 months",
    "basis": "Days between refuelling outages of a large water-cooled reactor, 18 to 24 months converted at 30.4 days a month.",
    "source": "Piece"
   },
   "permitMonths": {
    "value": [
     6,
     12
    ],
    "display": "6 to 12 months",
    "basis": "NRC review targets: 6 months for a measurement uncertainty recapture uprate, 9 for a stretch, 12 for an extended uprate (letter of 7 May 2024). Targets, not measured times.",
    "source": "NRC, Power Uprate Review Readiness",
    "url": "https://www.nrc.gov/reactors/operating/licensing/power-uprates/optimizepoweruprates",
    "date": "2026-10-29 (page reviewed)"
   },
   "bottleneck": {
    "value": null,
    "display": "None filed yet",
    "basis": "No AI-funded uprate had reached the NRC by September 2026; extended uprates also need the same transformers and generators as everyone else.",
    "source": "NRC, as cited in the piece",
    "date": "2026-09"
   },
   "fuel": {
    "value": null,
    "display": "Uranium, ~5% LEU",
    "basis": "Ordinary reactor fuel."
   },
   "elcc": {
    "value": 96,
    "display": "PJM ELCC 96%",
    "basis": "PJM's rating of nuclear for the 2029/30 auction.",
    "source": "PJM, ELCC class ratings for the 2029/2030 Base Residual Auction",
    "date": "2026-08-07"
   }
  },
  "ability": "The NRC aims to review an uprate in 6 to 12 months.",
  "weakness": "No AI-funded uprate had reached the NRC by September 2026.",
  "drawing": "The same reactor plant, with the parts an extended uprate replaces marked: the turbine, the generator and the pumps in the turbine hall."
 },
 {
  "id": "newreactor",
  "role": "Long game",
  "group": "nuclear",
  "name": "New reactor",
  "examples": "Kemmerer 1, Aurora, Hermes 2",
  "makers": [
   "TerraPower",
   "Oklo",
   "Kairos Power",
   "X-energy"
  ],
  "chapters": [
   {
    "slug": "nuclear-for-ai",
    "anchor": "why-do-the-advanced-reactors-wait-on-fuel"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": [
     50,
     345
    ],
    "display": "50 to 345 MW",
    "basis": "Kemmerer 1 (TerraPower Natrium) 345 MW, Oklo Aurora 75 MW, Kairos Hermes 2 up to 50 MW.",
    "source": "NRC and developers, as cited in the piece",
    "date": "2026-11-07"
   },
   "monthsToPower": {
    "value": [
     46,
     57
    ],
    "display": "46 to 57 months (target)",
    "basis": "Kemmerer 1: from its NRC construction permit (4 March 2026) to TerraPower's 2030 target; my arithmetic. Oklo targets 2028 to 2029 from groundbreaking in September 2025.",
    "source": "NRC and TerraPower, as cited in the piece",
    "date": "2026-03-04"
   },
   "costPerKW": {
    "value": 9800,
    "display": "about US$9,800/kW",
    "basis": "Vogtle 3 and 4 (AP1000, 2,234 MW), Georgia Power's own share net of the Toshiba payment and before financing, nominal; the only primary cost of a finished new US reactor in the pieces. No advanced reactor has a public cost. (Total to all owners about US$14,000/kW is a press figure.)",
    "source": "Southern Company Form 10-K for 2024, as cited in the piece",
    "date": "2025-02"
   },
   "capacityFactor": {
    "display": "n/a",
    "basis": "None of these designs is running; no capacity factor exists.",
    "value": null
   },
   "fuelDays": {"value": 730, "display": "24 months between refuellings (Natrium)", "short": "24 months (Natrium design)", "basis": "TerraPower: each Natrium reactor (Kemmerer 1) needs a refuelling outage every 24 months. Oklo's own target is for Aurora to run up to 10 years; Kairos designs its pebble-bed reactors to refuel while running. Designs and company targets, not operating records.", "source": "TerraPower, Application of Natrium Sodium Fast Reactor Plants to Supply Heat and Power to Industrial Facilities", "url": "https://www.terrapower.com/downloads/Process-Heat.pdf", "date": "2025-10-22"},
   "permitMonths": {
    "value": 23,
    "display": "about 23 months",
    "basis": "Kemmerer 1 construction permit: application submitted 28 March 2024 (NRC), permit 4 March 2026 per the piece; about 23 months, my arithmetic. NRC staff formally issued permit CPAR-1 on 9 March 2026 under Commission Order CLI-26-5. A construction permit, not an operating licence.",
    "source": "NRC, TerraPower Kemmerer Unit 1 application page; NRC release 'NRC Issues Construction Permit to US SFR Owner' (9 March 2026)",
    "url": "https://www.nrc.gov/reactors/new-reactors/advanced/who-were-working-with/applicant-projects/terrapower",
    "date": "2026-03-09"
   },
   "bottleneck": {
    "value": null,
    "display": "HALEU: 21 t against 40+ t",
    "basis": "DOE expects more than 40 tonnes of HALEU needed by 2030; its own stock reaches about 21.2 tonnes by 2028. America's only HALEU cascade has 16 centrifuges.",
    "source": "DOE Record of Decision (14 January 2025); DOE to GAO, GAO-26-107385 (20 August 2026), as cited in the piece",
    "date": "2026-08-20"
   },
   "fuel": {
    "value": null,
    "display": "HALEU (~19.75%)",
    "basis": "Kemmerer 1, Aurora and Hermes 2 all burn high-assay low-enriched uranium."
   },
   "elcc": {"value": 96, "display": "PJM ELCC 96% (nuclear class)", "short": "96% firm (nuclear class)", "basis": "PJM rates nuclear as one class; applied here to new reactors, none of which has yet run.", "source": "PJM, ELCC Class Ratings for the 2029/2030 Base Residual Auction", "url": "https://www.pjm.com/-/media/DotCom/planning/res-adeq/elcc/29-30-bra-elcc-class-ratings.pdf", "date": "2026-08-07"}
  },
  "ability": "Kemmerer 1 won its construction permit about 23 months after applying.",
  "weakness": "Needs HALEU: over 40 tonnes by 2030, against about 21 expected by 2028.",
  "drawing": "Cutaway of a sodium-cooled reactor with salt storage, as at Kemmerer 1: the core sits in a pool of liquid sodium, which heats salt held in a hot tank; the hot salt makes steam for a turbine and returns to a cold tank."
 },
 {
  "id": "micro",
  "role": "Prospect",
  "group": "micro",
  "name": "Microreactor",
  "examples": "Janus programme, Radiant Kaleidos, BWXT Pele",
  "makers": [
   "BWXT",
   "Radiant",
   "Westinghouse",
   "Antares",
   "General Atomics",
   "Aalo"
  ],
  "chapters": [
   {
    "slug": "microreactors",
    "anchor": "what-is-a-microreactor-and-how-small-is-small"
   }
  ],
  "stats": {
   "sizeMW": {
    "value": [
     1,
     20
    ],
    "display": "1 to 20 MW",
    "basis": "Typical microreactor output, megawatts electric (Idaho National Laboratory). Radiant Kaleidos 1 MWe, Pele 1.5 MWe, BWXT BANR 20 MWe.",
    "source": "Idaho National Laboratory (August 2024), as cited in the piece",
    "date": "2024-08"
   },
   "monthsToPower": {
    "value": 25,
    "display": "about 25 months (target)",
    "basis": "Army Janus programme: five companies chosen 26 August 2026, first reactor targeted for September 2028; my arithmetic. A target; Kaleidos has not yet run at power.",
    "source": "US Army, as cited in the piece",
    "date": "2026-08-26"
   },
   "costPerKW": {"value": [10825, 23592], "display": "US$10,825 to 23,592/kW (INL estimate)", "short": "US$10,800 to 23,600/kW (estimate)", "basis": "INL's overnight capital cost for its 20 MWth liquid-metal reference microreactor: US$23,592/kWe first of a kind, US$10,825/kWe mass-produced at ten a year. The design gives 6.2 MWe; the cost excludes fuel. A study estimate, not a vendor price; none has been built.", "source": "Idaho National Laboratory, MR Cost Basis Work Scope, 2025 Microreactor Program Review", "url": "https://gain.inl.gov/content/uploads/4/2025/03/02-Abdalla-Abou-Jaoude-MR-Cost-Basis-Work-Scope_2025-MRP-Review.pdf", "date": "2025-03"},
   "capacityFactor": {
    "display": "n/a",
    "basis": "No microreactor has run at power or sold electricity.",
    "value": null
   },
   "fuelDays": {
    "value": [
     1096,
     2922
    ],
    "display": "3 to 8 years unopened",
    "basis": "Design aim between refuellings, 3 to 8 years (Pele up to 3), converted at 365.25 days a year. Design targets, not operating records.",
    "source": "Piece"
   },
   "permitMonths": {
    "display": "n/a",
    "basis": "No microreactor holds an NRC operating licence. The Army regulates its own Janus reactors; an NRC microreactor rule proposed in May 2026 targets licences in six to twelve months but is not final.",
    "value": null
   },
   "bottleneck": {
    "value": null,
    "display": "TRISO: 0.7 t of uranium a year",
    "basis": "Nameplate US TRISO fuel capacity today (BWXT plus Standard Nuclear), the piece's arithmetic; HALEU itself is short too.",
    "source": "BWXT and Standard Nuclear, as cited in the piece",
    "date": "2026-11"
   },
   "fuel": {
    "value": null,
    "display": "HALEU TRISO",
    "basis": "Most designs burn uranium enriched to 19.75% in TRISO ceramic particles."
   },
   "elcc": {"value": 96, "display": "PJM ELCC 96% (nuclear class)", "short": "96% firm (nuclear class)", "basis": "PJM rates nuclear as one class; applied here to microreactors, none of which has yet run on a grid.", "source": "PJM, ELCC Class Ratings for the 2029/2030 Base Residual Auction", "url": "https://www.pjm.com/-/media/DotCom/planning/res-adeq/elcc/29-30-bra-elcc-class-ratings.pdf", "date": "2026-08-07"}
  },
  "ability": "Runs three to eight years unopened, then is refuelled in a factory.",
  "weakness": "First-of-a-kind power costs about 32.5 cents a kWh, against 8.6 industrial.",
  "drawing": "Cutaway of a gas-cooled microreactor: the core from above, hexagonal graphite blocks holding TRISO fuel inside a ring of control drums; beside it, the reactor and a helium turbine as modules on a trailer."
 }
];
