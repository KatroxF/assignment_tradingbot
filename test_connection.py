from bot.client import client

try:
    account = client.futures_account_balance()
    print("Connected Successfully")
    print(account)

except Exception as e:
    print("Connection Failed")
    print(e)