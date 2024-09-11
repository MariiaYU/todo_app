import glob

myfiles = glob.glob("../files/*.txt")

for each_file in myfiles:
    with open(each_file, "w") as file:
        file.writelines("Hello1")


