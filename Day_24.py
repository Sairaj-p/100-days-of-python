#Mail merge 


placeholder = "[name]"
with open("Day_24.txt",mode="r") as file:
    List = file.read()
    List = List.strip()
    names = List.split("\n")
    
with open(r"E:\New folder\Mail Merge Project Completed\Input\Letters\starting_letter.txt", mode= "r") as example:
    leter = example.read() 
    print(leter)
    for name in names:
        with open(f"letter_{name}.txt",mode="w") as letter:
            new_letter = leter.replace(placeholder,name)
            letter.write(f"{new_letter}")
