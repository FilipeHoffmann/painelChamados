from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import sys
import time
import pyautogui

class acessar_painel:
    def __init__(self,credenciais:tuple):
        self.credeciais = credenciais

    def abrir_navegador(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-fullscreen")
        navegador = webdriver.Chrome(options=options)
        navegador.get(self.credeciais.get("url"))
        login = navegador.find_element(By.XPATH, '//*[@id="login.login"]')
        senha = navegador.find_element(By.XPATH, '//*[@id="login.senha"]')
        time.sleep(3)
        login.send_keys(self.credeciais.get("login"))
        time.sleep(3)
        senha.send_keys(self.credeciais.get("senha"))
        time.sleep(3)
        entrar = navegador.find_element(By.XPATH, '//*[@id="entrar"]')
        entrar.click()
        navegador.get(self.credeciais.get("url"))
        pyautogui.click("fechar_aviso.png")
        keyboard.wait("f11")
