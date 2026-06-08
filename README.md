# Binance Trading Bot

## Objective

A CLI-based Python trading bot that places MARKET and LIMIT orders on Binance Testnet using Python and the python-binance library.

---

## Features

* Place MARKET orders
* Place LIMIT orders
* BUY and SELL support
* Command-line interface using argparse
* Input validation
* Structured code architecture
* Request and response logging
* Exception handling for invalid input and API errors
* Environment variable support using `.env`

---

## Project Structure

```text
trading_bot/
│
├── .env
├── .gitignore
├── cli.py
├── requirements.txt
├── README.md
├── trading_bot.log
│
└── bot/
    ├── __init__.py
    ├── client.py
    ├── orders.py
    ├── validators.py
    └── logging_config.py
```

---

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd trading_bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## Running the Application

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

---

## Sample Output

```text
===== ORDER REQUEST SUMMARY =====
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': '0.001'}

===== ORDER RESPONSE DETAILS =====
Order ID: 1913508
Status: FILLED
Executed Qty: 0.00100000
Avg Price: N/A

SUCCESS: Order placed successfully
```

---

## Logging

All order requests, responses, and errors are recorded in:

```text
trading_bot.log
```

Example:

```text
ORDER REQUEST: {...}
ORDER RESPONSE: {...}
ORDER ERROR: ...
```

---

## Validation

The application validates:

* Symbol format
* Order side (BUY/SELL)
* Order type (MARKET/LIMIT)
* Quantity > 0
* Price required for LIMIT orders
* Price > 0

---

## Assumptions

* Binance Testnet credentials are stored securely in a `.env` file.
* MARKET and LIMIT orders were tested successfully in the Binance test environment.
* Logging is enabled for debugging and auditing purposes.

---

## Requirements

* Python 3.10+
* python-binance
* python-dotenv
* requests
