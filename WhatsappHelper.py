from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WhatsappHelper():

    def __init__(self, driver: webdriver):
        self.driver = driver

    def checkLogin(self):
        try:
            # find the Search bar
            self.driver.find_element(By.CLASS_NAME, "uwk68")
            return True
        except NoSuchElementException:
            return False

    def getAllChats(self):
        return self.driver.find_elements(By.CLASS_NAME, '_3m_Xw')

    def getChatNames(self):
        chatNames = []
        chats = self.getAllChats()
        for chat in chats:
            name = chat.find_element(
                By.CLASS_NAME, 'le5p0ye3').get_attribute('innerHTML')
            chatNames.append(name)

        return chatNames

    def isChatOpen(self):
        try:
            # find the Messaging Box
            self.driver.find_element(By.CLASS_NAME, "_2cYbV")
            return True

        except NoSuchElementException:
            return False

    def newChat(self, name: str):
        newMsg = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div")
        newMsg.click()

        searchBox = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]")
        searchBox.click()
        searchBox.clear()
        searchBox.send_keys(name)

        sleep(1)

        first = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div/div/div/div[2]")
        first.click()

        return True

    def sendMessage(self, name: str, message: str):

        self.newChat(name)

        if not self.isChatOpen():
            print(f'{name} is not Open to send message')
            return False

        textBox = self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

        textBox.clear()
        textBox.send_keys(message)

        sendBtn = self.driver.find_element(By.CLASS_NAME, '_4sWnG')
        sendBtn.click()

        return True
