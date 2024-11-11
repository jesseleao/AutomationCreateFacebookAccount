# Automação de Criação de Conta no Facebook com Selenium  

Este é um script automatizado em Python que utiliza o Selenium WebDriver para criar uma conta no Facebook. Este projeto foi desenvolvido para fins de aprendizado e teste de automação web com Selenium.

### Explicação das Seções

- **Pré-requisitos:** Especifica o que o usuário precisa antes de rodar o código.
- **Configuração:** Instruções para clonar e preparar o ambiente.
- **Execução do Script:** Passo simples para rodar o código.
- **Tecnologias Utilizadas:** Python, Selenium WebDriver, ChromeDriver
- **Licença:** Projeto livre
- **Observações:** Aviso sobre o uso do script em relação aos Termos de Serviço.

## 📋 Pré-requisitos

- **Python 3.x**: Certifique-se de que o Python esteja instalado. [Instalar Python](https://www.python.org/downloads/)
- **Selenium**: Instale o Selenium usando o comando:
  ```bash
  pip install selenium
- Chromedriver: Baixe o ChromeDriver compatível com a versão do seu navegador Chrome.

## ⚙️ Configuração
- **Clonar o Repositório**
  ```bash
  git clone https://github.com/jesseleao/AutomationCreateFacebookAccount.git
  
  cd AutomationCreateFacebookAccount
- **Certifique-se de editar o código caso:**
- O script esteja configurado com os XPaths e as informações incorretas para criar a conta.

## 🚀 Execute o script com o comando:

  ```bash
  python Main.py
  ```
- O script abrirá o navegador Chrome e seguirá os passos para preencher o formulário de criação de conta no Facebook.

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Selenium WebDriver**
- **ChromeDriver**

## 📄 Licença

- Este projeto é livre para uso e modificação para fins educacionais e de teste.

## 📝 Observações

- Este script é feito apenas para fins de teste e aprendizado. Automação de criação de contas pode violar os Termos de Serviço de algumas plataformas, como o Facebook.
- O Facebook atualiza frequentemente o layout da página e os identificadores dos elementos, então os XPaths podem precisar de ajustes no futuro.
- O comando responsavel pelo "click" no botão "Cadastre-se" esta comentado pois o intuito não é dar continuidade na criação da conta, apenas servir como exemplo.