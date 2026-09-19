"""Content for the FMA Chapter 6 (Inventories) class-test guide.

Grounded in the course deck ch06-FA.pptx (42 slides, LO 1-4 + Appendix 6A) and the
textbook illustrations it reproduces. Every figure was recomputed before it went in.
"""

table = None  # injected by build.py

HERE = "Financial &amp; Managerial Accounting"

HERO = """
<header class="hero">
  <h1>Chapter 6 — Inventories</h1>
  <p>Everything the class test can ask from the Chapter 6 deck: classifying inventory, who owns goods in
  transit, the four costing methods, what each one does to profit and tax, inventory errors, presentation,
  and the perpetual versions in Appendix 6A. Ends with the two assignment problems worked in full, plus
  self-tests.</p>
  <div class="chips">
    <span class="chip">LO 1–4 + Appendix 6A</span>
    <span class="chip">FIFO · LIFO · Average-cost</span>
    <span class="chip">Periodic &amp; perpetual</span>
    <span class="chip">P6.5A and P6.8A solved</span>
  </div>
</header>
"""


def svg(w, h, inner, cap=None, label="diagram"):
    arrow = ('<defs><marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
             'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--muted)"/></marker></defs>')
    c = f'<div class="cap">{cap}</div>' if cap else ""
    return (f'<div class="figwrap"><svg viewBox="0 0 {w} {h}" role="img" aria-label="{label}">{arrow}{inner}</svg>{c}</div>')


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
def s_start():
    return """
<h2><small>Start here</small>The five things the whole chapter hangs on</h2>
<div class="formula">Beginning inventory + Purchases = Cost of goods available for sale<br>
Cost of goods available for sale − Ending inventory = <b>Cost of goods sold</b></div>
<p>Every costing method in this chapter splits the same pot of money — the cost of goods available for sale —
between what is still on the shelf (ending inventory, an asset) and what was sold (cost of goods sold, an
expense). Give more to one and you give less to the other.</p>
<ol class="steps">
<li><b>Classify it</b>A merchandiser has one inventory account. A manufacturer has three: raw materials, work in
process, finished goods. All of them are <b>current assets</b>.</li>
<li><b>Count it and decide who owns it</b>Goods in transit belong to whoever has legal title: FOB shipping point
means the buyer owns them the moment the carrier takes them; FOB destination means the seller owns them until
delivery. Consigned goods belong to the consignor, never to the shop holding them.</li>
<li><b>Cost it</b>Specific identification, FIFO, LIFO or average-cost. The assumption does <b>not</b> have to match
the physical flow of the goods.</li>
<li><b>Know the effects</b>When prices are rising: FIFO gives the highest ending inventory and net income; LIFO
gives the lowest net income and therefore the lowest income taxes; average-cost sits between them.</li>
<li><b>Watch for errors</b>An ending inventory error hits two years in opposite directions, and after two years
the total net income is correct again.</li>
</ol>
<div class="box say"><b>If you are asked to define cost</b>Inventory is recorded at <b>cost</b>, and cost includes
<b>all expenditures necessary to acquire the goods and put them in a condition ready for sale</b>.</div>
<h3>Numbers from the deck worth memorising</h3>
<div class="grid2">
  <div class="stat"><div class="v">3</div><div class="k">manufacturer classifications: raw materials, work in process, finished goods</div></div>
  <div class="stat"><div class="v">4</div><div class="k">costing methods: specific identification, FIFO, LIFO, average-cost</div></div>
  <div class="stat"><div class="v">$195,000</div><div class="k">Hasbeen Co. corrected inventory (200,000 − 15,000 + 10,000)</div></div>
  <div class="stat"><div class="v">$12,000</div><div class="k">Houston Electronics: cost of 1,000 units available for sale</div></div>
  <div class="stat"><div class="v">2</div><div class="k">years an inventory error affects, and they cancel out</div></div>
  <div class="stat"><div class="v">30%</div><div class="k">tax rate in the comparative income statements</div></div>
</div>
"""


def s_basics():
    return """
<h2><small>From zero</small>Inventory in plain English</h2>
<p>Skip this if you already know the vocabulary. If you missed the classes, read it first: everything later
depends on these five ideas.</p>
<h3>1. What inventory is</h3>
<p><b>Inventory is the goods a business is holding to sell.</b> A shop's shelves, a warehouse's boxes. It is an
<b>asset</b> while it sits there. The moment it is sold, its cost stops being an asset and becomes an expense
called <b>cost of goods sold</b>. That switch is the whole chapter.</p>
<h3>2. Why the cost has to be split</h3>
<p>During a month a shop starts with some goods, buys more, and sells some. Add the starting goods to the
purchases and you get everything it could have sold: the <b>cost of goods available for sale</b>. At month end
that pot is split in two.</p>
""" + svg(820, 200, "".join([
        box(20, 60, 200, 80, "bxw", ["Beginning inventory", "what was on the shelf", "at the start"]),
        box(20, 150, 200, 40, "bxw", ["+ Purchases"]),
        arrow(225, 110, 275, 110),
        box(280, 70, 230, 80, "bxa", ["Cost of goods", "available for sale", "the whole pot"]),
        arrow(515, 90, 565, 55), arrow(515, 130, 565, 165),
        box(570, 20, 230, 70, "bxg", ["Ending inventory", "still on the shelf = ASSET"]),
        box(570, 130, 230, 70, "bxv", ["Cost of goods sold", "sold = EXPENSE"]),
    ]), "Whatever you do not count as ending inventory is treated as sold. That is why the costing method changes profit.", "splitting the pot") + """
<div class="formula">Beginning inventory + Purchases − Ending inventory = Cost of goods sold</div>
<h3>3. The two record-keeping systems</h3>
""" + table(["", "Perpetual system", "Periodic system"], [
        ["When records update", "at every purchase and every sale", "only at the end of the period"],
        ["Cost of goods sold", "calculated at each sale", "calculated once, using the formula above"],
        ["Physical count is for", "checking the records and finding losses (theft, waste)", "finding out what is on hand at all"],
        ["Which problem is which", "P6.8A (Dempsey)", "P6.5A (Koetteritz)"],
    ]) + """
<h3>4. Why there are different costing methods</h3>
<p>A shop buys identical goods at different prices through the year: 100 at $10, then 200 at $11, then 300 at
$12. It sells some. <b>Which cost goes to the sold ones?</b> The goods are identical, so accounting has to
<i>assume</i> an order:</p>
<ul>
<li><b>FIFO</b> — assume the oldest are sold first. Newest costs stay in inventory.</li>
<li><b>LIFO</b> — assume the newest are sold first. Oldest costs stay in inventory.</li>
<li><b>Average-cost</b> — mix all the costs together and use one average.</li>
<li><b>Specific identification</b> — no assumption at all: track each actual unit. Only practical for things like
cars, where every unit is identifiable.</li>
</ul>
<div class="box deep"><b>A 3-unit example you can hold in your head</b>Buy one item for $10, then one for $12. Sell
one for $20. FIFO: cost of goods sold $10, inventory left $12, gross profit $10. LIFO: cost of goods sold $12,
inventory left $10, gross profit $8. Average: cost $11 each, gross profit $9. Same shop, same sale, three
different profits — all of them legal.</div>
<h3>5. The words that will be used from here on</h3>
""" + table(["Term", "Plain meaning"], [
        ["Cost of goods available for sale", "beginning inventory + purchases: everything that could be sold"],
        ["Ending inventory", "cost of the goods still unsold at period end (an asset)"],
        ["Cost of goods sold (COGS)", "cost of the goods that were sold (an expense)"],
        ["Gross profit", "net sales − cost of goods sold"],
        ["Gross profit rate", "gross profit ÷ net sales, as a percentage"],
        ["Net sales", "sales − sales returns"],
        ["Purchase return", "goods sent back to the supplier: reduces purchases"],
        ["Sales return", "goods a customer sends back: reduces sales, and the goods come back into inventory"],
        ["Unit cost", "what one unit cost to buy"],
        ["FOB", "\u201cfree on board\u201d: the point where ownership passes from seller to buyer"],
        ["Consignment", "holding someone else\u2019s goods to sell for a fee, without owning them"],
    ]) + """
<div class="box say"><b>How an exam answer is built</b>1. Work out the units and cost available for sale.
2. Work out how many units are left. 3. Cost those units by the method asked for. 4. Cost of goods available
minus ending inventory gives cost of goods sold. 5. Net sales minus cost of goods sold gives gross profit.</div>
"""


