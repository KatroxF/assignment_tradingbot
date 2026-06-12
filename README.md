# Binance Futures Testnet Trading Bot

A command-line Python application that places Market and Limit orders on Binance Futures Testnet (USDT-M).

## Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL orders
* Command-line interface using argparse
* Input validation
* Logging support
* Exception handling
* Environment variable configuration using `.env`

---

## Project Structure

```text
TRADINGBOT/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│
├── .env.example
├── .gitignore
├── cli.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd TRADINGBOT
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
```

You may use `.env.example` as a template.

---

## Usage

### Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Example Output

```text
===== SUCCESS =====

Order ID: 12345678
Status: FILLED
Executed Qty: 0.001
```

---

## Logging

Logs are stored in:

```text
logs/bot.log
```

The following events are logged:

* Order requests
* Order responses
* Validation failures
* API errors
* Runtime exceptions

---

## Validation Rules

* Side must be BUY or SELL
* Order type must be MARKET or LIMIT
* Quantity must be greater than 0
* LIMIT orders require a price

---

## Error Handling

The application handles:

* Invalid user input
* Missing parameters
* API authentication failures
* Network-related issues
* Binance API exceptions

---

## Assumptions

* The user provides valid Binance Futures Testnet credentials.
* API credentials are stored securely in a `.env` file.
* The application is executed from the project root directory.

---

## Notes

Due to Binance account verification requirements, API credentials are not included in this repository.

To test the application:

1. Create a Binance Futures Testnet account.
2. Generate API credentials.
3. Add credentials to the `.env` file.
4. Run the commands shown above.

The application can be verified using any valid Binance Futures Testnet API credentials.

---


