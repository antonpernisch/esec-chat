# -------------------------------------
#
# client-side handler
#
# group: communication
# class: DisconnectHandler
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

import socket
from Translation.English import English as Locale
from Modules.dialogs.ErrorDialog import ErrorDialog as Error
from Class.communication.MessageListener import MessageListener

class DisconnectHandler:
    def __init__(self, event):
        from Class.gui.MainFrame import MainFrame
        from Handler.button.ConnectHandler import ConnectHandler
        from Class.gui.LoginPanel import LoginPanel
        DisconnectHandler.disconnecting = True

        username = LoginPanel.username_textctrl.GetValue()
        host = LoginPanel.ip_textctrl.GetValue()
        port = 826

        if ConnectHandler.connected:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        try:
                            s.connect_ex((host, port))
                            body = b'END;' + bytes(username, 'utf-8')
                            s.sendall(body)
                            data = s.recv(1024).decode("utf-8")
                            if data:
                                MessageListener.s.close()
                                MainFrame.frame.Destroy()
                            else:
                                Error(Locale.dialog__error__failedDisconnection_title, Locale.dialog__error__failedDisconnection)
                                return
                        except:
                            try:
                                MessageListener.s.close()
                                MainFrame.frame.Destroy()
                            except:
                                MainFrame.frame.Destroy()
            except:
                try:
                    MessageListener.s.close()
                    MainFrame.frame.Destroy()
                except:
                    MainFrame.frame.Destroy()
        else:
            MainFrame.frame.Destroy()