import re
# from main import patterns

def search(patterns,text):
    l = []
    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            l.append(match.group())
        
    return l