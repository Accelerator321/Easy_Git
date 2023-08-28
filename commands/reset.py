
from execute import execute
from listen import listen
from speak import wreak

def reset():
    wreak('Enter log id')
    id = listen()
    out = execute(f'git reset {id}')
    return out