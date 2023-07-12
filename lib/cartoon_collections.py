def roll_call_dwarves(arr):
    call = []
    for i, j in enumerate(arr):
        call.append(f"{i + 1}. {j}")
    return print('\n'.join(call))

def summon_captain_planet(arr):
    summon = []
    for i in arr:
        summon.append(f"{i.title()}!")
    return summon

def long_planeteer_calls(arr):
    count = 0
    for i in arr:
        if(len(i) <= 4):
            count += 1
        else:
            count += 0
    if count == len(arr):
        return False
    else:
        return True

def find_the_cheese(arr):
    check = False
    cheese = ""
    temp = []
    for i in arr:
        temp.append(i.lower())
    for i in temp:
        if i == "cheddar" or i == "gouda" or i == "camembert":
            check = True
            cheese = i
            break
        else:
            check = False
    if check:
        return cheese
    else:
        return None