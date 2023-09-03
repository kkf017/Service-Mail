import hashlib
from typing import List, Dict, Union

from data import read_file_csv, read_json

###########################################################################################################
# FILE User.py + SQL part to get informations (ev.)


class User:
    def __init__(self, email, firstname=None, lastname=None, password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email.lower()
        
        self.emailHash = hashlib.md5((email.lower()).encode("UTF8")).hexdigest()
        
        #self.gender =  #informations
        
        #self.EmailLogs = None
      
 
        self.name = "{} {} <{}>".format(firstname, lastname, email)
        self.password = password
        
        
def get_users(filename:str)->List[User]:
    """
        function to get receivers from email-list .csv.
        input: 
            filename - name of the file 
        output: 
            list of users
    """
    data_users = read_file_csv(filename)
    return [ User(user[2], user[0], user[1]) for user in data_users]
    
    
def get_sender()->User:
    """
        function to get sender.
        input: 
            None
        output: 
            sender - as User object
    """
    data_sender = read_json("./config.json")
    sender = User(data_sender["SENDER"]["EMAIL"], data_sender["SENDER"]["FIRSTNAME"], data_sender["SENDER"]["LASTNAME"], data_sender["SENDER"]["PASSWORD"])
    sender.name = data_sender["SENDER"]["NAME"]
    return sender
        
