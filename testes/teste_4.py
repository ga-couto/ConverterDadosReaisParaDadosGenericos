import pandas as pd

planilha = pd.read_excel('atividades.xlsx')
colunas = planilha.columns.values.tolist()
print(colunas)#print
print(planilha[colunas[0]].to_list())
print('---------------------------------------')
planilha_df = pd.DataFrame(zip(planilha[colunas[0]].to_list(),
                                   planilha[colunas[1]].to_list()),
                               columns=[colunas[0],colunas[1]])

coluna_0 = planilha[colunas[0]].to_list()
print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
print(coluna_0)
print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
for valor in coluna_0:
    i = 0
    for index, value in enumerate(coluna_0):
        nome_generico = value.replace(valor, f'Colaborador {i}')
        if value == valor:
            coluna_0[index] = nome_generico
    i += 1
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(coluna_0)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

planilha_df.to_excel('atividades_pronto.xlsx')
print(planilha_df)


# if _name_ == '_main_':
#     nomes = ['Gabriel','Thomas','Laiana','Gabriel','Laiana', 'Gabriel','Gabriel','Gabriel']
#     for nome in nomes:
#         for index, value in enumerate(nomes):
#             nome_generico = value.replace(nome, f'Colaborador {i}')
#             if value == nome:
#                 nomes[index] = nome_generico
#         i += 1
#     print(nomes)