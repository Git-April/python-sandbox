import os #Python Delete Files

#Python Read Files
f = open("file_handling_demofile.txt")
f = open("file_handling_demofile.txt", "rt")

f = open("file_handling_demofile.txt")
print(f.read())

with open("file_handling_demofile.txt") as f:
    print(f.read())

f = open("file_handling_demofile.txt")
print(f.readline())
f.close()

with open("file_handling_demofile.txt") as f:
    print(f.read(5))

with open("file_handling_demofile.txt") as f:
    print(f.readline())

with open("file_handling_demofile.txt") as f:
    print(f.readline())
    print(f.readline())

with open("file_handling_demofile.txt") as f:
    for x in f:
        print(x)

#Python Write/Create Files
with open("file_handling_demofile.txt", "a") as f:
    f.write("Now the file has more content!")

with open("file_handling_demofile.txt") as f:
    print(f.read())

with open("file_handling_demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

with open("file_handling_demofile.txt") as f:
    print(f.read())

#Python Delete Files
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")