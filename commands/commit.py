from execute import execute
from listen import listen
from speak import wreak

def commit():
    message= '\n'

    wreak('Enter commit message-')
    message = listen(read = True)
    out = execute(f'git commit -m "{message}"')
    return out