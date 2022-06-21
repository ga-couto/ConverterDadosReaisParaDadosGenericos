import pandas as pd

#Lendo pasta_com_arquivo_excel_original Origem e trazendo para o Python p trabalhar em cima da pasta_com_arquivo_excel_original
planilha = pd.read_excel('atividades.xlsx')
#Criando lista com o nome das colunas
colunas = planilha.columns.values.tolist()
#print das colunas para verificar se leu o nome delas corretamente
print(colunas)
#Print dos valores da primeira'0' coluna para verificar.
print(planilha[colunas[0]].to_list())
print('-----------------------------------------------------------------------------')
j = 0
t = 0
coluna_x_da_planilha = planilha[colunas[t]].to_list()
while t < len(colunas):
    for nome in coluna_x_da_planilha:
        for index, value in enumerate(coluna_x_da_planilha):
            nome_generico = value.replace(nome, f'Genérico {j}')
            if value == nome:
                coluna_x_da_planilha[index] = nome_generico
        j += 1
    t += 1
print(f'T: {t}')
print(coluna_x_da_planilha)
print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
#Transformando pasta_com_arquivo_excel_original num DataFrame utilizando a biblioteca PANDAS 'pd'
quant_col = len(colunas)
x =0
f = 'pd.DataFrame(zip('
y =f'planilha[colunas[{x}]].to_list())'
z = f'columns=[colunas[{x}]'
while x < quant_col:
    y += f',planilha[colunas[{x+1}]].to_list())'
    z +=  f',colunas[{x+1}]'
    x += 1
concatenar_f_y_z = f+ y +','+z+'])'
#Falta conseguir colocar o 'concatenar_f_y_z' p construir uma variável 'planilha_df' semelhante a essa abaixo
planilha_df = pd.DataFrame(zip(planilha[colunas[0]].to_list(), planilha[colunas[1]].to_list()),
                               columns=[colunas[0], colunas[1]])
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
planilha_df.to_excel('atividades_pronto.xlsx')
print(planilha_df)
print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
# e = 0
# nomes = pasta_com_arquivo_excel_original[colunas[0]].to_list()
# for nome in nomes:
#     for index, value in enumerate(nomes):
#         nome_generico = value.replace(nome, f'Colaborador {e}')
#         if value == nome:
#             nomes[index] = nome_generico
#     e += 1
# print(nomes)