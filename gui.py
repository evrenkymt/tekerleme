import PySimpleGUI as sg
import random

lines = open('tekerlemeler.txt').read().splitlines()
myline = random.choice(lines)

layout = [[sg.Text(myline, key='text')], [[sg.Column([[sg.Button("yenile", size=(15,1))]], element_justification='center')]]]

window = sg.Window("gunluk", layout=layout)
while True:
    event, values = window.read()
    if event == 'yenile':
        myline = random.choice(lines)
        window['text'].update(myline)  # Update the text of the 'text' element
    if event == sg.WIN_CLOSED:
        break

window.close()