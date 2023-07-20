from execute import execute
import os
from listen import listen

def new_branch():
    new = '\n'

    while(new == '\n'):
        print('Enter branch name-')
        new = listen(read = True)
    new = new.replace(' ',"")
    
    try:
        os.system(f"git branch {new}")

        print(f"Successfully created the branch '{new}'")
    except OSError as e:
        print(f"Failed to create the branch. Error: {e}")

