"""Content for the FMA Chapter 6 (Inventories) class-test guide.

Exam-oriented: the rules in one screen, then every example from the ch06-FA deck solved
step by step, then the two assignment problems. Figures recomputed and cross-checked
against the deck's own illustrations.
"""

table = None  # injected by build.py

HERO = """
<header class="hero">
  <h1>FMA Chapter 6: Inventories</h1>
  <p>Rules on one screen, every slide example solved, both assignment problems worked.</p>
  <div class="chips">
    <span class="chip">Rules cheat sheet</span>
    <span class="chip">6 slide examples solved</span>
    <span class="chip">P6.5A + P6.8A solved</span>
    <span class="chip">Quiz</span>
  </div>
</header>
"""


def svg(w, h, inner, cap=None, label="diagram"):
    arrow = ('<defs><marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
             'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--muted)"/></marker></defs>')
    c = f'<div class="cap">{cap}</div>' if cap else ""
    return f'<div class="figwrap"><svg viewBox="0 0 {w} {h}" role="img" aria-label="{label}">{arrow}{inner}</svg>{c}</div>'


def box(x, y, w, h, cls, lines):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="{cls}"/>']
    n = len(lines)
    for i, ln in enumerate(lines):
        ty = y + h / 2 + (i - (n - 1) / 2) * 16 + 4
        out.append(f'<text x="{x + w/2}" y="{ty:.0f}" text-anchor="middle" class="{"t-b" if i == 0 else "t-s"}">{ln}</text>')
    return "".join(out)


def arrow(x1, y1, x2, y2):
    return f'<path d="M{x1},{y1} L{x2},{y2}" class="ar"/>'


def qa(tag, q, a):
    return (f'<details class="qa" data-tag="{tag}"><summary>{q}<span class="tag">{tag}</span></summary>'
            f'<div class="a">{a}</div></details>')


# ---------------------------------------------------------------- sections
def s_cheat():
    return """
<h2><small>One screen</small>Rules and formulas</h2>
<div class="formula">Beginning inventory + Purchases = Cost of goods available for sale<br>
Cost of goods available for sale − Ending inventory = Cost of goods sold<br>
Net sales − Cost of goods sold = Gross profit &nbsp;·&nbsp; Gross profit ÷ Net sales = Gross profit rate</div>
<h3>The four costing methods</h3>
""" + table(["Method", "Rule", "Ending inventory holds"], [
        ["Specific identification", "cost each actual unit sold", "the actual units left (rare in practice)"],
        ["FIFO", "earliest costs → cost of goods sold", "newest costs (<b>LISH</b>: last in still here)"],
        ["LIFO", "latest costs → cost of goods sold", "oldest costs (<b>FISH</b>: first in still here)"],
        ["Average-cost", "one weighted-average unit cost = cost available ÷ units available", "units × that average"],
    ]) + """
<h3>Rising prices</h3>
""" + table(["", "FIFO", "LIFO", "Average"], [
        ["Ending inventory", "highest", "lowest", "middle"],
        ["Cost of goods sold", "lowest", "highest", "middle"],
        ["Gross profit / net income", "highest", "lowest", "middle"],
        ["Income tax", "highest", "<b>lowest</b>", "middle"],
    ]) + """
<h3>Inventory errors</h3>
""" + table(["Error", "Cost of goods sold", "Net income"], [
        ["Beginning inventory understated", "understated", "overstated"],
        ["Beginning inventory overstated", "overstated", "understated"],
        ["Ending inventory understated", "overstated", "understated"],
        ["Ending inventory overstated", "understated", "overstated"],
    ]) + """
<p>Balance sheet: assets and equity move with the ending-inventory error; liabilities never. Error reverses next period.</p>
<h3>Ownership, classification, disclosure</h3>
<ul>
<li><b>FOB shipping point</b> → buyer owns goods in transit. <b>FOB destination</b> → seller owns them.</li>
<li><b>Consigned goods</b> stay with the consignor; the holder never counts them.</li>
<li>Merchandiser: one <b>Inventory</b> account. Manufacturer: <b>raw materials, work in process, finished goods</b>. All current assets.</li>
<li>Cost = all expenditures to acquire the goods and make them ready for sale.</li>
<li>Disclose: classifications, basis of accounting, costing method. LIFO for tax ⇒ LIFO for reporting (<b>conformity rule</b>).</li>
<li>Perpetual: records update at every sale. Periodic: only at period end. <b>FIFO gives the same answer in both</b>; LIFO and average do not.</li>
</ul>
<div class="box say"><b>Answer shape</b>units + cost available → units left → cost them by the method → available − ending = COGS → net sales − COGS = gross profit.</div>
"""


