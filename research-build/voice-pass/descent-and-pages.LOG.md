# Voice pass: descent and fixed pages (16 Nov 2026)

Files edited: src/components/Descent.astro, src/data/stack.ts (STACK `what` / `constraint` only), src/pages/journal/[id].astro (article footer line).
Checked, no change needed: src/pages/map.astro, glossary.astro, numbers.astro (redirects, one plain link line), src/layouts/Base.astro (nav labels and footer already plain).
factlock.py PASS on all seven files; no em dashes; `npm run build` complete (225 pages).

## Before and after

1. Descent, chapter 1 card
   - Before: In Johor and Singapore, the right to draw that power, not the supply of chips, now decides who gets to build.
   - After: In Johor and Singapore, what decides who gets to build now isn't the chips, it's the right to draw that power.

2. Descent, equipment card
   - Before: Nothing switches on without them, and they are made in a handful of factories, so the grid cannot simply build its way out.
   - After: Nothing switches on without them, and they're made in a handful of factories. That's why the grid can't just build its way out.

3. Descent, turbine "What binds"
   - Before: Skipping the grid queue means joining the turbine makers' queue instead.
   - After: Basically, you skip the grid queue and join the turbine makers' queue instead.

4. Descent, battery "What binds"
   - Before: A four-hour battery reaches the evening, not the night, so buyers turn to power that runs all year.
   - After: A four-hour battery gets you through the evening but not the night. So buyers turn to power that runs all year.

5. Descent, microreactor card
   - Before: What paces them is the fuel, not the machine.
   - After: The machine isn't what holds them back, it's the fuel.

6. Descent, closing card (colon list removed)
   - Before: The grid, the machines at the gate, the turbines, the winter night and the reactors' fuel: each way to the next gigawatt for AI has a queue of its own. The slowest one sets the date.
   - After: Every way to the next gigawatt for AI has its own queue, whether it's the grid, the machines at the gate, the turbines, the winter night or the reactors' fuel. Basically, the slowest one sets the date.

7. Descent, winter-night label
   - Before: a four-hour battery reaches the evening; a December night lasts about fifteen hours
   - After: a four-hour battery gets you to the evening, but a December night lasts about fifteen hours

8. Descent, makers label
   - Before: Hitachi Energy, Siemens Energy and Eaton add factories only as orders justify
   - After: Hitachi Energy, Siemens Energy and Eaton only add factories when orders justify it

9. stack.ts, equipment constraint
   - Before: The makers add factories only as fast as signed orders justify, so the wait is kept, not cleared.
   - After: The makers only add factories as fast as signed orders justify, so the wait never really clears.

10. stack.ts, nuclear constraint
   - Before: Most new reactors need a richer fuel, HALEU, that America makes on one demonstration line.
   - After: Most new reactors need a richer fuel called HALEU, and America only makes it on one demonstration line.

11. stack.ts, grid constraint
   - Before: The wait for a connection now runs to years, and the grid decides who is served first.
   - After: The wait for a connection now runs to years, and it's the grid that decides who gets served first.

12. Article footer ([id].astro)
   - Before: If you think the argument is wrong, I would genuinely like to hear it:
   - After: If you think I've got this wrong, I'd genuinely like to hear it:

Also: "The problem is an AI data centre draws..." (winter-night card), "So builders skip the grid..." (power next door card), "comes in over" for "arrives over", semicolons split into two sentences in the stack strings. Headings, rail names, short labels and all numbers left as they were.

## Review (independent reviewer, 16 Nov)

Meaning fixes (old original / agent version / my fix):
1. about.astro: "That layer is where the physics is slow, the data is public, and the constraint is real. It is also the part that almost nobody explains in plain language." / "I think this layer matters because the physics is slow, the data is public and the constraint is real. And almost nobody explains it in plain English." (added "I think" and "because") / "This layer is where the physics is slow, the data is public and the constraint is real. It's also the part almost nobody explains in plain English."
2. stack.ts: "so the wait is kept, not cleared." / "so the wait never really clears." (harder claim) / "so the wait stays where it is instead of clearing."
3. stack.ts (nuclear next): "...and their fuel is the gate." / "...and the real gate is their fuel." ("the real" tell) / "...and the gate is their fuel."
Descent.astro, index.astro and config.ts: read against main, no meaning drift found; Descent has 2 "Basically", within the cap.
Checks: factlock PASS on all seven files, no em dash, build OK.
