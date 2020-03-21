import math
import heapq
import timeit

### TODO ###
# 1. Dodac przerwania

plik = open("data20.txt", "r")
linie = plik.readlines()
n = int(linie[0].split()[0])

zadania = []
for i in range(1, n+1):
    linia = linie[i].split()
    zadania.append([int(linia[0]),int(linia[1]),int(linia[2]), i])
plik.close()

def sortR(zad):
    while True:
        zmiana = False
        for j in range(0, n-1):
            if zad[j][0] > zad[j+1][0]:
                zad[j], zad[j+1] = zad[j+1], zad[j]
                zmiana = True

        if zmiana == False:
            return

def sortRQ(zad):
    sortR(zad)

    while True:
        zmiana = False
        for j in range(0, n - 1):
            if zad[j][0] == zad[j+1][0]:
                if zad[j][2] < zad[j + 1][2]:
                    zad[j], zad[j + 1] = zad[j + 1], zad[j]
                    zmiana = True

        if zmiana == False:
            return

def calculate(zad):
    S = []
    C = []
    Cmax = 0

    S.append(zad[0][0])
    C.append(S[0] + zad[0][1])
    Cmax = C[0] + zad[0][2]

    for i in range(1, n):
        S.append(max(zad[i][0], C[i-1]))
        C.append(S[i] + zad[i][1])
        Cmax = max(Cmax, C[i] + zad[i][2])

    return Cmax

def getOrder(zad):
    kolejnosc = []
    for i in range(0, len(zad)):
        kolejnosc.append(zad[i][3])
    return kolejnosc

def minr(z):
    minimum = math.inf
    minimum_indeks = None
    for i in range(0, len(z)):
        if z[i][0] < minimum:
            minimum = z[i][0]
            minimum_indeks = i
    return minimum_indeks

def maxq(z):
    maksimum = 0
    maksimum_indeks = None
    for i in range(0, len(z)):
        if z[i][2] > maksimum:
            maksimum = z[i][2]
            maksimum_indeks = i
    return maksimum_indeks

def schrage(zad):
    start = timeit.default_timer()
    pi = []
    G = []
    N = zad
    t = N[minr(N)][0]

    while len(G) != 0 or len(N) != 0:
        while len(N) != 0 and N[minr(N)][0] <= t:
            indeks = minr(N)
            G.append(N[indeks])
            N.pop(indeks)
        if len(G) != 0:
            indeks = maxq(G)
            pi.append(G[indeks])
            t = t + G[indeks][1]
            G.pop(indeks)
        else:
            t = N[minr(N)][0]

    end = timeit.default_timer()
    print("Czas wykonania: {:f}".format(end-start))
    return pi
    
def schrageWithHalfHeap(zad):
    start = timeit.default_timer()
    pi = []
    G = []
    N = zad
    heapq.heapify(N)
    t = N[0][0]

    while len(G) != 0 or len(N) != 0:
        while len(N) != 0 and N[0][0] <= t:
            G.append(N[0])
            heapq.heappop(N)
        if len(G) != 0:
            indeks = maxq(G)
            pi.append(G[indeks])
            t = t + G[indeks][1]
            G.pop(indeks)
        else:
            t = N[0][0]

    end = timeit.default_timer()
    print("Czas wykonania: {:f}".format(end-start))
    return pi

def schrageWithHeap(zad):
    start = timeit.default_timer()
    pi = []
    G = []
    heapq.heapify(G) # kopiec przechwowujacy zadania wedlug malejacego q (max na szczycie)
    N = zad
    heapq.heapify(N) # kopiec przechowujacy zadania wedlug rosnacego r (min na szczycie)
    t = N[0][0]

    while len(G) != 0 or len(N) != 0:
        while len(N) != 0 and N[0][0] <= t:
            temp = N[0] # bierzemy zadanie z najmniejszym r
            temp[0], temp[2] = temp[2]*-1, temp[0] # zamieniamy miejscami r na -q a q na r [r,p,q]->[-q,p,r]
            heapq.heappush(G, temp) # dzieki powyzszemu kopiec G bedzie mial na szczycie zadanie z najwiekszym q
            heapq.heappop(N)
        if len(G) != 0:
            temp = heapq.heappop(G)
            temp[0], temp[2] = temp[2], temp[0]*-1 # odwracamy poprzednia zamiane, czyli teraz -q spowrotem na r, a r na -(-q) [-q,p,r]->[r,p,q]
            pi.append(temp)
            t = t + temp[1]
        else:
            t = N[0][0]

    end = timeit.default_timer()
    print("Czas wykonania: {:f}".format(end-start))
    return pi
'''
# Oryginal
print("- Oryginal -")
print("Kolejnosc: ", getOrder(zadania))
print("Czas: ", calculate(zadania))
# Sort R
print("- SortR -")
sortR(zadania)
print("Kolejnosc: ", getOrder(zadania))
print("Czas: ", calculate(zadania))
# Sort RQ
print("- SortRQ -")
sortRQ(zadania)
print("Kolejnosc: ", getOrder(zadania))
print("Czas: ", calculate(zadania))
'''
print("- Schrage -")
nowe_zadania = schrage(zadania.copy())
print("Kolejnosc: ", getOrder(nowe_zadania))
print("Czas: ", calculate(nowe_zadania))

print("- SchrageWithHalfHeap -")
nowe_zadania = schrageWithHalfHeap(zadania.copy())
print("Kolejnosc: ", getOrder(nowe_zadania))
print("Czas: ", calculate(nowe_zadania))

print("- SchrageWithHeap -")
nowe_zadania = schrageWithHeap(zadania.copy())
print("Kolejnosc: ", getOrder(nowe_zadania))
print("Czas: ", calculate(nowe_zadania))
