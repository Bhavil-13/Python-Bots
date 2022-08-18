import pyautogui, time
import webbrowser as wb


wb.open('https://web.whatsapp.com/')

# Go to SpamMsg.txt and write your spam message and copy paste it the number of times you want to spam it.

f = open("SpamMsg.txt", 'r')   

# This time thing is the wait period(in seconds) before the bot stats executing the for loop, so that you get the time to 
# Select the person/grout you want to spam. You can change the time fromm 10 to whatever your requirenments are.
time.sleep(10)
for i in f:
    pyautogui.typewrite(i)
    pyautogui.press('enter')