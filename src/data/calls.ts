// ── The calls scorecard ──────────────────────────────────────────────────────
//
// The pitch itself (src/content/calls/<slug>.md) is fixed on the day it
// publishes and is never rewritten. This file is the only thing that moves:
// every two weeks, with Tommy's approval, each open call gets one dated mark.
// Nothing is ever deleted, right or wrong. A resolved call keeps every mark
// and gains a short dated post-mortem. See CALLS-SPEC.md.

export type Mark = {
  date: string;        // YYYY-MM-DD, the close the price is
  price: number;
  falsifier: string;   // one sentence: has anything in "wrong if" happened?
};

export type Resolution = {
  date: string;        // YYYY-MM-DD
  outcome: 'Right' | 'Wrong' | 'Mixed';
  postmortem: string;  // two or three sentences: what happened and what I learned
};

export type Score = {
  id: string;          // the pitch slug
  marks: Mark[];       // oldest first; the first refresh (6 Nov 2026) added the first one
  resolved?: Resolution;
};

export const SCORECARD_REFRESHED: string | null = '2026-11-06';   // YYYY-MM-DD of the last refresh

export const SCORES: Score[] = [
  { id: 'ajinomoto', marks: [{ date: '2026-11-05', price: 4872, falsifier: "Revisit not crossed: the shares sit between the ¥3,799 and ¥5,825 levels; first half results are due about 9 November 2026 and the Functional Materials tests fall due in May 2027." }] },
  { id: 'asml', marks: [{ date: '2026-11-05', price: 1250, falsifier: "Revisit crossed: the shares closed at or below about €1,475, which the note says points long, on 15 October 2026. No business test triggered: ASML said planned supply for 2027 and 2028 will not fully meet demand, and gave no cut to 2027 shipments and no 2028 order cover (results, 14 Oct 2026)." }] },
  { id: 'bloom-energy', marks: [{ date: '2026-11-05', price: 167.52, falsifier: "Triggered: the shares closed below US$200 on 23 October 2026, outside the band the note says proves it wrong, and below the US$210 revisit level. Third quarter non-GAAP product gross margin was 38.4 per cent, the first of the two quarters at 38 per cent or more that the revisit test needs (results, 22 Oct 2026)." }] },
  { id: 'broadcom', marks: [{ date: '2026-11-05', price: 291.53, falsifier: "Not triggered: the shares are above the US$270 level in the test, no cut to the fiscal 2027 AI revenue outlook has been announced and no Backstop payment has been reported; fourth quarter results are due about 10 December 2026." }] },
  { id: 'caterpillar', marks: [{ date: '2026-11-05', price: 553.64, falsifier: "Revisit not crossed: the shares are above about US$520. No business test triggered: the backlog rose to a record in the third quarter, and 2026 Power Generation sales are due on 2 February 2027." }] },
  { id: 'clp-holdings', marks: [{ date: '2026-11-05', price: 80, falsifier: "Revisit not crossed: the shares are above about HK$68.80 and no addition to the Development Plan has been approved; Hong Kong earnings for 2026 come with the annual results in late February 2027." }] },
  { id: 'coherent', marks: [{ date: '2026-11-05', price: 169.76, falsifier: "Not triggered: first quarter non-GAAP gross margin was 40.6 per cent, with 40 to 42 per cent guided for the second quarter and fiscal 2027 pro forma revenue growth expected above 60 per cent (results, 4 Nov 2026)." }] },
  { id: 'constellation', marks: [{ date: '2026-11-05', price: 239.65, falsifier: "Revisit crossed: the shares closed below about US$253 on 4 November 2026. No business test triggered: third quarter results are due about 9 November 2026, full year 2026 earnings in February 2027, and Crane is still targeted for 2027." }] },
  { id: 'corning', marks: [{ date: '2026-11-05', price: 103.43, falsifier: "Triggered: the shares closed below US$110 on 5 November 2026, outside the band the note says proves it wrong, after crossing the US$127 revisit level on 22 October. Third quarter Optical Communications sales were US$2,379 million, up 44 per cent, at a segment net margin of 22.4 per cent (results, 27 Oct 2026)." }] },
  { id: 'eaton', marks: [{ date: '2026-11-05', price: 327.02, falsifier: "Not triggered: third quarter Electrical Americas operating margin was 29.8 per cent, up 2.3 points on the second quarter, and the 2026 adjusted earnings guide rose to US$13.70 to US$13.80 (results, 3 Nov 2026)." }] },
  { id: 'entergy', marks: [{ date: '2026-11-05', price: 110.3, falsifier: "Revisit not crossed: the shares are above US$106.57. No business test triggered: Entergy Louisiana settled with commission staff on the second Meta agreement, with the commission's vote still pending, and the 2026 adjusted earnings guide is US$4.35 to US$4.45 (results, 2 Nov 2026)." }] },
  { id: 'ge-vernova', marks: [{ date: '2026-11-05', price: 770.51, falsifier: "Revisit crossed: the shares closed below about US$910 on 19 October 2026. No business test triggered: gas backlog and slot reservations rose to 122 gigawatts from 116 in June, and the full year adjusted EBITDA margin guide rose to 13.5 to 14.5 per cent (results, 28 Oct 2026)." }] },
  { id: 'hitachi', marks: [{ date: '2026-11-05', price: 4772, falsifier: "Revisit crossed: the shares closed below about ¥5,600 on 23 October 2026. No business test triggered: Hitachi raised its fiscal 2026 forecast for Hitachi Energy's adjusted EBITA margin to 15.7 per cent from 14.8 per cent, and the backlog rose to US$66.9 billion (results, 28 Oct 2026)." }] },
  { id: 'infineon', marks: [{ date: '2026-11-05', price: 45.95, falsifier: "Revisit crossed: the shares closed below about €48, which the note says would make it long, on 5 November 2026. The other revisit test, the fiscal 2027 AI revenue guide, comes with fiscal 2026 results on 10 November 2026." }] },
  { id: 'kinder-morgan', marks: [{ date: '2026-11-05', price: 30.19, falsifier: "Revisit not crossed, but close: the shares are less than 1 per cent above about US$30. No business test triggered: Permian Link is still expected in service in the third quarter of 2030 and the Southeast Connector from the fourth quarter of 2030 (results, 21 Oct 2026)." }] },
  { id: 'lumentum', marks: [{ date: '2026-11-05', price: 509.7, falsifier: "Triggered: the shares closed below US$750 on 2 November 2026, outside the band the note says proves it wrong, after crossing the US$860 revisit level on 16 October. That day Lumentum agreed to be bought by Marvell for 4.5 Marvell shares each, and reported a September quarter GAAP gross margin of 51.0 per cent (results and merger release, 2 Nov 2026)." }] },
  { id: 'marvell', marks: [{ date: '2026-11-05', price: 133.55, falsifier: "Triggered: the shares closed below US$230 on 16 October 2026, which the note says proves the call wrong. On 2 November Marvell agreed to buy Lumentum for 4.5 Marvell shares each, with completion expected in the first half of 2028, and said third quarter revenue was in line with its guidance (merger release, 2 Nov 2026)." }] },
  { id: 'micron', marks: [{ date: '2026-11-05', price: 656.39, falsifier: "Revisit crossed: the shares closed at or below about US$726, which the note says points long, on 5 November 2026. No business test can be read before results for the quarter to November, due in December 2026." }] },
  { id: 'mitsubishi-heavy', marks: [{ date: '2026-11-05', price: 3052, falsifier: "Revisit crossed: the shares closed below about ¥3,200 on 5 November 2026. No business test triggered yet: MHI booked 19 large frame gas turbines in the first half, and cut its fiscal 2026 Energy Systems margin forecast to 14.3 per cent from 15.5 per cent, against a 14 per cent test (results, 6 Nov 2026)." }] },
  { id: 'nebius', marks: [{ date: '2026-11-05', price: 120.37, falsifier: "Revisit crossed: the shares closed below about US$185 on 16 October 2026. No business test can be read yet; third quarter results are due on 12 November 2026." }] },
  { id: 'nvidia', marks: [{ date: '2026-11-05', price: 181.6, falsifier: "Not yet testable: Nvidia reports its October quarter on 17 November 2026, and it has disclosed no payment under its land, power and shell guarantees." }] },
  { id: 'oklo', marks: [{ date: '2026-11-05', price: 19.2, falsifier: "Target reached: the shares closed below the US$28 target on 16 October 2026. Not triggered: Oklo has disclosed no binding power purchase agreement of 500 MW or more and no Aurora-INL cost per kilowatt; third quarter results are due on 6 November 2026." }] },
  { id: 'samsung-electronics', marks: [{ date: '2026-11-05', price: 201500, falsifier: "Not yet testable: no results since the call; the fourth quarter results and the final 2026 shareholder return are both due in late January 2027." }] },
  { id: 'schneider-electric', marks: [{ date: '2026-11-05', price: 227.85, falsifier: "Revisit crossed: the shares closed at or below about €242 on 22 October 2026. No business test triggered: third quarter organic growth was 16.9 per cent with Systems at 35 per cent of revenue, and the full year organic growth target rose to 12 to 14 per cent (revenues, 16 Oct 2026)." }] },
  { id: 'seagate', marks: [{ date: '2026-11-05', price: 466.53, falsifier: "Revisit not crossed, but close: the shares are about 1 per cent above the US$460 level that points long. No business test can be read before second quarter results, expected in late January 2027." }] },
  { id: 'siemens-energy', marks: [{ date: '2026-11-05', price: 113.84, falsifier: "Not yet testable: the three business tests use fiscal 2027 figures, due in November 2027, and the shares have not closed a month below €105; fiscal 2026 results are due on 11 November 2026." }] },
  { id: 'sk-hynix', marks: [{ date: '2026-11-05', price: 1.264e+06, falsifier: "Not yet testable: no results since the call; the fourth quarter and full year 2026 free cash flow are due in late January 2027." }] },
  { id: 'spacex', marks: [{ date: '2026-11-05', price: 123.62, falsifier: "Revisit not crossed: the shares sit between about US$98 and US$150, and SpaceX has disclosed no compute satellite in service; the revenue test uses 2027, reported in early 2028." }] },
  { id: 'texas-instruments', marks: [{ date: '2026-11-05', price: 278.15, falsifier: "Revisit not crossed: the shares are above about US$244. Not triggered: third quarter gross margin was 64.2 per cent, below the 65 per cent test (results, 21 Oct 2026)." }] },
  { id: 'tsmc', marks: [{ date: '2026-11-05', price: 353.1, falsifier: "Revisit crossed: the ADR closed below about US$400 on 2 November 2026. No business test triggered: TSMC left its through the cycle gross margin floor at 56 per cent at the third quarter results, which showed a 66.4 per cent gross margin (results, 15 Oct 2026)." }] },
  { id: 'vertiv', marks: [{ date: '2026-11-05', price: 176.73, falsifier: "Not triggered: third quarter adjusted operating margin was 25.2 per cent, up 2.9 points on a year earlier, and the full year adjusted EPS guide rose to US$7.10 to US$7.20 (results, 28 Oct 2026)." }] },
  { id: 'wartsila', marks: [{ date: '2026-11-05', price: 24.94, falsifier: "Not yet testable: both business tests use 2027 figures, and the shares have not closed a month below €20; the 2026 full year report is due on 5 February 2027." }] },
  { id: 'williams', marks: [{ date: '2026-11-05', price: 64.25, falsifier: "Revisit crossed: the shares closed below about US$67.60 on 5 November 2026. No business test triggered: Williams says 2026 Adjusted EBITDA is tracking toward the upper half of its US$8.3 to US$8.5 billion guide (results, 2 Nov 2026)." }] },
];

// Coverage was launched in sector batches. The research table groups notes by
// launch (dates inclusive, Singapore time); a note outside every launch is
// grouped by its month. Each note keeps its own publication date and price.
export type Launch = { from: string; to: string; title: string };
export const LAUNCHES: Launch[] = [
  { from: '2026-10-06', to: '2026-10-09', title: 'Launch of coverage' },
  { from: '2026-10-22', to: '2026-10-30', title: 'Grid equipment and nuclear' },
  { from: '2026-11-02', to: '2026-11-02', title: 'Second wave' },
];

export const scoreOf = (id: string) => SCORES.find((s) => s.id === id);
