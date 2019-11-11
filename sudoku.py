def check_sudoku(grille):
    def check_rows(plateau):
        res = False
        repere = 0
        counter = []
        poss = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        rangee = 0
        for elem in plateau:
            colonne = 0
            counter.clear()
            for composant in elem:
                if composant in poss and composant not in counter:
                    counter.append(composant)
                colonne += 1
            rangee += 1
            if len(counter) < 9:
                repere += 1
        if repere == 0:
            res = True
        return res

    def check_cols(plateau):
        res = False
        repere = 0
        counter = []
        poss = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        colonne = 0
        for elem in plateau:
            rangee = 0
            counter.clear()
            for composant in elem:
                if plateau[rangee][colonne] in poss and plateau[rangee][colonne] not in counter:
                    counter.append(plateau[rangee][colonne])
                rangee += 1
            colonne += 1
            print(counter)
            if len(counter) < 9:
                repere += 1
        if repere == 0:
            res = True
        return res

    def check_regions(plateau):
        res = False
        repere = 0
        counter = []
        cop = []
        poss = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        rangee = 1
        for elem in plateau:
            a = 0
            colonne = 1
            for composant in elem:
                if colonne % 3 == 0 and composant in poss:
                    counter.append(plateau[rangee - 1][a:colonne])
                    a = 0
                    a += colonne
                colonne += 1
            rangee += 1
        print(counter)
        for i in range(len(counter)):
            if i == 0 or i == 3 or i == 6:
                cop.append(counter[i])
            elif i ==

