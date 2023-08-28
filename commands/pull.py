
from listen import listen
from execute import execute

def pull(mode = ""):
    print("Pull from -")
    sources = execute('git remote')

    for i  in range(len(sources)):
        print(i+1,"- ", sources[i])
    
    source_ind = -1

    while(True):
        soruce_ind = listen(read=True)
        if(source_ind<=0 or source_ind >len(sources)):
            print("Please enter a valid index")
        else:
            break
    soruce_ind -=1
    out =execute(f"git pull {mode} {sources[soruce_ind]}")
    return out

    


