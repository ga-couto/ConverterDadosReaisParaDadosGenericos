import pandas as pd
#Lendo pasta_com_arquivo_excel_original Origem e trazendo para o Python p trabalhar em cima da pasta_com_arquivo_excel_original
planilha = pd.read_excel('atividades.xlsx')
#Criando lista com o dado das colunas
colunas = planilha.columns.values.tolist()
#print das colunas para verificar se leu o dado delas corretamente 'Nomes das colunas'
print(colunas)
print('-----------------------------------------------------------------------------')
j = 0
indice_col = 0
while indice_col < len(colunas):
    #Print dos valores da primeira'0' coluna para verificar.
    print(planilha[colunas[indice_col]].to_list())
    #transformando dados reais em valores genéricos
    coluna_x_da_planilha = planilha[colunas[indice_col]].to_list()
    for dado in coluna_x_da_planilha:
        for indice, valor in enumerate(coluna_x_da_planilha):
            dado_generico = valor.replace(dado, f'{colunas[indice_col]} {j}')
            if valor == dado:
                coluna_x_da_planilha[indice] = dado_generico
        j += 1
    print(coluna_x_da_planilha)
    #Transformando pasta_com_arquivo_excel_original num DataFrame utilizando a biblioteca PANDAS 'pd'
    planilha_df = pd.DataFrame(zip(coluna_x_da_planilha),columns=[colunas[indice_col]])
    planilha_df.to_excel(f'atividades_coluna_{indice_col}.xlsx')
    print(planilha_df)
    indice_col += 1

