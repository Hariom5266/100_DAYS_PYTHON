# 🍵 , Hanji Kaise ho aap sabhi this is 26th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ==================== NATO ALPHABET ==================== #

import pandas

data=pandas.read_csv("./DAY_26/project/data.csv")
# print(data)
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
# print(phonetic_dict)
word=input("Enter a words: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)





