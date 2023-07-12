import sqlite3

# NOTE create tables
create_banks_stmt = """
    CREATE TABLE IF NOT EXISTS BANKS (
        BNK_ID INTEGER PRIMARY KEY,
        BNK_NAME VARCHAR(50)
    );
"""

create_codes_stmt = """
    CREATE TABLE IF NOT EXISTS EMPLOYEES (
        EM_ID INTEGER PRIMARY KEY,
        EM_BANKID INTEGER REFERENCES BANKS(BNK_ID),
        EM_NAME VARCHAR(100),
        EM_SALARY REAL
    );
"""

with sqlite3.connect('test.db') as conn:
    cursor = conn.cursor()
    cursor.execute(create_banks_stmt)
    cursor.execute(create_codes_stmt)
    conn.commit()
