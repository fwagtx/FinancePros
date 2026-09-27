"""Template scripts for the rest of week 1 (Sep 27 - Oct 2), written by hand with the facts already verified for the week-1 episodes.
Run: python concepts/week_scripts.py  -> concepts/scripts/w1-*.json"""
import json, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts")


def L(text, t, say=None, who="ticker", **sc):
    return {"who": who, "text": text, "say": say or text, "scene": dict(t=t, **sc)}


CTA = L("That's the money. Follow for more.", "cta")
S = {}

S["w1-strong-dollar"] = {"header": "What a strong dollar\nmeans for you", "cover": {"title": "What a Strong Dollar Means", "countries": ["us", "japan"]}, "lines": [
    L("A strong dollar sounds like good news. It's more complicated than that.", "hook", title="What a [strong dollar] means", prop="bill"),
    L("It means one dollar buys more of other currencies.", "board", lines=["Strong dollar =", "$1 buys more abroad"]),
    L("Take a 100 euro hotel room. At a dollar ten per euro, it costs you 110 dollars.", "compare", say="Take a one hundred euro hotel room. At a dollar ten per euro, it costs you one hundred and ten dollars.",
      title="A €100 hotel, in dollars", left={"label": "€1 = $1.10", "value": "$110", "tone": "up", "sub": "stronger dollar"}, right={"label": "€1 = $1.25", "value": "$125", "tone": "down", "sub": "weaker dollar"}),
    L("At a dollar twenty-five, the same room costs 125. The stronger dollar saves you 15.", "compare", keep=True, winner="left", say="At a dollar twenty-five, the same room costs one hundred and twenty-five. The stronger dollar saves you fifteen."),
    L("It's good for travelers and imported goods. It's harder for U.S. companies selling abroad.", "split", title="Who wins, who doesn't",
      left={"title": "Easier", "items": ["Trips abroad", "Imported goods"], "tone": "up"}, right={"title": "Harder", "items": ["U.S. exporters", "Profits earned abroad"], "tone": "down"}),
    L("And exchange rates move every trading day, so this changes all the time.", "countries", cast=[{"name": "us", "mood": "happy", "says": "my $ goes far!"}, {"name": "japan", "mood": "worried"}], caption="rates move every trading day"),
    CTA]}

S["w1-buy-borrow-die"] = {"header": "How the rich avoid\nselling their stock", "cover": {"title": "Why Billionaires Borrow Instead of Selling", "prop": "bag", "label": "LOAN"}, "lines": [
    L("Why do billionaires borrow money when they're already rich? Because selling costs them.", "hook", title="Why the rich [borrow]", prop="bag", label="LOAN"),
    L("Sell stock that went up, and you owe capital gains tax on the profit.", "board", lines=["Sell stock that grew", "= capital gains tax"]),
    L("So instead, they borrow against their stock. A loan isn't income, so there's no tax on it.", "compare", title="Two ways to get cash",
      left={"label": "Sell the stock", "value": "taxed", "tone": "down", "sub": "capital gains"}, right={"label": "Borrow against it", "value": "no tax", "tone": "up", "sub": "a loan isn't income"}),
    L("The stock keeps growing, and they pay interest on the loan instead.", "compare", keep=True, winner="right"),
    L("People call it buy, borrow, die. Buy assets. Borrow against them. And hold them until death.", "list", title="Buy, borrow, die", items=["Buy assets that grow", "Borrow against them", "Hold them for life"], reveal=3),
    L("Under current U.S. law, heirs usually get a stepped-up basis, so the gains during the owner's life may never be taxed.", "board", lines=["Heirs get a", "stepped-up basis", "(current U.S. law)"]),
    L("It only works with a lot of assets, and borrowing always carries risk if prices fall.", "hook", title="Big assets. Big [risk].", prop="chart-down", mood="worried"),
    CTA]}

S["w1-rule-of-72"] = json.load(open(os.path.join(OUT, "rule-of-72.json")))

