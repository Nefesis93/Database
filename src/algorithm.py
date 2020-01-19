def chiusura(r, f, x):
    def condition(f, out):
        s = set()
        for x in f:
            if x[0] - out == set():
                for y in x[1]:
                    s.add(y)
        return s
    out = x
    s = condition(f, out)
    while s - x != set():
        out |= s
        s |= condition(f, out)
    return out

def chiusuraG(r, f, x, ro):
    def subf(r, f, s, out, ro):
        for subSch in ro:
            s |= chiusura(r, f, out & subSch) & subSch
        return s
    out = x
    s = subf(r, f, set(), out, ro)
    while s - out != set():
        out |= s
        s = subf(r, f, s, out, ro)
    return out

def checkSheme(r, f, ro):
    for x in f:
        print(x, "dipendenza")
        h = chiusuraG(r, f, x[0], ro)
        print(h, "chiusura G")
        if x[1] - h != set():
            return False
    return True

def isKey(r, f, k):
    confronto = chiusura(r, f, k)
    for x in r:
        if x not in confronto:
            return False
    return True



R = {"A", "B", "C", "D"}
F = [[{"A", "B"}, {"C"}], [{"D"}, {"C"}], [{"D"}, {"B"}], [{"C"}, {"B"}], [{"D"}, {"A"}]]
RO = [{"A", "B", "C"}, {"A", "B", "D"}]

print(checkSheme(R, F, RO))

print(chiusuraG(R, F, {"D"}, RO), "chiusura G di D")