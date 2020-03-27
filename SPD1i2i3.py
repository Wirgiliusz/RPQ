import math
import heapq
import timeit
import copy

### TODO ###
#1. Dodac Carliera
#2. Zrobic pomiary

plik = open("data/data500.txt", "r")
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

def calculate_Cmax(zad):
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

def calculate_Cmax_toidx(zad, idx):
    S = []
    C = []
    Cmax = 0
    idx += 1

    S.append(zad[0][0])
    C.append(S[0] + zad[0][1])
    Cmax = C[0]

    for i in range(1, idx):
        S.append(max(zad[i][0], C[i-1]))
        C.append(S[i] + zad[i][1])
        Cmax = max(Cmax, C[i])

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

def minq(z):
    minimum = math.inf
    minimum_indeks = None
    for i in range(0, len(z)):
        if z[i][2] < minimum:
            minimum = z[i][2]
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
            zadN_minR_idx = minr(N)
            G.append(N[zadN_minR_idx])
            N.pop(zadN_minR_idx)
        if len(G) != 0:
            zadG_maxQ_idx = maxq(G)
            pi.append(G[zadG_maxQ_idx])
            t = t + G[zadG_maxQ_idx][1]
            G.pop(zadG_maxQ_idx)
        else:
            t = N[minr(N)][0]

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
            zadN_minR = N[0] # bierzemy zadanie z najmniejszym r
            zadN_minR[0], zadN_minR[2] = zadN_minR[2]*-1, zadN_minR[0] # zamieniamy miejscami r na -q a q na r [r,p,q]->[-q,p,r]
            heapq.heappush(G, zadN_minR) # dzieki powyzszemu kopiec G bedzie mial na szczycie zadanie z najwiekszym q
            heapq.heappop(N)
        if len(G) != 0:
            zadG_maxQ = heapq.heappop(G)
            zadG_maxQ[0], zadG_maxQ[2] = zadG_maxQ[2], zadG_maxQ[0]*-1 # odwracamy poprzednia zamiane, czyli teraz -q spowrotem na r, a r na -(-q) [-q,p,r]->[r,p,q]
            pi.append(zadG_maxQ)
            t = t + zadG_maxQ[1]
        else:
            t = N[0][0]

    end = timeit.default_timer()
    print("Czas wykonania: {:f}".format(end-start))
    return pi

def schragePMTN(zad):
    start = timeit.default_timer()
    G = []
    N = zad
    t = N[minr(N)][0]
    l = [0,0,0]
    Cmax = 0

    while len(G) != 0 or len(N) != 0:
        while len(N) != 0 and N[minr(N)][0] <= t:
            zadN_minR_idx = minr(N)
            G.append(N[zadN_minR_idx])
            if(N[zadN_minR_idx][2] > l[2]):
                l[1] = t - N[zadN_minR_idx][0]
                t = N[zadN_minR_idx][0]
                if(l[1] > 0):
                    G.append(l)
            N.pop(zadN_minR_idx)

        if len(G) != 0:
            zadG_maxQ_idx = maxq(G)
            t = t + G[zadG_maxQ_idx][1]
            l = G[zadG_maxQ_idx]
            Cmax = max(Cmax, t + G[zadG_maxQ_idx][2])
            G.pop(zadG_maxQ_idx)
        else:
            t = N[minr(N)][0]
        
    end = timeit.default_timer()
    print("Czas wykonania: {:f}".format(end-start))
    return Cmax

def schragePMTNWithHeap(zad):
    start = timeit.default_timer()
    G = []
    heapq.heapify(G) # kopiec przechwowujacy zadania wedlug malejacego q (max na szczycie)
    N = zad
    heapq.heapify(N) # kopiec przechowujacy zadania wedlug rosnacego r (min na szczycie)
    t = N[0][0]
    l = [0,0,0]
    Cmax = 0

    while len(G) != 0 or len(N) != 0:
        while len(N) != 0 and N[0][0] <= t:
            zadN_minR = heapq.heappop(N) # bierzemy zadanie z najmniejszym r
            if(zadN_minR[2] > l[2]):
                l[1] = t - zadN_minR[0]
                t = zadN_minR[0]
                if(l[1] > 0):
                    l[0], l[2] = l[2]*-1, l[0]
                    heapq.heappush(G, l)
            zadN_minR[0], zadN_minR[2] = zadN_minR[2]*-1, zadN_minR[0] # zamieniamy miejscami r na -q a q na r [r,p,q]->[-q,p,r]
            heapq.heappush(G, zadN_minR) # dzieki powyzszemu kopiec G bedzie mial na szczycie zadanie z najwiekszym q

        if len(G) != 0:
            zadG_maxQ = heapq.heappop(G)
            zadG_maxQ[0], zadG_maxQ[2] = zadG_maxQ[2], zadG_maxQ[0]*-1 # odwracamy poprzednia zamiane, czyli teraz -q spowrotem na r, a r na -(-q) [-q,p,r]->[r,p,q]
            t = t + zadG_maxQ[1]
            l = zadG_maxQ
            Cmax = max(Cmax, t + zadG_maxQ[2])
        else:
            t = N[0][0]

    end = timeit.default_timer()
    print("Czas wykonania: {:f}".format(end-start))
    return Cmax