def s_lo1():
    return """
<h2><small>LO 1</small>Classifying and determining inventory</h2>
<h3>Classification</h3>
""" + table(["Type of company", "Inventory accounts", "Shown as"], [
        ["Merchandising company", "One account: <b>Inventory</b> (goods bought ready for resale)", "Current asset"],
        ["Manufacturing company", "Three: <b>raw materials</b>, <b>work in process</b>, <b>finished goods</b>", "Current assets"],
    ]) + """
<div class="box"><b>Helpful hint from the deck</b>Whatever the classification, companies report <b>all</b>
inventories under current assets on the balance sheet.</div>
<h3>Why a physical count is taken</h3>
""" + table(["System", "Reason for taking a physical inventory"], [
        ["Perpetual", "check the accuracy of the inventory records; measure inventory lost to waste, shoplifting or employee theft"],
        ["Periodic", "determine the inventory on hand; determine the cost of goods sold for the period"],
    ]) + """
<p>Taking a physical inventory means <b>counting, weighing or measuring</b> each kind of inventory on hand.
Companies usually do it when the business is closed or slow, and at the end of the accounting period.</p>
<h3>Who owns the goods</h3>
""" + svg(820, 190, "".join([
        box(20, 20, 360, 70, "bxa", ["FOB SHIPPING POINT", "ownership passes when the carrier", "accepts the goods from the seller"]),
        box(20, 105, 360, 70, "bxg", ["FOB DESTINATION", "ownership stays with the seller", "until the goods reach the buyer"]),
        arrow(385, 55, 430, 55), arrow(385, 140, 430, 140),
        box(435, 20, 170, 70, "bx", ["BUYER", "counts them"]),
        box(435, 105, 170, 70, "bx", ["SELLER", "counts them"]),
        box(625, 55, 175, 85, "bxv", ["CONSIGNED GOODS", "held to sell for a fee,", "ownership never passes:", "consignor still counts them"]),
    ]), "Goods in transit go in the inventory of whoever holds legal title, and the terms of sale decide that.", "ownership of goods") + """
<div class="box say"><b>DO IT! Hasbeen Company</b>Inventory counted at $200,000.
(1) It <b>included</b> $15,000 of goods held on consignment for Falls Co. — those belong to Falls, so
<b>deduct $15,000</b>. (2) It <b>omitted</b> $10,000 of purchased goods in transit, FOB shipping point — title has
already passed to Hasbeen, so <b>add $10,000</b>. (3) It omitted goods it had sold, costing $12,000, in transit FOB
shipping point — title passed to the customer, so leaving them out was <b>correct</b>.<br>
Corrected inventory = $200,000 − $15,000 + $10,000 = <b>$195,000</b>.</div>
<div class="box trap"><b>Exam trap</b>"Goods in transit should be included in the inventory of the buyer when …"
The answer is <b>the terms of sale are FOB shipping point</b> (equivalently: when the public carrier accepts the
goods from the seller).</div>
"""


