# import os;
# print(os.environ['PATH'])

# Write into a file
print("--Write into a file")
file = open("C:/Users/inasahu/PycharmProjects/DemoText_write.txt", "w")
file.write("This is a few file with text")
file.close()

# Appending a line at the end of the newly created file
print("--Read first 5 characters of the file")
file1 = open("C:/Users/inasahu/PycharmProjects/DemoText_write.txt", "a")
file1.write("This is a second line")
file1.write("\nThis is a third line")
file1.close()


