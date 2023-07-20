from execute import execute
from listen import listen

def commit():
    message= '\n'

    print('Enter commit message-')
    message = listen(read = True)
    out = execute(f'git commit -m "{message}"')
    return out