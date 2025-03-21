a = {'A': [[1.0, 1.0, 10.0, 10.0, 10.0], [10.0, 1.0, 10.0, 10.0, 3.0], [5.0, 6.0, 5.0, 4.0, 4.0], [6.0, 5.0, 5.0, 6.0, 54.0]]}

# print(a)
# print(a['A'])
media = []
soma=[0,0,0,0,0]

for k,v in a.items():
    #print(k, v)
    for conteudo in v:
        m=0
        pos_soma=0
        for pos, nota in enumerate(conteudo):
            print(pos, nota)
            soma[pos] = (soma[pos] + nota)
            #print(nota)

        print()
for s in soma:
    media.append(s/4)

print(soma)
print(media)