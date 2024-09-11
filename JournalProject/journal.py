date = input("Enter today's date: ").replace("/", ".")

rate = input("How do you rate your day today? from 1 to 10: ")

thoughts = input("Let your thoughts flow: ")

with open(f"journal/{date}.txt", "w") as file:
    file.write(f"Your day rate that day: {rate}\nYour thoughts this day: {thoughts}")

