while True:
    user_password = input("Enter your password: ")

    result = {}

    for symbol in user_password:
        if symbol.isupper():
            result["upper_symbol"] = True
            break
        else:
            result["upper_symbol"] = False
    for symbol in user_password:
        if symbol.isdecimal():
            result["num_symbol"] = True
            break
        else:
            result["num_symbol"] = False

    if len(user_password) >= 8 and all(result.values()):
        print("Thank you!")
        break
    else:
        print("Wrong password! Try again")
