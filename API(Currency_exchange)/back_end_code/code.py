import requests  # Importing request
# Please download and install request package in the Python interpreter, remember to do the same
# before running the code in your IDE
website = "https://openexchangerates.org/api/latest.json?app_id=68595289ef6b40468258a5a36aa4805b"
# Using openexchangerates.org API to call and get the exchange rates data
response = requests.get(website)
exchange_rates = response.json()["rates"]
