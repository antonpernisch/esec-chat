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

        username = LoginPanel.username_textctrl.GetValue()
        host = LoginPanel.ip_textctrl.GetValue()
        port = 826

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as MessageListener.s:
                MessageListener.s.connect_ex((host, port))
                body = b'ACK;' + bytes(username, "utf-8")
                MessageListener.s.sendall(body)
                data = MessageListener.s.recv(1024).decode("utf-8").split(";")
            if data[0] == "NEW":
                    ConnectHandler.lister_thread = threading.Thread(target=MessageListener)
                    ConnectHandler.lister_thread.start()

                    username_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u"Ebrima")
                    message_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u"Ebrima")

                    ChatboxPanel.chatbox.BeginParagraphSpacing(0, 0)
                    ChatboxPanel.chatbox.BeginFontSize(12)
                    ChatboxPanel.chatbox.WriteText("\n")
                    ChatboxPanel.chatbox.BeginBold()
                    ChatboxPanel.chatbox.WriteText(data[1] + ": ")
                    ChatboxPanel.chatbox.EndBold()
                    ChatboxPanel.chatbox.WriteText(data[2])
                    ChatboxPanel.chatbox.ShowPosition(ChatboxPanel.chatbox.GetLastPosition())
                    return
            else:
                Error(Locale.dialog__error__connLost_title, Locale.dialog__error__connLost)
                ConnectHandler.connected = False
                MainFrame.show_login(MainFrame)
                return
        except:
            Error(Locale.dialog__error__connLost_title, Locale.dialog__error__connLost)
            ConnectHandler.connected = False
            MainFrame.show_login(MainFrame)
            return