import instaloader

insta = instaloader.Instaloader()

acc = 'account_name'     #acoount name

insta.download_profile(acc,profile_pic_only=True)

# "pip install pywhatkit"
import pywhatkit

pywhatkit.sendwhatmsg('+91','as','')   # number,msg,time