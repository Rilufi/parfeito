from selenium import webdriver
from time import sleep
from secrets import username, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from secrets import username, password


class ParfeitoBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-extensions")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        self.driver = webdriver.Chrome(options=options)


    def login(self, username, password):
        self.driver.get('https://www.parperfeito.com.br/')

        sleep(2)

        cookie = self.driver.find_element("xpath",'//*[@id="onetrust-accept-btn-handler"]')
        cookie.click()

        sleep(2)

        fb_btn = self.driver.find_element("xpath",'//*[@id="__next"]/div/div/div/button/span')
        fb_btn.click()

        email_in = self.driver.find_element("xpath",'//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element("xpath",'//*[@id="password"]')
        pw_in.send_keys(password)

        sleep(5)

        login_btn = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'span.css-1e2yn3q'))
)
        login_btn.click()

        sleep(15)



    def like(self):
        like_btn = self.driver.find_element("xpath",'//*[@id="mainContent"]/div[2]/section/div[1]/div/div[4]/span/button/span/div[2]')
        like_btn.click()
    def like2(self):
        like_btn2 = self.driver.find_element("xpath",'//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/span/button')
        like_btn2.click()

    def dislike(self):
        dislike_btn = self.driver.find_element("xpath",'//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/div[2]/button/span/span[2]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(1)
            try:
                self.like()
            except NoSuchElementException:
                try:
                    self.like2()
                except NoSuchElementException:
                    try:
                        self.close_popup()
                    except NoSuchElementException:
                        self.close_match()

    def close_popup(self):
        try:
            # Encontrar o elemento inicial para garantir que a página tem o foco
            initial_element = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]')

            # Pressionar Tab duas vezes para focar no botão 'Pular'
            ActionChains(self.driver).move_to_element(initial_element).send_keys(Keys.TAB).send_keys(Keys.TAB).perform()

            # Pressionar Enter para clicar no botão 'Pular'
            ActionChains(self.driver).send_keys(Keys.ENTER).perform()

        except NoSuchElementException:
            print("Elemento 'Pular' não encontrado.")

    def close_match(self):
        try:
            # Aguarda até 10 segundos para a presença do botão "Pular"
            skip_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    '//span[@class="css-1e2yn3q"]'
                    '//span[@class="css-ls1su9"]/svg[@color="light"]'
                    '/ancestor::span[text()="Pular"]'
                ))
            )
            skip_btn.click()
        except NoSuchElementException:
            pass
            print('kd o pulo')

bot = ParfeitoBot()
bot.login(username, password)

try:
    bot.auto_swipe()
except:
    ask = input("Deseja continuar? ")
    if ask != 'n':
        bot.auto_swipe()
    else:
        pass
