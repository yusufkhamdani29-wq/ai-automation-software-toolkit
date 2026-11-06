# AI Automation & Software Toolkit — README

## Product summary

**Title:** AI Automation & Software Toolkit — 10 AI Workflows, Spreadsheet Automation, Tested Scripts & No-Code Templates
**Prices:** Starter $19 / Professional $49 / Premium $99
**Status:** Built and ready — NOT published (no Gumroad listing created, no live product changed).

A toolkit for small businesses that want their time back: 10 ready-to-use
AI workflows, spreadsheet automation, five tested Python scripts,
no-code templates, and browser productivity tools. No code is needed for
the workflows; the scripts need only copy-paste commands.

## Market context (estimates, not verified sales)

Market figures in this product are drawn from the **Gumroad Market Data
2026** dataset (github.com/Pinous/gumroad-market-data, CC BY 4.0, updated
March 2026; 146,271 products across 43,884 sellers). All revenue figures
from that dataset are **estimates**, not verified sales.

The dataset estimates the **Software Development** category at **$65.8M
revenue across 1,083 products (average price $39.95, average 293 sales
per product, median price $11.97, median 17 sales)**. Its price-tier data
shows the **$30–$49.99 band as the highest-sales band at a solid price**
(1,409 products, 268 average sales, ~$15.0M estimated revenue), with the
$50–$99.99 band close behind (~$14.5M). This product's three tiers
($19 / $49 / $99) sit in and around those bands. No sales, income, or
earnings are promised anywhere in this product.

## Built with Gemini 4 Argon Canvas

Part of this toolkit was built in a **Gemini 4 Argon Canvas** session on
6 November 2026 (chat: https://gemini.google.com/app/a9e04579a90acc08): 5 Canvas documents (AI workflows, spreadsheet automation,
Python scripts, no-code templates, browser tools) containing 23 files.
Every Canvas file was extracted, and every script, snippet, and table was
tested before anything joined the product (test log in `QC_LOG.md`).

Three Canvas files joined the product because they add new content that
passed testing: `prompts/AI-Workflows-Guide.md` and `prompts/prompts.txt`
(the 10 workflows as one guide and one plain-text pack), and
`spreadsheets/02-spreadsheet-automation.md` (specs for two more workbooks
to build yourself). The remaining Canvas files — alternative versions of
the Python scripts, Apps Script snippets, no-code tables, browser tools,
and their guides — are kept as source material in the `canvas/` folder
and are NOT part of the tier ZIPs. The tested files already in this kit
stay the canonical versions; nothing untested was shipped as a product file.

## Tier manifest

| File / folder | Starter $19 | Professional $49 | Premium $99 |
|---|---|---|---|
| `guide/AI_Automation_Software_Toolkit_Guide.pdf` (4 pp.) | ✓ | ✓ | ✓ |
| `guide/Quick_Start.pdf` (1 p.) | ✓ | ✓ | ✓ |
| `prompts/` — 10 AI workflow prompt packs (.md) + Canvas guide (`AI-Workflows-Guide.md`) + plain-text prompt pack (`prompts.txt`) | ✓ | ✓ | ✓ |
| `browser/` — 3 bookmarklets + 1 userscript | ✓ | ✓ | ✓ |
| `spreadsheets/` — 2 XLSX workbooks + 4 Apps Script snippets + README + Canvas workbook specs (`02-spreadsheet-automation.md`) | – | ✓ | ✓ |
| `no-code/` — Notion / Airtable / Trello templates + setup guide | – | ✓ | ✓ |
| `scripts/` — 5 Python scripts + sample data + setup README | – | – | ✓ |
| `examples/` — 3 worked examples (CSV cleaner, invoice generator, AI workflow) | – | – | ✓ |
| `checklist/Automation_Audit_Checklist.pdf` | – | – | ✓ |
| `worksheet/Automation_Worksheet.pdf` (fillable, 7 fields) | – | – | ✓ |
| `bonus/50_Automation_Prompts.md` + `bonus/Which_Tool_For_Which_Job.pdf` | – | – | ✓ |
| `LICENSE.txt` | ✓ | ✓ | ✓ |

ZIP files (built by `package_and_qc.py`):
- `AI-Automation-Software-Toolkit-Starter-19.zip` — Starter contents
- `AI-Automation-Software-Toolkit-Professional-49.zip` — Professional contents
- `AI-Automation-Software-Toolkit.zip` — Premium contents (the full kit)

## What's inside (Premium)

- **10 AI workflows** (`prompts/01`–`10`): content repurposing, email
  triage, meeting notes to tasks, research summarising, social
  scheduling, customer reply drafting, invoice chasing, lead
  qualification, weekly planning, file organisation. Each file: the
  problem, what you need, copy-paste prompts, steps, tools (free tiers),
  and an honest time-saved note. Also included: `prompts/AI-Workflows-Guide.md`
  and `prompts/prompts.txt` — the same 10 workflows as a single guide and
  a plain-text copy-paste pack, built with Gemini 4 Argon Canvas (see below).
- **Spreadsheet automation** (`spreadsheets/`): Business Automation
  Dashboard (Tasks / Invoices / Summary with live formulas — verified
  computing: 6 tasks, 290 min, $91.50 invoiced, $60 paid, $31.50
  outstanding) and Profit Calculator (Gumroad fees at 12.9% + $0.80 per
  order — verified: 20 orders × $5 = $100 gross, $28.90 fees, $61.10 net,
  61.1% margin), plus 4 Google Apps Script snippets (syntax-checked).
  Also included: `02-spreadsheet-automation.md` — cell-by-cell specs to
  build two more workbooks yourself (an Invoice Tracker with overdue
  flags and monthly rollups, and a Content Calendar with auto-status
  counts). Those two workbooks are specs only, not .xlsx files: the
  shipped workbooks do not include them, and no .xlsx was fabricated
  from the spec — follow the guide to build them in Excel or Google Sheets.
