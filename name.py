import PySimpleGUI as sg

# layout
layout = [[sg.Text('What is your name?')],
            [sg.Input()],
            [sg.Button('OK')]]

# window
window = sg.Window('name', layout)

event, values = window.Read()

window.close()

sg.Popup(f'Hello {values[0]}, welcome!')