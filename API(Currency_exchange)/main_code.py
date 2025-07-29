from back_end_code.code import exchange_rates


Text = """
Base currency: USD
Covertable currencies:
Enter 1 for AED(UAE Dirham),
Enter 2 for EUR(EURO),
Enter 3 for INR(Indian Rupee),
Enter 4 for CAD(Canadian Dollar),
Enter 5 for KWD(Kuwaiti Dinar)
"""


def currency_exchange():

    print(Text)

    user_currency = int(input
    ("Enter the currency you want USD to convert into(Example: type 1 for AED),enter 0 to exit: "))

    while user_currency != 0:
        if user_currency > 5:
            print("There is no assigned currency under the provided input: {}".format(user_currency))
        elif user_currency >= 1 or user_currency <= 5:
            usd_amount = float(input("Enter the USD($) Amount: "))
            if user_currency == 1:
                aed_amount = usd_amount * exchange_rates["AED"]
                print(f"{usd_amount} USD($) = {aed_amount:.2f} AED(UAE Dirham)")
            elif user_currency == 2:
                eur_amount = usd_amount * exchange_rates["EUR"]
                print(f"{usd_amount} USD($) = € {eur_amount:.2f} EUR(EURO)")
            elif user_currency == 3:
                inr_amount = usd_amount * exchange_rates["INR"]
                print(f"{usd_amount} USD($) = ₹ {inr_amount:.2f} INR(Indian Rupee)")
            elif user_currency == 4:
                cad_amount = usd_amount * exchange_rates["CAD"]
                print(f"{usd_amount} USD($) = CA$ {cad_amount:.2f} CAD(Canadian Dollar)")
            elif user_currency == 5:
                kwd_amount = usd_amount * exchange_rates["KWD"]
                print(f"{usd_amount} USD($) = {kwd_amount:.2f} KWD(Kuwaiti Dinar)")

            print("-------------------------------------------------------------------------------------------------")

        user_currency = int(input("Enter the currency you want USD to convert into"
                                  "(Example: type 1 for AED),enter 0 to exit: "))


currency_exchange()







