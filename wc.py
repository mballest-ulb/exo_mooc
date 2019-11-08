def wc(nomFichier):
    with open(nomFichier, encoding='utf-8') as mon_fichier:
        cas_poss = [' ', '\n', '\t']
        c_debut = 0
        c_fin = 0
        res = mon_fichier.read()
        liste_1 = list(res)
        liste_2 = []
        x = len(liste_1)
        z = 0
    for elem in liste_1:
        if elem == '\n':
                z += 1
    for elem in liste_1:
        if (elem.isalnum() == False or elem in cas_poss) and liste_1[c_fin - 1].isalnum():
            liste_2.append(liste_1[c_debut:c_fin])
            c_debut = 0
            c_debut += c_fin + 1
        elif (elem.isalnum() == False or elem in cas_poss) and (liste_1[c_fin - 1] in cas_poss or liste_1[c_fin - 1] is not liste_1[c_fin - 1].isalnum()):
            c_debut += 1
        c_fin += 1
    y = len(liste_2)
    return x,y,z



