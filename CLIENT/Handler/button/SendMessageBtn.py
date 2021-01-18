# -------------------------------------
#
# client-side handler
#
# group: Button
# class: SendMessageBtn
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

from Translation.English import English as Locale

class SendMessageBtn:
    def __init__(self, event):
        from Class.gui.ChatboxPanel import ChatboxPanel
        from GUI import Initialization

        current_message = ChatboxPanel.messagebox.GetValue()

        if current_message != "":
            ChatboxPanel.chatbox.AppendText(current_message + "\n")
            ChatboxPanel.messagebox.SetValue("")
            ChatboxPanel.messagebox.SetHint(Locale.send_message)
            ChatboxPanel.messagebox.SetFocus()
        else:
            ChatboxPanel.messagebox.SetFocus()
            return