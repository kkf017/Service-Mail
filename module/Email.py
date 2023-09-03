from typing import List, Dict, Union

from data import read_txt
from User import User

###########################################################################################################
# FILE Email.py

class Email:
    def __init__(self, sender, receiver, subject, html, opts=None, attachment=None):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.html = html
        self.opts = opts
        self.attachment = attachment
        
        self.campaign = None
        
        
def get_emails(filename:str, folder:str, receivers:List[User], sender:User, opts:Dict[str, Union[str, List[str]]])->List[Email]:
    """
        function to get emails - to send -.
        input: 
            filename - name of the (working) directory
            folder - name of the folder (containing html content and subject)
            receivers - list of receivers
            sender -
        output: 
            list of emails (to send)
    """
    return [Email(sender, receiver, 
                               ''.join(read_txt("{}{}/subject.txt".format(filename,folder))), 
                               ''.join(read_txt("{}{}/email-content.html".format(filename,folder))), 
                                opts, None) for receiver in receivers]


