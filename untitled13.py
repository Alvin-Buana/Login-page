def yey (l):
    l.sort(key=lambda s: list(map(int, s.split('.'))))
    for i in l:
        if(i == l[-1]):
            print(str(i),end=(' '))
        else:
            print(str(i),end=(','))
    

ok = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
yey(ok)
