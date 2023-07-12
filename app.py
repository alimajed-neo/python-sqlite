import sqlite3
import json
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get-banks')
def get_banks():
    with sqlite3.connect('test.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        result = cursor.execute("SELECT BNK_ID as id, BNK_NAME as name FROM BANKS")
        rows = result.fetchall()
    response = [{k: item[k] for k in item.keys()} for item in rows]
    return jsonify(response)

@app.route('/get-employees')
def get_employees():
    with sqlite3.connect('test.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        result = cursor.execute("SELECT EM_ID as id, EM_BANKID as bank_id, EM_NAME as name, EM_SALARY as salary FROM EMPLOYEES")
        rows = result.fetchall()
        print(rows)

    response = [{k: item[k] for k in item.keys()} for item in rows]
    return jsonify(response)

@app.route('/get-min-max-avg')
def get_min_max_avg():
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    with sqlite3.connect('test.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        result = cursor.execute("SELECT  MIN(EM_SALARY) as minimum_salary, MAX(EM_SALARY) as max_salary, AVG(EM_SALARY) as avg_salary FROM EMPLOYEES")
        rows = result.fetchall()
        print(rows)

    response = [{k: item[k] for k in item.keys()} for item in rows]
    return jsonify(response)

# write 2 queries that select bank having salaries > 1500