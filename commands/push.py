from listen import listen
from execute import execute
from search import search
import json

# commands_file = open('./commands.json','r')

# commands = commands_file.read()
# commands_file.close()
# commands = json.loads(commands)
# patterns = commands.keys()



def push(mode=""):
    # branches= execute('git branch -r')
    # branches = branches[0: len(branches)-1]
    # branches = branches.split('\n')

    # print('push to-\n')
    # for i in range(len(branches)):
    #     print(f'{i+1}.{branches[i]}')

    # print('Enter option- No')
    # while(True):
    #     try:
    #         ind = int(input()) -1
    #         break
    #     except Exception:
    #         continue

    
    # if(ind <0 or ind>= len(branches)): ind = 0
    print('Enter branch name-')
    branch = listen()

    # out = execute(f'git push {mode} {branches[ind]}')
    out = execute(f'git push {mode} origin {branch}')

    print(out)

