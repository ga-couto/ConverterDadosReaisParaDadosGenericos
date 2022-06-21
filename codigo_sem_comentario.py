import pandas as pd
import glob
print('Hoje, o código atende somente arquivos excel até que seja melhorado')
nome_arquivo_excel_original = 'atividades'#input('Digite o nome do arquivo original: ')
caminho_do_arquivo_excel_original = 'pasta_com_arquivo_excel_original'
planilhas_com_coluna_unica = 'planilhas_com_coluna_unica'
planilha = pd.read_excel(f'{caminho_do_arquivo_excel_original}\\{nome_arquivo_excel_original}.xlsx')
colunas = planilha.columns.values.tolist()
print(colunas)
print('-----------------------------------------------------------------------------')
j = int(0)
indice_col = 0
while indice_col < len(colunas):
    print(planilha[colunas[indice_col]].to_list())
    coluna_x_da_planilha = planilha[colunas[indice_col]].to_list()
    for dado in coluna_x_da_planilha:
        for indice, valor in enumerate(coluna_x_da_planilha):
            if valor is type(int):
                 break
            dado_generico = valor.replace(dado, f'{colunas[indice_col]} {j+1}')
            if valor == dado:
                coluna_x_da_planilha[indice] = dado_generico
        j += 1
    print(coluna_x_da_planilha)
    planilha_coluna_unica = pd.DataFrame(zip(coluna_x_da_planilha),columns=[colunas[indice_col]])
    planilha_coluna_unica.to_excel(f'{planilhas_com_coluna_unica}\\{nome_arquivo_excel_original}_coluna_{indice_col+1}.xlsx')
    print(planilha_coluna_unica)
    j = 0
    indice_col += 1
indice_col = 0
num_planilha_coluna_unica = 0
planilhas_coluna_unica_x = glob.glob(f'{planilhas_com_coluna_unica}\\{nome_arquivo_excel_original}_coluna_*.xlsx')
print(planilhas_coluna_unica_x)
planilha_resultado = pd.DataFrame()
for i in planilhas_coluna_unica_x:
    tabela = pd.read_excel(i)
    planilha_resultado = pd.concat([planilha_resultado,tabela], axis = 1, ignore_index=True)
planilha_resultado.to_excel(f'planilha_resultado.xlsx')

print("""        ------------------------------
        |             FIM            |
        ------------------------------""")

