import socket
import time


print ("### Hello and welcome to VAC bot ### \n")
HOST = "irc.twitch.tv"      
CHANNEL = input("What channel would you like to join? ").lower()
NICK = "wandererocular"
PASS = "oauth:wq5hz0ckho233q88ik27wdjchs9pt8"

### Sends a message to the chatroom ###
def sendMessage(s,message):
    messageMain = "PRIVMSG #" + CHANNEL + " :" + message
    s.send((messageMain + "\n").encode())
    print("Sent: " + messageMain)

def join():
    s = socket.socket() 
    s.connect((HOST, 6667))
    s.send(("PASS " + PASS + "\n").encode())
    s.send(("NICK "+ NICK + "\n").encode())                           
    s.send(("JOIN #"+ CHANNEL + "\n").encode())
    while True:
        text = s.recv(4080).decode()
        print(text)
        print(text.find("End of /NAMES list") != -1)
        if text.find("/NAMES list") != -1:
            s.send(("PRIVMSG #" + CHANNEL + " :Joined\n").encode())
            return s

def counter(s):
    number = 0
    text = s.recv(2040).decode()
    if "vac" in text.lower():
        end = time.time() + 60 ## Need to add in variable time
        number = number + 1
        while time.time() < end:
            if number == 1: ## Need to put in variable counter
                ## Need to add in Twitch API
                print ("Clip")

    


####Socket connection###
#s = socket.socket() 
#print ("Connecting to:"+HOST)                                                 
#s.send(("USER "+ NICK +" "+ NICK +" "+ NICK +"\n").encode())

#text=s.recv(2040)  
#print (text.decode())
    #if text.find(b"End of /NAMES list") != -1:
    #    Loading = False
    #if text.find(b'PING') != -1:                          
    #    s.send('PONG ' + text.split() [1] + '\n')
#text = s.recv(2040)
#print(text.decode())

#sendMessage(s,"Successfully joined chat")

#text = s.recv(2040)
#print(text.decode())

if __name__ == '__main__':
    s = join()
    counter(s)
    