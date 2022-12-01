import argparse
from argparse import ArgumentParser
import os
import csv
import numpy as np

parser: ArgumentParser = argparse.ArgumentParser()
parser.add_argument('-d','--dataset', type=str,required=True,help="path of dataset csv")
parser.add_argument('-o','--output', type=str,default='codes.txt',help="path of codes vocabs")
args = parser.parse_args()


d_headers=["id","context","question","answer0","answer1","answer2","answer3","label"]#dataset headers data

def get_info(data_dir):
    total_num=0
    csv_files=os.listdir(data_dir)
    print(data_dir)
    for csv_file in csv_files:        
        with open(os.path.join(data_dir,csv_file),encoding='utf-8') as f:
            rows = csv.reader(f, delimiter = '\t')
            next(rows)
            csv_array=[r for r in rows]  
            total_num+=len(csv_array)
            print("{} Num:\t {}".format(csv_file,len(csv_array)))
    print("Total Num:\t",total_num)

def main():
    dirs=["C","JAVA","C-JAVA"]
    for dir_ in dirs:
        data_dirs=os.listdir(dir_)
        for data_dir in data_dirs:
            get_info(os.path.join(dir_,data_dir))
   


if __name__ == '__main__':
    main()