S["w1-acorn-dca"] = {"series": "acorn", "header": "Dollar-cost averaging,\nexplained with acorns", "cover": {"title": "Dollar-Cost Averaging, With Acorns", "prop": "acorns"}, "lines": [
    L("Squirrel wants to buy acorns. But acorn prices change every day.", "squirrel", who="nutty", kind="think", caption="acorn prices?"),
    L("Squirrel could wait for the perfect day. Squirrel never knows the perfect day.", "squirrel", who="nutty", kind="wait", caption="waiting..."),
    L("So squirrel buys a little every month, no matter the price. That's dollar-cost averaging.", "board", who="nutty", lines=["Same amount,", "every month,", "any price"]),
    L("When acorns are cheap, the same money buys more. When they're expensive, it buys fewer.", "compare", who="nutty", title="$100 every month",
      left={"label": "acorns at $10", "value": "10", "tone": "up", "sub": "acorns bought"}, right={"label": "acorns at $20", "value": "5", "tone": "down", "sub": "acorns bought"}),
    L("Over those two months, squirrel paid 200 dollars for 15 acorns. About 13.33 each, less than the 15 dollar average price.", "stat", who="nutty",
      say="Over those two months, squirrel paid two hundred dollars for fifteen acorns. About thirteen dollars thirty-three each, less than the fifteen dollar average price.",
      label="$200 for 15 acorns", value="$13.33", sub="each, vs a $15 average price", tone="up"),
    L("It doesn't promise profits, and prices can fall. But it takes the guessing out.", "squirrel", who="nutty", kind="basket", label="EVERY MONTH"),
    L("Squirrel explained dollar-cost averaging. Squirrel would like one follow.", "cta", who="nutty")]}

S["w1-myth-renting"] = {"header": "Is renting really\nthrowing money away?", "cover": {"title": "Is Renting Throwing Money Away?", "prop": "house", "value": "MYTH?"}, "lines": [
    L("Myth: renting is throwing money away.", "hook", title="Renting = [wasted] money?", prop="house", value="MYTH?"),
    L("Owners throw money away too. It's just called something else.", "board", lines=["Owners have", "unrecoverable costs too"]),
    L("Mortgage interest, property taxes, insurance and repairs never come back to you.", "list", title="Money owners don't get back", items=["Mortgage interest", "Property taxes", "Insurance", "Repairs"], reveal=4),
    L("One popular rule of thumb puts those costs at around 5% of the home's value per year.", "stat", say="One popular rule of thumb puts those costs at around five percent of the home's value per year.",
      label="A rule of thumb for owners' yearly costs", value="~5%", sub="of the home's value (varies a lot)", tone="neutral"),
    L("On a 400,000 dollar home, that's about 20,000 dollars a year, or 1,667 a month.", "money", say="On a four hundred thousand dollar home, that's about twenty thousand dollars a year, or sixteen hundred sixty-seven a month.",
      **{"from": {"label": "home value", "value": "$400,000"}, "to": {"label": "a year in unrecoverable costs", "value": "~$20,000"}}),
    L("So compare rent to that number, not to the whole mortgage payment. Sometimes renting wins, sometimes buying does.", "compare", title="Compare the right numbers",
      left={"label": "Rent", "value": "rent", "tone": "neutral", "sub": "all unrecoverable"}, right={"label": "Own", "value": "~5%", "tone": "neutral", "sub": "unrecoverable part"}),
    CTA]}

S["w1-scam-toll-texts"] = {"header": "That toll text\nis a scam", "cover": {"title": "That Toll Text Is a Scam", "prop": "car", "value": "SCAM"}, "lines": [
    L("You owe 4 dollars and 15 cents in unpaid tolls. Pay now or get fined. That text is a scam.", "hook", title="The [unpaid toll] text", prop="car", value="SCAM", say="You owe four dollars and fifteen cents in unpaid tolls. Pay now or get fined. That text is a scam."),
    L("The FBI and the Federal Trade Commission have warned about fake toll texts sent to people across the country.", "news", headline="FBI, FTC warn of fake unpaid-toll texts", source="FBI IC3 and FTC consumer alerts"),
    L("The link goes to a fake payment page that steals your card number.", "board", lines=["The link =", "a fake payment page"]),
    L("Red flags: a tiny amount, a threat, and a link you didn't ask for.", "list", title="Red flags", items=["A tiny amount due", "A threat or deadline", "A link you didn't ask for"], reveal=3),
    L("Don't click. Check your account on the toll agency's real website, and forward the text to 7726.", "list", title="What to do", items=["Don't click the link", "Check the official site", "Forward to 7726 (SPAM)"], reveal=3,
      say="Don't click. Check your account on the toll agency's real website, and forward the text to seven seven two six."),
    L("Send this to someone who drives. That's the money.", "cta")]}

