# Import principal de bibliotecas usadas
# Comandos relevantes pyaotugui.press -- pyautogui.click -- pyautogui.write -- pyautogui.hotkey -- pyautogui.screenshot
import pyautogui
import pandas
import time

#Começo do código abrindo o navegador
pyautogui.press("win")
pyautogui.sleep(1)
pyautogui.write("Edge")
pyautogui.press("enter")
pyautogui.sleep(2)

# Acesso a URL desejada (LEMBRE DE JOGAR O LINK DA PAGINA DE LOGIN)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
pyautogui.sleep(4)


#Dados de login
pyautogui.press("tab")
pyautogui.write("iuri")
pyautogui.sleep(1)
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")
pyautogui.sleep(2)


# Começo do acesso a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)
pyautogui.sleep(2)

# Cadastro de produtos com FOR pra repetição e atribuição da variável LINHA com o valor de tabela.index
for linha in tabela.index:

    pyautogui.click(x=-1038, y=280)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    time.sleep(1)

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    time.sleep(1)

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    time.sleep(1)

    cate = str(tabela.loc[linha, "categoria"])
    pyautogui.write(cate)
    pyautogui.press("tab")
    time.sleep(1)

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    time.sleep(1)

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    time.sleep(1)

    obs = str(tabela.loc[linha, "obs"])

    # Verifica se a observação não é "nan" antes de escrever
    # Se a célula estiver vazia, não escreve nada
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    time.sleep(1)

    # Concluir o cadastro
    pyautogui.press("enter")
    time.sleep(1)

    # Resetar o cadastro
    pyautogui.scroll(1000)