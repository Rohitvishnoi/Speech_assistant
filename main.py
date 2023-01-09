import speech_recognition as sr
import datetime
import time
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
import pyautogui

r = sr.Recognizer()

def record_audio(ask = False, shop = False):
    # playsound.playsound('sound.wav')
    with sr.Microphone() as source:
        if ask:
            ultron_speak(ask)
        audio = r.listen(source, phrase_time_limit=5)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            if shop:
                ultron_speak('Sorry, I can not understand the product, please try again.')
            else:
                ultron_speak('Sorry, I did not get that')
        except sr.RequestError:
            ultron_speak('Sorry, my speech service is down')
        return voice_data
def shopping(platform):
    if platform == 'amazon':
        url = 'https://www.amazon.in/s?k='
    elif platform == 'flipkart' or platform == 'flipcart' or platform == 'flip cart' or platform == 'flip kart':
        url = 'https://www.flipkart.com/search?q='
    elif platform == 'myntra' or platform == 'mintra' or platform == 'min tara' or platform == 'myn tara':
        url = 'https://www.myntra.com/'
    else:
        ultron_speak('Sorry, no such website found')
        return
    product = record_audio('Which product you want to buy from '+platform+'?',True)
    product = product.lower()
    if product != '':
        url = url+product
        webbrowser.get().open(url)
        ultron_speak('Here are all the products I found for '+product+' on '+platform+'.')
        pyautogui.hotkey('alt','tab')
    else:
        return

def ultron_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,1000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'name' in voice_data:
        ultron_speak('My name is Ultron')
    if 'date' in voice_data:
        today = datetime.date.today()
        ultron_speak(today.strftime("%B %d, %Y"))
    if 'time' in voice_data:
        ultron_speak(time.strftime("%I:%M"))
    if 'search' in voice_data:
        search = record_audio('What do you want to search?')
        url = 'https://google.com/search?q='+ search
        webbrowser.get().open(url)
        ultron_speak('Here is what I found for '+ search)
        pyautogui.hotkey('alt','tab')
    if 'find location' in voice_data:
        location = record_audio('What is the location you want to search for?')
        url = 'https://google.nl/maps/place/'+ location + '/&amp;'
        webbrowser.get().open(url)
        ultron_speak('Here is the location of '+ location)
        pyautogui.hotkey('alt','tab')
    if 'play video' in voice_data:
        search_video = record_audio('Which video you want to search for, on YouTube?')
        url = 'https://www.youtube.com/results?search_query=' + search_video
        webbrowser.get().open(url)
        ultron_speak('Here is the video for '+ search_video)
        pyautogui.hotkey('alt','tab')
    if 'information' in voice_data:
        wiki_article = record_audio('Which wikipedia article you want to see?')
        url = 'https://en.wikipedia.org/wiki/'+wiki_article
        webbrowser.get().open(url)
        ultron_speak('Here is the wikipedia article for '+wiki_article)
        pyautogui.hotkey('alt','tab')
    if 'open' in voice_data:
        application = record_audio('Which application you want to open?')
        application = application.lower()
        if application == 'word' or application == 'world' or application == 'ms word' or application == 'bird':
            application = 'winword'
        elif application == 'terminal' or application == 'command prompt':
            application = 'cmd'
        os.system('start '+application)
        ultron_speak('Opening '+ application)
        pyautogui.hotkey('alt','tab')
    if 'website' in voice_data:
        url = ''
        website = record_audio('Which website you want to open?')
        website = website.lower()
        if website == 'facebook' or website == 'face book':
            url = 'https://www.facebook.com/'
        elif website == 'youtube':
            url = 'https://www.youtube.com/'
        elif website == 'google':
            url = 'https://google.com/'
        elif website == 'gateoverflow' or website == 'gate overflow':
            url = 'https://gateoverflow.in/'
        elif website == 'amazon':
            url = 'https://www.amazon.in/'
        elif website == 'gmail' or website == 'g mail':
            url = 'https://mail.google.com/mail/u/0/'
        elif website == 'twitter':
            url = 'https://twitter.com/home'
        elif website == 'unacademy' or website == 'un academy':
            url = 'https://unacademy.com'
        if url != '':
            webbrowser.get().open(url)
            ultron_speak('Opening the website of '+website)
            pyautogui.hotkey('alt','tab')
        else:
            ultron_speak('Sorry no website found! Try again.')
            return
    if 'shopping' in voice_data or 'shop' in voice_data or 'buy' in voice_data or 'purchase' in voice_data:
        platform = ''
        platform = record_audio('From which E commerce website you want to shop?')
        platform = platform.lower()
        if platform !='':
            shopping(platform)
        else:
            ultron_speak('Sorry No such website found')
    if 'exit' in voice_data or 'bye' in voice_data or 'good bye' in voice_data or 'go to hell' in voice_data:
        ultron_speak('Closing the application. Good Bye!')
        exit()

time.sleep(1)
ultron_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