def s_ex_own():
    return """
<h2><small>Slide example 1</small>Hasbeen Company: what to count</h2>
<p><b>DO IT! LO 1.</b> Count $200,000. (1) It included $15,000 of goods held on
consignment for Falls Co. (2) It left out $10,000 of purchased goods in transit, FOB shipping point. (3) It left
out goods it had sold, costing $12,000, in transit FOB shipping point.</p>
""" + table(["Item", "Rule", "Action"], [
        ["1. Consigned goods $15,000", "consignee never owns them", "<b>deduct 15,000</b>"],
        ["2. Purchases in transit $10,000, FOB shipping point", "title passed to Hasbeen when the carrier took them", "<b>add 10,000</b>"],
        ["3. Sales in transit $12,000, FOB shipping point", "title already passed to the customer", "<b>no change</b> (correctly excluded)"],
    ]) + """
<div class="formula">$200,000 − $15,000 + $10,000 = <b>$195,000</b></div>
"""


def s_ex_spec():
    return """
<h2><small>Slide example 2</small>Crivitz TV: specific identification</h2>
<p>Three identical TVs at $700 (Feb 3), $750 (Mar 5), $800 (May 22). Two sold at $1,200 each: the Feb 3 and May 22 sets.</p>
""" + table(["", "Working", "Answer"], [
        ["Cost of goods sold", "$700 + $800", "<b>$1,500</b>"],
        ["Ending inventory", "the March 5 set", "<b>$750</b>"],
        ["Gross profit", "(2 × $1,200) − $1,500", "<b>$900</b>"],
    ]) + """
<div class="box trap"><b>Why it matters</b>Choose the other two sets and the profit changes, so this method fits identifiable units only.</div>
"""


def s_ex_periodic():
    return """
<h2><small>Slide example 3</small>Houston Electronics: periodic FIFO, LIFO, average</h2>
""" + table(["Date", "Explanation", "Units", "Unit cost", "Total cost"], [
        ["Jan. 1", "Beginning inventory", "100", "$10", "$1,000"],
        ["Apr. 15", "Purchase", "200", "11", "2,200"],
        ["Aug. 24", "Purchase", "300", "12", "3,600"],
        ["Nov. 27", "Purchase", "400", "13", "5,200"],
        (["", "<b>Available for sale</b>", "<b>1,000</b>", "", "<b>$12,000</b>"], "tot"),
        ["", "Units sold", "550", "", ""],
        ["", "Ending inventory", "450", "", ""],
    ], num=(2, 3, 4)) + """
<h3>FIFO: newest costs stay</h3>
""" + table(["Ending inventory", "", "Cost of goods sold", ""], [
        ["400 @ $13", "$5,200", "Available for sale", "$12,000"],
        ["50 @ $12", "600", "Less ending inventory", "5,800"],
        (["<b>Total</b>", "<b>$5,800</b>", "<b>Cost of goods sold</b>", "<b>$6,200</b>"], "tot"),
    ], num=(1, 3)) + """
<h3>LIFO: oldest costs stay</h3>
""" + table(["Ending inventory", "", "Cost of goods sold", ""], [
        ["100 @ $10", "$1,000", "Available for sale", "$12,000"],
        ["200 @ $11", "2,200", "Less ending inventory", "5,000"],
        ["150 @ $12", "1,800", "", ""],
        (["<b>Total</b>", "<b>$5,000</b>", "<b>Cost of goods sold</b>", "<b>$7,000</b>"], "tot"),
    ], num=(1, 3)) + """
<h3>Average-cost</h3>
""" + table(["Step", "Working", "Answer"], [
        ["Weighted-average unit cost", "$12,000 ÷ 1,000 units", "<b>$12.00</b>"],
        ["Ending inventory", "450 × $12.00", "<b>$5,400</b>"],
        ["Cost of goods sold", "$12,000 − $5,400", "<b>$6,600</b>"],
    ]) + """
<div class="box trap"><b>Marks lost here</b>Average is <b>not</b> (10+11+12+13) ÷ 4 = $11.50. Total cost ÷ total units.</div>
"""


