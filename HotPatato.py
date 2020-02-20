from Queen import Queen

def hotpatato(namelist,num):
    patqueen = Queen()
    for name in namelist:
        patqueen.enqueen(name)

    while patqueen.size() > 1:
        for i in range(num):
            patqueen.enqueen(patqueen.dequeen())

        patqueen.dequeen()

    return patqueen.dequeen()

name = ["a","b","c","d","e","f","g","h"]
num = 5
result = hotpatato(name,num)
print(result)
