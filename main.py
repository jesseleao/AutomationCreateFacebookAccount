from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa o navegador usando o Chrome
navegador = webdriver.Chrome()

# Acessa a página de registro do Facebook
navegador.get("https://www.facebook.com/r.php")


# Espera o botão para aceitar os cookies e clica nele (caso esteja presente) usando o XPATH para identificar o campo
try:
    WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="facebook"]/body/div[3]/div[2]/div/div/div/div/div[3]/div[2]/div/div[1]/div[2]/div'))).click()
except:
    pass  # Ignora se o botão dos termos não aparecer

# Preenche os campos com informações atualizadas usando o nome do campo
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, "firstname"))).send_keys("Agenor")

navegador.find_element(By.NAME, "lastname").send_keys("Yes, it's him")
navegador.find_element(By.NAME, "reg_email__").send_keys("bruh@gmail.com")
navegador.find_element(By.NAME, "reg_passwd__").send_keys("P(_)dding123")

# Seleciona data de nascimento usando o nome do campo
navegador.find_element(By.NAME, "birthday_day").send_keys("17")
navegador.find_element(By.NAME, "birthday_month").send_keys("Nov")
navegador.find_element(By.NAME, "birthday_year").send_keys("2000")

# Seleciona o gênero
navegador.find_element(By.XPATH, '//*[@name="sex" and @value="2"]').click()  # 1 para feminino, 2 para masculino

# Clica no botão de cadastro
# WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.NAME, "websubmit"))).click()

input('')  # Para pausar o script antes de fechar o navegador e ver os dados preenchidos
