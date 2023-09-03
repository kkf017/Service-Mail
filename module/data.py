import csv
import json
from datetime import datetime

from typing import List, Dict, Union

###########################################################################################################
# FILE data.py

def get_date(format:int)->str:
    """
        function to get date.
        input: 
            
        output: 
            date (format)
    """
    date = datetime.now()
    match format:
        case 0:
            return "{}h{}min{}s {}/{}/{}".format(str(date.hour), str(date.minute), str(date.second), str(date.day), str(date.month), str(date.year))
        case 1:
            return "{}-{}-{}_{}-{}-{}".format(str(date.year), str(date.month), str(date.day), str(date.hour), str(date.minute), str(date.second))
        case _:
            raise Exception("[-] Error: Unknown option to set date.")
            
            
def read_txt(filename: str)->List[str]:
    """
        function to reads a .txt file
        input: 
            filename - name of the file to read
        output: 
            list of the strings contained in the .txt file
    
    """
    x = []
    for line in open(filename, 'r'):
        item = line.rstrip()
         #item = item.split()
        x.append(item)
    x = list(filter(lambda x: x != '', x))
    return x
    
  
def read_json(filename:str) -> Dict[str, Union[str, int]]:
    """"
        function to read .json file.
        input: 
            filename - name of the file to read
        output: 
            None
    
    """
    with open(filename, "r") as f:
        return json.load(f)
        
            
def create_file_csv(filename:str, x:List[str])->None:
    """
        function to create a .csv file.
        input: 
            filename - name of the file to create
            rows - name of the columns
        output: 
            None
    """
    with open(filename , 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(x)
        
        
def write_file_csv(filename:str, x:List[str])->None:
    """
        function to write on a .csv file.
        input: 
            filename - name of the file to write
            x - data to write
        output: 
            None
    """
    with open(filename , 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(x)
        
def read_file_csv(filename: str) -> List[List[str]]:
    """
        function to read a .csv file.
        input: 
            filename - name of the file 
        output: 
            data contained in .csv file
    """
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data.append(row)
    data = data[1:]
    return data
