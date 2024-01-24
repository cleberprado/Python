#!/usr/bin/env python
# coding: utf-8

# ## criando sistemas de finanças

# In[19]:


get_ipython().system('pip install yfinance')


# In[20]:


import yfinance


# In[27]:


codigo = input("Digite o codigo desejado: ")
tempo = input("digite o tempo desejado: ")
email = input("para qual email sera enviado: ")
gestor = input(" Qual o nome do Gestor: ") 

dados = yfinance.Ticker(codigo).history(tempo)
fechamento = dados.Close
maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]
fechamento.plot()


# In[10]:


get_ipython().system('pip install pyautogui')


# In[24]:


import pyautogui
import pyperclip


# In[28]:


pyautogui.PAUSE = 4
#abrir uma nova aba no navegador
pyautogui.hotkey("ctrl", "t")
#digitar o site 
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

#escrever email
pyautogui.click(x=106, y=216)

#adicionar email
pyperclip.copy(email)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#adicionar o assunto
pyperclip.copy("Relatorio de "+codigo+" em "+ tempo)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
#adicionar o corpo do email
mensagem = f"""
Prezado {gestor}

 Seguem os dados coletados, para a ação {codigo}
 
 Cotação Max: {round(maxima,2)}
 Cotação Min: {round(minima,2)}
 Cotação atual: {round(atual,2)}
 
 Qualquer duvida estou a disposição.
 
 Cleber Prado


"""
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=209, y=667)


# In[17]:


# pegar cordenadas do mouse
#import time
#time.sleep(5)
#pyautogui.position()


# In[ ]:




