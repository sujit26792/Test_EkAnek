from collections import OrderedDict

def printCheapestFlights(d_to_m, m_to_d, k):
    sum_dict = {}
    for i in d_to_m:
        for j in m_to_d:
            s =  i + j
            if (i, j) not in sum_dict:
                sum_dict[(i, j)] = s

    d = OrderedDict(sorted(sum_dict.items(), key=lambda t: t[1]))
    f_l = list(d)[0:k]
    print(f_l)

if __name__ == "__main__":
    k = 10
    delhi_to_mumbai = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    mumbai_to_delhi = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]

    printCheapestFlights(delhi_to_mumbai, mumbai_to_delhi, k)
