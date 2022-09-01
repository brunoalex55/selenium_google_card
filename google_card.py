import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json


def Salva_Dados_Completo(cnpj,razao_social,cidade,estado,site,endereco,telefone,rota,ramo_atividade,nota_google):
    dictionary ={ 
        "cnpj" : cnpj, 
        "razao_social" : razao_social, 
        "cidade" : cidade, 
        "estado" : estado,
        "site" : site,
        "endereco" : endereco,
        "telefone" : telefone,
        "rota_maps" : rota,
        "ramo_atividade": ramo_atividade,
        "nota_google" : nota_google
    } 
    json_object = json.dumps(dictionary, indent = 4) 
    with open('google_processado_card/'+cnpj+".json", "a") as outfile: 
        outfile.write(json_object)
        outfile.write('\n')
        outfile.write('\n')


browser = webdriver.Chrome(ChromeDriverManager().install())
with open("empresas.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)
for i in dados:
    cnpj = i['CNPJ']
    open('google_processado_card/'+cnpj+'.json', 'a+')
    razao_social = i['Razao_social']
    cidade = i['Cidade']
    estado = i['Estado']
    nome_empresa = i['Razao_social']
    browser.get('http://www.google.com')
    search = browser.find_element(By.NAME,'q')
    search.send_keys(nome_empresa)
    search.send_keys(Keys.RETURN) # hit return after you enter search text
    time.sleep(4)
    try:
        site = browser.execute_script("return document.getElementsByClassName('ab_button')[0].getAttribute('href')")
        endereco = browser.execute_script("return document.getElementsByClassName('LrzXr')[0].innerText")
        telefone = browser.execute_script("return document.getElementsByClassName('LrzXr')[1].innerText")
        rota_maps = browser.execute_script("return document.getElementsByClassName('ab_button')[1].getAttribute('data-url')")
        ramo_atividade = browser.execute_script("return document.getElementsByClassName('YhemCb')[0].innerText")
        nota_google = browser.execute_script("return document.getElementsByClassName('Aq14fc')[0].innerText")
        rota = 'https://google.com'+rota_maps
        print('Ramo atividade '+ramo_atividade)
        print('Nota google '+nota_google)
        print('Endereço do site : '+site)
        print('Endereço da empresa: '+endereco)
        print('Telefone da empresa: '+telefone)
        print('Rota  do google maps: '+rota)  
    except Exception as e:
        pass

    Salva_Dados_Completo(cnpj,razao_social,cidade,estado,site,endereco,telefone,rota,ramo_atividade,nota_google)
    time.sleep(5) # sleep for 5 seconds so you can see the results
