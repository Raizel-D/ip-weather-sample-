#! python3
import geocoder
import webbrowser, sys, pyperclip
g=geocoder.ip('me')
address =' '.join(str(elem) for elem in g)
s=address.split()[0]
l=s[1:-1]
webbrowser.open("weather of "+ l )