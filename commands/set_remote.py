from execute import execute
from listen import listen
from speak import wreak

def set_remote():
    print('set url of-')
    options = execute('git remote')
    options = options.split()

    
    for i in range(len(options)):
        print(f'{i+1}. {options[i]}')
    
    print('\n')
    wreak("Enter option no")

    while(True):
        try:
            ind = int(listen(read = True)) -1
            break
        except Exception:
            continue
    
    if(ind <0 or ind >= len(options)): ind = 0
    wreak('Enter url')
    url = listen()
    out = execute(f'git remote set-url {options[ind]} {url}')
    