import json
from algorithm import *

def morph_r(l):
    return {x for x in l}

def morph_f(l):
    f_out = []
    for dipendenza in l:
        f_out.append([{x for x in dipendenza[0]}, {y for y in dipendenza[1]}])
    return f_out

with open("../data/assert.json") as f:
    test = json.load(f)
with open("../data/test.json") as f:
    dati = json.load(f)

keyw_test = ["chiusuraF", "chiave"]
kew_dati = ["R", "F", "X", "RO"]

#print(test)
#print(dati)

for i in range(len(test)):
    r = morph_r(dati["R"][0])
    f = morph_f(dati["F"][0])
    lista_x = dati["X"]
    for j in range(len(test[keyw_test[i]])):
        soluz = test[keyw_test[i]][j]
        print(soluz)
        assert chiusuraF(r, f, set()) == set(soluz)
