import time
import sys
import os

from typing import List, Dict, Union

sys.path.insert(1, './module')
from User import User
from Email import Email
from data import create_file_csv, read_json, get_date
from service import check_dir_logs, check_message, send_mail 
from preparation import func1, func2
    
###########################################################################################################
# FILE main.py


def main(filename:str, folder:str)->int:
    
    
    # check if log directory exists
    logsDir = check_dir_logs(filename)
    FILE_LOG = "{}logs/sent-log_{}.csv".format(filename, get_date(1))
    create_file_csv(FILE_LOG, ['row','firstname','lastname', 'email','Date','Subject', 'Mail sent', 'Hash', 'Subject'])
    
    
    receivers, sender, emails = func1(filename, folder)


    # send email
        # function sent email for only one user

    emailCheck = check_message(sender)
    data = read_json("./config.json")
    port = data["SERVER"]["PORT"]
    host = data["SERVER"]["HOST"]
    checkInterval = data["CHECK"]["CHECK INTERVAL"]
    
    i = 0
    for email in emails:
        flag = func2(i, FILE_LOG, email, port, host)
        
        if i % checkInterval == 0:
            send_mail(i, sender, sender, emailCheck , port, host)
        
        i += 1
        time.sleep(5)
    
    return 0
    
    
if __name__ == "__main__":

    filename = sys.argv[1] # Name of folder containing the campains
    folder = sys.argv[2] # name of the selected campaign
 
    main(filename, folder)
