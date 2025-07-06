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

# Author
Abely J. Abely
Email: codewithabel1@gmail.com
WhatsApp: +255 714 1315 19.
