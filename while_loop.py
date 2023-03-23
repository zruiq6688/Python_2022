lst=["Sam", "", "Ben", "Olivia", "Alicia"]


def name_adder(lst):
    i=0
    new_list = []
    while i < len(lst):
        if lst[i] != '':
            new_list.append(lst[i])
            i = i+1
        else :
            break
    return new_list