def s_lo2():
    return """
<h2><small>LO 2</small>Cost flow methods</h2>
<p>Inventory is accounted for at <b>cost</b>: all expenditures needed to acquire the goods and bring them to a
condition ready for sale. Unit costs are then applied to quantities using one of four methods.</p>
""" + table(["Method", "What it assumes", "Note from the deck"], [
        ["Specific identification", "each item sold is costed at its own actual cost", "an actual physical-flow method; <b>practice is relatively rare</b>"],
        ["FIFO (first-in, first-out)", "earliest costs go to cost of goods sold", "often parallels the actual physical flow of goods"],
        ["LIFO (last-in, first-out)", "latest costs go to cost of goods sold", "seldom matches physical flow — exceptions are goods stored in piles, like coal or hay"],
        ["Average-cost", "one weighted-average unit cost for everything", "allocates the cost of goods available for sale on a weighted-average basis"],
    ]) + """
<div class="box trap"><b>Remember this sentence</b>Cost flow assumptions <b>do not need to be consistent with the
physical movement of the goods</b>. Only specific identification tracks actual units.</div>
<div class="box deep"><b>The rules the slides state, in the words to quote</b>
<ul>
<li>Inventory is accounted for at <b>cost</b>; cost includes all expenditures necessary to acquire the goods and
place them in a condition ready for sale.</li>
<li>Goods in transit are included in the inventory of the company that has <b>legal title</b>; the terms of sale
decide it.</li>
<li>Cost flow assumptions <b>do not need to be consistent with the physical movement</b> of the goods.</li>
<li>FIFO: the costs of the <b>earliest</b> goods purchased are the first recognised in cost of goods sold.</li>
<li>LIFO: the costs of the <b>latest</b> goods purchased are the first recognised in cost of goods sold.</li>
<li>Average-cost allocates the cost of goods available for sale on the basis of <b>weighted-average unit cost</b>.</li>
<li>An error in ending inventory of the current period has a <b>reverse effect</b> on net income of the next
period, and over the two years the total net income is correct.</li>
<li>The LIFO conformity rule: LIFO for tax means LIFO for financial reporting.</li>
</ul></div>
<h3>Specific identification — the Crivitz example</h3>
<p>Crivitz TV buys three identical 50-inch TVs for $700, $750 and $800, and sells two of them for $1,200 each.
If the ones sold were the February 3 ($700) and May 22 ($800) sets, then cost of goods sold is
<b>$1,500</b> and ending inventory is <b>$750</b>. Choose different sets and the profit changes — which is why the
method is only allowed when units are genuinely identifiable.</p>
<h3>The Houston Electronics data (the deck's running example)</h3>
""" + table(["Date", "Explanation", "Units", "Unit cost", "Total cost"], [
        ["Jan. 1", "Beginning inventory", "100", "$10", "$ 1,000"],
        ["Apr. 15", "Purchase", "200", "11", "2,200"],
        ["Aug. 24", "Purchase", "300", "12", "3,600"],
        ["Nov. 27", "Purchase", "400", "13", "5,200"],
        (["", "<b>Total units available for sale</b>", "<b>1,000</b>", "", "<b>$12,000</b>"], "tot"),
        ["", "Units in ending inventory", "450", "", ""],
        ["", "Units sold", "550", "", ""],
    ], num=(2, 3, 4)) + """
<h4>FIFO — cost the ending inventory with the <i>newest</i> costs</h4>
<p>Mnemonic in the deck: <b>LISH — last in still here</b>.</p>
""" + table(["Ending inventory (450 units)", "", "Cost of goods sold", ""], [
        ["400 units @ $13 (Nov. 27)", "$5,200", "Cost of goods available for sale", "$12,000"],
        ["50 units @ $12 (Aug. 24)", "600", "Less: ending inventory", "5,800"],
        (["<b>Ending inventory</b>", "<b>$5,800</b>", "<b>Cost of goods sold</b>", "<b>$6,200</b>"], "tot"),
    ], num=(1, 3)) + """
<h4>LIFO — cost the ending inventory with the <i>oldest</i> costs</h4>
<p>Mnemonic: <b>FISH — first in still here</b>.</p>
""" + table(["Ending inventory (450 units)", "", "Cost of goods sold", ""], [
        ["100 units @ $10 (Jan. 1)", "$1,000", "Cost of goods available for sale", "$12,000"],
        ["200 units @ $11 (Apr. 15)", "2,200", "Less: ending inventory", "5,000"],
        ["150 units @ $12 (Aug. 24)", "1,800", "", ""],
        (["<b>Ending inventory</b>", "<b>$5,000</b>", "<b>Cost of goods sold</b>", "<b>$7,000</b>"], "tot"),
    ], num=(1, 3)) + """
<h4>Average-cost — one weighted-average unit cost</h4>
<div class="formula">Weighted-average unit cost = Cost of goods available for sale ÷ Total units available for sale</div>
""" + table(["Step", "Working", "Result"], [
        ["Weighted-average unit cost", "$12,000 ÷ 1,000 units", "$12.00"],
        ["Ending inventory", "450 units × $12.00", "$5,400"],
        ["Cost of goods sold", "$12,000 − $5,400", "$6,600"],
    ], num=(2,)) + """
<div class="box warn"><b>Do not average the unit prices</b>The weighted average is not (10 + 11 + 12 + 13) ÷ 4 =
$11.50. It is total cost ÷ total units = $12.00, because the purchases are different sizes.</div>
<h3>Financial statement and tax effects</h3>
""" + table(["", "FIFO", "LIFO", "Average-cost"], [
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
<p>Prices were rising in this example ($10 → $13), and that is the case every exam question uses.</p>
""" + table(["Effect (period of rising prices)", "FIFO", "LIFO"], [
        ["Ending inventory on the balance sheet", "highest — close to current cost", "lowest — may be badly understated in current-cost terms"],
        ["Cost of goods sold", "lowest", "highest"],
        ["Net income", "highest", "lowest"],
        ["Income taxes", "highest", "<b>lowest</b>"],
    ]) + """
<div class="box deep"><b>LIFO conformity rule</b>If a company uses LIFO for tax purposes, it must also use LIFO for
financial reporting. That is why the tax saving comes at the cost of reporting lower profit.</div>
<div class="box"><b>Who uses what (deck examples)</b>FIFO: Reebok International, Wendy's International.
LIFO: Campbell Soup, Krogers, Walgreen Drugs. Average-cost: Bristol-Myers Squibb, Starbucks, Motorola.
Stanley Black &amp; Decker uses LIFO for domestic and FIFO for foreign inventories. All three methods are
acceptable; a company must disclose which it uses.</div>
"""


def s_errors():
    return """
<h2><small>LO 3</small>Inventory errors</h2>
<p><b>Common causes:</b> failing to count or price the inventory correctly, and not properly recognising the
transfer of legal title to goods in transit. An error hits both the income statement and the balance sheet.</p>
<h3>Income statement effects</h3>
<p>Work from the formula. Cost of goods sold = beginning inventory + purchases − ending inventory.</p>
""" + table(["The error", "Cost of goods sold", "Net income"], [
        ["Beginning inventory <b>understated</b>", "understated", "overstated"],
        ["Beginning inventory <b>overstated</b>", "overstated", "understated"],
        ["Ending inventory <b>understated</b>", "overstated", "understated"],
        ["Ending inventory <b>overstated</b>", "understated", "overstated"],
    ]) + svg(820, 150, "".join([
        box(20, 40, 230, 70, "bxw", ["Year 1: ending inventory", "overstated by $3,000", "net income overstated $3,000"]),
        arrow(255, 75, 300, 75),
        box(305, 40, 250, 70, "bxa", ["Year 2: that becomes", "beginning inventory", "net income understated $3,000"]),
        arrow(560, 75, 605, 75),
        box(610, 40, 190, 70, "bxg", ["Two years combined", "total net income", "is correct"]),
    ]), "An ending inventory error reverses itself in the next period, because this year's ending inventory is next year's beginning inventory.", "two year error effect") + """
<h3>Balance sheet effects</h3>
<p>Use the accounting equation: Assets = Liabilities + Stockholders' equity.</p>
""" + table(["Ending inventory error", "Assets", "Liabilities", "Stockholders' equity"], [
        ["Overstated", "overstated", "no effect", "overstated"],
        ["Understated", "understated", "no effect", "understated"],
    ]) + """
<div class="box say"><b>DO IT! Visual Company</b>2016 ending inventory overstated by $22,000.<br>
<b>2016:</b> ending inventory overstated $22,000 · cost of goods sold understated $22,000 · stockholders' equity
overstated $22,000.<br>
<b>2017:</b> ending inventory no effect · cost of goods sold <b>overstated $22,000</b> · stockholders' equity
no effect (the two errors have cancelled).</div>
<div class="box trap"><b>Deck question</b>"Understating ending inventory will overstate: assets / cost of goods
sold / net income / stockholders' equity." Answer: <b>cost of goods sold</b>. The other three are understated.</div>
"""


def s_presentation():
    return """
<h2><small>LO 4</small>Presentation and analysis</h2>
""" + table(["Statement", "How inventory appears"], [
        ["Balance sheet", "inventory as a <b>current asset</b>"],
        ["Income statement", "<b>cost of goods sold</b> subtracted from sales revenue"],
    ]) + """
<p>Companies must also disclose:</p>
<ul>
<li>the major <b>inventory classifications</b>,</li>
<li>the <b>basis of accounting</b> (cost, or lower-of-cost-or-market / net realisable value), and</li>
<li>the <b>costing method</b> used (FIFO, LIFO or average-cost).</li>
</ul>
<div class="box"><b>If your paper goes past the deck</b>The textbook's LO 4 also covers two ratios:
<b>inventory turnover = cost of goods sold ÷ average inventory</b>, and
<b>days in inventory = 365 ÷ inventory turnover</b>. Average inventory = (beginning + ending) ÷ 2.
A higher turnover means inventory is sold faster and less cash is tied up.</div>
"""


def s_perpetual():
    return """
<h2><small>Appendix 6A (LO 5)</small>The same methods in a perpetual system</h2>
<p>In a perpetual system the inventory account is updated at <b>every</b> purchase and sale, so cost of goods sold
is computed as each sale happens. Same Houston Electronics data, but now the 550-unit sale happens on September 10,
<b>before</b> the November 27 purchase.</p>
""" + table(["Date", "Explanation", "Units", "Unit cost", "Total cost", "Balance in units"], [
        ["1/1", "Beginning inventory", "100", "$10", "$1,000", "100"],
        ["4/15", "Purchase", "200", "11", "2,200", "300"],
        ["8/24", "Purchase", "300", "12", "3,600", "600"],
        ["9/10", "<b>Sale</b>", "550", "", "", "50"],
        ["11/27", "Purchase", "400", "13", "5,200", "450"],
        (["", "", "", "", "<b>$12,000</b>", ""], "tot"),
    ], num=(2, 3, 4, 5)) + table(["Method", "Cost of goods sold", "Ending inventory", "Same as periodic?"], [
        ["FIFO", "$6,200 <span class='t-s'>(100@10 + 200@11 + 250@12)</span>", "$5,800 <span class='t-s'>(50@12 + 400@13)</span>", "<b>Yes</b> — FIFO always gives the same answer either way"],
        ["LIFO", "$6,300 <span class='t-s'>(300@12 + 200@11 + 50@10)</span>", "$5,700 <span class='t-s'>(50@10 + 400@13)</span>", "No — periodic LIFO gave $7,000 / $5,000"],
        ["Moving-average", "$6,233", "$5,767", "No — periodic average gave $6,600 / $5,400"],
    ]) + """
<h3>FIFO, step by step</h3>
""" + table(["Date", "Purchases", "Cost of goods sold", "Balance (units and cost)"], [
        ["Jan. 1", "", "", "(100 @ $10) $1,000"],
        ["Apr. 15", "(200 @ $11) $2,200", "", "(100 @ $10) (200 @ $11) $3,200"],
        ["Aug. 24", "(300 @ $12) $3,600", "", "(100 @ $10) (200 @ $11) (300 @ $12) $6,800"],
        ["Sept. 10", "", "(100 @ $10) + (200 @ $11) + (250 @ $12) = <b>$6,200</b>", "(50 @ $12) $600"],
        ["Nov. 27", "(400 @ $13) $5,200", "", "(50 @ $12) (400 @ $13) <b>$5,800</b>"],
    ]) + """
<h3>LIFO, step by step</h3>
""" + table(["Date", "Purchases", "Cost of goods sold", "Balance (units and cost)"], [
        ["Jan. 1", "", "", "(100 @ $10) $1,000"],
        ["Apr. 15", "(200 @ $11) $2,200", "", "(100 @ $10) (200 @ $11) $3,200"],
        ["Aug. 24", "(300 @ $12) $3,600", "", "(100 @ $10) (200 @ $11) (300 @ $12) $6,800"],
        ["Sept. 10", "", "(300 @ $12) + (200 @ $11) + (50 @ $10) = <b>$6,300</b>", "(50 @ $10) $500"],
        ["Nov. 27", "(400 @ $13) $5,200", "", "(50 @ $10) (400 @ $13) <b>$5,700</b>"],
    ]) + """
<h3>Moving-average, step by step</h3>
<p>A new average unit cost is computed <b>after every purchase</b>, never after a sale.</p>
""" + table(["Date", "Purchases", "Cost of goods sold", "Balance (units and cost)"], [
        ["Jan. 1", "", "", "(100 @ $10) $1,000"],
        ["Apr. 15", "(200 @ $11) $2,200", "", "(300 @ $10.667) $3,200"],
        ["Aug. 24", "(300 @ $12) $3,600", "", "(600 @ $11.333) $6,800"],
        ["Sept. 10", "", "(550 @ $11.333) <b>$6,233</b>", "(50 @ $11.333) $567"],
        ["Nov. 27", "(400 @ $13) $5,200", "", "(450 @ $12.816) <b>$5,767</b>"],
    ]) + """
<div class="box trap"><b>The one difference that catches people</b>Under a perpetual system, <b>LIFO and
moving-average give different answers from the periodic versions</b>, because a sale is costed using only the goods
on hand at that moment. FIFO is the exception: the oldest costs are the oldest costs whenever you look, so
perpetual FIFO = periodic FIFO.</div>
<div class="box"><b>Returns in a perpetual system</b>A <b>sales return</b> puts goods back into inventory at the
cost they were taken out at. A <b>purchase return</b> removes the returned units at their purchase cost, and under
moving-average it forces a fresh average.</div>
"""


def s_problems():
    return """
<h2><small>Worked problems</small>The two assignment questions, solved</h2>
<h3>P6.5A — Koetteritz Inc., June 2020 (periodic)</h3>
""" + table(["Date", "Description", "Units", "Unit cost / price"], [
        ["June 1", "Beginning inventory", "40", "$40"],
        ["June 4", "Purchase", "135", "43"],
        ["June 10", "Sale", "110", "70"],
        ["June 11", "Sale return", "15", "70"],
        ["June 18", "Purchase", "55", "46"],
        ["June 18", "Purchase return", "10", "46"],
        ["June 25", "Sale", "65", "76"],
        ["June 28", "Purchase", "35", "50"],
    ], num=(2, 3)) + """
<h4>Step 1 — goods available for sale</h4>
""" + table(["Item", "Units", "Cost"], [
        ["Beginning inventory 40 @ $40", "40", "$1,600"],
        ["Purchase 135 @ $43", "135", "5,805"],
        ["Purchase 55 @ $46", "55", "2,530"],
        ["Purchase return 10 @ $46", "(10)", "(460)"],
        ["Purchase 35 @ $50", "35", "1,750"],
        (["<b>Cost of goods available for sale</b>", "<b>255</b>", "<b>$11,225</b>"], "tot"),
        ["Units sold (110 − 15 + 65)", "(160)", ""],
        ["<b>Ending inventory in units</b>", "<b>95</b>", ""],
    ], num=(1, 2)) + """
<h4>Step 2 — net sales</h4>
<p>(110 × $70) − (15 × $70) + (65 × $76) = $7,700 − $1,050 + $4,940 = <b>$11,590</b></p>
<h4>Step 3 — the three methods</h4>
""" + table(["", "LIFO", "FIFO", "Average-cost"], [
        ["Ending inventory, 95 units costed",
         "40 @ $40 = 1,600<br>55 @ $43 = 2,365",
         "35 @ $50 = 1,750<br>45 @ $46 = 2,070<br>15 @ $43 = 645",
         "$11,225 ÷ 255 = $44.02<br>95 × $44.02"],
        (["<b>(i) Ending inventory</b>", "<b>$3,965</b>", "<b>$4,465</b>", "<b>$4,181.90</b>"], "sub"),
        ["<b>(ii) Cost of goods sold</b>", "$7,260", "$6,760", "$7,043.10"],
        ["<b>(iii) Gross profit</b>", "$4,330", "$4,830", "$4,546.90"],
        (["<b>(iv) Gross profit rate</b>", "<b>37.4%</b>", "<b>41.7%</b>", "<b>39.2%</b>"], "tot"),
    ], num=(1, 2, 3)) + """
<p>Cost of goods sold = $11,225 − ending inventory. Gross profit rate = gross profit ÷ net sales
($4,330/11,590 = 37.36%; $4,830/11,590 = 41.67%; $4,546.90/11,590 = 39.23%).</p>
<div class="box say"><b>Part (b), in one sentence</b>Prices rose through June ($40 → $50), so FIFO keeps the dearest
costs in inventory and reports the highest gross profit ($4,830), LIFO reports the lowest ($4,330), and
average-cost falls between them ($4,546.90) — with identical sales in all three.</div>
<h3>P6.8A — Dempsey Inc., January 2020 (perpetual)</h3>
<p>Units available 310, cost available $5,460, units sold 190, ending inventory 120 units.<br>
Net sales = (110 × $28) − (10 × $28) + (90 × $32) = $3,080 − $280 + $2,880 = <b>$5,680</b>.</p>
<h4>(1) LIFO, perpetual</h4>
""" + table(["Date", "Purchases", "Cost of goods sold", "Balance (units and cost)"], [
        ["Jan. 1", "", "", "(100 @ $15) $1,500"],
        ["Jan. 5", "(140 @ $18) $2,520", "", "(100 @ $15) (140 @ $18) $4,020"],
        ["Jan. 8", "", "(110 @ $18) $1,980", "(100 @ $15) (30 @ $18) $2,040"],
        ["Jan. 10", "<i>sale return</i>", "(10 @ $18) ($180)", "(100 @ $15) (40 @ $18) $2,220"],
        ["Jan. 15", "(55 @ $20) $1,100", "", "… (55 @ $20) $3,320"],
        ["Jan. 16", "<i>purchase return</i> (5 @ $20) ($100)", "", "(100 @ $15) (40 @ $18) (50 @ $20) $3,220"],
        ["Jan. 20", "", "(50 @ $20) + (40 @ $18) = $1,720", "(100 @ $15) $1,500"],
        ["Jan. 25", "(20 @ $22) $440", "", "(100 @ $15) (20 @ $22) $1,940"],
        (["", "", "<b>COGS $3,520</b>", "<b>Ending inventory $1,940</b>"], "tot"),
    ]) + """
<p>Gross profit = $5,680 − $3,520 = <b>$2,160</b>.</p>
<h4>(2) FIFO, perpetual</h4>
""" + table(["Date", "Purchases", "Cost of goods sold", "Balance (units and cost)"], [
        ["Jan. 8", "", "(100 @ $15) + (10 @ $18) = $1,680", "(130 @ $18) $2,340"],
        ["Jan. 10", "<i>sale return</i>", "(10 @ $18) ($180)", "(140 @ $18) $2,520"],
        ["Jan. 20", "", "(90 @ $18) $1,620", "(50 @ $18) (50 @ $20) $1,900"],
        ["Jan. 25", "(20 @ $22) $440", "", "(50 @ $18) (50 @ $20) (20 @ $22) $2,340"],
        (["", "", "<b>COGS $3,120</b>", "<b>Ending inventory $2,340</b>"], "tot"),
    ]) + """
<p>Gross profit = $5,680 − $3,120 = <b>$2,560</b>.</p>
<h4>(3) Moving-average, perpetual (unit cost to three decimals)</h4>
""" + table(["Date", "Event", "Cost of goods sold", "Balance (units and cost)"], [
        ["Jan. 1", "", "", "(100 @ $15.000) $1,500.00"],
        ["Jan. 5", "purchase 140 @ $18", "", "(240 @ $16.750) $4,020.00"],
        ["Jan. 8", "sale 110", "(110 @ $16.750) $1,842.50", "(130 @ $16.750) $2,177.50"],
        ["Jan. 10", "sale return 10", "($167.50)", "(140 @ $16.750) $2,345.00"],
        ["Jan. 15", "purchase 55 @ $20", "", "(195 @ $17.667) $3,445.00"],
        ["Jan. 16", "purchase return 5 @ $20", "", "(190 @ $17.605) $3,345.00"],
        ["Jan. 20", "sale 90", "(90 @ $17.605) $1,584.45", "(100 @ $17.605) $1,760.55"],
        ["Jan. 25", "purchase 20 @ $22", "", "(120 @ $18.338) $2,200.55"],
        (["", "", "<b>COGS $3,259.45</b>", "<b>Ending inventory $2,200.55</b>"], "tot"),
    ]) + """
<p>Gross profit = $5,680 − $3,259.45 = <b>$2,420.55</b> (≈ $2,421).</p>
""" + table(["", "LIFO", "FIFO", "Moving-average"], [
        ["Cost of goods sold", "$3,520", "$3,120", "$3,259.45"],
        ["Ending inventory", "1,940", "2,340", "2,200.55"],
        (["<b>Gross profit</b>", "<b>$2,160</b>", "<b>$2,560</b>", "<b>$2,420.55</b>"], "tot"),
    ], num=(1, 2, 3)) + """
<div class="box warn"><b>Check your work in one line</b>Cost of goods sold + ending inventory must equal the cost
of goods available for sale: $3,520 + $1,940 = $3,120 + $2,340 = $3,259.45 + $2,200.55 = <b>$5,460</b>. If it does
not, a layer is wrong.</div>
"""


QA = [
    ("lo 1", "How does a merchandiser's inventory differ from a manufacturer's?",
     "A merchandising company has one inventory account: goods purchased ready for resale. A manufacturer has three: raw materials, work in process and finished goods. All are current assets."),
    ("lo 1", "Why does a company with a perpetual system still take a physical count?",
     "To check the accuracy of the records, and to measure inventory lost through wasted raw materials, shoplifting or employee theft."),
    ("lo 1", "Why does a periodic system need a physical count?",
     "Because it has no running record: the count determines the inventory on hand and, through the formula, the cost of goods sold for the period."),
    ("lo 1", "What does taking a physical inventory involve?",
     "Counting, weighing or measuring each kind of inventory on hand, usually when the business is closed or slow and at the end of the accounting period."),
    ("lo 1", "Who owns goods in transit?",
     "Whoever has legal title, which the terms of sale decide. FOB shipping point: title passes when the public carrier accepts the goods, so the buyer includes them. FOB destination: title passes on delivery, so the seller includes them."),
    ("lo 1", "What are consigned goods and who counts them?",
     "Goods held by one party to sell on behalf of the owner for a fee, without taking ownership. The consignor (the owner) includes them in inventory; the holder never does."),
    ("lo 2", "What is included in the cost of inventory?",
     "All expenditures necessary to acquire the goods and put them in a condition ready for sale."),
    ("lo 2", "Name the four costing methods.",
     "Specific identification, FIFO, LIFO and average-cost. The last three are cost flow assumptions."),
    ("lo 2", "When is specific identification used, and why is it rare?",
     "When each unit can actually be identified, such as cars or jewellery. It is rare because tracking every unit is impractical, and with identical goods it lets management pick which cost to expense."),
    ("lo 2", "Must the cost flow assumption match the physical movement of goods?",
     "No. Only specific identification follows actual units; FIFO, LIFO and average-cost are assumptions about costs, not about goods."),
    ("lo 2", "Explain FIFO in one line, and how you compute ending inventory under it.",
     "The costs of the earliest goods purchased are the first charged to cost of goods sold. Ending inventory is costed from the most recent purchase working backwards — LISH, last in still here."),
    ("lo 2", "Explain LIFO in one line.",
     "The costs of the latest goods purchased are the first charged to cost of goods sold, so the oldest costs stay in ending inventory — FISH, first in still here. It seldom matches physical flow, except for goods stored in piles like coal or hay."),
    ("lo 2", "How is the weighted-average unit cost calculated?",
     "Cost of goods available for sale ÷ total units available for sale. In the Houston example, $12,000 ÷ 1,000 = $12.00, giving ending inventory of $5,400 and cost of goods sold of $6,600. It is not the simple average of the unit prices."),
    ("lo 2", "In a period of rising prices, which method gives the highest net income, and why?",
     "FIFO. The oldest, cheapest costs go to cost of goods sold, so cost of goods sold is lowest and both gross profit and net income are highest. Ending inventory is also closest to current cost."),
    ("lo 2", "Which method gives the lowest income taxes when prices are rising?",
     "LIFO, because the newest and dearest costs go to cost of goods sold, giving the lowest taxable income. Its weakness is that ending inventory on the balance sheet is understated relative to current cost."),
    ("lo 2", "What is the LIFO conformity rule?",
     "If a company uses LIFO for tax purposes, it must also use LIFO in its financial reporting."),
    ("lo 3", "What causes inventory errors?",
     "Failing to count or price inventory correctly, and failing to recognise the transfer of legal title to goods in transit."),
    ("lo 3", "If ending inventory is understated, what happens to cost of goods sold and net income?",
     "Cost of goods sold is overstated and net income is understated. Assets and stockholders' equity are understated too."),
    ("lo 3", "If beginning inventory is overstated, what happens?",
     "Cost of goods sold is overstated and net income is understated for that period."),
    ("lo 3", "Why do inventory errors affect two periods?",
     "This period's ending inventory is next period's beginning inventory, so the error reverses. Over the two years combined, total net income is correct."),
    ("lo 3", "Visual Company overstated 2016 ending inventory by $22,000. What are the effects in 2016 and 2017?",
     "2016: ending inventory overstated $22,000, cost of goods sold understated $22,000, stockholders' equity overstated $22,000. 2017: cost of goods sold overstated $22,000, with no effect on ending inventory or stockholders' equity."),
    ("lo 3", "How do you work out balance sheet effects of an inventory error?",
     "Use Assets = Liabilities + Stockholders' equity. An overstated ending inventory overstates assets and equity; liabilities are never affected."),
    ("lo 4", "How is inventory presented in the financial statements?",
     "As a current asset on the balance sheet, and through cost of goods sold, subtracted from sales revenue on the income statement."),
    ("lo 4", "What must a company disclose about inventory?",
     "The major inventory classifications, the basis of accounting (cost, or lower-of-cost-or-market / net realisable value) and the costing method used (FIFO, LIFO or average-cost)."),
    ("lo 4", "What do inventory turnover and days in inventory measure?",
     "Inventory turnover = cost of goods sold ÷ average inventory: how many times inventory is sold in a period. Days in inventory = 365 ÷ inventory turnover: the average number of days a unit sits in stock."),
    ("6A", "Which method gives the same answer under periodic and perpetual, and why?",
     "FIFO. The earliest costs are the earliest costs whether you cost sales as they happen or all at once at period end. LIFO and average-cost differ, because in a perpetual system each sale can only use the layers on hand at that moment."),
    ("6A", "How does moving-average work?",
     "A new weighted-average unit cost is computed after every purchase (and after a purchase return). Each sale is costed at the average in force at that moment. In the Houston example the averages are $10.667, $11.333 and $12.816, giving cost of goods sold $6,233 and ending inventory $5,767."),
    ("6A", "In perpetual LIFO, what happens to a sales return?",
     "The goods go back into inventory at the cost they were charged out at, and cost of goods sold is reduced by that amount. In P6.8A the January 10 return of 10 units re-enters at $18."),
    ("problems", "In P6.5A, why is the answer the same whichever order you do the purchases in?",
     "Because it is a periodic system: only the totals matter. You add up all units and costs available for sale ($11,225 for 255 units), decide ending inventory units (95), then cost those 95 units according to the method."),
    ("problems", "In P6.5A, how do you handle the purchase return and sales return?",
     "The purchase return reduces units and cost available for sale (10 units, $460). The sales return reduces units sold and sales revenue (15 units, $1,050), so net sales are $11,590 and units sold are 160."),
    ("problems", "In P6.8A, what is the quickest check on your three answers?",
     "Cost of goods sold plus ending inventory must equal the $5,460 cost of goods available for sale under every method, and net sales stay $5,680 throughout."),
]


def s_qa():
    return ("""
<h2><small>Self-check</small>Question bank</h2>
<p>Answer out loud, then open the card. Filter by learning objective.</p>
<div class="filters" id="qa-filters"></div>
""" + "".join(qa(t, q, a) for t, q, a in QA))


MCQ = [
    {"q": "Goods in transit should be included in the inventory of the buyer when the:", "o": [
        "public carrier accepts the goods from the seller", "goods reach the buyer",
        "terms of sale are FOB destination", "seller ships the invoice"], "a": 0,
     "why": "FOB shipping point: title passes when the carrier accepts the goods. (The deck's own question, LO 1.)"},
    {"q": "The cost flow method that often parallels the actual physical flow of merchandise is the:", "o": [
        "FIFO method", "LIFO method", "average-cost method", "gross profit method"], "a": 0,
     "why": "FIFO: most businesses genuinely sell their oldest goods first."},
    {"q": "In a period of inflation, the cost flow method that results in the lowest income taxes is the:", "o": [
        "FIFO method", "LIFO method", "average-cost method", "gross profit method"], "a": 1,
     "why": "LIFO charges the newest, highest costs to cost of goods sold, so taxable income is lowest."},
    {"q": "Understating ending inventory will overstate:", "o": [
        "assets", "cost of goods sold", "net income", "stockholders' equity"], "a": 1,
     "why": "Lower ending inventory means more cost stays in cost of goods sold. Assets, net income and equity are all understated."},
    {"q": "A manufacturing company reports which three inventory accounts?", "o": [
        "Merchandise, supplies, equipment", "Raw materials, work in process, finished goods",
        "Purchases, freight-in, returns", "Direct materials, overhead, cost of goods sold"], "a": 1,
     "why": "And all three are current assets."},
    {"q": "Houston Electronics has 1,000 units costing $12,000 available and 450 units left. Under FIFO, ending inventory is:", "o": [
        "$5,000", "$5,400", "$5,800", "$6,200"], "a": 2,
     "why": "400 @ $13 + 50 @ $12 = $5,800. $5,000 is LIFO, $5,400 average-cost, $6,200 is FIFO cost of goods sold."},
    {"q": "With the same data, average-cost ending inventory is:", "o": [
        "$5,175", "$5,400", "$5,767", "$6,600"], "a": 1,
     "why": "$12,000 ÷ 1,000 = $12.00 per unit; 450 × $12 = $5,400."},
    {"q": "Which statement about the weighted-average unit cost is true?", "o": [
        "It is the simple average of the unit prices",
        "It is cost of goods available for sale ÷ units available for sale",
        "It is recomputed after every sale in a periodic system",
        "It always equals the most recent purchase price"], "a": 1,
     "why": "Purchases of different sizes must be weighted, so you divide total cost by total units."},
    {"q": "Goods held on consignment by a store should be:", "o": [
        "included in the store's inventory", "excluded from the store's inventory",
        "split equally between the two parties", "recorded as a purchase when received"], "a": 1,
     "why": "Ownership never passes to the consignee, so the consignor keeps them in inventory."},
    {"q": "Which method gives the same ending inventory under both periodic and perpetual systems?", "o": [
        "LIFO", "FIFO", "Average-cost", "All three"], "a": 1,
     "why": "FIFO. LIFO and average-cost depend on what is on hand at the moment of each sale."},
    {"q": "An error that overstates ending inventory this year will, next year:", "o": [
        "overstate net income again", "understate net income",
        "have no effect on net income", "overstate assets again"], "a": 1,
     "why": "It becomes an overstated beginning inventory, so cost of goods sold is overstated and net income understated. The two years cancel."},
    {"q": "Under the LIFO conformity rule, a company that uses LIFO for tax purposes must:", "o": [
        "also use LIFO for financial reporting", "use FIFO for financial reporting",
        "disclose FIFO values only", "switch methods every three years"], "a": 0,
     "why": "Tax and reporting must agree."},
    {"q": "In P6.8A the January 10 sale return of 10 units is recorded under LIFO at:", "o": [
        "$15", "$18", "$20", "$28"], "a": 1,
     "why": "Returns go back in at the cost they were sold at; that sale was costed at $18."},
    {"q": "In P6.5A, cost of goods available for sale is:", "o": [
        "$9,625", "$11,225", "$11,590", "$12,000"], "a": 1,
     "why": "$1,600 beginning + $9,625 net purchases = $11,225. $11,590 is net sales."},
    {"q": "Which disclosure is NOT required for inventory?", "o": [
        "Major inventory classifications", "Basis of accounting",
        "Costing method used", "Names of major suppliers"], "a": 3,
     "why": "The first three are required; supplier names are not."},
]

BLANKS = [
    {"s": "Cost of goods available for sale − ending inventory = ___.", "a": ["cost of goods sold", "COGS"]},
    {"s": "A manufacturing company classifies inventory as raw materials, work in process and ___.", "a": ["finished goods"]},
    {"s": "All inventories are reported on the balance sheet as ___ assets.", "a": ["current"]},
    {"s": "Under FOB ___, ownership passes when the public carrier accepts the goods from the seller.", "a": ["shipping point", "shipping-point"]},
    {"s": "Under FOB destination, ownership stays with the ___ until the goods reach the buyer.", "a": ["seller"]},
    {"s": "Goods held for another party to sell for a fee, without transfer of ownership, are ___ goods.", "a": ["consigned", "consignment"]},
    {"s": "Hasbeen Company's corrected inventory is $___.", "a": ["195,000", "195000"]},
    {"s": "Inventory cost includes all expenditures necessary to acquire goods and put them in a condition ready for ___.", "a": ["sale"]},
    {"s": "The actual physical flow costing method is ___ identification.", "a": ["specific"]},
    {"s": "FIFO ending inventory is remembered by the mnemonic ___ (last in still here).", "a": ["LISH"]},
    {"s": "LIFO ending inventory is remembered by the mnemonic ___ (first in still here).", "a": ["FISH"]},
    {"s": "Weighted-average unit cost = cost of goods available for sale ÷ ___.", "a": ["units available for sale", "total units available for sale", "total units"]},
    {"s": "In the Houston Electronics example the weighted-average unit cost is $___.", "a": ["12", "12.00"]},
    {"s": "In a period of rising prices, ___ produces the highest net income.", "a": ["FIFO"]},
    {"s": "In a period of rising prices, ___ produces the lowest income taxes.", "a": ["LIFO"]},
    {"s": "The rule that a company using LIFO for tax must also use it for reporting is the LIFO ___ rule.", "a": ["conformity"]},
    {"s": "An overstated ending inventory ___ cost of goods sold.", "a": ["understates", "understated"]},
    {"s": "An inventory error affects net income in ___ periods.", "a": ["two", "2"]},
    {"s": "On the income statement, cost of goods sold is subtracted from ___.", "a": ["sales", "sales revenue", "net sales"]},
    {"s": "Inventory turnover = cost of goods sold ÷ ___ inventory.", "a": ["average"]},
    {"s": "Days in inventory = ___ ÷ inventory turnover.", "a": ["365"]},
    {"s": "The only method whose answer is identical under periodic and perpetual systems is ___.", "a": ["FIFO"]},
    {"s": "In P6.5A gross profit under FIFO is $___.", "a": ["4,830", "4830"]},
    {"s": "In P6.8A gross profit under LIFO is $___.", "a": ["2,160", "2160"]},
    {"s": "In P6.8A the cost of goods available for sale is $___.", "a": ["5,460", "5460"]},
]

DRILL = [
    {"task": "Company counted $200,000. It included $15,000 of goods held on consignment and left out $10,000 of purchases in transit FOB shipping point. Correct inventory?",
     "cmd": ["200,000 - 15,000 (not ours: consignor's)", "        + 10,000 (title already passed to us)", "        = 195,000"]},
    {"task": "1,000 units cost $12,000 available; 450 units left; purchases were 100@$10, 200@$11, 300@$12, 400@$13. FIFO ending inventory and cost of goods sold?",
     "cmd": ["EI  = 400 x 13 + 50 x 12 = 5,800", "COGS = 12,000 - 5,800   = 6,200"]},
    {"task": "Same data, LIFO.",
     "cmd": ["EI  = 100 x 10 + 200 x 11 + 150 x 12 = 5,000", "COGS = 12,000 - 5,000 = 7,000"]},
    {"task": "Same data, average-cost.",
     "cmd": ["unit = 12,000 / 1,000 = 12.00", "EI   = 450 x 12.00 = 5,400", "COGS = 12,000 - 5,400 = 6,600"]},
    {"task": "Ending inventory is understated by $5,000. What happens to cost of goods sold, net income, assets and equity?",
     "cmd": ["COGS      overstated  5,000", "Net income understated 5,000", "Assets    understated 5,000", "Equity    understated 5,000"]},
    {"task": "P6.5A: state cost of goods available for sale, units sold and ending inventory units.",
     "cmd": ["available: 40 + 135 + 55 - 10 + 35 = 255 units, $11,225", "sold:     110 - 15 + 65 = 160 units", "ending:   95 units"]},
    {"task": "P6.5A: gross profit rate under FIFO.",
     "cmd": ["GP   = 11,590 - 6,760 = 4,830", "rate = 4,830 / 11,590 = 41.7%"]},
    {"task": "P6.8A: moving average after the January 15 purchase.",
     "cmd": ["balance 140 units, 2,345.00", "+ 55 @ 20 = 1,100  ->  195 units, 3,445.00", "avg = 3,445 / 195 = 17.667"]},
    {"task": "Perpetual LIFO sale on January 20 of 90 units, layers on hand 100@$15, 40@$18, 50@$20.",
     "cmd": ["newest first: 50 @ 20 = 1,000", "              40 @ 18 =   720", "COGS for this sale     = 1,720"]},
]


def s_checklist():
    return """
<h2><small>Night before</small>Must be automatic</h2>
<ol class="steps">
<li><b>The formula</b>Beginning inventory + purchases = cost of goods available for sale; minus ending inventory = cost of goods sold.</li>
<li><b>Three manufacturing classes</b>Raw materials, work in process, finished goods — all current assets.</li>
<li><b>FOB rules</b>Shipping point → buyer owns in transit. Destination → seller owns in transit.</li>
<li><b>Consignment</b>Consignee never owns; consignor counts the goods.</li>
<li><b>Four methods</b>Specific identification, FIFO, LIFO, average-cost. Assumptions need not match physical flow.</li>
<li><b>LISH and FISH</b>FIFO leaves the newest costs in inventory; LIFO leaves the oldest.</li>
<li><b>Weighted average</b>Total cost ÷ total units, never the average of prices.</li>
<li><b>Rising prices</b>FIFO: highest inventory, highest net income, highest tax. LIFO: lowest net income, lowest tax. Average in between.</li>
<li><b>LIFO conformity rule</b>LIFO for tax means LIFO for reporting.</li>
<li><b>Error effects</b>Ending inventory overstated → cost of goods sold understated → net income, assets and equity overstated; reverses next year.</li>
<li><b>Disclosure</b>Classifications, basis of accounting, costing method.</li>
<li><b>Perpetual</b>FIFO same as periodic; LIFO and moving-average differ. Recompute the average only after a purchase.</li>
<li><b>Your two problems</b>P6.5A gross profits 4,330 / 4,830 / 4,546.90 (LIFO/FIFO/average). P6.8A gross profits 2,160 / 2,560 / 2,420.55.</li>
<li><b>The check</b>Cost of goods sold + ending inventory = cost of goods available for sale, every time.</li>
</ol>
"""


def s_quiz():
    return """
<h2><small>Self-test</small>Quiz and drills</h2>
<p>Click an answer; the correct one turns green and the reason appears.</p>
<span class="score" id="mcq-score"></span> <button class="btn" id="mcq-reset">reset</button>
<div class="quiz" id="mcq"></div>
<h3>Fill in the blanks</h3>
<div class="quiz" id="blanks"></div>
<h3>Computation drills</h3>
<p>Work it on paper first, then reveal.</p>
<div class="drill" id="drill"></div>
"""


def sections():
    return [
        ("start", "Start", s_start()),
        ("basics", "From zero", s_basics()),
        ("lo1", "LO 1 Classify", s_lo1()),
        ("lo2", "LO 2 Cost flow", s_lo2()),
        ("errors", "LO 3 Errors", s_errors()),
        ("presentation", "LO 4 Presentation", s_presentation()),
        ("perpetual", "Appendix 6A", s_perpetual()),
        ("problems", "Worked problems", s_problems()),
        ("qa", "Q&A", s_qa()),
        ("quiz", "Quiz", s_quiz()),
        ("checklist", "Checklist", s_checklist()),
    ]
