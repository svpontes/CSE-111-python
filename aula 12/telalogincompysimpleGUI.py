from PySimpleGUI import PySimpleGUI as sg

#layout

sg.theme("Reddit")

layout = [

    [sg.Text("User"), sg.Input(key="user")],
    [sg.Text("Password"), sg.Input(key="Password", password_char="*")],
    [sg.Checkbox("Salvar o Login?")],
    [sg.Button("send")]
]

#user_password_list = [
#    ["sergio", "123456789"],
#    ["murilo","789456123"]   
#]

#window
window = sg.Window("Login", layout)

while True:
    event, value = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "send":
        if value["user"] == "Sergio" and value["Password"] == "123456789":
            print ("Olá.Bem vindo")