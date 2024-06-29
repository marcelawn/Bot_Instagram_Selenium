from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ExpectedCondition
from selenium.webdriver.common.keys import Keys

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR','--window-size=1300,1000','--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
        chrome_options.add_experimental_option('prefs',{
            'download.prompt_for_download':False,
            'profile.default_content_setting_values.notifications': 2,
            'profile.default_content_setting_values.automatic_downloads':1
        })
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
        wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
            ]
        )
        return driver, wait
    
driver , wait = iniciar_driver()

driver.get('https://www.instagram.com')
sleep(1)

campo_usuario = wait.until(ExpectedCondition.element_to_be_clickable((By.XPATH,'//input[@name="username"]')))
campo_usuario.send_keys('email')
sleep(1)
campo_senha = wait.until(ExpectedCondition.element_to_be_clickable((By.XPATH,'//input[@name="password"]')))
sleep(1)
campo_senha.send_keys('senha')
sleep(1)
botao_login = wait.until(ExpectedCondition.element_to_be_clickable((By.XPATH,'//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]')))
botao_login.click()
sleep(10)

driver.get('https://www.instagram.com/devaprender')


postagem = wait.until(ExpectedCondition.visibility_of_any_elements_located((By.XPATH,'//div[@class="_aagw"]')))
sleep(1)
postagem[0].click()
sleep(1)

try:
        verifica_curtida = driver.find_element(By.XPATH,
                                               '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]//div[@role="button"]//*[@aria-label="Curtir"]')
except:
    print('A imagem já havia sido curtida.')
else:
    botao_curtir = driver.find_elements(By.XPATH,
                                            '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]//div[@role="button"]')
    sleep(5)
    driver.execute_script('arguments[0].click()', botao_curtir[0])
    print('Deu certo! A imagem acabou de ser curtida.')
    sleep(86400)


input('')
driver.close()