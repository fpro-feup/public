from pandas_ods_reader import read_ods
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# https://moodle.up.pt/grade/report/grader/index.php?id=2126

df = read_ods('FEUP-EIC0005-20192020-1S Pauta.ods', 1)
df = df[['Nome', 'Endereço de e-mail', 'Total da unidade curricular (Real)']]
df.columns = ['name', 'email', 'grades']

df['up'] = [email.split('@')[0] for email in df['email']]
df['up'] = [email.split('@')[0][2:] for email in df['email']]

# plots
# replace '-' by nan
df['grades'] = df['grades'].replace('-', np.nan)

plt.hist(df['grades'])
plt.show()

print(np.max(df['grades']))
print(df['grades'].max())

# LE=0.1
# RE=0.1
# PE=0.5
# TE=0.3

df['grades'] = df['grades'] / 0.7

plt.hist(df['grades'])
plt.show()

df['grades'].hist()
plt.show()

plt.boxplot(df['grades'])
plt.show()

plt.boxplot(df['grades'][~np.isnan(df['grades''])])
plt.show()

#################################################################

# https://sigarra.up.pt/feup/pt/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=436425

import requests
from getpass import getpass

session = requests.session()
html = session.get('https://sigarra.up.pt/feup/pt/it_listagem.lista_turma_disciplina?pv_curso_id=742&pv_ocorrencia_id=436425&pv_ano_lectivo=2019&pv_periodo_id=1&pv_no_menu=1').text
html.find('1MIEIC01')

# ooops?

session = requests.session()
session.post('https://sigarra.up.pt/feup/pt/vld_validacao.validacao', {'p_user': input('username:'), 'p_pass': getpass('password:')})
html = session.get('https://sigarra.up.pt/feup/pt/it_listagem.lista_turma_disciplina?pv_curso_id=742&pv_ocorrencia_id=436425&pv_ano_lectivo=2019&pv_periodo_id=1&pv_no_menu=1').text
html.find('Turma: 1MIEIC01')

turmas = {}
for turma in range(1, 9):
    i = html.find('Turma: 1MIEIC0%d' % turma)
    j = html.find('Turma: 1MIEIC0%d' % (turma+1))
    texto_turma = html[i:j]
    for k, ch in enumerate(texto_turma):
        if ch == '@':
            up = texto_turma[texto_turma[:k].rfind('<td class="k t">')+len('<td class="k t">'):k+texto_turma[k:].find('</td>')]
            #print(up)
            turmas[turma] = turmas.get(turma, []) + [up]
    #print(texto_turma[:100])

df['turma'] = [[k for k, v in turmas.items() if email in v] for email in df['email']]

df['turma'] = [t[0] if t else np.nan for t in df['turma']]

df.groupby('turma')['grades'].median()
df.groupby('turma')['grades'].median().plot(kind='bar')
plt.show()

#################################################################

df2 = pd.wide_to_long(df, 'pe', 'email', 'teste')

df.boxplot(column='grades', by='turma')
plt.show()

#grouped = data['2013-08-17'].groupby(axis=1, level='SPECIES').T
#grouped.boxplot()

################################################################

df = read_ods('FEUP-EIC0005-20192020-1S Pauta.ods', 1)



[[f(nome) for f in l if f(nome) != 0] for nome in df['Nome']]

def e_mulher(nome):
    nome = nome.split()[0]
    return nome[-1] == 'a' or nome in ('Isabel', 'Alice', 'Raquel', 'Inês', 'Adelaide')


df['gender'] = ['F' if e_mulher(nome) else 'M' for nome in df['name']]

df['nota'] = df['nota'].replace('-', np.nan)

df.boxplot('grades', 'gender')


################################################################

df['ano'] = [email[2:6] for email in df['Endereço de e-mail']]
df['ano'].unique()


np.logical_or(df['ano'] == '0828', df['ano'] == '1011')

df = df[np.logical_and(df['ano'] != '0828', df['ano'] != '1011')]

df = df.sort_values('ano')

df['ano'].value_counts()

df['ano'].value_counts().plot(kind='bar')
plt.show()

df.boxplot('nota', 'ano')
plt.show()



