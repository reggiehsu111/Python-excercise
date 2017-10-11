import os
import string
# -*- coding: utf-8 -*-

def rename_files():
    #(1)Get file names from a folder
    file_list= os.listdir(r"C:\Users\user\coding\python\prank\prank")
    print(file_list)
    saved_path=os.getcwd()
    print("Current Working Directory is:"+saved_path)
    os.chdir(r"C:\Users\user\coding\python\prank\prank")
    trantab= str.maketrans("0123456789","          ")
    #(2)for each file, rename file name
    for filename in file_list:
        os.rename(filename,filename.translate(trantab))
    #os.chdir(saved_path)


rename_files()