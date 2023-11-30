import gtts  
from playsound import playsound  
import pyttsx3  
import os

accents = {'Australia':'com.au','United Kingdom':'com.uk','United States':'us','Canada':'ca','India':'co.in','Ireland':'ie','South Africa':'co.za'}


onlyfiles = [f for f in os.listdir('/Users/coding/Documents/vs/FluentFriend/model/dataset/output')]

def runner_3():
    try:
        for o in onlyfiles:
            oo = o.replace("_out.txt","")
            f = open('/Users/coding/Documents/vs/FluentFriend/model/dataset/output/'+o,'r')
            txt = f.read()
            tsf = gtts.gTTS(txt, lang='en', tld=accents['United Kingdom'])

            tsf.save('/Users/coding/Documents/vs/FluentFriend/model/database/db_output/'+oo+'_out.mp3')
    except:
        pass

