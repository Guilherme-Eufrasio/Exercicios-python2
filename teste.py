import json


with open('notas.txt', 'r',  encoding="utf-8") as file:
    alunos = json.load(file)
soma = [0,0,0,0,0]
medias = []
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
    print(medias)
    

