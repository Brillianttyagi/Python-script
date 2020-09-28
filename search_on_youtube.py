import webbrowser
search = input("enter:  ")
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
search = 'www.youtube.com/'+search+"/"
webbrowser.get(chrome_path).open(search)