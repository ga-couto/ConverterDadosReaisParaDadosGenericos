import pandas as pd
import glob
print('Hoje, o código atende somente arquivos excel até que seja melhorado')
nome_arquivo_excel_original = 'atividades'#input('Digite o nome do arquivo original: ')
#salvando nome das pastas em variáveis
caminho_do_arquivo_excel_original = 'pasta_com_arquivo_excel_original'
planilhas_com_coluna_unica = 'planilhas_com_coluna_unica'
#Lendo pasta_com_arquivo_excel_original Origem e trazendo para o Python p trabalhar em cima dela
planilha = pd.read_excel(f'{caminho_do_arquivo_excel_original}\\{nome_arquivo_excel_original}.xlsx')
#planilhaa = pd.read_excel(nome_arquivo_excel_original+'.xlsx')
#Criando lista com o dado das colunas
colunas = planilha.columns.values.tolist()
#print das colunas para verificar se leu o dado delas corretamente 'Nomes das colunas'
print(colunas)
print('-----------------------------------------------------------------------------')
j = int(0)
indice_col = 0
while indice_col < len(colunas):
    #Print dos valores da primeira'0' coluna para verificar.
    print(planilha[colunas[indice_col]].to_list())
    #transformando dados reais em valores genéricos
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
    #Transformando pasta_com_arquivo_excel_original num DataFrame utilizando a biblioteca PANDAS 'pd'
    planilha_coluna_unica = pd.DataFrame(zip(coluna_x_da_planilha),columns=[colunas[indice_col]])
    planilha_coluna_unica.to_excel(f'{planilhas_com_coluna_unica}\\{nome_arquivo_excel_original}_coluna_{indice_col+1}.xlsx')
    print(planilha_coluna_unica)
    j = 0
    indice_col += 1
indice_col = 0
num_planilha_coluna_unica = 0
#Pegar vários arquivos de acordo com o critério abaixo. Lembrando q posso acessar uma pasta, se necessário. Utilizando 'glob' abaixo...
planilhas_coluna_unica_x = glob.glob(f'{planilhas_com_coluna_unica}\\{nome_arquivo_excel_original}_coluna_*.xlsx')
print(planilhas_coluna_unica_x)
planilha_resultado = pd.DataFrame()
#Aqui abaixo dentro do 'for', irá ler cada plhanilha e concatenar na 'planilha_resultado' seguindo o eixo das colunas 'axis = 1'.
for i in planilhas_coluna_unica_x:
    tabela = pd.read_excel(i)
    planilha_resultado = pd.concat([planilha_resultado,tabela], axis = 1, ignore_index=True)
planilha_resultado.to_excel(f'planilha_resultado.xlsx')

print("""        ------------------------------
        |             FIM            |
        ------------------------------""")

