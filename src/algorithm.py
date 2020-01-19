def chiusuraF(r, f, x):
    def condition(f, out):
        s = set()
        for x in f:
            if x[0] - out == set():
                for y in x[1]:
                    s.add(y)
        return s
    out = {elem for elem in x}
    s = condition(f, out)
    while s - out != set():
        out |= s
        s = condition(f, out)
    return out

def chiusuraG(r, f, x, ro):
    def subf(r, f, s, out, ro):
        for subSch in RO:
            s |= (chiusuraF(r, f, out & subSch) & subSch)
        return s
    out = {elem for elem in x}
    s |= subf(r, f, set(), out, ro)
    while s - out != set():
        out |= s
        s |= subf(r, f, s, out, ro)
    return out

def scheme_preserveF(r, f, ro):
    for x in f:
        h = chiusuraG(r, f, x[0], ro)
        if x[1] - h != set():
            return False
    return True

def scheme_no_information_lose(r, f, ro): # ------------da finire
    matrix = []
    r = list(r)
    ro = list(ro)
    mapR = dict()
    mapRO = dict()
    for i in range(len(r)):
        mapR[r[i]] = i
    for i in range(len(ro)):
        mapRO[tuple(ro[i])] = i
    for i in range(len(ro)):
        l = []
        for j in range(len(r)):
            if r[j] in ro[i]:
                l.append("a")
            else:
                l.append(f"b{i}{j}")
        matrix.append(l)
    change = True
    print(mapR)
    print(mapRO)
    print(matrix)
    while change:
        for x in f:
            for i in range(len(matrix)):
                continue #proseguire da qui

def get_minimalF(f): #-------------------------- da finire
    def divide_dependencies(f): #step1
        for i in reversed(range(len(f))):
            if len(f[i][1]) > 1:
                x = f[i][0]
                y = f[i][1]
                f.pop(i)
                for elem in y:
                    f.append([x, {elem}])
        return f

    def check_dependencies(f): #step2
        def check_minimality(dip): #da scrivere
            return False
        for i in reversed(range(len(f))):
            h = check_minimality(f[i])
            if h:
                f[i] = h
        return f

    def check_redoundance(f): #step3
        for i in reversed(range(len(f))):
            dip = f[i]
            x_pre_remove = chiusuraF({}, f, dip[0])
            f.pop(i)
            x_post_remove = chiusuraF({}, f, dip[0])
            if x_pre_remove != x_post_remove:
                f.append(dip)
        return f

#    out = divide_dependencies(f) #ok
#    out = check_dependencies(f)
#    out = check_redoundance(f) #ok
    return out

def decay(r, f):
    #f = get_minimalF(f)
    s = set()
    ro = []
    det_or_dip = {y for x in f for y in x[0]} | {y for x in f for y in x[1]}
    for a in r:
        if a not in det_or_dip:
            s |= a
    if s != set():
        ro.append(s)
        r = r - s
    for x in f:
        if x == [r - x[1], x[1]]:
            ro.append(r)
    else:
        for x in f:
            ro.append(x[0] | x[1])
    return ro


def isKey(r, f, k):
    confronto = chiusuraF(r, f, k)
    for x in r:
        if x not in confronto:
            return False
    return True



R = {"A", "B", "C", "D", "E", "L"}
F = [[{"B", "C"}, {"E"}], [{"C"}, {"D"}], [{"B"}, {"D"}], [{"E"}, {"L"}], [{"D"}, {"A"}]]
#RO = [{"A", "C"}, {"A", "D", "E"}, {"C", "D", "E"}, {"A", "D"}, {"B"}]


#print(decay(R, F))

