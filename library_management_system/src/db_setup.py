import sqlite3
from config import DATABASE, SCHEMA_FILE

def load_schema():
    #Load schema from SQL file into SQLite db
    conn = sqlite3.connect(DATABASE)
    # Read and execute the schema file
    with open(SCHEMA_FILE, 'r') as file:
        schema = file.read()
        conn.executescript(schema)
    conn.commit()
    conn.close()
    print(f"Database '{DATABASE}' has been set up using '{SCHEMA_FILE}'.")
    # ENDDEF
