# Convert elevator floors
inp = input("Europe floor?")
euf=int(inp)
if (euf<0):
    print('wrong floor')


else:
    usf = euf +1
    if (euf>=12):
        usf=euf+ 2
    print ('US floor', usf )

