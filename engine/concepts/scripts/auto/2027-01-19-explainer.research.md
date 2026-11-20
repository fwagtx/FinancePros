# Research brief: Marginal vs effective tax rate (posts Jan 19, 2027)

Scope: US FEDERAL INCOME TAX ONLY. No state tax, no FICA (Social Security/Medicare), no credits. Education only, not advice.

## Timely angle
- Tax season approaching: returns for tax year 2026 are filed in early 2027. The 2026 brackets and standard deduction below are what those returns use.
- IRS released the tax year 2026 inflation adjustments on Oct 9, 2025 (news release IR-2025-103; Revenue Procedure 2025-32), including amendments from the One, Big, Beautiful Bill Act (OBBBA, P.L. 119-21, signed July 4, 2025).

## Key facts (with dates)
- Seven federal income tax rates for tax year 2026 (unchanged): 10%, 12%, 22%, 24%, 32%, 35%, 37%. OBBBA made the TCJA rate structure permanent.
- 2026 single-filer taxable-income thresholds (IRS, Rev. Proc. 2025-32):
  - 10%: $0 to $12,400
  - 12%: over $12,400 to $50,400
  - 22%: over $50,400 to $105,700
  - 24%: over $105,700 to $201,775
  - 32%: over $201,775 to $256,225
  - 35%: over $256,225 to $640,600
  - 37%: over $640,600 (married filing jointly: over $768,700)
- 2026 standard deduction: $16,100 single / married filing separately; $32,200 married filing jointly; $24,150 head of household (IRS IR-2025-103).
- 2025 law change: OBBBA raised the tax year 2025 standard deduction to $15,750 single, $31,500 joint, $23,625 head of household (from the earlier inflation-adjusted $15,000 single).
- Definitions:
  - Marginal rate = the rate on your NEXT (last) dollar of taxable income, i.e. your top bracket.
  - Effective (average) rate = total tax divided by income (on taxable income or on gross income; say which).
  - Brackets apply in layers: each rate only applies to the dollars inside that bracket. Moving into a higher bracket only taxes the dollars above the threshold at the higher rate.

## Worked example (OUR MATH, tax year 2026, single filer, federal income tax only, standard deduction, no credits)
- Gross income: $75,000
- Minus 2026 standard deduction $16,100 -> taxable income $58,900
- 10% x $12,400 = $1,240
- 12% x ($50,400 - $12,400 = $38,000) = $4,560
- 22% x ($58,900 - $50,400 = $8,500) = $1,870
- Total federal income tax = $1,240 + $4,560 + $1,870 = $7,670
- Marginal rate: 22%
- Effective rate on taxable income: $7,670 / $58,900 = 13.02% (about 13%)
- Effective rate on gross income: $7,670 / $75,000 = 10.23% (about 10%)
- Only $8,500 of the $75,000 is taxed at 22%.

## Chartable series
A) OUR MATH: 2026 effective federal income tax rate on GROSS income, single filer, standard deduction only (x = gross income in $ thousands, evenly spaced):
| Gross | Taxable | Tax | Eff. on gross | Eff. on taxable |
|---|---|---|---|---|
| $25,000 | $8,900 | $890 | 3.56% | 10.0% |
| $50,000 | $33,900 | $3,820 | 7.64% | 11.27% |
| $75,000 | $58,900 | $7,670 | 10.23% | 13.02% |
| $100,000 | $83,900 | $13,170 | 13.17% | 15.70% |
| $125,000 | $108,900 | $18,734 | 14.99% | 17.20% |
Shows the effective rate rises smoothly (no cliff), always well below the top bracket rate.

B) REAL official series: single-filer standard deduction by tax year (IRS):
2022 $12,950; 2023 $13,850; 2024 $14,600; 2025 $15,750 (OBBBA); 2026 $16,100.

## The surprising fact
Someone "in the 22% bracket" at $75,000 gross (2026, single) pays about 10% of gross in federal income tax: only the last $8,500 of taxable income is taxed at 22%. A raise that crosses into a higher bracket never lowers take-home pay from federal income tax; only the dollars above the line get the higher rate.

## Uncertain / caveats
- IRS.gov pages could not be fetched directly from this session; thresholds confirmed via the IRS release snippet (standard deduction $16,100, 37% over $640,600) and multiple consistent secondary tables (Kiplinger, NerdWallet, Motley Fool, Experian) citing Rev. Proc. 2025-32.
- 2022/2023 standard deduction values from prior IRS releases (IR-2021-219, IR-2022-182); 2023 not re-confirmed by search this session.
- Real tax bills differ: credits, other deductions, state tax and FICA not included.

SOURCES:
- IRS, "IRS releases tax inflation adjustments for tax year 2026, including amendments from the One, Big, Beautiful Bill" (IR-2025-103, Oct 9, 2025): https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill
- IRS Revenue Procedure 2025-32 (2026 inflation adjustments)
- Kiplinger, 2026 tax brackets: https://www.kiplinger.com/taxes/tax-brackets/602222/income-tax-brackets
- NerdWallet, "IRS Announces 2026 Income Tax Brackets, Updated Standard Deduction": https://www.nerdwallet.com/article/taxes/tax-changes-2026
- Motley Fool, 2026 tax brackets under OBBB: https://www.fool.com/money/banks/articles/the-irs-just-announced-the-2026-tax-brackets-heres-whats-changing-under-the-one-big-beautiful-bill
- Axios, Oct 9, 2025: https://www.axios.com/2025/10/09/irs-2026-tax-brackets-deductions-credits
- Fox Business, IRS 2026 adjustments (2025 standard deduction $15,750 under OBBBA): https://foxbusiness.com/economy/irs-reveals-2026-tax-adjustments-changes-from-big-beautiful-bill
