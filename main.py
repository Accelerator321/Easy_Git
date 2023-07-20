
import json

from search import search
from execute import execute
from listen import listen
from commands.push import push
from commands.new_branch import new_branch
from commands.change_branch import change_branch
from commands.commit import commit
from commands.reset import reset
from commands.add_remote import add_remote
from commands.set_remote import set_remote



# execute(com)

# Reading all commands 
# commands_file = open('./commands.json','r')

# commands = commands_file.read()
# commands_file.close()
# commands = json.loads(commands)
# patterns = commands.keys()


read = True
while(True):

    if(read):
        print("Enter Input-")
    text = listen()



    if 'init' in text or 'initialize' in text:
        out =execute('git init')
        print(out)

    elif 'remote' in text:
        if "add" in text:
            out = add_remote()
            if(out != None):
                print('Added succesfully')
        
        if "set" in text:
            out = set_remote()
            out = execute('git remote -v')
            print(out)
        
        else:
            v = ""
            if "-v" in text:
                v = '-v'
            out = execute(f'git remote {v}')
            print(out)
        
        
        # if "set" in text:
        #     out = set_remote()
        #     print(out)

    elif ('new' in text or 'create' in text) and 'branch' in text:
        new_branch()

    elif ('change' in text  and 'branch' in text) or 'checkout' in text:
        change_branch()

    elif 'push' in text:
        if '-f' in text or "force" in text:
            push('-f')
        else:
            push()

    elif "add" in text and 'remote' not in text:
        out = execute('git add .')
        print("added all files")

    elif "status" in text:
        out = execute('git status')
        print(out)

    elif "log" in text or "logs" in text:
        out = execute('git log')
        print(out)

    elif "commit" in text:
        out =commit()
        print(out)

    elif "reset" in text:
        out = reset()
        print(out)
    
    else:
        print('No matching command found')
    
    print('\n'+'_'*10 + "divider" +"_"*10 + '\n')




