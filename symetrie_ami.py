def symetrise_amis(d, englobe):
    capture = []
    for key in d:
        capture.append([key, d[key]])
    print(capture)
    if englobe:
        for key in d:
            pointeur = 0
            for i in range(len(capture)):
                if {key} <= capture[i][1]:
                    d[key] |= {capture[pointeur][0]}
                pointeur += 1
    elif not englobe:
        for key in d:
            pointeur = 0
            for i in range(len(capture)):
                if {key} <= capture[i][1] and d[key] >= {capture[i][0]}:
                    pointeur += 1
                    if d[key] > {capture[i][0]}:
                        compteur = 0
                        for j in range(len(capture)):
                            compteur += 1
                            if {capture[j][0]} <= d[key] and capture[j][1] == set():
                                d[key].discard(capture[compteur - 1][0])
            if pointeur == 0:
                d[key] = set()