S["w1-stocks"] = {"header": "What a stock\nactually is", "cover": {"title": "What Is a Stock, Really?", "prop": "chart-up"}, "lines": [
    L("Everyone talks about stocks. But what are you actually buying?", "hook", title="What is a [stock]?", prop="chart-up"),
    L("A stock is a tiny piece of ownership in a company. Each piece is called a share.", "board", lines=["1 share =", "a tiny piece of", "a company"]),
    L("If a company has a million shares and you own a hundred, you own one hundredth of one percent.", "stat", label="100 shares of 1,000,000", value="0.01%", sub="small, but real ownership", tone="up",
      say="If a company has a million shares and you own a hundred, you own one hundredth of one percent."),
    L("You can make money two ways: the price goes up, or the company pays a dividend.", "list", title="How owners make money", items=["The price goes up", "Dividends (some companies)"], reveal=2),
    L("But prices can fall, even to zero. That's why many people spread their money across many companies.", "hook", title="Prices can [fall] too", prop="chart-down", mood="worried"),
    CTA]}

S["w1-roth-vs-traditional"] = {"header": "Roth vs traditional:\npay tax now or later?", "cover": {"title": "Roth or Traditional IRA?", "prop": "bag", "label": "IRA"}, "lines": [
    L("Roth IRA or traditional IRA? It comes down to one question: pay the tax now, or later?", "hook", title="Pay the tax [now] or later?", prop="bag", label="IRA"),
    L("Traditional: your contributions may be tax-deductible now, and withdrawals are taxed as income in retirement.", "compare", title="Two kinds of IRA",
      left={"label": "Traditional", "value": "later", "tone": "neutral", "sub": "tax break now"}, right={"label": "Roth", "value": "now", "tone": "neutral", "sub": "tax-free later"}),
    L("Roth: you put in money you've already paid tax on, and qualified withdrawals in retirement are tax-free.", "board", lines=["Roth: taxed going in,", "qualified withdrawals", "tax-free"]),
    L("Rule of thumb: if you expect a higher tax rate later, a Roth often wins. If you expect a lower one, traditional can.", "split", title="Rule of thumb",
      left={"title": "Higher rate later?", "items": ["Roth often wins"], "tone": "up"}, right={"title": "Lower rate later?", "items": ["Traditional can win"], "tone": "up"}),
    L("Roth IRAs have income limits. Either way, starting early matters most.", "hook", title="Either way: [start early]", prop="chart-up", mood="up"),
    CTA]}

S["w1-tax-bracket-myth"] = {"header": "Can a raise make you\ntake home less?", "cover": {"title": "Can a Raise Lower Your Pay?", "prop": "bill", "value": "MYTH"}, "lines": [
    L("Myth: a raise can push you into a higher tax bracket and leave you with less money.", "hook", title="A raise that [costs] you?", prop="bill", value="MYTH"),
    L("Federal income tax brackets don't work that way. Only the dollars above each line get the higher rate.", "board", lines=["Only the dollars", "ABOVE the line", "get the higher rate"]),
    L("Simple example: say the 22% bracket starts at 50,000, and your pay rises from 49,000 to 51,000.", "compare", title="Tax on a $2,000 raise (simplified)",
      say="Simple example: say the twenty-two percent bracket starts at fifty thousand, and your pay rises from forty-nine to fifty-one thousand.",
      left={"label": "$1,000 below the line", "value": "$120", "tone": "neutral", "sub": "at 12%"}, right={"label": "$1,000 above it", "value": "$220", "tone": "down", "sub": "at 22%"}),
    L("That's 340 dollars in federal income tax. You keep the rest of the raise.", "stat", label="Extra federal income tax", value="$340", sub="the rest of the $2,000 is yours", tone="up",
      say="That's three hundred forty dollars in federal income tax. You keep the rest of the raise."),
    L("So take the raise. Higher brackets only touch the top slice.", "hook", title="Take the [raise]", prop="coins", mood="up"),
    CTA]}

