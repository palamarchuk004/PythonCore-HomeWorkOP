          # Are You Playing Banjo?

def areYouPlayingBanjo(name):
    if name[0]  == 'r':
        return name + " " 'plays banjo'
    elif name[0]  == 'R':
        return name + " " 'plays banjo'
    else:
        return name + " " 'does not play banjo'
x=str(input('Input name: '))
print(areYouPlayingBanjo(x))
