# -------------------------------------
#
# client-side class
#
# group: communication
# class: MessageListener
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

import wx
from Class.communication.ReciveMessage import ReciveMessage
import socket
from Class.gui.LoginPanel import LoginPanel
from Modules.dialogs.ErrorDialog import ErrorDialog as Error

class MessageListener:
    def __init__(self):
        print("messagelistener class init called LMAO")
        from Handler.button.ConnectHandler import ConnectHandler

        username = LoginPanel.username_textctrl.GetValue()
        host = LoginPanel.ip_textctrl.GetValue()
        port = 826

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #try:
            s.connect_ex((host, port))
            body = b'ACK'
            s.sendall(body)
            data = s.recv(1024).decode("utf-8").split(";")
        if data[0] == "NEW":
            print("LOOOOOOOOOOOOOL")
            #except:
                #Error(Locale.dialog__error__connUnsuccessful_title, Locale.dialog__error__connUnsuccessful)
                #return