# -------------------------------------
#
# client-side handler
#
# group: Button
# class: ConnectHandler
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

import socket
import wx
import threading
from Translation.English import English as Locale
from Modules.dialogs.ErrorDialog import ErrorDialog as Error

class ConnectHandler:
    def __init__(self, event):
        from Class.gui.LoginPanel import LoginPanel
        from Class.gui.MainFrame import MainFrame
        from Class.gui.ChatboxPanel import ChatboxPanel
        from Class.communication.MessageListener import MessageListener
        from Handler.communication.DisconnectHandler import DisconnectHandler

        DisconnectHandler.disconnecting = True

        ConnectHandler.listener_threads = list()

        username = LoginPanel.username_textctrl.GetValue()
        host = LoginPanel.ip_textctrl.GetValue()
        port = 826

        if username != "":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.connect_ex((host, port))
                    body = b'SYN;' + bytes(username, 'utf-8')
                    s.sendall(body)
                    data = s.recv(1024).decode("utf-8").split(";")
                except:
                    Error(Locale.dialog__error__connUnsuccessful_title, Locale.dialog__error__connUnsuccessful)
                    return
            if data[0] == "SYN-ACK":
                ChatboxPanel.chatbox.SetValue("")
                MainFrame.show_chatbox(MainFrame)
                ConnectHandler.connected = True
                newThread = threading.Thread(target=MessageListener)
                ConnectHandler.listener_threads.append(newThread)
                newThread.start()

                username_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u"Ebrima")
                message_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u"Ebrima")

                ChatboxPanel.chatbox.BeginParagraphSpacing(0, 0)
                ChatboxPanel.chatbox.BeginFontSize(12)
                ChatboxPanel.chatbox.BeginBold()
                ChatboxPanel.chatbox.WriteText(Locale.chat__self + ": ")
                ChatboxPanel.chatbox.EndBold()
                ChatboxPanel.chatbox.WriteText(Locale.chat__connected.replace("{ip}", host).replace("{port}", str(port)).replace("{username}", username))
                ChatboxPanel.chatbox.ShowPosition(ChatboxPanel.chatbox.GetLastPosition())

                ChatboxPanel.messagebox.SetValue("")
                ChatboxPanel.messagebox.SetHint(Locale.send_message)
                ChatboxPanel.messagebox.SetFocus()
            elif data[0] == "ERR":
                if data[1] == "USR_TAKEN":
                    Error(Locale.dialog__error__usrTaken_title, Locale.dialog__error__usrTaken)
        else:
            return