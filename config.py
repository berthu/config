import subprocess
import csv
import os
import difflib
import datetime
from os.path import expanduser

db_dict = {}
db_dict_dirs = {}
home = expanduser("~")

def update():
    with open('files.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if len(row) == 3:
                replace_home = row[1].replace("~",home)
                if row[2] == "f":
                    db_dict_dirs[row[0]] = replace_home
                else:
                    db_dict[row[0]] = replace_home

def display():
    print(" ")
    print("<<Files>>:")
    for (k,v) in db_dict.items():
        print(k + " <-> " + v)
    print(" ")
    print("<<Directories>>:")
    for (k,v) in db_dict_dirs.items():
        print(k + " <-> " + v)
            
def confirmation(ask_string, run_func):
    conf = True
    while conf:
        print("""
        1. Accept
        2. Deny
        """)
        conf=raw_input(ask_string + " ")
        if conf=="1":
            run_func()
            conf = False
        elif conf=="2":
            "Execution denied. Returning..."
            conf = False
        elif conf != "":
            print("\n Not a valid choice. Try again.")

def arg_string(args):
    return " ".join(args)
            
def deploy():
    print("Deploying:")
    for (k,v) in db_dict.items():
        if os.path.isfile(v): # file exists, make a backup
            args = ['cp',v,v + ".bak"]
            subprocess.Popen(args)
            print(arg_string(args))
        args = ['cp',k,v]
        subprocess.Popen(args)
        print(arg_string(args))
    for (k,v) in db_dict_dirs.items():
        v_parent = os.path.abspath(v + "..")
        if os.path.isdir(v): # file exists, make a backup
            dirname = os.path.dirname(v)
            args = ['cp','-r',v,dirname +  ".bak"]
            print(arg_string(args))            
        args = ['cp','-r',k,v_parent]
        subprocess.Popen(args)
        print(arg_string(args))        
    
def generate_bash_script():
    file = open("./deployment.sh","w")
    file.write("#!/bin/bash\n")
    print("#!/bin/bash")
    for (k,v) in db_dict.items():
        args = ['cp',k,v]
        print(arg_string(args))
        file.write(arg_string(args) + "\n")
    for (k,v) in db_dict_dirs.items():
        v_parent = os.path.abspath(v + "..")
        args = ['cp','-r',k,v_parent]
        print(arg_string(args))
        file.write(arg_string(args) + "\n")
    file.close()
        
def collect():
    print("Collection")
    for (k,v) in db_dict.items():
        if os.path.isfile(k): # file exists, make a backup
            args = ['cp',k,k+".bak"]
            subprocess.Popen(args)
            print(arg_string(args))
        args = ['cp',v,k]
        subprocess.Popen(args)
        print(arg_string(args))        
    for (k,v) in db_dict_dirs.items():
        k_parent = os.path.abspath(k + "..")
        if os.path.isdir(k): # file exists, make a backup
            dirname = os.path.dirname(k)
            args = ['cp','-r',k,dirname + ".bak"]
            subprocess.Popen(args)
            print(arg_string(args))
        args = ['cp','-r',v,k_parent]
        subprocess.Popen(args)
        print(arg_string(args))

def check_diff_files(file1, file2):
    result = ""
    with open(file1, 'r') as hosts0:
        with open(file2, 'r') as hosts1:
            diff = difflib.unified_diff(
                hosts0.readlines(),
                hosts1.readlines(),
                fromfile=file1,
                tofile=file2,
            )
            for line in diff:
               result += line
    return result
                
def checkdiff(deploy=True):
    if deploy:
        arrow_string = " -> "
    else:
        arrow_string = " <- "
        
    print("The following files will be overwritten:")
    for (k,v) in db_dict.items():
        if ~os.path.isfile(v) or ~os.path.isfile(k):
            continue
        out = check_diff_files(v,k)
        if out != "":
            print(k + arrow_string + v)

    for (k,v) in db_dict_dirs.items():
        if ~os.path.isdir(k) or ~os.path.isdir(v):
            continue
        k_files = os.listdir(k)
        v_files = os.listdir(v)
        if deploy:
            for k_file in k_files:
                k_file_verbose = k  + k_file
                if k_file in v_files:
                    v_file_verbose = v  + v_files[v_files.index(k_file)]
                    out = check_diff_files(k_file_verbose,v_file_verbose)
                    if out != "":
                        print(k_file_verbose + arrow_string + v_file_verbose)    
                else:
                    print(k_file_verbose + arrow_string + v + k_file)
        else:
            for v_file in v_files:
                v_file_verbose = v  + v_file
                if v_file in k_files:
                    k_file_verbose = k  + k_files[k_files.index(v_file)]
                    out = check_diff_files(v_file_verbose, k_file_verbose)
                    if out != "":
                        print(k_file_verbose + arrow_string + v_file_verbose)    
                else:
                    print(k + v_file + arrow_string + v_file_verbose)


def diff():
    for (k,v) in db_dict.items():
        out = check_diff_files(v,k)
        if out != "":
            print(out)
    
    for (k,v) in db_dict_dirs.items():
        k_files = os.listdir(k)
        v_files = os.listdir(v)
        if deploy:
            for k_file in k_files:
                k_file_verbose = k  + k_file
                if k_file in v_files:
                    v_file_verbose = v  + v_files[v_files.index(k_file)]
                    out = check_diff_files(k_file_verbose,v_file_verbose)
                    if out != "":
                        print(out)
                else:
                    print(k_file + " does not exist locally.")
        else:
            for v_file in v_files:
                v_file_verbose = v  + v_file
                if v_file in k_files:
                    k_file_verbose = k  + k_files[k_files.index(v_file)]
                    out = check_diff_files(v_file_verbose, k_file_verbose)
                    if out != "":
                        print(out)
                else:
                    print(v_file + " does not exist on the repo.")

if __name__ == "__main__":
    ans=True
    while ans:
        update()
        print ("""
        1. List configs
        2. Deploy configs
        3. Collect configs
        4. Diff configs
        5. Generate bash deployment script
        6. Exit
        """)
        ans=raw_input("Hello Bert, what would you like to do? ")
        if ans=="1":
            print("\n List of configs:")
            display()
        elif ans=="2": 
            print("\n DEPLOYMENT")
            checkdiff(deploy=True)
            confirmation("Deploy?", deploy)
        elif ans=="3":
            print("\n COLLECTION: The following files will be collected")
            checkdiff(deploy=False)            
            confirmation("Collect?", collect)
        elif ans=="4":
            print("\n DIFF: Diff files:")
            diff()
        elif ans=="5":
            print("\n Generate deployment script:")
            generate_bash_script()
        elif ans=="6":
            print("\n Goodbye!")
            ans = False
        elif ans !="":
            print("\n Not a valid choice. Try again.") 

