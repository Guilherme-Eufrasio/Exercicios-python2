alunos={}
materias =["portugues","matematica","historia","geografia","ingles"]
cont_aluno = 1
while (True):
    aluno=input(f"Digite o nome do º aluno: ")
    desempenho = []
    for i in range(1,5):
        print(f"{i}º BIMESTRE")
        notas=[]
        for n in range(0,5):
            nota=float(input(f"Digite a nota do aluno em {materias[n]} ").replace(",","."))
            notas.append(nota)
        desempenho.append(notas)
    alunos[aluno] = desempenho

    opc=input("Quer continuar? (s) ou (n)").lower()
    

    if(opc=='n'):
        break
    cont_aluno+=1
    

# print(alunos)
# for a in alunos:
#     print(a)

medias = []
soma=[0,0,0,0,0]
boletim = {}
for k,v in alunos.items():
    #print(k, v)
    media = []
    soma = [0,0,0,0,0]    
    for conteudo in v:
        pos_soma=0
        for pos, nota in enumerate(conteudo):
            print(pos, nota)
            soma[pos] = (soma[pos] + nota)
        print()
   
    for s in soma:        
        media.append(s/4)
    medias.append(media)
    v.extend(medias)
    boletim[k]=v

print(medias)
print(boletim)
with open("notas.txt","w") as arquivo:
    arquivo.write(f"{boletim}")
# for k,v in alunos.items():
#     #print(k, v)
#     for conteudo in v:
#         m=0
#         pos_soma=0
#         for pos, nota in enumerate(conteudo):
#             print(pos, nota)
#             soma[pos] = (soma[pos] + nota)
#             #print(nota)

#         print()
# for s in soma:
#     media.append(s/4)

# # print(soma)
# print(media)