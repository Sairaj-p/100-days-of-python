# Try,except,else,finally Statements

try:
    file = open(r"Text.txt")
except FileNotFoundError:
    file =open(r"Text.txt",mode="w")
    file.write("Hello World!")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("End")
