#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"


with open ("./Input/Names/Invited_names.txt", mode = "r") as names:
    rel_name = names.readlines()
print(rel_name)

with open("./Input/Letters/starting_letter.txt", mode = "r") as file:
    content = file.read()
    for name in rel_name:
        stripped_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/send_to_{stripped_name}.txt", mode= "w") as send_letter:
            send_letter.write(new_letter)



# print(content)

