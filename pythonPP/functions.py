import readline

def completer(text,state):
    options = [i for i in commands if i.star]