from execute import execute
from commands.new_branch import new_branch

def change_branch():
    branches= execute('git branch -r')
    branches = branches[0: len(branches)-1]
    branches = branches.split('\n')

    print('change to-\n')
    for i in range(len(branches)):
        print(f'{i+1}.{branches[i]}')

    print(f'{len(branches)}. create New BRANCH')

    while(True):
        try:
            ind = int(input()) -1
            break
        except Exception:
            continue
    
    if(ind >= len(branches)):
        new_branch()
        return
    
    if(ind <0): ind = 0

    out = execute(f'git checkout {branches[ind]}')

    print(out)


