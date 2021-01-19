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
from Translation.English import English as Locale

class ConnectHandler:
    def __init__(self, event):
        from Class.gui.LoginPanel import LoginPanel
        from Class.gui.MainFrame import MainFrame
        from Class.gui.ChatboxPanel import ChatboxPanel

        username = LoginPanel.username_textctrl.GetValue()
        host = LoginPanel.ip_textctrl.GetValue()
        port = 826

        listenPort = 926

        if username != "":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect_ex((host, port))
                body = b'SYN;' + bytes(username, 'utf-8') + b";" + bytes(listenPort, 'utf-8')
                s.sendall(body)
                data = s.recv(1024)
            if data.decode("utf-8") == "ACK":
                MainFrame.show_chatbox(MainFrame)

                username_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u"Ebrima")
                message_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u"Ebrima")

                ChatboxPanel.chatbox.BeginParagraphSpacing(0, 0)
                ChatboxPanel.chatbox.BeginFontSize(12)
                ChatboxPanel.chatbox.BeginBold()
                ChatboxPanel.chatbox.WriteText("SELF" + ": ")
                ChatboxPanel.chatbox.EndBold()
                ChatboxPanel.chatbox.WriteText("You have been connected to " + host + ":" + str(port) + " as " + username + ". Have fun!")
                ChatboxPanel.chatbox.ShowPosition(ChatboxPanel.chatbox.GetLastPosition())

                ChatboxPanel.messagebox.SetValue("")
                ChatboxPanel.messagebox.SetHint(Locale.send_message)
                ChatboxPanel.messagebox.SetFocus()
            else:
                print(":(((((((((")
        else:
            return