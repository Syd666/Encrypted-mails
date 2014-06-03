#!/usr/bin/env python
import smtplib
from email.header    import Header
from email.mime.text import MIMEText
from getpass         import getpass
from smtplib         import SMTP_SSL

def sendMail(msg,sndr,rcvr):
    
# -*- coding: utf-8 -*-
    login, password = sndr , getpass('Gmail password:')
    recipients = rcvr

# create message
    
# send it via gmail
    s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    s.set_debuglevel(1)
    try:
        s.login(login, password)
        s.sendmail(sndr, recipients, msg.as_string())
    finally:
        s.quit()

def composeMail():
    print("[*] Please enter Sender's Email Address")
    sender = raw_input()
    print("[*] Please enter Reciever's Email address")
    recvr = raw_input()
    print("[*] Please enter your message.")
    usrmsg = raw_input()
    print("[*] Please enter subject.")
    subject = raw_input()
    msg = subject + ' ' + usrmsg
    mail = (msg, sender, recvr)
    return mail
def ceasarCipher(msg):
    print("[*] Enter the key you want to encrypt your message with")
    key = raw_input()
    key = int(key)
    encmsg = ''
    mode = 'Encrypt'
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newsymbol = 0
    msg = msg.upper()

    for symbol in msg:
        if symbol in LETTERS:
            i = LETTERS.find(symbol)
            if mode == 'Encrypt':
                newsymbol = i + key
            elif mode == 'Decrypt':
                newsymbol = i - key
            if newsymbol >= len(LETTERS):
                newsymbol = newsymbol - len(LETTERS)
            elif newsymbol == 0:
                newsymbol = len(LETTERS)
        encmsg = encmsg + LETTERS[newsymbol]

    return encmsg
def main():
    msg = composeMail()
    msg = str(msg)
    encmsg = ceasarCipher(msg[1])
    encmsg = str(encmsg)
    sendMail(encmsg,msg[2],msg[3])
if __name__ == "__main__":
    main()