def s_ex_effects():
    return """
<h2><small>Slide example 4</small>Houston Electronics: the three income statements</h2>
<p>Same data, tax rate 30%. Learn the shape: only ending inventory changes, and everything below it follows.</p>
""" + table(["", "FIFO", "LIFO", "Average"], [
        ["Sales revenue", "$18,500", "$18,500", "$18,500"],
        ["Beginning inventory", "1,000", "1,000", "1,000"],
        ["Purchases", "11,000", "11,000", "11,000"],
        ["Cost of goods available for sale", "12,000", "12,000", "12,000"],
        ["Ending inventory", "<b>5,800</b>", "<b>5,000</b>", "<b>5,400</b>"],
        ["Cost of goods sold", "6,200", "7,000", "6,600"],
        (["Gross profit", "12,300", "11,500", "11,900"], "sub"),
        ["Operating expenses", "9,000", "9,000", "9,000"],
        ["Income before income taxes", "3,300", "2,500", "2,900"],
        ["Income tax expense (30%)", "990", "750", "870"],
        (["<b>Net income</b>", "<b>$2,310</b>", "<b>$1,750</b>", "<b>$2,030</b>"], "tot"),
    ], num=(1, 2, 3)) + """
<p><b>If asked to comment:</b> with rising prices FIFO gives the highest net income and an ending inventory near current cost, LIFO the lowest net income and the lowest tax, with ending inventory understated.</p>
"""


def s_ex_error():
    return """
<h2><small>Slide example 5</small>Visual Company: an inventory error</h2>
<p><b>DO IT! LO 3.</b> 2016 ending inventory overstated by $22,000.</p>
""" + table(["", "2016", "2017"], [
        ["Ending inventory", "<b>$22,000 overstated</b>", "no effect"],
        ["Cost of goods sold", "<b>$22,000 understated</b>", "<b>$22,000 overstated</b>"],
        ["Stockholders' equity", "<b>$22,000 overstated</b>", "no effect"],
    ]) + """
<p>2016 ending inventory = 2017 beginning inventory → cost of goods sold overstated in 2017; the two years cancel.</p>
"""


def s_ex_perpetual():
    return """
<h2><small>Slide example 6</small>Appendix 6A: the same data, perpetual</h2>
<p>Sale of 550 now falls on 9/10, <b>before</b> the 11/27 purchase, so each sale uses only the layers on hand then.</p>
""" + table(["Date", "Explanation", "Units", "Unit cost", "Balance in units"], [
        ["1/1", "Beginning inventory", "100", "$10", "100"],
        ["4/15", "Purchase", "200", "11", "300"],
        ["8/24", "Purchase", "300", "12", "600"],
        ["9/10", "<b>Sale</b>", "550", "", "50"],
        ["11/27", "Purchase", "400", "13", "450"],
    ], num=(2, 3, 4)) + """
<h3>FIFO</h3>
""" + table(["Date", "Cost of goods sold", "Balance"], [
        ["9/10", "(100 @ $10) + (200 @ $11) + (250 @ $12) = <b>$6,200</b>", "(50 @ $12) $600"],
        ["11/27", "", "(50 @ $12) (400 @ $13) <b>$5,800</b>"],
    ]) + """
<h3>LIFO</h3>
""" + table(["Date", "Cost of goods sold", "Balance"], [
        ["9/10", "(300 @ $12) + (200 @ $11) + (50 @ $10) = <b>$6,300</b>", "(50 @ $10) $500"],
        ["11/27", "", "(50 @ $10) (400 @ $13) <b>$5,700</b>"],
    ]) + """
<h3>Moving-average</h3>
""" + table(["Date", "Purchases", "Cost of goods sold", "Balance (units and cost)"], [
        ["1/1", "", "", "(100 @ $10) $1,000"],
        ["4/15", "(200 @ $11) $2,200", "", "(300 @ $10.667) $3,200"],
        ["8/24", "(300 @ $12) $3,600", "", "(600 @ $11.333) $6,800"],
        ["9/10", "", "(550 @ $11.333) <b>$6,233</b>", "(50 @ $11.333) $567"],
        ["11/27", "(400 @ $13) $5,200", "", "(450 @ $12.816) <b>$5,767</b>"],
    ]) + """
""" + table(["Method", "Periodic", "Perpetual", "Same?"], [
        ["FIFO", "COGS 6,200 · EI 5,800", "COGS 6,200 · EI 5,800", "<b>yes</b>"],
        ["LIFO", "COGS 7,000 · EI 5,000", "COGS 6,300 · EI 5,700", "no"],
        ["Average", "COGS 6,600 · EI 5,400", "COGS 6,233 · EI 5,767", "no"],
    ]) + """
<div class="box trap"><b>Trick question</b>Same under both systems = <b>FIFO</b>. New average only after a purchase, never after a sale.</div>
"""


