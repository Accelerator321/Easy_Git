from execute import execute
from listen import listen

def new_branch():
    new = '\n'

    while(new == '\n'):
        print('Enter branch name-')
        new = listen(read = True)
    new = new.replace(' ',"")
    
    out = execute(f'git branch {new}')

    print(out)
