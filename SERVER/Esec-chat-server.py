# -------------------------------------
#
# server-side script
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

# --- ~~~ ---
# START OF CAN-CHANGE SECTION
# --- ~~~ ---

host = '89.203.250.155' # IPv4 address of this machine (server)
port = 826 # default port for esec-chat server is 826

# --- ~~~ ---
# END OF CAN-CHANGE SECTION
# --- ~~~ ---

import socket
import threading
import time
import sys
from datetime import datetime

clients = {"BOT": (host, port)}
clients_spamCounter = {}
clients_spamTimer = {}
spamLimit = 300000

bridgingThreads = list()
clientshreads = list()
toSend_message = ""
toSend_sender = ""
clients_spamCounter = {}
clients_spamTimer = {}
keepThreadAlive = True
listening_run = True

# ---> Listening thread
def thread__listen():
    global clients_spamCounter
    global clients_spamTimer
    global s
    global connMain
    while listening_run:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        connMain, addr = s.accept()
        data = connMain.recv(1024)
        print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Accepted connection from ' + addr[0] + ':' + str(addr[1]))
        t = threading.Thread(target=thread__bridge, args=(connMain, addr, data, ))
        bridgingThreads.append(t)
        t.start()
    return

# ---> Bridging thread that does decisions and connects listening thread to thread__client
def thread__bridge(conn, addr, data):
    global toSend_message
    global toSend_sender
    global keepThreadAlive
    global clients_spamCounter
    global clients_spamTimer
    currentRequest = data.decode('utf-8').split(';')
    if currentRequest[0] == "SYN":
        if clients.get(currentRequest[1], None) == None:
            clients[currentRequest[1]] = addr
            clients_spamCounter[currentRequest[1]] = 0
            clients_spamTimer[currentRequest[1]] = spamLimit + 1
            print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Replying with SYN-ACK back to ' + addr[0] + ':' + str(addr[1]))
            conn.sendall(b'SYN-ACK;' + bytes(addr[0], 'utf-8'))
            toSend_sender = "BOT"
            toSend_message = "User " + currentRequest[1] + " has connected to the chat, say hello!"
            keepThreadAlive = False
        else:
            print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Username ' + currentRequest[1] + ' is taken. Replying with ERR;USR_TAKEN back to ' + addr[0] + ':' + str(addr[1]))
            conn.sendall(b'ERR;USR_TAKEN')
    elif currentRequest[0] == "ACK":
        keepThreadAlive = True
        newThread = threading.Thread(target=thread__client, args=(conn, currentRequest[1]))
        clientshreads.append(newThread)
        newThread.start()
    elif currentRequest[0] == "MES":
        try:
            if clients[currentRequest[1]][0] == addr[0]:
                currentUsr = currentRequest[1]
                if clients_spamCounter[currentUsr] < 4 and clients_spamTimer[currentUsr] > spamLimit:
                    # usr is ok, no spam detected
                    print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Replying with ACK-MES back to ' + addr[0] + ':' + str(addr[1]))
                    conn.sendall(b'ACK-MES')
                    clients_spamTimer[currentUsr] = 0
                    toSend_sender = currentRequest[1]
                    toSend_message = currentRequest[2]
                    keepThreadAlive = False
                elif clients_spamCounter[currentUsr] < 4 and clients_spamTimer[currentUsr] <= spamLimit:
                    # usr is ok, but started spamming
                    print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Replying with ACK-MES back to ' + addr[0] + ':' + str(addr[1]) + ' but giving spam warning')
                    conn.sendall(b'ACK-MES')
                    clients_spamTimer[currentUsr] = 0
                    toSend_sender = currentRequest[1]
                    toSend_message = currentRequest[2]
                    keepThreadAlive = False
                    clients_spamCounter[currentUsr] += 1
                elif clients_spamCounter[currentUsr] >= 4:
                    # usr spammed, deny message
                    print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] User ' + currentUsr + ' on '  + addr[0] + ':' + str(addr[1]) + ' is spamming. Sending ERR;SPAM')
                    conn.sendall(b'ERR;SPAM')
                    clients_spamCounter[currentUsr] = 0
            else:
                print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Address ' + addr[0] + ':' + str(addr[1]) + ' is not associated with username ' + currentRequest[1] + '. Unauthorized')
                conn.sendall(b'ERR;UNAUTH')
        except:
            print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Address ' + addr[0] + ':' + str(addr[1]) + ' is not associated with username ' + currentRequest[1] + '. Unauthorized')
            conn.sendall(b'ERR;UNAUTH')
    elif currentRequest[0] == "END":
        if clients[currentRequest[1]][0] == addr[0]:
            print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Sender valid, disconnecting ' + currentRequest[1] + ' from server')
            del clients[currentRequest[1]]
            conn.sendall(b'ACK-END')
    else:
        # unknown request prefix, reply with ERR
        print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Replying with ERR back to ' + addr[0] + ':' + str(data.addr[1]))
        conn.sendall(b'ERR;UNKNOWN')

# ---> Thread that is keeping conn open with one client each
def thread__client(conn, usr):
    global toSend_message
    global toSend_sender
    global keepThreadAlive
    global clients_spamCounter
    global clients_spamTimer
    spam_timer = 0
    while keepThreadAlive and usr in clients:
        if spam_timer >= sys.maxsize - 1000000:
            # user is inactive
            conn.sendall(b'ERR;INACTIVE')
            del clients[currentRequest[1]]
            print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] User ' + usr + ' is inactive. Kicking him')
        else:
            spam_timer += 1
        if usr not in clients:
            print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Terminating connection with ' + usr)
            return
        continue
    if toSend_sender == usr:
        clients_spamTimer[usr] = spam_timer
    try:
        if toSend_message != "":
            conn.sendall(b'NEW;' + bytes(toSend_sender, 'utf-8') + b';' + bytes(toSend_message, 'utf-8'))
            print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Message ' + toSend_message + ' was sent to ' + usr)
        else:
            conn.close()
    except ConnectionResetError:
        try:
            del clients[usr]
        except:
            pass
        print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] User ' + usr + ' lost connection')
        return
    return

try:
    mainT = threading.Thread(target=thread__listen)
    mainT.daemon = True
    mainT.start()
    print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Starting esec-chat server binded to ' + host + ':' + str(port))
    while listening_run:
        time.sleep(0.2)
except KeyboardInterrupt:
    toSend_message = ""
    toSend_sender = ""
    listening_run = False
    keepThreadAlive = False
    clients.clear()
    connMain.close()
    print('[esec-chat server @ ' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' +  str(datetime.now().second) + '] Closing server...')
    sys.exit(0)
