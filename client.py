import socket
from tkinter import *

def send(listbox,entry):
    message_to_server =  entry.get()
    listbox.insert('end',"Client: "+message_to_server)
    entry.delete(0,END)
    s.send(bytes(message_to_server,"utf-8"))
def receive(listbox):
    message_from_server = s.recv(100)
    listbox.insert('end', "Server: "+message_from_server.decode("utf-8"))
    if 'bye' in message_from_server.decode("utf-8"):
        s.close()

root = Tk()
root.title("Chatbox: Client")
entry = Entry()
entry.pack(side=BOTTOM, fill=X)
listbox = Listbox(root, width=35, height = 10)
listbox.pack(fill=BOTH, expand=True)

button = Button(root,text="Send",command= lambda : send(listbox,entry))
button.pack(side=RIGHT)
rbutton = Button(root,text="Receive", command = lambda : receive(listbox))
rbutton.pack(side = LEFT)

# Created a Socket with configurations of IPv4 and TCP Protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

HOST_NAME = socket.gethostname() # Retreiving the host name
PORT = 1234  #Port number at which Client and Server Connect..

s.connect((HOST_NAME,PORT)) # Connecting to Server using the Hostname and port number..

# Buffer:- Buffer is used to make the message split into chunks 
# such that whenever a longer message or data transfer occurs we need not wait in the line for the longer time..
# Instead we keep on receiving the message in chunks to un interrupt the data transfer until complete loading.. 


root.mainloop()