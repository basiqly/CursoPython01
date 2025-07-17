import pandas as pd

#criando um dataframe com pandas
data = {
        'Nome': ['Caio', 'Andressa', 'Emily', 'Davi', 'Jesreel', 'Eloara','Alice'],
        'Idade': [15, 20, 25, 30, 35, 40, 45],
        'Salario': [1000, 2000, 3000, 4000, 5000, 6000, 7000]
        }
df = pd.DataFrame(data)

#exibir o dataframe
print('Dataframe criado:')
print(df)

#Selecionar uma coluna especifica
print('\n Mostra a Coluna de nome')
print(df['Nome'])

#filtrar linhas
print('\n Pessoas com idade maior que 30: ')
print(df[df['Idade'] > 30])

#selecionar uma nova coluna
df['Imposto'] = df['Salario'] * 0.1
print('\n Dataframe agora com a coluna imposto')
print(df)

#Media dos salarios
media_salario = df['Salario'].mean()
print('\n Media de salario')
print(media_salario)

#Media do imposto 
media_imposto = df['Imposto'].mean()
print('\n Media do imposto')
print(media_imposto)

#salvando o dataframe em um arquivo csv
df.to_csv('salarios.csv', index=False)

#carregar arquivo externo de dados
df_externo = pd.read_csv('salarios.csv')
print('\n Tabela CSV externa')
print(df_externo)
