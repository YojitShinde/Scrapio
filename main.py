import scraping_bot
import messaging_bot
import time

while(True):
    scraping_bot.scrape()
    messaging_bot.mail()
    time.sleep(15)
