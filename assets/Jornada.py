# Passo a passo do programa de cadastro de produtos

# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o passo 4 até acaber a lista de produtos


# Bibliotecas = pacote de codigo
# pyautogui > pip install pyautogui > no terminal do VSCode

import pyautogui
import time

# pyautogui.click > Clica
# pyautogui.write > Escreve
# pyautogui.press > Pressiona uma tecla
# pyautogui.hotkey > Pressiona uma combinação de teclas
# pyautogui.sleep > Pausa o programa por alguns segundos
# pyautogui.alert > Mostra uma mensagem na tela
# pyautogui.confirm > Mostra uma mensagem com botões de confirmação
# pyautogui.prompt > Mostra uma mensagem com um campo de texto para o usuário digitar algo
# pyautogui.copy > Copia o texto selecionado

pyautogui.PAUSE = 0.5  # Pausa de 0.5 segundos entre cada ação do pyautogui
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# Passo 1: Entrar no sistema da empresa
pyautogui.press('win')
pyautogui.write('chrome') # Pode ser que o nome do navegador seja diferente, ou um programa diferente.
time.sleep(5)  # Pausa de 5 segundos para o site carregar

pyautogui.press('enter')
time.sleep(2) # Pausa de 2 segundos para o site carregar

pyautogui.write(link)
pyautogui.press('enter')
time.sleep(5)  # Pausa de 5 segundos para o site carregar


# Passo 2: Fazer login
pyautogui.click(x=730, y=370)  # Clica no campo de email, muda as coordenadas de acordo com a resolução do seu monitor
pyautogui.write('usuario@exemplo.com')
pyautogui.press('tab') # Vai para o próximo campo
pyautogui.write('SENHA')
pyautogui.press('tab')
pyautogui.press('enter') # Pressiona Enter para fazer login

time.sleep(4)  # Pausa de 4 segundos para o site carregar

# Passo 3: Abrir a base de dados (importar o arquivo)
#pandas > pip install pandas > no terminal do VSCode
import pandas as pd

tabela = pd.read_csv('produtos.csv') # O py precisa ter o arquivo Produtos.csv na mesma pasta que o código, ou colocar o caminho completo do arquivo

print(tabela) # Mostra a tabela no terminal

# Passo 5: Repetir o passo 4 até acaber a lista de produtos
for linha in tabela.index: # Para cada linha da tabela

   # Passo 4: Cadastrar um produto
    pyautogui.click(x=737, y=248) # Clica no campo de email, muda as coordenadas de acordo com a resolução do seu monitor
    
    codigo = str(tabela.loc[linha, 'codigo']) # Pega o código do produto em texto
    pyautogui.write(codigo) # Escreve o código do produto
    pyautogui.press('tab')

    marca = str(tabela.loc[linha, 'marca']) # Pega a marca do produto em texto
    pyautogui.write(marca) # Escreve a marca do produto
    pyautogui.press('tab')

    tipo = str(tabela.loc[linha, 'tipo']) # Pega o tipo do produto em texto
    pyautogui.write(tipo) # Escreve o tipo do produto
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria']) # Pega a categoria do produto em texto
    pyautogui.write(categoria) # Escreve a categoria do produto
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario']) # Pega o preço unitário do produto
    pyautogui.write(preco_unitario) # Escreve o preço unitário do produto
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo']) # Pega o preço de custo do produto
    pyautogui.write(custo) # Escreve o preço de custo do produto
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs']) # Pega as observações do produto
    if obs != 'nan':  # Verifica se há observações
        pyautogui.write(obs) # Escreve observações do produto
    pyautogui.press('tab') # Passa para o botão enviar

    pyautogui.press('enter') # Pressiona Enter para enviar o produto

    pyautogui.scroll(5000) # Rola a tela para cima, para o próximo produto ficar visível

#Pausar o programa é só levar o mouse para o canto superior esquerdo da tela, que o pyautogui vai parar de rodar.