- **Business automation scripts** (`scripts/`): bulk file renamer,
  CSV cleaner, invoice PDF generator, folder organiser, daily report
  generator. All five were executed on the sample data before shipping;
  expected outputs are in `examples/`. Renamer and organiser default to
  dry-run.
- **No-code templates** (`no-code/`): Notion-style Business OS (4 CSV
  databases + 2 Markdown pages), Airtable-style base (4 CSV tables),
  Trello-style board (CSV + JSON, 5 lists, 8 cards), with a setup guide.
  Import-ready structures, not official integrations.
- **Browser tools** (`browser/`): 3 bookmarklets (copy page as Markdown,
  text counter, tab title cleaner) as an HTML page + plain-text file,
  and a Tampermonkey userscript (Alt+M). All JavaScript syntax-checked.
- **Worked examples** (`examples/`): CSV cleaner before/after (8 rows →
  5 rows), invoice generator (3 real PDFs: $11.00, $49.00, $6.50),
  AI workflow end-to-end (one blog post → 5 social posts + newsletter +
  60-second video script).
- **Checklist + worksheet**: 18-item automation audit checklist and a
  fillable 1-page worksheet (7 fields) to pick the buyer's first
  3 automations.
- **Bonus**: 50-prompt library and a "Which Tool for Which Job?" decision sheet.
- **Cover**: `cover/cover_1600x900.jpg`.

## Gumroad listing draft (copy-paste ready — NOT published)

**Title:** AI Automation & Software Toolkit — 10 AI Workflows, Spreadsheet Automation, Tested Scripts & No-Code Templates

**Subtitle:** Stop doing the same task by hand every day. 10 AI workflows, spreadsheet automation, tested scripts, and no-code templates — in one kit.

**Description:**
> You do the same tasks every day: triage the inbox, repurpose a post, chase an invoice, sort a folder. Each one takes 10 minutes. Together, they eat the day.
>
> This toolkit automates the repetitive work so you can keep the creative work.
>
> **What you get (Premium, $99):**
> - **10 AI workflow blueprints** — content repurposing, email triage, meeting notes to tasks, research summarising, social scheduling, customer replies, invoice chasing, lead qualification, weekly planning, and file organisation. Each one: the problem, copy-paste prompts, steps, and the free tools you need.
> - **Spreadsheet automation** — a business dashboard with live formulas (tasks, invoices, outstanding amounts) and a profit calculator with Gumroad fees built in, plus 4 Google Apps Script snippets.
> - **5 tested Python scripts** — bulk file renamer, CSV cleaner, invoice PDF generator, folder organiser, and daily report generator — with sample data and a setup guide. Every script was run before shipping.
> - **No-code templates** — a Business OS for Notion, Airtable, and Trello (import-ready structures with setup guides).
> - **Browser productivity tools** — 3 bookmarklets and a userscript: copy any page as Markdown, count words, clean tab titles.
> - **3 worked examples** — a CSV cleaned end to end, 3 invoices generated from one file, and one blog post turned into 8 pieces of content.
> - **Checklist + fillable worksheet** — audit your repetitive tasks and pick your first 3 automations.
> - **Bonus** — 50 extra automation prompts and a "which tool for which job" decision sheet.
>
> **Three tiers:**
> - Starter ($19) — the guide, Quick Start, 10 workflow packs, and browser tools.
> - Professional ($49) — Starter plus the spreadsheet workbooks, Apps Script snippets, and no-code templates.
> - Premium ($99) — everything, including the Python scripts, worked examples, checklist, worksheet, and bonuses.
>
> **How it works:** pick one repetitive task, open the matching workflow or script, follow the steps. The Quick Start gets your first automation running in 15 minutes.
>
> No code is needed for the workflows. The scripts need only copy-paste commands, and the renamer and organiser run in dry-run mode by default — they show you what they would do before changing anything.
>
> *Scripts are provided as-is, without warranty. AI prompts run in the AI chat tool of your choice; never paste private data into them. See the licence file for full terms.*

**Benefits (bullet list for the listing):**
- 10 ready-to-use AI workflows — copy, paste, done
- Spreadsheet dashboard and profit calculator with live formulas
- 5 Python scripts, actually tested before shipping — with sample data
- No-code templates for Notion, Airtable, and Trello
- Browser tools that run entirely on your own computer
- Worked examples show every tool doing real work
- Quick Start: your first automation running in 15 minutes

**FAQ:**
- *Do I need to know how to code?* No — for the workflows, spreadsheets, and no-code templates. The Python scripts need only copy-paste commands from the setup guide.
- *Do the scripts work on Windows and Mac?* Yes — Python 3.8+ runs on Windows, Mac, and Linux.
- *Can I use the templates for client work?* Yes — for your own business and client projects. You may not resell or redistribute the files as-is.
- *Do the AI prompts send my data anywhere?* The prompts run in the AI chat tool you choose. Never paste private data into them.
- *Are the scripts guaranteed?* No — they are provided as-is, without warranty. They were tested on the sample data before shipping, and the renamer and organiser default to dry-run mode.
- *What is the difference between the three tiers?* Starter has the workflows and browser tools; Professional adds spreadsheets and no-code templates; Premium adds the Python scripts, worked examples, checklist, worksheet, and bonuses.

**CTA:** Get the toolkit — automate your first task in 15 minutes.

**Suggested Gumroad settings:** Three separate listings (Starter $19, Professional $49, Premium $99) OR one Premium listing at $99 with the lower tiers as separate products. Cover: `cover/cover_1600x900.jpg`. Upload the matching tier ZIP as the product file for each listing.
