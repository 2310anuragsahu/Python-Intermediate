# import os;
# print(os.environ['PATH'])

# Read the entire file
print("--Read the entire file")
file = open("C:/Users/inasahu/PycharmProjects/DemoText.txt", "r")
print(file.read())
file.close()
print()

# Read first 5 characters of the file
print("--Read first 5 characters of the file")
file1 = open("C:/Users/inasahu/PycharmProjects/DemoText.txt", "r")
print(file1.read(5))
file1.close()
print()

# Read the first line of the file
print("--Read the first line of the file")
file2 = open("C:/Users/inasahu/PycharmProjects/DemoText.txt", "r")
print(file2.readline())
file2.close()
print()

# Read first 5 characters from the first line file
print("--Read first 5 characters from the first line file")
file3 = open("C:/Users/inasahu/PycharmProjects/DemoText.txt", "r")
print(file3.readline(5))
file3.close()
print()

# Read first 5 characters of the file
print("--Read first 5 characters of the file")
file4 = open("C:/Users/inasahu/PycharmProjects/DemoText.txt", "r")
print(file4.readlines())
file4.close()
print()

# Fast and Efficient way to print the entire line
print("--Fast and Efficient way to print the entire line")
file5 = open("C:/Users/inasahu/PycharmProjects/DemoText.txt", "r")
for line in file5.readlines():
    print(line.title())
file5.close()
print()
