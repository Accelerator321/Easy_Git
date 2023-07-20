
import json

from search import search
from execute import execute
from listen import listen
from commands.push import push
from commands.new_branch import new_branch
from commands.change_branch import change_branch



# execute(com)

# Reading all commands 
commands_file = open('./commands.json','r')

commands = commands_file.read()
commands_file.close()
commands = json.loads(commands)
patterns = commands.keys()


text = listen()

if 'init' in text or 'initialize' in text:
    out =execute('git init')
    print(out)


elif ('new' in text or 'create' in text) and 'branch' in text:
    new_branch()

elif ('change' in text  and 'branch' in text) or 'checkout' in text:
    change_branch()

elif 'push' in text:
    push()



