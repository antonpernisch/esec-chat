# -------------------------------------
#
# client-side language locale
#
# group: English
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

class English:
    # -------------
    # Login content
    # -------------

    # hading
    login__heading = "esec's chat"

    # ip address text
    login__enter_ip = "Server IPv4 address (default port 826):"

    #ip address hint
    login__ip_hint = "IP address..."

    # must login text
    login__must_login = "Enter your username to connect:"

    # text input hint
    login__username_hint = "Username..."

    # connect button
    login__connect = "Connect"

    # -------------
    # Chatbox content
    # -------------

    # textbox hint
    send_message = "Send message..."

    # button text
    send_button = "SEND"

    # -------------
    # Dialogs
    # -------------

    # > ERRORS
    # connection unsuccessful title
    dialog__error__connUnsuccessful_title = "Connection unsuccessful"

    # connection unsuccessful
    dialog__error__connUnsuccessful = "Server was not found or is not running as esec-chat server"

    # username taken title
    dialog__error__usrTaken_title = "Denied"

    # username taken
    dialog__error__usrTaken = "Username already taken"

    # disconnection failed title
    dialog__error__failedDisconnection_title = "Couldn't disconnect"

    # disconnection failed
    dialog__error__failedDisconnection = "Unable to disconnect from the server. Please try again"

    # conn lost title
    dialog__error__connLost_title = "Terminated"

    # conn lost failed
    dialog__error__connLost = "Connection lost"

    # unauthorized title
    dialog__error__unauth_title = "Unauthorized"

    # unauthorized
    dialog__error__unauth = "You're not allowed to do that"

    # too fast sending title
    dialog__error__tooFast_title = "Denied"

    # too fast sending
    dialog__error__tooFast = "You're typing too fast, calm down and let us proccess something!"

    # too fast sending title
    dialog__error__banned_title = "Denied"

    # too fast sending
    dialog__error__banned = "You're banned because of spamming, please wait 5 seconds..."

    # -------------
    # Client-side chat information
    # -------------

    # message prefix for info messages
    chat__self = "SELF"

    # connected message for client-side, variables are {ip} for ip address of connected server
    # {port} for the connected port and {username} for chosen username
    chat__connected = "You have been connected to {ip} as {username}. Have fun!"