import sqlite3


banks_data = [
    {
        "id": "1",
        "name": "Bank Audi"
    }, {
        "id": "2",
        "name": "Bank SGBL"
    }, {
        "id": "3",
        "name": "Bank Byblos"
    }, {
        "id": "4",
        "name": "Bank Beirut"
    }
]

employee_data = [
    {
        "id": "1",
        "bank_id": "1",
        "name": "jane doe",
        "salary": 1000.0
    }, {
        "id": "2",
        "bank_id": "2",
        "name": "john doe",
        "salary": 1250.0
    }, {
        "id": "3",
        "bank_id": "2",
        "name": "billy doe",
        "salary": 1050.0
    }, {
        "id": "4",
        "bank_id": "1",
        "name": "nathaly doe",
        "salary": 1500.0
    }, {
        "id": "5",
        "bank_id": "4",
        "name": "mike doe",
        "salary": 2000.0
    }, {
        "id": "6",
        "bank_id": "4",
        "name": "anthony doe",
        "salary": 1800.0
    }, {
        "id": "7",
        "bank_id": "2",
        "name": "jessica doe",
        "salary": 1400.0
    }, {
        "id": "8",
        "bank_id": "2",
        "name": "george doe",
        "salary": 1900.0
    }, {
        "id": "9",
        "bank_id": "3",
        "name": "jamal doe",
        "salary": 1100.0
    }, {
        "id": "10",
        "bank_id": "1",
        "name": "grace doe",
        "salary": 1400.0
    }
]

def seed_data():
    with sqlite3.connect('test.db') as conn:
        cursor = conn.cursor()
        for bank in banks_data:
            cursor.execute(f"INSERT INTO BANKS (BNK_ID,BNK_NAME) VALUES ({bank['id']},'{bank['name']}');")
        print("banks seeded successfully")
        for employee in employee_data:
            cursor.execute(f"INSERT INTO EMPLOYEES (EM_ID,EM_BANKID,EM_NAME,EM_SALARY) VALUES ({employee['id']},{employee['bank_id']},'{employee['name']}',{employee['salary']});")
        print("employees seeded successfully")
        conn.commit()

seed_data()