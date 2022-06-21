import pandas as pd
#Lendo pasta_com_arquivo_excel_original Origem e trazendo para o Python p trabalhar em cima da pasta_com_arquivo_excel_original
planilha = pd.read_excel('atividades.xlsx')
#Criando lista com o nome das colunas
colunas = planilha.columns.values.tolist()
#print das colunas para verificar se leu o nome delas corretamente
print(colunas)
#Print dos valores da primeira'0' coluna para verificar.
print(planilha[colunas[0]].to_list())
coluna_x_da_planilha = planilha[colunas[0]].to_list()
print('-----------------------------------------------------------------------')
x =0
quant_col = 3
print(quant_col)
planilha_df = pd.DataFrame(zip(coluna_x_da_planilha, planilha[colunas[1]].to_list()),
                               columns=[colunas[0], colunas[1]])
y =f'planilha[colunas[{x}]].to_list())'
z = f'columns=[colunas[{x}]'
f = 'pd.DataFrame(zip('
while x < quant_col:
    y += f',planilha[colunas[{x+1}]].to_list())'
    z +=  f',colunas[{x+1}]'
    x += 1
concatenar_f_y_e_z = f+ y +','+z+'])'
planilha_df_teste = (concatenar_f_y_e_z)
print(y)
print(z)
print('---------------kkkkkkkkkkkkkkkkkkkkkkk------------------')
print(concatenar_f_y_e_z)
print('--------------jjjjjjjjjjjjjjjjjjjjjjjjj-----------------------')
print(planilha_df_teste)
print('--------hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh-----------')
print(planilha_df)