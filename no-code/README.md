# No-Code Templates — Setup Guide

These are import-ready structures for tools you already use. They are
**not** official integrations and are not affiliated with Notion, Airtable,
or Trello. You import the files below into your own workspace and adapt
them.

## Folder contents

- `notion/` — A Notion-style "Business OS": Markdown pages plus CSV tables
  you can import as databases (Tasks, Clients, Projects, Invoices).
- `airtable/` — CSV tables for an Airtable-style base (Clients, Projects,
  Tasks, Invoices) plus a field guide.
- `trello/` — A board structure (lists + cards) as JSON and CSV, plus a
  guide for recreating the board in Trello in about 10 minutes.

## Notion import (about 10 minutes)

1. In Notion, create a new page called "Business OS".
2. Import each CSV in `notion/` as a new database (Import > CSV).
   Notion maps the header row to properties automatically.
3. Create linked views: on the home page, add linked database views for
   Tasks (filter: Status = Open), Invoices (filter: Status = Open), and
   Clients.
4. Import `notion/Home.md` and `notion/Weekly-Review.md` as pages
   (Import > Markdown) and link them from the home page.

## Airtable import (about 10 minutes)

1. Create a blank base called "Business OS".
2. Create four tables (Clients, Projects, Tasks, Invoices) and import the
   matching CSV into each (Add table > Import data > CSV file).
3. Link the tables: Tasks → Projects (link field), Projects → Clients
   (link field), Invoices → Clients (link field).
4. Add a Gallery or Kanban view on Tasks grouped by Status.

## Trello setup (about 10 minutes)

Trello does not import a board from a JSON file directly, so use
`trello/board.csv` as the build list:

1. Create a board called "Business OS".
2. Create the lists in order: Inbox, This Week, Doing, Waiting, Done.
3. Add the cards from `board.csv` to the matching list (copy the Title;
   the Labels and Due columns map to Trello labels and due dates).
4. `board.json` holds the same structure in machine-readable form for
   tools that accept JSON board imports.

## What is inside

- **Tasks** — what needs doing, who owns it, when it is due.
- **Clients** — who you work for, with contact and rate.
- **Projects** — the work itself, linked to a client, with a status.
- **Invoices** — what you billed, what is paid, what is outstanding.

All sample rows are fictional (Acme Cafe, Budi Studio, Citra Bakery,
Dewi Crafts). Replace them with your own data.
