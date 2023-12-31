from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import username, password

class ParPerfeitoBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.parperfeito.com.br/')

        sleep(2)

        # Aceitar cookies
        cookie_btn = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        cookie_btn.click()

        sleep(2)

        # Clicar no botão de login com Facebook
        fb_btn = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/button/span')
        fb_btn.click()

        email_in = self.driver.find_element(By.ID, 'email')
        email_in.send_keys(username)

        pw_in = self.driver.find_element(By.ID, 'password')
        pw_in.send_keys(password)

        # Clicar no botão de login
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/form/div/div[1]/div[5]/button/span')
        login_btn.click()

        sleep(15)

    def like(self):
        # Clicar no botão de curtir
        like_btn = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[4]/span/button/span/div[2]')
        like_btn.click()

    def like2(self):
        # Clicar no segundo botão de curtir
        like_btn2 = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/span/button')
        like_btn2.click()

    def dislike(self):
        # Clicar no botão de descurtir
        dislike_btn = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/div[2]/button/span/span[2]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(1)
            try:
                self.like()
            except Exception:
                try:
                    self.like2()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        self.close_match()

    def close_popup(self):
        # Clicar no botão para fechar o popup
        popup_3 = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/div/div[2]/div/button')
        popup_3.click()

    def close_match(self):
        # Clicar no botão para fechar a janela de match
        match_popup = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[4]/div/div[2]/div/button')
        match_popup.click()

bot = ParPerfeitoBot()
bot.login()

try:
    bot.auto_swipe()
except:
    print("Nope")
