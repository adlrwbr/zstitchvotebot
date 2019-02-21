from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import datetime
import time

# CHANGE THIS
path_to_webdriver = "C:/Users/adler/Desktop/Drivers/geckodriver"
# ^^^^^^^^^^^^^^^^^^ CHANGE THIS



# XPaths/CSS Selectors of Google's login page
x_login_email = '//*[@id="identifierId"]'
x_button_next = '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content/span'
css_login_password = '.I0VJ4d > div:nth-child(1) > input:nth-child(1)'
css_button_submit = '#passwordNext > content:nth-child(3) > span:nth-child(1)'

# XPaths/CSS Selectors of Google docs
x_zstitch_bubble = '/html/body/div/div[2]/form/div/div[2]/div[2]/div/div/div[2]/div/content/div/div[40]/label/div/div[1]/div[3]/div'
x_zstitch_submit = '/html/body/div/div[2]/form/div/div[2]/div[3]/div[2]/div/div/content/span'
x_submitanotherresponse = '/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/a'


#take user information
info_is_correct = False
while not info_is_correct:
    email = input("\nWhat is your kenstonapps email address?: ")
    password = input("What is your password?: ")
    print("\n\tGoogle login information:\nEmail:  %s\nPassword:  %s\n" % (email, password))
    if input("Does this information look correct? (y/n): ") == "y":
        info_is_correct = True

while True:
    try:
        number_of_submissions = int(input("How many times woud you like to worship his holiness?: "))
        break
    except ValueError:
        print("Input a number please.")
    


def login(email, password): 
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe69eMDCHxtMZkq93_A3J8iiJGyq7OttWmxD7Rk9zm_1C774w/viewform")
    
    
    # attempt to identify elements on email page by their XPaths
    try:
        login_email = driver.find_element_by_xpath(x_login_email)
        button_next = driver.find_element_by_xpath(x_button_next)
        print('Found all elements. Moving on!')
    except Exception as e:
        print('Some element(s) could not be found.')
        return e
    # input email into Google input box and click Next
    login_email.send_keys(email)
    button_next.click()
    
    # attempt to identify elements on password page by their CSS Selectors (note: xpaths throw error...I went old-school)
    time.sleep(2) # NOTE----ONLY INCREASE THIS VALUE IF ELEMENT IS "Not reachable by keyboard" in the error.
    try:
        login_password = driver.find_element_by_css_selector(css_login_password)
        button_submit = driver.find_element_by_css_selector(css_button_submit)
        print('Found all elements. Moving on!')
    except Exception as e:
        print('\nSome element(s) could not be found. If you are getting this message you may need to increase the time.sleep value in the code above.')
        return e
    # input password into Google input box and submit
    login_password.send_keys(password)
    button_submit.click()
    return True
    
    
    
    
    
    
    
def spam():
    # attempt to identify elements on survey page by their XPaths
    while True:
        try:
            zstitch_bubble = driver.find_element_by_xpath(x_zstitch_bubble)
            zstitch_submit = driver.find_element_by_xpath(x_zstitch_submit)
            break
        except NoSuchElementException as e:
            print(e)
            print('\nSome element(s) could not be found. Trying again in 2 seconds.')
            time.sleep(2)
    # click both buttons and submit survey
    zstitch_bubble.click()
    zstitch_submit.click()
    
    
    # attempt to submit another response
    while True:
        try:
            submitanotherresponse = driver.find_element_by_xpath(x_submitanotherresponse)
            break
        except NoSuchElementException as e:
            print(e)
            print('\nSome element(s) could not be found. Trying again in 2 seconds.')
            time.sleep(2)
    # click both buttons and submit survey
    submitanotherresponse.click()
    
    
    
    
print("\nInitializing browser...\n")
driver = webdriver.Firefox(executable_path=path_to_webdriver)
loggedin = login(email, password)
if (loggedin != True):
    input(str(loggedin)+'\n\n\n'+'Error. Press enter to exit.')
    exit()
else:
    print("Nice! You're logged in! Redirecting to the survey now...")
    
    for i in range(number_of_submissions):
        spam()
        print("Voted for Z-Stitch %i times" % (i+1))
    print("\nCongratulations, the voting sequence is over. You voted for Z-Stitch %i times under %s.\n\nHave a good day." % (number_of_submissions, email))
    input()
    