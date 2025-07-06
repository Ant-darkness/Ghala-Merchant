# Ghala Payment Simulation System

A simple Flask-based simulation system for managing merchant payments and customer orders. Each merchant can configure their own payment method, provider, and settings.
Orders simulate payment confirmation after a short delay.Tailwind css is used for clean and modern UI.

# Features
- Registor merchants with costome payment settings.
- Create orders linked to specific merchants.
- Simulated payment confirmation after 5seconds.
- Order status updates automatically.
- Dynamic form fields based on selected method.
- Built with Flask + SQlite + Tailwind CSS.

# ARCHITECTURE + THINKING

1.. Supporting multiple merchants. 
Since each merchant has their own name, method, provider adn a flexible config field stored in their merchants table.This allows different setups without changing the database structure.

2.. Supporting commission rates.
Add a commission_rate field to the merchants table. during oreders are processed:

    commission = total * commission_rate
    Merchant_get = total - commission
This support different agreements per merchant.

3.. Scaling to 10000+ merchants.
*Use PostgreSQL or MYSQL instead of SQLite.
*Add indexing example on merchant_id.
*Paginate orders view.
*Split services.

# How to run this project
To run this project locally on your computer:
1.Clone the repository

    git clone https://github.com/Ant-darkness/Ghala-Merchant.git

    cd Ghala-merchant

2. Install dependecies
   Make sure you have python installed (3.8+). Then install flask:

       pip install flask

3. Run flask server
   
       python ghala.py

   *Then open your browser and visit
   
       http://127.0.0.1:50000
   *Registor merchants.
   *Create and View orders.
   *Before View order you must add id, product,and total of reistered merchant
   *Simulate payments.
    

# Author
    Abely J. Abely
    Email: codewithabel1@gmail.com
    WhatsApp: +255 714 1315 19.
