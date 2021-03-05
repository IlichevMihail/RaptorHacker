import PySimpleGUI as sg

from Logika import Log


def Win():
    a=50
    b=100
    SHButton = int(a/20)
    SWButton = int(b/20)

    sg.theme('Black')

    groop1 = [
        [sg.Button('7',size=(SWButton,SHButton),key='7'), sg.Button('8',size=(SWButton,SHButton),key='8'), sg.Button('9',size=(SWButton,SHButton),key='9'),],
        [sg.Button('4',size=(SWButton,SHButton),key='4'), sg.Button('5',size=(SWButton,SHButton),key='5'), sg.Button('6',size=(SWButton,SHButton),key='6'),],
        [sg.Button('1',size=(SWButton,SHButton),key='1'), sg.Button('2',size=(SWButton,SHButton),key='2'), sg.Button('3',size=(SWButton,SHButton),key='3'),],
        [sg.Button('0',size=(SWButton,SHButton),key='0'), sg.Button('.',size=(SWButton,SHButton),key='.'), sg.Button('+/-',size=(SWButton,SHButton),key='+/-'),],
    ]
    groop2 =[
        [sg.Button('+', size=(SWButton, SHButton),key='+'), sg.Button('-', size=(SWButton, SHButton),key='-'),sg.Button('=', size=(SWButton, SHButton),key='=')],
        [sg.Button('*', size=(SWButton, SHButton),key='*'), sg.Button('/', size=(SWButton, SHButton),key='/'),sg.Button('C', size=(SWButton, SHButton),key='C')],
        [sg.Button('',size=(SWButton,SHButton),key=''), sg.Button('',size=(SWButton,SHButton),key=''), sg.Button('',size=(SWButton,SHButton),key='')],
        [sg.Button('',size=(SWButton,SHButton),key=''), sg.Button('',size=(SWButton,SHButton),key=''), sg.Button('',size=(SWButton,SHButton),key='')],
        ]

    groop3=[
        [sg.Button('', size=(SWButton, SHButton),key=''), sg.Button('', size=(SWButton, SHButton),key=''),sg.Button('', size=(SWButton, SHButton),key='')],
        [sg.Button('', size=(SWButton, SHButton), key=''), sg.Button('', size=(SWButton, SHButton), key=''),sg.Button('', size=(SWButton, SHButton), key='')],
        [sg.Button('', size=(SWButton, SHButton), key=''), sg.Button('', size=(SWButton, SHButton), key=''), sg.Button('', size=(SWButton, SHButton), key='')],
        [sg.Button('', size=(SWButton, SHButton), key=''), sg.Button('', size=(SWButton, SHButton), key=''),sg.Button('', size=(SWButton, SHButton), key='')],
    ]

    groop4 = [
        [sg.Button('', size=(SWButton, SHButton), key=''), sg.Button('', size=(SWButton, SHButton), key=''),sg.Button('', size=(SWButton, SHButton), key='')],
        [sg.Button('', size=(SWButton, SHButton), key=''), sg.Button('', size=(SWButton, SHButton), key=''),sg.Button('', size=(SWButton, SHButton), key='')],
        [sg.Button('', size=(SWButton, SHButton), key=''), sg.Button('', size=(SWButton, SHButton), key=''),sg.Button('', size=(SWButton, SHButton), key='')],
        [sg.Button('', size=(SWButton, SHButton), key=''), sg.Button('', size=(SWButton, SHButton), key=''),sg.Button('', size=(SWButton, SHButton), key='')],
    ]

    layout =[[sg.Text('Menu',key='res')],
             [sg.Column(groop1),sg.Column(groop2),sg.Column(groop3),sg.Column(groop4)],
             [sg.Text('History')]
             ]

    window = sg.Window('Cal', layout, margins=(a,b))
    while True:
        event, values = window.read()

        if event ==sg.WIN_CLOSED:
            break
        Log(event)

    window.close()