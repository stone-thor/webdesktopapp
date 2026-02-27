

containsMoreThanOne(sequence, of):
    found = False
    for it in of:
        if sequence.count(it) == 1 && found == False:
            found = True
        elif sequence.count(it) == 1 && found == True:
            return True
    return False