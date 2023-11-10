username = "T Daki"

area_managers = ["Owen Kunaka", "Simon Mahufe", "Trymore Chihwai"]
restart = "y"
chances = 3

while chances >= 0:
    password = int(input("Enter a 4 digit PIN  :🛅"))
    if password == 1234:
        print("Welcome 🤝To our 🏧💱 \n==========\nYou are logged in as", username, "=======================")
        while restart not in ("n", "no", "N", "NO"):
            print("Press 1 ")
            print("Press 2 D-C-S")
            print("Press 3 Update Grower info")
            print("Press 4 Stock Management")
            print("Press 5 Accounting ")
            option = int(input("Select "))
            if option == 1:
                print(
                    "======================== Info Check...... ========================")
                print("Info Check")

            if option == 2:
                print("DATA CAPTURING SYSTEM")

            if option == 3:
                print("Information Update 👤")

            if option == 4:
                grower = int(input("Enter your 6 digit grower number :"))

            ####
            # ==========================================================   ACCOUNTING MODULE   ===================================================================
            ####
            if option == 5:
                account_float = 200
                print(
                    "========================🏧 💰💵 ACCOUNTING  🏧 💰💵========================")

                while restart not in ("n", "no", "N", "NO"):

                    restart = ("y", "yes", "Yes", "Y")
                    out = ("n", "no", "N", "NO")

                    print("Press 1 Load Account  💰💳💳")
                    print("Press 2 Withdrawals  💱💵🏧")
                    print("Press 3 Account Balance 💰💰💳")
                    print("Press 4 Account Statement 📝💰")
                    print("Press 5 Transfer 💹🤑💹")

                    option = int(input("Select "))
                    if option == 1:
                        account_load = int(input("Amount"))
                        account_float = account_float + account_load
                        print("Your account was funded with $", account_load,
                              "You account balance is now", account_float)
                        restart = input("Do you want to add more")
                    elif option == 2:
                        print(
                            "========================🏧 💰💵 ACCOUNT WITHDRAWALS  🏧 💰💵========================")
                        account_withdrawal = int(
                            input("Withdrawal amount \n Select amount Below   5,10,15,20,25,30,35,40,45,50"))
                        if account_withdrawal in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]:
                            account_float = account_float - account_withdrawal
                            print("You have made a withdrawal of $", account_withdrawal, "You account balance is now",
                                  account_float)
                            restart = input("Do you still want to transact more:")
                    elif option == 3:
                        account_balance = account_float
                        print(account_balance)
                    elif option == 5:
                        accounts = "784855562725"
                        print("========================🏧 💰💵 ACCOUNT TRANSFERS  🏧 💰💵========================")
                        transfer_account = input("Transfer Account Number")
                        while transfer_account not in "784855562725":
                            if transfer_account == accounts:
                                print("This account is valid")
                                continue
                            elif transfer_account != "784855562725":
                                print("Account is not valid")
                                quit()

                        transfer_amount = int(input("Transfer Amount : $"))
                        if transfer_amount > account_float:
                            print("You can not transfer more than what you have in your account", account_float, )
                            break
                        elif transfer_amount < account_float:
                            print("You have successfully transferred  to Acc// :", transfer_account, "$",
                                  transfer_amount,
                                  "\n Your Account Balance is $", account_float - transfer_amount)
                        account_float = account_float - transfer_amount







    ####
    #                END OF ACCOUNTING MODULE
    ###

    elif password != 1234:
        print("Incorrect pin")
        chances -= 1
        if chances == 2:
            print("2 chances left")
        if chances == 1:
            print("Last chance")
        if chances == 0:
            print("🚫✋ Incorrect PIN \n Good bye")
            break
