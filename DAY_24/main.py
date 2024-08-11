# 🍵 Hanji, Kaise ho aap sabhi, This is 24th day of #100DaysOfPython ! I'm back and ready to code and solve the problem ! Let's start program

persons=['harish','hiren','sandip','ashish','chetan','hairom']

with open("email_blueprint.txt", "r") as email_blueprint:
    blueprint = email_blueprint.read() 
    # name = "hariom"  
    # personalized_email = blueprint.replace("{name}", name)  
    # print(personalized_email) 

    for person in persons:
        name = person
        personalized_email = blueprint.replace("{name}",name)
        # print(personalized_email)
        with open(f"emails/{name}.txt",mode='w') as person_email:
            person_email.write(personalized_email)