lesmas = []
grupo = int(input(""))
try:
    lesma_entrada=input("").split()[:grupo]
    for lesma in lesma_entrada:
        lesmas.append(int(lesma))                
        maior=max(lesmas)
except EOFError:
        pass
    
if maior<10:
    print("1")
elif maior>=10 and maior<20:
    print("2")
elif maior==20:
    print("3")