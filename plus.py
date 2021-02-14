import PySimpleGUI as sg

#layout
layout = [[sg.Text('Add 2 numbers')],
            [sg.Input(key='input1'), sg.Text(' + '), sg.Input(key='input2'), sg.Text(' = '), sg.Text(key = 'answer')],
            [sg.Button('ADD')]]

# window
window = sg.Window('ADD', layout)

while True:
    button, values = window.Read()

    if button is None: 
        break

    num1 = int(values['input1'])
    num2 = int(values['input2'])

    ans = num1 + num2
    
    window.FindElement('answer').Update(ans)
window.close()