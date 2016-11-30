import sys
try:
    file_name = sys.argv[1]
except IndexError:
    print("Please enter file name")
    exit()
try:
    with open("backend/images_version/" + file_name, "r+") as f:
        content = f.readlines()
        f.seek(0)
        f.truncate()
        for str in content:
            for i in str.split(","):
                f.write(i.strip().split("(")[0] + "\n")
except IOError:
    print("Can't find the file")
    exit()
