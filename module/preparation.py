import hashlib
from typing import List, Dict, Union


from data import write_file_csv, read_json, get_date 
from service import send_mail
from User import User, get_users, get_sender
from Email import Email, get_emails


###########################################################################################################
# FILE ??.py


def func1(filename:str, folder:str)->Union[List[User],User,List[Email]]:
    """
        function to prepare Receivers, Sender, and Emails.
        input: 
            filename - name of the (working) directory
            folder - name of the folder (containing html content and subject)
          
        output: 
            list of receivers - as User object
            sender - as User object
            list of emails (to send)
    """
 
    # prepare receivers
    receivers = get_users("{}{}/email-list.csv".format(filename, folder))
    
    # GET INFORMATIONS - from database SQL
  
    # prepare sender
    sender = get_sender()
    
    # GET EMAIL SUBJECT for each user
            # Update campaign field in Email class
 
    # prepare Emails 
    dataOpts = read_json("./config.json")
    opts = {}
    opts['reply-to'] = dataOpts["OPTS"]["REPLY_TO"]
  
    emails = get_emails(filename, folder, receivers, sender, opts) 
    
    return receivers, sender, emails
    
  
    
def func2(i:int, filename:str, email:Email, port:int, host:str)->bool:
    """
        function to send email, and write log.
        input:
            i - 
            filename - name of the (working) directory
            email - email to send
            port - 
            host -
          
        output: 
            True if mail has been sent, False otherwise
    """
    
    date = get_date(1)

    flag = send_mail(i, email.sender, email.receiver, email, port, host)
    #send_mail(i:int, sender:User, receiver:User, mail:Email, port:int, smtp_server:str)
    
    hashEmail = email.receiver.emailHash  
    log = [i]+[email.receiver.firstname]+[email.receiver.lastname]+ [email.receiver.email]+[date]+[email.campaign]+[flag]+[hashEmail]
    write_file_csv(filename, log)
    return flag
  
