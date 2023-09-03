import os

from typing import List, Dict, Union


from User import User
from Email import Email

###########################################################################################################
# FILE service.py

SEND_CHECK_INTERVAL = 50

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
    return Email(sender, sender, 'PSYND Newsletter: Email checking', """\
                                                                <html>
                                                                    <body>
                                                                        <p><br>
                                                                        UPDATE:  """ + str(SEND_CHECK_INTERVAL) + """ emails sent since last email.</p>
                                                                    </body>
                                                                </html>

                                                                """, {}, None)
  

def send_msg(msg:Email)->int:
    # send email
    # write log file
    #
    return 0
    
    