UB = math.inf
pistar = []
def carlier(zad):
    global UB
    global pistar
    pi = schrageWithHeap(copy.deepcopy(zad))
    U = calculate_Cmax(pi)
    if U < UB:
        UB = U
        pistar = copy.deepcopy(pi)
    # szukanie b
    Cmax = 0
    idx_max = 0
    for j in range(0, len(pi)):
        C = calculate_Cmax_toidx(pi,j) + pi[j][2]
        if C >= Cmax:
            Cmax = C
            idx_max = j
    b = pi[idx_max]
    # szukanie a
    Cmax = 0
    p_sum = 0
    idx_min = 0
    for j in range(0, len(pi)):
        p_sum = 0
        for k in range(j, idx_max+1):
            p_sum += pi[k][1]
        C = pi[j][0] + b[2] + p_sum
        if C > Cmax:
            Cmax = C
            idx_min = j
    a = pi[idx_min]
    # szukanie c
    c = None
    idx_c = -1
    for j in range(idx_min, idx_max):
        if pi[j][2] < b[2]:
            idx_c = j
    if idx_c != -1:
        c = pi[idx_c]
    else:
        return pistar
    
    K = []
    for i in range(idx_c+1, idx_max+1):
        K.append(pi[i])
    rhat = K[minr(K)][0]
    qhat = K[minq(K)][2]
    phat = 0
    for task in K:
        phat += task[1]
    cr_old = c[0]
    pi[idx_c][0] = max(c[0], rhat + phat)
    LB = schragePMTNWithHeap(copy.deepcopy(pi)) #?
    if LB < UB:
        carlier(pi)
    pi[idx_c][0] = cr_old
    cq_old = c[2]
    pi[idx_c][2] = max(c[2], qhat + phat)
    LB = schragePMTNWithHeap(copy.deepcopy(pi)) #?
    if LB < UB:
        carlier(pi)
    pi[idx_c][2] = cq_old
    return pistar


'''
# Oryginal
print("- Oryginal -")
print("Kolejnosc: ", getOrder(zadania))
print("Czas: ", calculate_Cmax(zadania))
# Sort R
print("- SortR -")
sortR(zadania)
print("Kolejnosc: ", getOrder(zadania))
print("Czas: ", calculate_Cmax(zadania))
# Sort RQ
print("- SortRQ -")
sortRQ(zadania)
print("Kolejnosc: ", getOrder(zadania))
print("Czas: ", calculate_Cmax(zadania))
'''
'''
print("- Schrage -")
nowe_zadania = schrage(copy.deepcopy(zadania))
print("Kolejnosc: ", getOrder(nowe_zadania))
print("Czas: ", calculate_Cmax(nowe_zadania))

print("- SchrageWithHeap -")
nowe_zadania = schrageWithHeap(copy.deepcopy(zadania))
print("Kolejnosc: ", getOrder(nowe_zadania))
print("Czas: ", calculate_Cmax(nowe_zadania))

print("- SchragePMTN -")
print("Czas: ", schragePMTN(copy.deepcopy(zadania)))
'''
print("- SchragePMTNWithHeap -")
print("Czas: ", schragePMTNWithHeap(copy.deepcopy(zadania)))

#print(calculate_Cmax(zadania))
#print(calculate_Cmax_toidx(zadania, 0))
#print(calculate_Cmax_toidx(zadania, 0)+zadania[0][2])

#carlier(copy.deepcopy(zadania))
#print(calculate_Cmax(pistar))

print(calculate_Cmax(carlier(copy.deepcopy(zadania))))