from execute import execute
from listen import listen

def add_remote():
    print('ADD AS-')
    print('1. origin')
    print("2. upstream")
    print("3. new")
    
    d = {1:'origin', 2:"upstream"}
    print('Enter option no-')
    while(True):
        try:
            opt = int(listen(read = True))
            break
        except Exception:
            continue

    if(opt >=3):
        print('Enter Name-')
        origin = listen()
    elif opt<=0:
        opt = 1
    else:
        origin = d[opt]
    
    print('Enter Url-')
    url = listen()

    out = execute(f'git remote add {origin} {url}')