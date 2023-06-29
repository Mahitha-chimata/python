#URL shortener
#install pip package
import pyshorteners as sh

#Take original URL as input
long_url=input("Enter the URL : ")

def shorter(long_url):
    x=sh.Shortener()
    short_url= x.tinyurl.short(long_url)
    print("Short URL : ",short_url)
    
#calling the fuction
shorter(long_url)