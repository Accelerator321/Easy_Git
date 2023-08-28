
import json

from search import search
from execute import execute
from listen import listen
from commands.pull import pull
from commands.new_branch import new_branch
from commands.change_branch import change_branch
from commands.commit import commit
from commands.reset import reset
from commands.add_remote import add_remote
from commands.set_remote import set_remote





read = True
while(True):

    if(read):
        print("Enter Input-")
    query = listen()
    query =query.split()
    d = {}
    for item in query:
        d[item] = 1

    query = d
    



    if 'init' in query or 'initialize' in query:
        out =execute('git init')
        print(out)

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

    elif ('new' in query or 'create' in query) and 'branch' in query:
        new_branch()

    elif ('change' in query  and 'branch' in query) or 'checkout' in query:
        change_branch()

    elif 'push' in query:
        if '-f' in query or "force" in query:
            push('-f')
        else:
            push()
    
    elif "pull" in query:
        if '-f' in query or "force" in query:
            pull('-f')
        else:
            pull()

    elif "add" in query and 'remote' not in query:
        out = execute('git add .')
        print("added all files")

    elif "status" in query:
        out = execute('git status')
        print(out)

    elif "log" in query or "logs" in query:
        out = execute('git log')
        print(out)

    elif "commit" in query:
        out =commit()
        print(out)

    elif "reset" in query:
        out = reset()
        print(out)
    
    else:
        print('No matching command found')
    
    print('\n'+'_'*10 + "divider" +"_"*10 + '\n')




