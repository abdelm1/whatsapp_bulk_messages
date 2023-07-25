from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import keyboard as key
import time
import pandas
from tkinter import filedialog as fd
from __main__ import *

global logs

p=r'dev.xlsx'
path=r''


def loaddata():
    global p,data
    filetypes = (
        ('Excel files', '*.xlsx'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir = '/WtspAutomation/',
        filetypes=filetypes)

    p=filename
    data = pandas.read_excel(p)
    print(data)
    print(p)


def loadimage():
    global pathimg
    filetypes = [('All files', '*.*')]

    filename = fd.askopenfilename(
        title='Upload your image!',
        initialdir = '/WtspAutomation/',
        filetypes=filetypes)

    pathimg=filename
    print(pathimg)
def msgbox():
    global msg
    msg=tk.Toplevel(app)
    msg.title("AutoWZ | Write your message!")
    msg.iconbitmap(r"logo.ico")
    msg.geometry('430x360')
    msg.resizable(False, False)
    labeltxt=tk.Label(master=msg,text='Remarque : Ici, où vous pouvez personnaliser\nvotre message à envoyer, vous pouvez utiliser\n{nom} pour insérer le nom de chaque personne,\naussi {note} pour les notes.')
    labeltxt.config(font =("Courier", 11))
    labeltxt.pack()
    global text_box
    text_box = tk.Text(
    msg,
    height=12,
    width=50
    )
    text_box.pack()
    text_box.config()

    
def send_msg(msg=str):
    driver = webdriver.Chrome("C:\chromedriver.exe")
    i=0
    data = pandas.read_excel(p)
    for name in data['Names']:
        while True:
            try:
                WebDriverWait(driver, 5).until (EC.alert_is_present())
                alert = driver.switch_to.alert
                alert.accept()
                break
            except TimeoutException:
                break
        driver.get(f"https://web.whatsapp.com/send?phone=+212{str(data['Numbers'][i])}&text={msg.format(note=data['Notes'][i],nom=str(data['Names'][i]))}&app_absent=1")
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))
        WebDriverWait(driver, 2)
        driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        print(f"[{data['Numbers'][i]}]The message has been sent successfully to {name}")
        i+=1
        time.sleep(2)

#send_msg(numbers, 'test_2.47')

item1 = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div'
item2 = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button'
send = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span'


def send_img(msg=str):
    path=pathimg
    data = pandas.read_excel(p)
    driver = webdriver.Chrome("C:\chromedriver.exe")
    i=0

    #change / to \
    new_path = pathimg.replace("/", "\\")
    
    for number in data['Numbers']:
        #check for alert and accept it 
        while True:
            try:
                WebDriverWait(driver, 5).until (EC.alert_is_present())
                alert = driver.switch_to.alert
                alert.accept()
                break
            except TimeoutException:
                break
        #open web
        driver.get(f"https://web.whatsapp.com/send?phone=+212{str(data['Numbers'][i])}&text={msg.format(note=data['Notes'][i],nom=str(data['Names'][i]))}&app_absent=1")
        WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, item1)))
        driver.find_element(By.XPATH, item1).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, item2)))
        driver.find_element(By.XPATH, item2).click()
        #past path
        time.sleep(3)
        key.write(new_path)
        time.sleep(1)
        key.press('enter')
        #send
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, send)))
        driver.find_element(By.XPATH, send).click()
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'r83rrh3w')))
        # WebDriverWait(driver, 100).until(EC.invisibility_of_element_located(By.CSS_SELECTOR, '#main > div._2gzeB > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs > div:nth-child(13) > div > div > div.ItfyB._3nbHh > div._27K43 > div._2_-To > div > div > span'))
        print(f"[@{number}]The Image has been sent successfully {data['Names'][i]}")
        i+=1
        

# Documents send function:
item3='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button'

def send_doc(msg=str , path=str):
    data = pandas.read_excel(p)
    driver = webdriver.Chrome("C:\chromedriver.exe")
    i=0
    for number in data['Numbers']:
        #check for alert and accept it 
        while True:
            try:
                WebDriverWait(driver, 5).until (EC.alert_is_present())
                alert = driver.switch_to.alert
                alert.accept()
                break
            except TimeoutException:
                break
        #open web
        driver.get(f"https://web.whatsapp.com/send?phone=+212{str(data['Numbers'][i])}&text={msg.format(note=data['Notes'][i],nom=str(data['Names'][i]))}&app_absent=1")
        WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, item1)))
        driver.find_element(By.XPATH, item1).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, item3)))
        driver.find_element(By.XPATH, item3).click()
        #past path
        time.sleep(5)
        key.write(path)
        time.sleep(1)
        key.press('enter')
        #send
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, send)))
        driver.find_element(By.XPATH, send).click()
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'r83rrh3w')))
        time.sleep(2)
        print(f"[@{number}]The File has been sent successfully {data['Names'][i]}")
        i+=1


def aboutus():
    driver = webdriver.Chrome("C:\chromedriver.exe")
    driver.get('https://linktr.ee/abdu.exe')
    time.sleep(100)

