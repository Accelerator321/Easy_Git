
import json
from execute import execute
from listen import listen
from commands.pull import pull
from commands.push import push
from commands.new_branch import new_branch
from commands.change_branch import change_branch
from commands.commit import commit
from commands.reset import reset
from commands.add_remote import add_remote
from commands.set_remote import set_remote
from speak import wreak
import os






#  Trying to read the mode of operation - Text\Speech
try:
    file = open('mode.json')
    mode_data = json.load(file)
except Exception:
    file = open('mode.json',"w")
    file.write('{"read": "true"}')
    mode_data = {"read":True}

file.close()

read = mode_data["read"]



print("\n",10*"_",end="")
print("Welcome to Easy Git",end="")
print(10*"_","\n")
print("Currently working at-", os.getcwd())
while(True):

    #  Taking user input
    if(read):
        wreak("Please enter Input-")
    else:
        wreak("Please speak your command")
    query = listen(read)
    query =query.split()
    d = {}
    for item in query:
        d[item] = 1

    query = d
    
    #  Stop the programm
    if "stop" in query or "exit" in query:
        exit()


    #  Show current directory
    elif "current" in query or 'working' in query or "directory" in query:
        print(os.getcwd())


    #  Change working directory 
    elif 'change' in query and ('folder' in query or 'directory' in query):
        
    
        while(True):
            wreak("Please enter the directory path")
            try:
                dir = listen(read)
                os.chdir(dir)
                print('now working at - dir')
                break
            
            except Exception:
                wreak('Enter valid directory')
                continue


    # Change operation mode  
    elif ("change" in query or "switch" in query )and "mode" in query:
        read  = (not read)
        print(read)
        mode_data["read"] = read
        json_object= json.dumps(mode_data)

        with open("mode.json", "w") as outfile:
            outfile.write(json_object)
        if read:
            print("Switched to text mode")
        else:
            print("Switched to speech mode")


    #  Initialize repository
    elif 'init' in query or 'initialize' in query:
        out =execute('git init')
        print(out)


    #  Add remote repository

    elif 'remote' in query:
        if "add" in query:
            out = add_remote()
            if(out != None):
                print('Added succesfully')
        
        if "set" in query:
            out = set_remote()
            out = execute('git remote -v')
            print(out)
        
        else:
            v = ""
            if "-v" in query:
                v = '-v'
            out = execute(f'git remote {v}')
            print(out)



    #  Create new branch
    elif ('new' in query or 'create' in query) and 'branch' in query:
        new_branch()


    #  Change branch
    elif ('change' in query  and 'branch' in query) or 'checkout' in query:
        change_branch()


    #  Push changes
    elif 'push' in query:
       
        if '-f' in query or "force" in query:
            out= push('-f')
        else:
            out= push()
      
        print(out)
    

    #  Pull command
    elif "pull" in query:
        
        if '-f' in query or "force" in query:
           out =  pull('-f')
        else:
            out = pull()
        
        print(out)

    

    #  Add or stage changes

    elif ("add" in query or "stage" in query) and 'remote' not in query:
        out = execute('git add .')
        wreak("added all files")


    #  Status command
    elif "status" in query:
        out = execute('git status')
        print(out)


    # Check logs

    elif "log" in query or "logs" in query:
        out = execute('git log')
        print(out)


    # Commit changes
    elif "commit" in query:
        out =commit()
        print(out)


    #  Reset changes
    elif "reset" in query:
        out = reset()
        print(out)
    
    else:
        print('No matching command found')
    
    print('\n'+'_'*10 + "divider" +"_"*10 + '\n')




