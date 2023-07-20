
from execute import execute
from listen import listen

def reset():
    print('Enter log id-')
    id = listen()
    out = execute(f'git reset {id}')
    return out