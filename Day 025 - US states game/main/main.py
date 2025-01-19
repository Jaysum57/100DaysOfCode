from navigator import Navigator
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

navigator = Navigator()


TITLE = "Guess the state"
PROMPT = "Guess the state"

prompt2 = "What's another state name?"

data = pandas.read_csv("50_states.csv")

states = data["state"].tolist()
answer_state = screen.textinput(title=TITLE, prompt=PROMPT).title()

guessed_states = []

score = 0

while len(guessed_states) < len(states):
    
    if answer_state == "Exit":
        missing_states = []

        for state in states:
            if state in guessed_states:
                continue
            else:
                missing_states.append(state)
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        
        break

    elif answer_state in states:
        guessed_states.append(answer_state)
        state = data[data["state"] == answer_state]
        navigator.move(int(state.x),int(state.y))
        navigator.write(answer_state)
        score += 1

    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt=prompt2).title()


