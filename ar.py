import time
import pygame
import os
import subprocess
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 

ENTER_TEXT = "[id='__next'] .grow.overflow-x-auto .relative.flex.h-full.w-full textarea";
BUTTON_ICON = "[id='__next'] .grow.overflow-x-auto .relative.flex.h-full.w-full button";
REPLY_TEXT = "[id='__next'] [class='py-1 relative break-anywhere']  span";
def speak(data):
    voice = 'en-CA-LiamNeural'
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

speak(f"hello there . i am ethan")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query
def getReplyFromPi(question):
    # driver = webdriver.Chrome()
    chrome_options = Options()

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://pi.ai/home")
    time.sleep(5)

    if driver.current_url == "https://pi.ai/onboarding":
        print('ghkkfgkhgfkh')
        driver.get("https://pi.ai/home")

    # driver.maximize_window()
    i = 2
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ENTER_TEXT).click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ENTER_TEXT).send_keys(question)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, BUTTON_ICON).click()
    time.sleep(2)
    ele = driver.find_elements(By.CSS_SELECTOR, REPLY_TEXT)
    return ele[i+1].text

if __name__ == "__main__":

     while True:
          query = takeCommand().lower()
          if(query=='exit'):
              break
          else:
               text1 = getReplyFromPi(query)
               speak(text1)