import socket
from tkinter import *

def send(listbox,entry):
    message_to_client =  entry.get()
    listbox.insert('end',"Server: "+message_to_client)
    entry.delete(0,END)
    client.send(bytes(message_to_client,"utf-8"))
def receive(listbox):
    message_from_client = client.recv(100)
    listbox.insert('end',"Client: "+message_from_client.decode("utf-8"))
    if 'bye' in message_from_client.decode("utf-8"):
        client.close()

root = Tk()
root.title("Chatbox: Server")
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

s.bind((HOST_NAME,PORT))

s.listen(4)  #Listen is basically How many unsuccessful times the socket will listen before terminating the connection..

client, address = s.accept()

root.mainloop()