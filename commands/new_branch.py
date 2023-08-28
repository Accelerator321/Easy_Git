from execute import execute
from listen import listen
from speak import wreak

def new_branch():
    new = '\n'

    wreak('Enter branch name-')
    new = listen(read = True)
    new = new.replace(' ',"")
    
    out = execute(f'git branch {new}')

    print(out)
