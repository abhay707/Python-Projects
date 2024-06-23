import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
correct_state = []

while len(correct_state) < 50:
    answer = screen.textinput(title=f"{len(correct_state)}/50 States Correct",
                              prompt="What's another state's name?").title()

    if answer == "Exit":
        missing_states = [state for state in states if state not in correct_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break


    if answer in states:
        correct_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

