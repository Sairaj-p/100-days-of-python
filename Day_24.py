#Mail merge 

with open("Day_24.txt",mode="r") as file:
    List = file.read()
    names = List.split("\n")

for name in names:
    with open(f"letter_{name}.txt",mode="w") as letter:
        letter.write(f"{name} you are invited to the event.")

    
 
