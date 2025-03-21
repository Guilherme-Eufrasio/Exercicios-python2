cpf=[5,4,0,3,8,0,7,7,8,0,2]
mult=cpf[0]*10,cpf[1]*9,cpf[2]*8,cpf[3]*7,cpf[4]*6,cpf[5]*5,cpf[6]*4,cpf[7]*3,cpf[8]*2
soma=sum(mult)
div1=soma%11
if (div1<0):
    v=0
else:
    va=11-div1
nmult=cpf[0]*11,cpf[1]*10,cpf[2]*9,cpf[3]*8,cpf[4]*7,cpf[5]*6,cpf[6]*5,cpf[7]*4,cpf[8]*3,cpf[9]*2
nsoma=sum(nmult)
ndiv1=nsoma%11
# ndiv2=nsoma/11
if (ndiv1<2):
    p2=0
else:
    p2=11-ndiv1
print(mult)
print(div1)
print(p2)

