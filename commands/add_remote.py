from execute import execute
from listen import listen
from speak import wreak

def add_remote():
    print('ADD AS-')
    print('1. origin')
    print("2. upstream")
    print("3. new")
    
    d = {1:'origin', 2:"upstream"}
    wreak('Enter option no-')
    while(True):
        try:
            opt = int(listen(read = True))
            break
        except Exception:
            continue

    if(opt >=3):
        wreak('Enter Name-')
        origin = listen()
    elif opt<=0:
        opt = 1
    else:
        origin = d[opt]
    
    wreak('Enter Url-')
    url = listen()

    out = execute(f'git remote add {origin} {url}')