def s_slide_mcq():
    return """
<h2><small>Straight from the slides</small>The four questions in the deck</h2>
""" + table(["Question", "Answer"], [
        ["Goods in transit should be included in the inventory of the buyer when…", "the terms of sale are <b>FOB shipping point</b> (the public carrier accepts the goods from the seller)"],
        ["The cost flow method that often parallels the actual physical flow of merchandise is…", "<b>FIFO</b>"],
        ["In a period of inflation, the cost flow method that results in the lowest income taxes is…", "<b>LIFO</b>"],
        ["Understating ending inventory will overstate…", "<b>cost of goods sold</b> (assets, net income and equity are understated)"],
    ])


def s_problems():
    return """
<h2><small>Assignment</small>P6.5A and P6.8A, solved</h2>
<h3>P6.5A: Koetteritz Inc., June 2020 (periodic)</h3>
""" + table(["Item", "Units", "Cost"], [
        ["Beginning inventory 40 @ $40", "40", "$1,600"],
        ["Purchase 135 @ $43", "135", "5,805"],
        ["Purchase 55 @ $46", "55", "2,530"],
        ["Purchase return 10 @ $46", "(10)", "(460)"],
        ["Purchase 35 @ $50", "35", "1,750"],
        (["<b>Available for sale</b>", "<b>255</b>", "<b>$11,225</b>"], "tot"),
        ["Units sold (110 − 15 + 65)", "(160)", ""],
        ["<b>Ending inventory</b>", "<b>95</b>", ""],
    ], num=(1, 2)) + """
<p><b>Net sales</b> = (110 × $70) − (15 × $70) + (65 × $76) = <b>$11,590</b></p>
""" + table(["", "LIFO", "FIFO", "Average"], [
        ["Ending inventory, 95 units", "40@40 = 1,600<br>55@43 = 2,365", "35@50 = 1,750<br>45@46 = 2,070<br>15@43 = 645", "11,225 ÷ 255 = 44.02<br>95 × 44.02"],
        (["<b>(i) Ending inventory</b>", "<b>$3,965</b>", "<b>$4,465</b>", "<b>$4,181.90</b>"], "sub"),
        ["<b>(ii) Cost of goods sold</b>", "$7,260", "$6,760", "$7,043.10"],
        ["<b>(iii) Gross profit</b>", "$4,330", "$4,830", "$4,546.90"],
        (["<b>(iv) Gross profit rate</b>", "<b>37.4%</b>", "<b>41.7%</b>", "<b>39.2%</b>"], "tot"),
    ], num=(1, 2, 3)) + """
<h3>P6.8A: Dempsey Inc., January 2020 (perpetual)</h3>
<p>Available 310 units / $5,460 · units sold 190 · ending inventory 120 units ·
net sales = (110 × $28) − (10 × $28) + (90 × $32) = <b>$5,680</b></p>
<h4>LIFO</h4>
""" + table(["Date", "Cost of goods sold", "Balance (units and cost)"], [
        ["Jan. 8", "(110 @ $18) $1,980", "(100 @ $15) (30 @ $18) $2,040"],
        ["Jan. 10 <i>sale return</i>", "(10 @ $18) ($180)", "(100 @ $15) (40 @ $18) $2,220"],
        ["Jan. 15 purchase 55 @ $20", "", "… (55 @ $20) $3,320"],
        ["Jan. 16 <i>purchase return</i>", "", "(100 @ $15) (40 @ $18) (50 @ $20) $3,220"],
        ["Jan. 20", "(50 @ $20) + (40 @ $18) = $1,720", "(100 @ $15) $1,500"],
        ["Jan. 25 purchase 20 @ $22", "", "(100 @ $15) (20 @ $22) $1,940"],
        (["<b>(i) COGS $3,520</b>", "<b>(iii) Gross profit $2,160</b>", "<b>(ii) Ending inventory $1,940</b>"], "tot"),
    ]) + """
<h4>FIFO</h4>
""" + table(["Date", "Cost of goods sold", "Balance (units and cost)"], [
        ["Jan. 8", "(100 @ $15) + (10 @ $18) = $1,680", "(130 @ $18) $2,340"],
        ["Jan. 10 <i>sale return</i>", "(10 @ $18) ($180)", "(140 @ $18) $2,520"],
        ["Jan. 20", "(90 @ $18) $1,620", "(50 @ $18) (50 @ $20) $1,900"],
        ["Jan. 25 purchase 20 @ $22", "", "(50 @ $18) (50 @ $20) (20 @ $22) $2,340"],
        (["<b>(i) COGS $3,120</b>", "<b>(iii) Gross profit $2,560</b>", "<b>(ii) Ending inventory $2,340</b>"], "tot"),
    ]) + """
<h4>Moving-average (unit cost to 3 decimals)</h4>
""" + table(["Date", "Event", "Cost of goods sold", "Balance"], [
        ["Jan. 5", "purchase 140 @ $18", "", "(240 @ $16.750) $4,020.00"],
        ["Jan. 8", "sale 110", "$1,842.50", "(130 @ $16.750) $2,177.50"],
        ["Jan. 10", "sale return 10", "($167.50)", "(140 @ $16.750) $2,345.00"],
        ["Jan. 15", "purchase 55 @ $20", "", "(195 @ $17.667) $3,445.00"],
        ["Jan. 16", "purchase return 5", "", "(190 @ $17.605) $3,345.00"],
        ["Jan. 20", "sale 90", "$1,584.45", "(100 @ $17.605) $1,760.55"],
        ["Jan. 25", "purchase 20 @ $22", "", "(120 @ $18.338) $2,200.55"],
        (["", "", "<b>(i) COGS $3,259.45</b>", "<b>(ii) Ending inventory $2,200.55</b>"], "tot"),
    ]) + """
<p>(iii) Gross profit = $5,680 − $3,259.45 = <b>$2,420.55</b> ($2,421 rounded).</p>
<div class="box say"><b>One-line check</b>Cost of goods sold + ending inventory = cost of goods available for
sale: 3,520 + 1,940 = 3,120 + 2,340 = 3,259.45 + 2,200.55 = <b>$5,460</b>.</div>
"""


