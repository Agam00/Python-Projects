import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on=True
data = pandas.read_csv("50_states.csv")
state_list= data["state"].str.lower().tolist()
guess_count=0
guessed_states=[]
states_not_guessed=[]

def text_move(sdata):

    t= turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(sdata.x.item(),sdata.y.item())
    t.write(sdata.state.item())




while game_is_on:
    answer_state = screen.textinput(title=f"{guess_count}/50 states correct", prompt="What's the another state's name")
    if answer_state.lower() in state_list:
        if answer_state.lower() not in guessed_states:
            guessed_states.append(answer_state.lower())
            guess_count=guess_count+1
            state_data=data[data.state.str.lower()==answer_state.lower()]
            text_move(state_data)

    elif answer_state.lower() == "exit":
        break
    elif guess_count == 50:
        game_is_on=False

for i in state_list:
    if i not in guessed_states:
        states_not_guessed.append(i)
file=pandas.DataFrame(states_not_guessed)
file.to_csv("states missed")
