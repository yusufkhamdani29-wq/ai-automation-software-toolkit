# Workflow 10 — File Organisation — Find Anything in 30 Seconds

## The problem

Files land in Downloads with names like 'final_v2_REAL.pdf'. You waste time searching, and sometimes redo work you already did because you cannot find it.

## What you need

A folder of messy files and the two scripts in this toolkit (bulk_file_renamer.py and folder_organiser.py).

## Copy-paste prompts

### Prompt 1: Design the naming rule

```
My work files are mostly: [TYPES, e.g. client photos, invoices, contracts].

Suggest a file-naming rule using this pattern: YYYY-MM-DD_client_project_version. Give 3 examples with my file types, and list 3 common mistakes to avoid (vague names, 'final' in the name, dates in different formats).
```

### Prompt 2: Write the folder map

```
Design a folder structure for a small business with these areas: [AREAS, e.g. Clients, Finance, Marketing, Products]. Give the top-level folders and one level of subfolders. Keep it under 20 folders total. Add one line per folder explaining what belongs in it.
```

## Steps

1. Run prompts 1 and 2 and write down your naming rule and folder map.
2. Use folder_organiser.py (dry-run first) to sort the messy folder, then bulk_file_renamer.py to rename one batch.
3. From now on, save every new file with the naming rule on the spot — sorting later is what created the mess.

## Tools

The two Python scripts in this toolkit. Python 3.8+.

## Time saved

Searching for files costs most people 10–20 minutes a day. A naming rule plus one sorting pass usually cuts that to a couple of minutes — the saving compounds every day.