QA = [
    ("rules", "Define cost of goods available for sale.", "Beginning inventory plus purchases: everything the business could have sold during the period."),
    ("rules", "What is included in the cost of inventory?", "All expenditures necessary to acquire the goods and put them in a condition ready for sale."),
    ("rules", "FIFO in one line.", "The costs of the earliest goods purchased are the first charged to cost of goods sold, so the newest costs stay in ending inventory."),
    ("rules", "LIFO in one line.", "The costs of the latest goods purchased are charged to cost of goods sold first, so the oldest costs stay in ending inventory."),
    ("rules", "How is the weighted-average unit cost found?", "Cost of goods available for sale ÷ total units available for sale. In the Houston example, $12,000 ÷ 1,000 = $12.00."),
    ("rules", "Must the cost flow assumption match the physical flow?", "No. Only specific identification follows actual units."),
    ("rules", "Which method gives the lowest tax when prices rise, and why?", "LIFO: the newest and dearest costs go to cost of goods sold, so net income and tax are lowest."),
    ("rules", "What is the LIFO conformity rule?", "A company using LIFO for tax purposes must also use LIFO in its financial statements."),
    ("rules", "Who includes goods in transit?", "Whoever holds legal title. FOB shipping point: the buyer, from the moment the carrier accepts the goods. FOB destination: the seller, until delivery."),
    ("rules", "Who counts consigned goods?", "The consignor, who still owns them. The consignee holds them to sell for a fee but never owns them."),
    ("rules", "What must be disclosed about inventory?", "The major classifications, the basis of accounting, and the costing method used."),
    ("errors", "Ending inventory is understated. What happens?", "Cost of goods sold is overstated; net income, assets and stockholders' equity are understated."),
    ("errors", "Why do inventory errors affect two periods?", "This year's ending inventory is next year's beginning inventory, so the error reverses and the two years together are correct."),
    ("6A", "Which method is identical under periodic and perpetual?", "FIFO. LIFO and average-cost differ, because a perpetual sale can only use the layers on hand at that moment."),
    ("6A", "When is a new moving average computed?", "After every purchase and after a purchase return, never after a sale."),
    ("6A", "In a perpetual system, how is a sales return recorded?", "The goods go back into inventory at the cost they were charged out at, and cost of goods sold is reduced by that amount."),
    ("problems", "P6.5A: how are the returns handled?", "The purchase return cuts units and cost available for sale (10 units, $460). The sales return cuts units sold and sales (15 units, $1,050), leaving net sales of $11,590 and 160 units sold."),
    ("problems", "P6.8A: fastest check on the three answers?", "Cost of goods sold plus ending inventory must equal $5,460 under every method, with net sales fixed at $5,680."),
]


