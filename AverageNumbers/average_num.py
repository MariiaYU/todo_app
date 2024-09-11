def get_temperatures():
    with open("file_num/nums.txt", 'r') as file:
        num_list = file.readlines()[1:]

        data = num_list[1:]
        data = [float(num) for num in num_list]
        average_local = sum(data) / len(data)

        return average_local


average = get_temperatures()
print(average)
