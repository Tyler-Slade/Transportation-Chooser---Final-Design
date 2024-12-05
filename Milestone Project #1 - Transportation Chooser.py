from drafter import *
from dataclasses import dataclass
from bakery import assert_equal

@dataclass
class State:
    message: str
    view_trains: bool
    view_highways: bool
    
    """If a user checks the View Trains box, then a train picture will be displayed.
If a user checks the View Highways box, then a highway picture will be displayed."""

@route
def index(state: State) -> Page:
    return Page(state, [
        "The message is:",
        state.message,
        Button("Change the Message", change_message),
        "Are you okay seeing pictures of trains?",
        CheckBox("wants_to_view_trains", state.view_trains),
        "You can use the button below to go see a picture",
        Button("View the picture", view_picture)
    ])
    return Page(state, [
        "The message is:",
        state.message,
        Button("Change the Message", change_message),
        "Are you okay seeing pictures of trains?",
        CheckBox("wants_to_view_highways", state.view_highways),
        "You can use the button below to go see a picture",
        Button("View the picture", view_picture)
    ])

@route
def change_message(state: State) -> Page:
    state.message = "The new message!"
    return Page(state, [
        "Now the message is",
        state.message,
        "Would you like to change the message?",
        TextBox("new_message", state.message),
        Button("Save", set_new_message)
    ])

@route
def set_new_message(state: State, new_message: str) -> Page:
    state.message = new_message
    return index(state)

@route
def view_picture(state: State, view_trains: bool) -> Page:
    if view_trains:
        url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd_z7XqifUcMY7yaAG_xX5K388IOncpruo4JrFDa0p2iHZ_Vu6MSq4Q8awLonWtk1oJYs&usqp=CAU"
    state.view_trains = wants_to_view_trains
    return Page(state, [
        Image(url),
        Button("Return to the main page", index)
    ])
    if view_highways:
        url = "https://www.eastcoastroads.com/states/de/inter/i95/fullsize/95n05_14.jpg"
    state.view_highways = wants_to_view_highways
    return Page(state, [
        Image(url),
        Button("Return to the main page", index)
    ])

assert_equal(index(State("My message", True)),
             Page(State("My message", True), [
                "The message is:",
                "My message",
                Button("Change the Message", change_message),
                "Are you okay seeing pictures of trains?",
                CheckBox("wants_to_view_trains", True),
                "You can use the button below to go see a picture",
                Button("View the picture", view_picture)
             ]))

assert_equal(set_the_message(State("My message", True), "New message"),
             Page(State("New message", True), [
                "The message is:",
                "New message",
                Button("Change the Message", change_message),
                "Are you okay seeing pictures of trains?",
                CheckBox("wants_to_view_trains", True),
                "You can use the button below to go see a picture",
                Button("View the picture", view_picture)
             ]))

assert_equal(index(State("My message", True)),
             Page(State("My message", True), [
                "The message is:",
                "My message",
                Button("Change the Message", change_message),
                "Are you okay seeing pictures of trains?",
                CheckBox("wants_to_view_highways", True),
                "You can use the button below to go see a picture",
                Button("View the picture", view_picture)
             ]))

assert_equal(set_the_message(State("My message", True), "New message"),
             Page(State("New message", True), [
                "The message is:",
                "New message",
                Button("Change the Message", change_message),
                "Are you okay seeing pictures of trains?",
                CheckBox("wants_to_view_highways", True),
                "You can use the button below to go see a picture",
                Button("View the picture", view_picture)
             ]))
start_server(State("The original message", True))