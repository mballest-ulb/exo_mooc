def next_line(line):
    if not line:
        res = [1]
    else:
        compteur = 0
        res = []
        valeur = line[0]
        for n in line:
            if n == valeur:
                compteur += 1

            else:
                res.extend([compteur, valeur])
                valeur = n
                compteur = 1
        res.extend([compteur, valeur])
    return res