S["w1-50-30-20"] = {"header": "The 50/30/20 budget\nin 40 seconds", "cover": {"title": "The 50/30/20 Budget", "prop": "coins", "value": "50/30/20"}, "lines": [
    L("The simplest budget out there fits in three numbers: 50, 30, 20.", "hook", title="The [50/30/20] budget", prop="coins", say="The simplest budget out there fits in three numbers: fifty, thirty, twenty."),
    L("50% of your take-home pay goes to needs, 30% to wants, and 20% to savings or extra debt payments.", "list", title="Of your take-home pay", items=["50% needs", "30% wants", "20% savings or debt"], reveal=3,
      say="Fifty percent of your take-home pay goes to needs, thirty percent to wants, and twenty percent to savings or extra debt payments."),
    L("On 3,000 dollars a month after taxes, that's 1,500, 900 and 600.", "compare", title="$3,000 a month, after taxes", say="On three thousand dollars a month after taxes, that's fifteen hundred, nine hundred, and six hundred.",
      left={"label": "Needs + wants", "value": "$2,400", "tone": "neutral", "sub": "$1,500 + $900"}, right={"label": "Savings", "value": "$600", "tone": "up", "sub": "every month"}),
    L("It was popularized by Elizabeth Warren and Amelia Warren Tyagi in their book, All Your Worth.", "board", lines=["Popularized by", "Elizabeth Warren &", "Amelia Warren Tyagi"]),
    L("It's a starting point, not a law. If rent takes more than half, adjust the split.", "board", lines=["A starting point,", "not a law"]),
    CTA]}

S["w1-paycheck"] = {"header": "Where your paycheck goes\nbefore you see it", "cover": {"title": "Where Your Paycheck Goes", "prop": "bill", "label": "$4,000", "value": "-$306"}, "lines": [
    L("Your paycheck says one number. Your bank account gets a smaller one. Here's where the rest goes.", "hook", title="Where your [paycheck] goes", prop="bill", label="$4,000"),
    L("Gross pay is what you earn. Net pay is what actually lands in your account.", "compare", title="Gross vs net",
      left={"label": "Gross pay", "value": "earned", "tone": "neutral"}, right={"label": "Net pay", "value": "landed", "tone": "up"}),
    L("First, Social Security and Medicare take 7.65% of most paychecks.", "stat", label="Social Security 6.2% + Medicare 1.45%", value="7.65%", sub="of most paychecks", tone="down",
      say="First, Social Security and Medicare take seven point six five percent of most paychecks."),
    L("On 4,000 dollars a month, that's 306 dollars.", "money", say="On four thousand dollars a month, that's three hundred and six dollars.",
      **{"from": {"label": "monthly pay", "value": "$4,000"}, "to": {"label": "$248 + $58", "value": "-$306"}}),
    L("Then federal income tax, state income tax in most states, and anything you signed up for, like health insurance or a 401k.", "list", title="Also taken out",
      items=["Federal income tax", "State income tax", "Health insurance, 401(k)"], reveal=3,
      say="Then federal income tax, state income tax in most states, and anything you signed up for, like health insurance or a four oh one k."),
    L("Read your pay stub once. It lists every dollar, and it's how you catch mistakes.", "hook", title="Read your [pay stub] once", prop="paper", label="PAY STUB", mood="happy"),
    CTA]}

S["w1-hysa"] = {"header": "Is your savings paying\nyou almost nothing?", "cover": {"title": "Is Your Savings Paying Nothing?", "prop": "pot", "value": "$20?"}, "lines": [
    L("Is your savings account paying you almost nothing?", "hook", title="Savings paying [nothing]?", prop="mattress"),
    L("A high-yield savings account pays a much higher interest rate, often at online banks.", "board", lines=["High-yield savings =", "a higher rate", "(often online banks)"]),
    L("Here's 5,000 dollars for a year at example rates of 0.4% versus 3.5%.", "compare", title="$5,000 for one year (example rates)",
      say="Here's five thousand dollars for a year at example rates of zero point four percent, versus three point five percent.",
      left={"label": "Savings at 0.4%", "value": "$20", "tone": "down"}, right={"label": "High-yield at 3.5%", "value": "$175", "tone": "up"}),
    L("Look for FDIC insurance, which covers up to 250,000 dollars per depositor, per bank, per account type.", "stat", label="FDIC insurance limit", value="$250,000", sub="per depositor, per bank, per ownership type", tone="up",
      say="Look for F D I C insurance, which covers up to two hundred and fifty thousand dollars per depositor, per bank, per account type."),
    L("Rates change, so compare before you open one.", "hook", title="Rates [change]. Compare.", prop="chart-up"),
    CTA]}