def s_qa():
    return ("""
<h2><small>Rapid fire</small>Short answers</h2>
<div class="filters" id="qa-filters"></div>
""" + "".join(qa(t, q, a) for t, q, a in QA))


MCQ = [
    {"q": "Goods in transit are included in the buyer's inventory when the terms are:", "o": [
        "FOB destination", "FOB shipping point", "consignment", "cash on delivery"], "a": 1,
     "why": "Title passes when the carrier accepts the goods from the seller."},
    {"q": "Houston Electronics: 1,000 units cost $12,000, 450 units left. FIFO ending inventory is:", "o": [
        "$5,000", "$5,400", "$5,800", "$6,200"], "a": 2,
     "why": "400 @ $13 + 50 @ $12 = $5,800. $5,000 is LIFO and $5,400 average."},
    {"q": "Same data: LIFO cost of goods sold is:", "o": [
        "$6,200", "$6,600", "$7,000", "$5,000"], "a": 2,
     "why": "$12,000 − $5,000 ending inventory = $7,000."},
    {"q": "Same data: the weighted-average unit cost is:", "o": [
        "$11.50", "$12.00", "$12.50", "$13.00"], "a": 1,
     "why": "$12,000 ÷ 1,000 units. Not the average of the four prices."},
    {"q": "In a period of inflation, the method giving the lowest income taxes is:", "o": [
        "FIFO", "LIFO", "average-cost", "specific identification"], "a": 1,
     "why": "LIFO gives the highest cost of goods sold, so the lowest taxable income."},
    {"q": "Understating ending inventory will overstate:", "o": [
        "assets", "cost of goods sold", "net income", "stockholders' equity"], "a": 1,
     "why": "The other three are understated."},
    {"q": "Overstating this year's ending inventory means next year's net income is:", "o": [
        "overstated", "understated", "unaffected", "doubled"], "a": 1,
     "why": "It becomes an overstated beginning inventory, so cost of goods sold is overstated next year."},
    {"q": "Which method gives the same result under periodic and perpetual systems?", "o": [
        "LIFO", "FIFO", "average-cost", "all three"], "a": 1,
     "why": "FIFO. The others depend on what is on hand at the time of each sale."},
    {"q": "In perpetual moving-average, a new unit cost is computed after every:", "o": [
        "sale", "purchase", "month", "sales return"], "a": 1,
     "why": "Purchases (and purchase returns) change the average; sales are costed at the current average."},
    {"q": "A manufacturer's three inventory accounts are:", "o": [
        "purchases, freight-in, returns", "raw materials, work in process, finished goods",
        "direct, indirect, overhead", "opening, moving, closing"], "a": 1,
     "why": "All three are current assets."},
    {"q": "Goods held on consignment by a store are included in:", "o": [
        "the store's inventory", "the consignor's inventory", "neither party's inventory", "both inventories"], "a": 1,
     "why": "Ownership never passes to the consignee."},
    {"q": "P6.5A: cost of goods available for sale is:", "o": [
        "$9,625", "$11,225", "$11,590", "$12,000"], "a": 1,
     "why": "$1,600 beginning + $9,625 net purchases. $11,590 is net sales."},
    {"q": "P6.5A: gross profit under FIFO is:", "o": [
        "$4,330", "$4,546.90", "$4,830", "$6,760"], "a": 2,
     "why": "Net sales $11,590 − cost of goods sold $6,760."},
    {"q": "P6.8A: ending inventory under LIFO is:", "o": [
        "$1,940", "$2,200.55", "$2,340", "$3,520"], "a": 0,
     "why": "(100 @ $15) + (20 @ $22). $3,520 is its cost of goods sold."},
    {"q": "P6.8A: gross profit under moving-average is:", "o": [
        "$2,160", "$2,421", "$2,560", "$3,259.45"], "a": 1,
     "why": "$5,680 − $3,259.45 = $2,420.55, rounded to $2,421."},
]

