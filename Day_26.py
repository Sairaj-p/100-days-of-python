#List and Dictionary Comprehension
import pandas

data =pandas.read_csv(r"E:\New folder\NATO-alphabet-start\nato_phonetic_alphabet.csv")
data_dict = {}
data_dict={row.letter:row.code for (index,row) in data.iterrows()}
msg = input("Enter the Message:").upper()
msg_list =[data_dict[letter] for letter in msg]


