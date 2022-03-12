# Importing pysimplegui
from PySimpleGUI import PySimpleGUI as sg
import numpy as np

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Username'), sg.Input(key = 'user', size = (20, 1))],
    [sg.Text('Password'), sg.Input(key = 'password', password_char = '*', size = (20, 1))],
    [sg.Checkbox('Rember me')],
    [sg.Button('Login')],
]

# Window
window = sg.Window('Login screen', layout)

# Event listeners
while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Login':
        if values['user'] == 'bah' and values['password'] == '123':
            window.add_row([sg.Text('Respeita o pai!')])