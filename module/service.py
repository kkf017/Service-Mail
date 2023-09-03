import os
import socket
import smtplib, ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.nonmultipart import MIMENonMultipart
import os
from pathlib import Path
import mimetypes
from email.charset import Charset, BASE64

from typing import List, Dict, Tuple

from data import read_json
from User import User
from Email import Email



###########################################################################################################
# FILE service.py

def check_dir_logs(filename:str)->str:
    """
        function to check if directory containing log files exists.
        input: 
            filename - name of the directory
        output: 
            None
    """
    if not os.path.isdir("{}logs/".format(filename)):
            os.mkdir("{}logs/".format(filename)) 
    return "{}logs/".format(filename)


    
def check_message(sender:User)->Email:
    """
        function to build checking message.
        input: 
            None
        output: 
            Checking message - as Email object
    """
    dataCheck = read_json("./config.json")
    SEND_CHECK_INTERVAL = dataCheck["CHECK"]["CHECK INTERVAL"]
    return Email(sender, sender, 'PSYND Newsletter: Email checking', """\
                                                                <html>
                                                                    <body>
                                                                        <p><br>
                                                                        UPDATE:  """ + str(SEND_CHECK_INTERVAL) + """ emails sent since last email.</p>
                                                                    </body>
                                                                </html>

                                                                """, {}, None)
  









def send_mail(i:int, sender:User, receiver:User, mail:Email, port:int, smtp_server:str)->bool:
    """
        function to send the email
        input: 
            sender - sender of the email
            receiver - receiver of the email
            mail - content of the email
            port - nb of port to connect
            smtp_server - server to connect
        output: 
            None
    
    """
    
    message = MIMEMultipart("alternative")
    message["Subject"] =  mail.subject
    message["From"] = sender.name #sender.email 
    
    
    
    if type(receiver.email)==str: # case of a single receiver
        receivers = [receiver.email]
        message["To"] = receiver.email #receiver.name 
        
    if type(receiver.email)==list: # case of multiple receivers
        receivers = receiver.email
        message["To"] = receiver.name #receiver.name for multiple receivers

    
    
    if 'reply-to' in list(mail.opts.keys()):
        message['reply-to'] = mail.opts['reply-to']
        

    if 'Cc' in list(mail.opts.keys()):
        message["Cc"] =  ", ".join(mail.opts['Cc'])
        receivers += mail.opts['Cc']
    
    if 'Bcc' in list(mail.opts.keys()):
        message["Bcc"] =  ", ".join(mail.opts['Bcc'])
        receivers += mail.opts['Bcc']     

    
    # convert both parts to MIMEText objects and add them to the MIMEMultipart message
    #part1 = MIMEText(mail.html, "plain")
    part2 = MIMEText(mail.html, "html")
    #message.attach(part1)
    message.attach(part2)

    
    """
    if mail.attachment != None:
        print('')        
    """

    
    context = ssl.create_default_context()
    #with smtplib.SMTP_SSL(smtp_server , port, context=context) as server:
    with smtplib.SMTP(smtp_server , port) as server:
        try:
            #server.login(login, password)
            server.login(sender.email, sender.password)
            server.sendmail(
                sender.email, receivers , message.as_string()
            )
        except smtplib.SMTPException :
            print("[-] Error: unable to send email to {0} ({1})".format(receiver.email, i))
            return False
            
        else:
            print("[+] Mail sent Successfully.")
            return True

 
 
