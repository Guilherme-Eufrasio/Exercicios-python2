import ast
materias =["portugues","matematica","historia","geografia","ingles"]

with open("notas.txt","r", encoding="utf-8") as arquivo:
    conteudo=arquivo.read()

boletim_lido= ast.literal_eval(conteudo)
c = 0
#print(boletim_lido)
pagina = open("notas2.html","w", encoding="utf-8")
pagina.write('''
<!DOCTYPE html>
<html>
    <link rel="stylesheet" href="./css/custom.css">
    <head lang="pt-br">
        <meta charset="UTF-8"/>
        <meta name="viewport"
        content="witdh=device-width,initial-scale=1.0"/>
        <title>Boletim</title>
        <h1> JIM </h1>
    <table border ="1">
    
''')
#print(f"BOLETIM {boletim_lido}")
for aluno, desempenho in (boletim_lido.items()):
    pagina.write (f"""
        <th>{aluno}</th>
        <tr>
            <th>Matéria</th>
            <th>1° B</th>
            <th>2° B</th>
            <th>3° B</th>
            <th>4° B</th>
            <th>Média</th>
        </tr>
    """),

    #pagina.write(f"""{desempenho}""")
    
    for pos, notas in enumerate(desempenho):
        if pos == 5:
             break
        else:
            materia = materias[pos]
            pagina.write(f"""
                    <tr>
                        <td>{materia}</td>
            """)        
            for nota in notas:
                pagina.write(f"""<td>{nota}</td>""")
            pagina.write(f"""
                    </tr>
            """)    