BLANKS = [
    {"s": "Cost of goods available for sale − ending inventory = ___.", "a": ["cost of goods sold", "COGS"]},
    {"s": "Weighted-average unit cost = cost of goods available for sale ÷ ___.", "a": ["units available for sale", "total units available for sale", "total units"]},
    {"s": "Gross profit rate = gross profit ÷ ___.", "a": ["net sales", "sales"]},
    {"s": "Under FOB ___ the buyer owns goods in transit.", "a": ["shipping point", "shipping-point"]},
    {"s": "Goods held to sell for another party, without ownership, are ___ goods.", "a": ["consigned", "consignment"]},
    {"s": "A manufacturer's three inventories: raw materials, work in process and ___.", "a": ["finished goods"]},
    {"s": "Hasbeen Company's corrected inventory is $___.", "a": ["195,000", "195000"]},
    {"s": "Crivitz: cost of goods sold under specific identification is $___.", "a": ["1,500", "1500"]},
    {"s": "Houston Electronics FIFO ending inventory is $___.", "a": ["5,800", "5800"]},
    {"s": "Houston Electronics LIFO cost of goods sold is $___.", "a": ["7,000", "7000"]},
    {"s": "Houston Electronics average-cost unit cost is $___.", "a": ["12", "12.00"]},
    {"s": "Houston FIFO net income (30% tax) is $___.", "a": ["2,310", "2310"]},
    {"s": "In perpetual LIFO, Houston's cost of goods sold is $___.", "a": ["6,300", "6300"]},
    {"s": "In perpetual moving-average, Houston's ending inventory is $___.", "a": ["5,767", "5767"]},
    {"s": "Visual Company: 2017 cost of goods sold is ___ by $22,000.", "a": ["overstated"]},
    {"s": "An inventory error affects net income in ___ periods.", "a": ["two", "2"]},
    {"s": "LIFO for tax means LIFO for reporting: the LIFO ___ rule.", "a": ["conformity"]},
    {"s": "P6.5A gross profit under LIFO is $___.", "a": ["4,330", "4330"]},
    {"s": "P6.5A gross profit rate under average-cost is ___%.", "a": ["39.2", "39.23"]},
    {"s": "P6.8A cost of goods available for sale is $___.", "a": ["5,460", "5460"]},
]

