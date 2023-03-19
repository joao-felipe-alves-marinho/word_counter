from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Pick a file'), sg.InputText(), sg.FileBrowse(file_types=[('Pdf', '*.pdf'), ('Doc', '*.doc*')])],
    [sg.Text('Total number of characters: ' + str(0))],
    [sg.Button(button_text='Close'), sg.Button(button_text='Run')]
]

# Window
window = sg.Window('Word Counter', layout)

# Events
while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
