from listen import listen
from execute import execute
from search import search
import json




def push(mode=""):
    
    print("Push To-")
    sources = execute('git remote')

    sources = sources.split("\n")
    sources.pop()
    for i  in range(len(sources)):
        print(i+1,"- ", sources[i])
    

    print('\npleae enter an index-')
    
    source_ind = -1
    while(True):
        try:
            source_ind= int(listen(read=True))
        # break
        except Exception:
            print("Please enter a valid index trywala")
            continue

        if(source_ind<=0 or source_ind >len(sources)):
            print(source_ind, len(sources),source_ind<=0,source_ind >len(sources) )
        else:
            break
    
    
    source_ind -=1
    
    # if(ind <0 or ind>= len(branches)): ind = 0
    print('Enter branch name-')
    branch = listen()

    # out = execute(f'git push {mode} {branches[ind]}')
    out = execute(f'git push {mode} {sources[source_ind]} {branch}')

    print(out)

