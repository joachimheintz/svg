def loadFromDir(dir):
    """load all .py files in dir"""
    from os import listdir
    files = listdir(dir)
    for file in files:
        if file[-3:] == '.py':
            f = dir + '/' + file
            print(f)
            exec(open(f).read())
