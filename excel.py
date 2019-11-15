def reader_csv(folder1, folder2):
    POSS = [';']
    catch_component_f = []
    catch_component_s = []
    stick_first = []
    stick_second = []
    corrector_f = []
    corrector_s = []
    with open(folder1, encoding='utf-8') as my_first:
        read_first = my_first.read()
        for component in read_first:
            catch_component_f.append(component)
    with open(folder2, encoding='utf-8') as my_second:
        read_second = my_second.read()
        for component in read_second:
            catch_component_s.append(component)
    print(catch_component_s)
    # On s'occupe du premier fichier.
    counter_start = 0
    counter_end = 0
    for element in read_first:
        if element in POSS:
            stick_first.append(''.join(catch_component_f[counter_start:counter_end]))
            counter_start = 0
            counter_start += counter_end + 1
        if element == '\n':
            stick_first.append(''.join(catch_component_f[counter_start:counter_end]))
            stick_first.append(element)
            counter_start = 0
            counter_start += counter_end + 1
        counter_end += 1
    # Ici, du second.
    counter_end = 0
    counter_start = 0
    for element in read_second:
        if element in POSS:
            stick_second.append(''.join(catch_component_s[counter_start:counter_end]))
            counter_start = 0
            counter_start += counter_end + 1
        if element == '\n':
            stick_second.append(''.join(catch_component_s[counter_start:counter_end]))
            stick_second.append(element)
            counter_start = 0
            counter_start += counter_end + 1
        counter_end += 1
    print(stick_second)
    # On se réoccupe du premier.
    counter_start = 0
    counter_end = 0
    for element in stick_first:
        if element == '\n':
            corrector_f.append(stick_first[counter_start:counter_end])
            counter_start = 0
            counter_start += counter_end + 1
        counter_end += 1
    # et du second.
    counter_start = 0
    counter_end = 0
    for element in stick_second:
        if element == '\n':
            corrector_s.append(stick_second[counter_start:counter_end])
            counter_start = 0
            counter_start += counter_end + 1
        counter_end += 1
    print(corrector_s)

reader_csv('result-pass-fail-0.csv', 'result-count-0.csv')



























