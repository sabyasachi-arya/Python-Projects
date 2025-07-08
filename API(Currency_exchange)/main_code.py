# Using openexchangerates.org API to call and get the exchange rates data
# Importing request
# Please download and install request package in the Python interpreter, remember to do the same
# before running the code in your IDE

import requests

Text = """
Base currency: USD
Covertable currencies:
1. AED(UAE Dirham),
2. EUR(EURO),
3. INR(Indian Rupee),
4. CAD(Canadian Dollar),
5. KWD(Kuwaiti Dinar)
"""
response = requests.get("https://openexchangerates.org/api/latest.json?app_id=68595289ef6b40468258a5a36aa4805b")
exchange_rates = response.json()["rates"]

print(Text)

user_currency = int(input("Enter the currency you want USD to convert into(Ex.: type 1 for AED): "))
usd_amount = int(input("Enter the USD($) Amount: "))

if user_currency == 1:
    aed_amount = usd_amount * exchange_rates["AED"]
    print(f"{usd_amount} USD($) = {aed_amount} AED(UAE Dirham)")
elif user_currency == 2:
    eur_amount = usd_amount * exchange_rates["EUR"]
    print(f"{usd_amount} USD($) = {eur_amount} EUR(EURO)")
elif user_currency == 3:
    inr_amount = usd_amount * exchange_rates["INR"]
    print(f"{usd_amount} USD($) = {inr_amount} INR(Indian Rupee)")
elif user_currency == 4:
    cad_amount = usd_amount * exchange_rates["CAD"]
    print(f"{usd_amount} USD($) = {cad_amount} CAD(Canadian Dollar)")
elif user_currency == 5:
    kwd_amount = usd_amount * exchange_rates["KWD"]
    print(f"{usd_amount} USD($) = {kwd_amount} KWD(Kuwaiti Dinar)")
else:
    print("There is no assigned currency under the input {} provided".format(user_currency))







