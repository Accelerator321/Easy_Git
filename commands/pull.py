
from listen import listen
from execute import execute
from speak import wreak

def pull(mode = ""):
    print("Pull from -")
    sources = execute('git remote')

    sources = sources.split("\n")
    sources.pop()
    for i  in range(len(sources)):
        print(i+1,"- ", sources[i])
    

    print('\n')
    wreak('pleae enter an index')
    
    source_ind = -1
    while(True):
        try:
            source_ind= int(listen(read=True))
        # break
        except Exception:
            wreak("Please enter a valid index")
            continue

        if(source_ind<=0 or source_ind >len(sources)):
            wreak("Please enter a valid index")
            continue
        else:
            break
    
    
    source_ind -=1
    wreak("Enter-branch Name-")
    branch  = listen(read = True)
    
    out =execute(f"git pull {mode} {sources[source_ind]} {branch}")
    return out

    