DRILL = [
    {"task": "Beginning inventory $8,000, purchases $32,000, ending inventory $9,500. Cost of goods sold?",
     "cmd": ["8,000 + 32,000 = 40,000 available", "40,000 - 9,500 = 30,500"]},
    {"task": "Counted $150,000. Included $12,000 consigned goods held for others; excluded $7,000 bought FOB shipping point, in transit. Correct figure?",
     "cmd": ["150,000 - 12,000 + 7,000 = 145,000"]},
    {"task": "200 units available costing $4,400; 60 left. Average-cost ending inventory and COGS?",
     "cmd": ["unit = 4,400 / 200 = 22.00", "EI   = 60 x 22.00 = 1,320", "COGS = 4,400 - 1,320 = 3,080"]},
    {"task": "Layers 100@$10, 200@$11, 300@$12, 400@$13; 450 units left. FIFO and LIFO ending inventory?",
     "cmd": ["FIFO = 400x13 + 50x12 = 5,800", "LIFO = 100x10 + 200x11 + 150x12 = 5,000"]},
    {"task": "Net sales $11,590, cost of goods sold $6,760. Gross profit and gross profit rate?",
     "cmd": ["GP   = 11,590 - 6,760 = 4,830", "rate = 4,830 / 11,590 = 41.7%"]},
    {"task": "Ending inventory overstated $5,000. Effect on COGS, net income, assets, equity this year?",
     "cmd": ["COGS       understated 5,000", "Net income overstated  5,000", "Assets     overstated  5,000", "Equity     overstated  5,000"]},
    {"task": "Perpetual moving-average: 240 units cost $4,020, then buy 55 @ $20. New average?",
     "cmd": ["4,020 + 1,100 = 5,120 / 295 units", "= 17.356 per unit"]},
    {"task": "Perpetual LIFO sale of 90 units; layers on hand 100@$15, 40@$18, 50@$20. Cost of the sale?",
     "cmd": ["newest first: 50 x 20 = 1,000", "              40 x 18 =   720", "total                 = 1,720"]},
]


def s_quiz():
    return """
<h2><small>Self-test</small>Quiz and drills</h2>
<span class="score" id="mcq-score"></span> <button class="btn" id="mcq-reset">reset</button>
<div class="quiz" id="mcq"></div>
<h3>Fill in the blanks</h3>
<div class="quiz" id="blanks"></div>
<h3>Computation drills</h3>
<div class="drill" id="drill"></div>
"""


def s_checklist():
    return """
<h2><small>Last look</small>Before you walk in</h2>
<ol class="steps">
<li><b>The formula</b>Available for sale − ending inventory = cost of goods sold.</li>
<li><b>FIFO / LIFO</b>LISH and FISH: FIFO leaves the newest costs, LIFO the oldest.</li>
<li><b>Average</b>Total cost ÷ total units, never the average of the prices.</li>
<li><b>Rising prices</b>FIFO highest profit, LIFO lowest profit and lowest tax.</li>
<li><b>Errors</b>Ending inventory overstated → cost of goods sold understated → profit, assets, equity overstated; reverses next year.</li>
<li><b>Ownership</b>FOB shipping point = buyer; FOB destination = seller; consignment = consignor.</li>
<li><b>Perpetual</b>Only FIFO matches the periodic answer; average is recomputed after purchases only.</li>
<li><b>Slide numbers</b>Houston: 5,800 / 5,000 / 5,400 ending; 6,200 / 7,000 / 6,600 cost of goods sold; perpetual 6,300 LIFO and 6,233 average. Hasbeen $195,000. Crivitz $1,500. Visual $22,000.</li>
<li><b>Assignment numbers</b>P6.5A 4,330 / 4,830 / 4,546.90. P6.8A 2,160 / 2,560 / 2,420.55.</li>
<li><b>Always check</b>Cost of goods sold + ending inventory = cost of goods available for sale.</li>
</ol>
"""


def sections():
    return [
        ("cheat", "Rules", s_cheat()),
        ("own", "Ex 1 Ownership", s_ex_own()),
        ("spec", "Ex 2 Specific ID", s_ex_spec()),
        ("periodic", "Ex 3 Periodic", s_ex_periodic()),
        ("effects", "Ex 4 Effects", s_ex_effects()),
        ("error", "Ex 5 Error", s_ex_error()),
        ("perpetual", "Ex 6 Perpetual", s_ex_perpetual()),
        ("slidemcq", "Slide MCQs", s_slide_mcq()),
        ("problems", "P6.5A + P6.8A", s_problems()),
        ("qa", "Short answers", s_qa()),
        ("quiz", "Quiz", s_quiz()),
        ("checklist", "Checklist", s_checklist()),
    ]
