from listen import listen
from execute import execute
from search import search
import json

commands_file = open('./commands.json','r')

commands = commands_file.read()
commands_file.close()
commands = json.loads(commands)
patterns = commands.keys()



def push():
    branches= execute('git branch -r')
    branches = branches[0: len(branches)-1]
    branches = branches.split('\n')

    print('push to-\n')
    for i in range(len(branches)):
        print(f'{i+1}.{branches[i]}')

    while(True):
        try:
            ind = int(input()) -1
            break
        except Exception:
            continue
    
    if(ind <0): ind = 0

    out = execute(f'git push {branches[ind]}')

    print(out)

