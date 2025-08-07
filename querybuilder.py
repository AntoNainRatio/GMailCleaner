def build_query():
    f = open("filterFrom.txt",'r')
    res = ""
    lines = f.readlines()
    for i in range(len(lines)):
        if lines[i][-1] == '\n':
            res += "from:"+lines[i][0:-1]+" "
        else:
            res += "from:"+lines[i]+" "
        if i < len(lines) - 1:
            res += "OR "
    return res
