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
import socket
import threading
from Class.communication.ReciveMessage import ReciveMessage
from Class.gui.LoginPanel import LoginPanel
from Modules.dialogs.ErrorDialog import ErrorDialog as Error
from Translation.English import English as Locale

class MessageListener:
    def __init__(self):
        from Handler.button.ConnectHandler import ConnectHandler
        from Class.gui.ChatboxPanel import ChatboxPanel
        from Class.gui.MainFrame import MainFrame
        from Class.communication.SendMessage import SendMessage
        from Handler.communication.DisconnectHandler import DisconnectHandler

        username = LoginPanel.username_textctrl.GetValue()
        host = LoginPanel.ip_textctrl.GetValue()
        port = 826

        try:
            SendMessage.reserved = True
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as MessageListener.s:
                MessageListener.s.connect_ex((host, port))
                body = b'ACK;' + bytes(username, "utf-8")
                MessageListener.s.sendall(body)
                SendMessage.reserved = False
                data = MessageListener.s.recv(1024).decode("utf-8").split(";")
                SendMessage.reserved = True
            if data[0] == "NEW":
                    newThread = threading.Thread(target=MessageListener)
                    ConnectHandler.listener_threads.append(newThread)
                    newThread.start()
                    ReciveMessage.__init__(data[1], data[2])
                    return
            else:
                if not DisconnectHandler.disconnecting:
                    Error(Locale.dialog__error__connLost_title, Locale.dialog__error__connLost)
                    ConnectHandler.connected = False
                    MainFrame.show_login(MainFrame)
                    SendMessage.reserved = False
                    return
                else:
                    return
        except:
            if not DisconnectHandler.disconnecting:
                Error(Locale.dialog__error__connLost_title, Locale.dialog__error__connLost)
                ConnectHandler.connected = False
                MainFrame.show_login(MainFrame)
                SendMessage.reserved = False
                return
            else:
                return