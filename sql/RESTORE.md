
# PostgreSQL Restore – `threesixty_final.dump.zip`

1) **Unzip** the archive to get `threesixty_final.dump`

## A) If the dump is *custom format* (.dump)
```bash
# Create DB
createdb -U postgres threesixty

# Restore
pg_restore -U postgres -d threesixty -v "C:\path\to\threesixty_final.dump"
# or on Linux/Mac
pg_restore -U postgres -d threesixty -v /path/to/threesixty_final.dump
```

## B) If the dump is a *directory format* (a folder with toc.dat)
```bash
pg_restore -U postgres -d threesixty -v "C:\path\to\folder"
```

> **Fix common errors**
- *"does not appear to be a valid archive ('toc.dat' does not exist')"* → You selected the folder while the dump is a single-file custom format. Point to the `.dump` file itself.
- Use full paths without spaces or wrap them in quotes.
- Ensure PostgreSQL bin is on PATH (`pg_restore --version`).

## ERD Generation
- **pgAdmin**: Tools → ERD/Generate ERD (or use Database → ERD for newer versions)
- **SQL**: You can also export schema via `pg_dump -s` and convert with external tools.
