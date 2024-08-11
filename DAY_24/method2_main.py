PLACEHOLDER = "{name}"

with open("names.txt") as name_file:
    # name=name_file.read()  # this method read whole file
    names = name_file.readlines() # it turn name into list readline read one line and readlines read whole file
    # print(names)
    
with open("email_blueprint.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter=letter_content.replace(PLACEHOLDER,stripped_name)
        print(new_letter)
        with open(f"./emails/letter_for_{stripped_name}.txt",mode='w') as completed_letter:
            completed_letter.write(new_letter)