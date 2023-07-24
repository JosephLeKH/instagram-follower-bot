"""""
Purpose: Log in to an Instagram account and follow all of the people on an account's following list
Tools: Selenium (scrolling)
"""""
from instabot import InstaFollower

bot = InstaFollower()
bot.login()
bot.follow()
