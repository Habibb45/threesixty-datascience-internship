
# ERD Image – Export Steps (pgAdmin)
1. Open **pgAdmin** and connect to your `threesixty` database.
2. Navigate to **Schemas → public → Tables**; verify tables and FKs.
3. Use the built-in ERD / Graph tool (version-dependent) or export schema via `pg_dump -s` and render with an external ERD tool.
4. Export the ERD as **PNG** and save to `docs/ERD.png`.
5. In `docs/ERD.md`, add: `![ERD](./ERD.png)`.
6. Also reference the image in `README.md`.