S["w1-debit-vs-credit"] = {"header": "Debit vs credit:\nwhich is safer?", "cover": {"title": "Debit or Credit: Which Is Safer?", "prop": "card", "label": "DEBIT?"}, "lines": [
    L("Debit or credit? They look the same, but they work very differently.", "hook", title="Debit vs [credit]", prop="card"),
    L("Debit spends money you already have. Credit borrows it, and you pay it back.", "compare", title="Whose money is it?",
      left={"label": "Debit", "value": "yours", "tone": "neutral"}, right={"label": "Credit", "value": "borrowed", "tone": "neutral"}),
    L("Paying a credit card on time can build your credit score. Debit doesn't.", "split", title="Builds credit?",
      left={"title": "Debit", "items": ["No credit history"], "tone": "down"}, right={"title": "Credit", "items": ["Can build your score"], "tone": "up"}),
    L("And fraud? Federal law caps your credit card liability at 50 dollars. With debit, your protection depends on how fast you report it.", "compare", title="If it's stolen",
      say="And fraud? Federal law caps your credit card liability at fifty dollars. With debit, your protection depends on how fast you report it.",
      left={"label": "Credit card", "value": "$50 max", "tone": "up", "sub": "by federal law"}, right={"label": "Debit card", "value": "depends", "tone": "down", "sub": "on how fast you report"}),
    L("The catch: carry a balance on credit, and interest gets expensive fast.", "hook", title="Carry a balance? [Ouch].", prop="card", label="APR 24%", mood="worried"),
    CTA]}

S["w1-emergency-fund"] = {"header": "How big should your\nemergency fund be?", "cover": {"title": "How Big Is Your Emergency Fund?", "prop": "mattress", "value": "3-6 mo"}, "lines": [
    L("A car repair or a lost job shouldn't turn into credit card debt. That's what an emergency fund is for.", "hook", title="Your [emergency fund]", prop="car"),
    L("A common goal is three to six months of essential expenses.", "stat", label="The common goal", value="3-6 mo", sub="of essential expenses", tone="up"),
    L("If your essentials cost 2,500 a month, that's 7,500 to 15,000 dollars.", "compare", title="Essentials: $2,500 a month",
      say="If your essentials cost twenty-five hundred a month, that's seventy-five hundred to fifteen thousand dollars.",
      left={"label": "3 months", "value": "$7,500", "tone": "neutral"}, right={"label": "6 months", "value": "$15,000", "tone": "up"}),
    L("That sounds like a lot, so start small. A first goal of 500 dollars covers many surprise bills.", "timeline", events=[["Step 1", "$500 starter"], ["Step 2", "1 month of essentials"], ["Step 3", "3 to 6 months"]], reveal=3,
      say="That sounds like a lot, so start small. A first goal of five hundred dollars covers many surprise bills."),
    L("Automate it, keep it in a separate savings account, and only use it for real emergencies.", "board", lines=["Automate it.", "Keep it separate.", "Emergencies only."]),
    CTA]}

