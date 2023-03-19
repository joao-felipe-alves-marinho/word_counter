from PySimpleGUI import PySimpleGUI as sg
from file_reader import FileReader

# Layout
sg.theme('Reddit')

VALID_FILE_TYPE = [('txt file', '*.txt')]

layout = [
    [sg.Text('Pick a file'),
     sg.InputText(size=(25, 1), key='-PATH-'),
     sg.FileBrowse(file_types=VALID_FILE_TYPE)],
    [sg.Text('Total number of characters: 0', key='-CHAR-')],
    [sg.Exit(), sg.Button(button_text='Run')]
]

# Window
window = sg.Window('Word Counter', layout)

# Events
while True:
    events, values = window.read()
    if events in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif events == 'Run':
        file = FileReader(values['-PATH-'])
        characters = file.count_words()
        window['-CHAR-'].update(value='Total number of characters: ' + str(characters))

# Close window
window.close()
exit()
