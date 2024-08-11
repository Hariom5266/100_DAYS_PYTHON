# 🍵 , Hanji Kaise ho aap sabhi this is 25th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ====================== USA STATES ====================== #

import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. States Game")
image="./DAY_25/PROJECT/img.gif"

screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("./DAY_25/PROJECT/50_states.csv")
all_states=data.state.to_list()

guessed_states=[]

while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 states correct",prompt="What's another state name?").title()

    if answer_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # print(missing_states)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("./DAY_25/PROJECT/missing_states.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.state.item())



screen.exitonclick()