# ---------------- Wednesday long-form: Credit scores, completely explained ----------------
LF = []
def A(text, t, **k): LF.append(L(text, t, **k))
A("A three-digit number can change what you pay for a car, an apartment, and even a phone plan.", "hook", title="3 digits that [price] your life", prop="card", label="742")
A("It's your credit score. Today we're going to take it apart, piece by piece, so you know exactly how it works.", "board", lines=["Your credit score,", "taken apart"])
A("Chapter one. What a credit score actually is.", "chapter", n=1, title="What a credit score is")
A("A credit score is a number that sums up how reliably you've paid back money you borrowed.", "board", lines=["A grade for how you", "pay back what you borrow"])
A("The most widely used one, the FICO score, runs from 300 to 850.", "stat", label="The FICO score range", value="300-850", sub="the most widely used score", tone="neutral", say="The most widely used one, the FICO score, runs from three hundred to eight hundred fifty.")
A("It's calculated from your credit reports, which are kept by three big credit bureaus.", "hook", title="Kept by 3 [credit bureaus]", prop="paper", label="CREDIT REPORT")
A("Equifax, Experian, and TransUnion.", "list", title="The 3 credit bureaus", items=["Equifax", "Experian", "TransUnion"], reveal=3)
A("Your credit report is the record. Your score is a grade calculated from that record.", "compare", title="Report vs score", left={"label": "Credit report", "value": "record", "tone": "neutral", "sub": "your history"}, right={"label": "Credit score", "value": "grade", "tone": "neutral", "sub": "calculated from it"})
A("And you don't have just one score. There are different models, like FICO and VantageScore, and lenders pick which one they use.", "board", lines=["FICO, VantageScore...", "lenders pick one"])
A("Why it matters: a higher score can mean lower interest rates, smaller deposits, and more yeses when you apply.", "list", title="A higher score can mean", items=["Lower interest rates", "Smaller deposits", "More approvals"], reveal=3)
A("Chapter two. The five things that make up your score.", "chapter", n=2, title="The five ingredients")
A("FICO publishes how much each part counts. Here's the whole recipe.", "list", title="The FICO recipe", items=["Payment history 35%", "Amounts owed 30%", "Length of history 15%", "New credit 10%", "Credit mix 10%"], reveal=5)
A("Payment history is the biggest piece, at thirty-five percent. Amounts owed is next, at thirty.", "compare", title="The two biggest pieces", left={"label": "Payment history", "value": "35%", "tone": "up"}, right={"label": "Amounts owed", "value": "30%", "tone": "up"})
A("Together, those two are almost two-thirds of your score. So let's start there.", "stat", label="Together", value="65%", sub="almost two-thirds of your score", tone="up")
A("Chapter three. Payment history.", "chapter", n=3, title="Payment history")
A("This one is simple: do you pay your bills on time?", "hook", title="Do you pay [on time]?", prop="tag", label="DUE")
A("A payment usually gets reported as late once it's thirty days past due.", "stat", label="Usually reported late at", value="30 days", sub="past due", tone="down")
A("And a late payment can stay on your credit report for up to seven years.", "stat", label="A late payment can stay", value="7 years", sub="on your credit report", tone="down")
A("Paying a day or two late usually means a late fee, not a hit to your credit report. The thirty-day mark is what counts.", "board", lines=["1-2 days late = late fee", "30 days late = credit hit"])
A("If you do miss one, pay it as fast as you can. The longer it goes, the worse it gets, at sixty and ninety days.", "timeline", events=[["30 days", "reported late"], ["60 days", "worse"], ["90 days", "worse still"]], reveal=3)
A("The easiest fix is autopay for at least the minimum, so a busy week never becomes a late payment.", "hook", title="Turn on [autopay]", prop="card", label="AUTOPAY", mood="up")
A("Chapter four. Amounts owed.", "chapter", n=4, title="Amounts owed")
A("A big part of this is your credit utilization.", "board", lines=["Credit utilization =", "balance ÷ limit"])
A("If your limit is five thousand dollars and you owe one thousand, you're using twenty percent.", "stat", label="$1,000 owed on a $5,000 limit", value="20%", sub="credit utilization", tone="neutral")
A("Lower usage generally helps your score. Here's how the same five thousand dollar limit looks at different balances.", "compare", title="Same $5,000 limit", left={"label": "$500 owed", "value": "10%", "tone": "up"}, right={"label": "$4,000 owed", "value": "80%", "tone": "down"})
A("A common rule of thumb is to stay under thirty percent, and lower is better.", "stat", label="Common rule of thumb", value="< 30%", sub="lower is better", tone="up")
A("Paying your balance before the statement date can also lower the number that gets reported.", "board", lines=["Pay before the", "statement date"])
A("The good news: card balances are usually reported monthly, so paying them down can show up in your score fairly quickly.", "hook", title="Reported [monthly]", prop="chart-up", mood="up")
A("Chapter five. The last three pieces.", "chapter", n=5, title="The last three pieces")
A("Length of history is fifteen percent. Older accounts help, so closing your oldest card can shorten your history.", "stat", label="Length of history", value="15%", sub="older accounts help", tone="neutral")
A("New credit covers hard inquiries.", "stat", label="New credit", value="10%", sub="hard inquiries", tone="neutral")
A("A hard inquiry stays on your report for two years, and FICO scores only count it for about one year.", "timeline", events=[["Day 1", "hard inquiry"], ["~1 year", "FICO stops counting it"], ["2 years", "off your report"]], reveal=3)
A("Shopping around for a mortgage or car loan? Scoring models usually count several of those checks in a short window as one.", "board", lines=["Rate shopping:", "several checks", "count as one"])
A("Opening several new cards at once is different. It adds inquiries and lowers the average age of your accounts.", "split", title="Many new cards at once", left={"title": "Adds", "items": ["Hard inquiries"], "tone": "down"}, right={"title": "Lowers", "items": ["Average account age"], "tone": "down"})
A("And credit mix means having different kinds, like a card and an installment loan. It's the smallest piece, so never borrow just to improve it.", "stat", label="Credit mix", value="10%", sub="never borrow just to improve it", tone="neutral")
A("Chapter six. Checking your credit, for free.", "chapter", n=6, title="Checking your credit, free")
A("You can get free credit reports from all three bureaus every week at AnnualCreditReport dot com.", "stat", label="Free reports, every week", value="3 bureaus", sub="AnnualCreditReport.com", tone="up")
A("Checking your own credit is a soft inquiry, so it doesn't hurt your score.", "hook", title="Checking yours = [soft] check", prop="none", value="no hit", mood="happy")
A("Look for accounts you don't recognize or payments marked late by mistake, and dispute errors with the bureau.", "list", title="What to look for", items=["Accounts you don't know", "Wrong late payments", "Dispute any errors"], reveal=3)
A("Chapter seven. Starting from zero.", "chapter", n=7, title="Starting from zero")
A("If you have no credit history, you can't have a score yet. Here are the common ways people start.", "list", title="Common ways to start", items=["A secured credit card", "Authorized user", "Credit-builder loan"], reveal=3)
A("Whichever you use, the same rules apply: small balances, paid on time, every month.", "board", lines=["Small balances,", "paid on time,", "every month"])
A("Chapter eight. Myths that cost people money.", "chapter", n=8, title="Myths that cost money")
A("Myth: you need to carry a balance and pay interest to build credit.", "hook", title="Myth: carry a [balance]", prop="card", value="MYTH")
A("Fact: paying your full balance still shows on-time payments and low usage. You never have to pay interest to build credit.", "board", lines=["Pay in full =", "on time + low usage", "no interest needed"])
A("Myth: a higher income means a higher score. Fact: income isn't part of your credit score at all.", "compare", title="Does income count?", left={"label": "Your income", "value": "0%", "tone": "neutral", "sub": "not in your score"}, right={"label": "Payment history", "value": "35%", "tone": "up"})
A("Myth: closing an unused card always helps. It can actually hurt, because your total limit shrinks and your usage goes up.", "split", title="Closing an unused card", left={"title": "Your limit", "items": ["Total limit shrinks"], "tone": "down"}, right={"title": "Your usage", "items": ["Usage % goes up"], "tone": "down"})
A("Chapter nine. How long the bad stuff lasts.", "chapter", n=9, title="How long bad marks last")
A("Late payments and collections can stay for up to seven years. Some bankruptcies stay for up to ten.", "compare", title="How long marks can stay", left={"label": "Late payments, collections", "value": "7 yrs", "tone": "down"}, right={"label": "Some bankruptcies", "value": "10 yrs", "tone": "down"})
A("But their impact fades. Recent on-time payments matter more than old mistakes.", "board", lines=["Impact fades.", "Recent on-time payments", "matter more"])
A("So here's the whole thing in five moves.", "chapter", n=10, title="The whole thing in 5 moves")
A("Pay on time. Keep balances low. Keep old accounts open. And apply only when you need to.", "list", title="5 moves", items=["Pay on time", "Keep balances low", "Keep old accounts open", "Apply only when needed", "Check your reports"], reveal=4)
A("And check your reports every few months, for free, so nothing surprises you.", "list", keep=True, reveal=5)
A("Do those consistently, and your score takes care of itself over time.", "hook", title="Consistency [wins]", prop="chart-up", mood="up")
LF.append(L("That's the money. Follow for more.", "cta"))
S["w1-lf-credit-scores"] = {"format": "landscape", "cover": {"title": "Credit Scores, Completely Explained.", "prop": "card", "label": "742", "value": "300-850"}, "lines": LF}

for k, v in S.items():
    v = dict(v); v["id"] = k; v.setdefault("format", "vertical"); v.setdefault("series", "ticker")
    json.dump(v, open(os.path.join(OUT, k + ".json"), "w"), indent=1, ensure_ascii=False)
print(len(S), "scripts")
