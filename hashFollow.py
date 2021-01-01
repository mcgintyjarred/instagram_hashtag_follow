#https://towardsdatascience.com/increase-your-instagram-followers-with-a-simple-python-bot-fde048dce20d

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

# Get log in details
username_input = input("Please provide username: ")
password_input = input("Please provide the password for your account")

# Tags the user would like to use
hashtag_list = []
more_tags = "yes"
another = "yes"

while(more_tags == another):
    new_tag = input("New tag to search: ")
    hashtag_list.append(new_tag)

    another = input("Would you like to add another tag").lower()

# Go to instagram login page
webdriver = Chrome()
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

# Send keys for login
username = webdriver.find_element_by_name('username')
username.send_keys(username_input)
password = webdriver.find_element_by_name('password')
password.send_keys(password_input)

# Click login button
button_login = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
button_login.click()
sleep(3)

# Get rid of instagram pop up
#comment these last 2 lines out, if you don't get a pop up asking about notifications
notnow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
notnow.click() 



# can create file of people who have been followed

# prev_user_list = [] delete after first run
#prev_user_list = pd.read_csv('followed_list.csv', delimiter=',').iloc[:,1:2]  # useful to build a user log

#prev_user_list = pd.read_csv("followers_names.csv")
#prev_user_list = prev_user_list['followers']

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
    sleep(5)
    #first_thumbnail = webdriver.find_element_by_xpath(
    #    '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]')
    first_thumbnail.click()
    sleep(randint(1, 2))
    try:
        for x in range(1, 200):
            username = webdriver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text

            #if username not in prev_user_list:
            if x < 200:
                # If we already follow, do not unfollow
                if webdriver.find_element_by_xpath(
                        '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                    webdriver.find_element_by_xpath(
                        '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

                    #new_followed.append(username)
                    followed += 1

                    if (x == 1):
                        webdriver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click()
                    else:
                        webdriver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
                # Next picture
                if(x == 1):
                    webdriver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click()
                else:
                    webdriver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
                sleep(randint(4, 6))

    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:

        pass

print('Followed {} new people.'.format(followed))
