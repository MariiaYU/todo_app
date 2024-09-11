def convert(user_params):
    params_list = user_params.split(" ")
    feet = float(params_list[0])
    inches = float(params_list[1])
    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_inches = input("Write feet and inches: ")

answer = convert(feet_inches)
print(f"In meters is: {answer}")