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

from Class.communication.SendMessage import SendMessage
from Modules.dialogs.WarningDialog import WarningDialog as Warning
from Translation.English import English as Locale

class SendMessageBtn:
    def __init__(self, event):
        if not SendMessage.reserved:
            SendMessage()
        else:
            Warning(Locale.dialog__error__tooFast_title, Locale.dialog__error__tooFast)