from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import threading
import time

ghala = Flask(__name__)

DB = "Ghala.db"

# DATABASE CONNECTION & TABLES
def db_open():
    with sqlite3.connect(DB) as conn:
        query = conn.cursor()
        # MERCHANTS TABLE
        query.execute("""
            CREATE  TABLE IF NOT EXISTS merchants (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      method TEXT,
                      provider TEXT,
                      config TEXT
                      )
                """)
        # ORDERS TABLE
        query.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      merchant_id INTEGER,
                      product TEXT,
                      total REAL,
                      status TEXT DEFAULT 'pending'
                      )
                """)
        conn.commit()

# HOME PAGE
@ghala.route('/')
def home():
    return render_template('index.html')

# MERCHANT SETTINGS
@ghala.route('/merchant-settings', methods=['GET','POST'])
def merchant_settings():
    if request.method == 'POST':
        name = request.form['name']
        method = request.form['method']
        provider = request.form['provider']
        config = request.form['config']

        with sqlite3.connect(DB) as conn:
            query = conn.cursor()
            query.execute(
                "INSERT INTO merchants (name, method, provider, config) VALUES (?, ?, ?, ?)",
                (name, method, provider, config)
            )

            conn.commit()
        return redirect(url_for('home'))
    return render_template("merchant.html")

# CREATE ORDER
@ghala.route('/create-order', methods=['POST'])
def create_order():
    merchant_id = request.form['merchant_id']
    product = request.form['product']
    total = request.form['total']

    with sqlite3.connect(DB) as conn:
        query = conn.cursor()
        query.execute(
            "INSERT INTO orders (merchant_id, product, total) VALUES (?,?,?)",
            (merchant_id, product, total)
        )

        conn.commit()

    return redirect(url_for('view_orders'))

# VIEW ORDERS

@ghala.route('/orders')
def view_orders():
    with sqlite3.connect(DB) as conn:
        query = conn.cursor()
        query.execute("""
            SELECT o.id, m.name, o.product, o.total, o.status
            FROM orders o
            JOIN merchants m ON o.merchant_id = m.id
                      """)
        orders = query.fetchall()
    return render_template('orders.html', orders=orders)

# SIMULATE PAYMENT CONFIRMATION AFTER 5s
@ghala.route('/simulate-payment/<int:order_id>')
def simulate_payment(order_id):

    def update_delay():
        time.sleep(5)
        with sqlite3.connect(DB) as conn:
            query = conn.cursor()
            query.execute(
                "UPDATE orders SET status = 'paid' WHERE id = ?", (order_id,)
            )
            conn.commit()
    threading.Thread(target=update_delay).start()

    return redirect(url_for('view_orders'))

if __name__ == '__main__':
    db_open()
    ghala.run(debug=True)