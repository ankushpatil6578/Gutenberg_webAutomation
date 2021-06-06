from selenium import webdriver
import time

cat = input("Enter your category name = ")
search_text = input("Enter your text for search book by name/auther = ")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver\chromedriver.exe")
website_url = "http://skunkworks.ignitesol.com:3000/"
driver.get(website_url)
driver.maximize_window()
def test_search_book_by_nameAuther(category_name):
    FICTION = '//*[@id="root"]/div/div/div/div[2]/div[1]/div/div/a/button/span[1]/span'
    DRAMA = '//*[@id="root"]/div/div/div/div[2]/div[2]/div/div/a/button/span[1]/span'
    HUMOR ='//*[@id="root"]/div/div/div/div[2]/div[3]/div/div/a/button/span[1]/span'
    POLITICS ='//*[@id="root"]/div/div/div/div[2]/div[4]/div/div/a/button/span[1]/span'
    PHILOSOPHY ='//*[@id="root"]/div/div/div/div[2]/div[8]/div[1]/div/div/a/button/span[1]/span'
    HISTORY ='//*[@id="root"]/div/div/div/div[2]/div[8]/div[2]/div/div/a/button/span[1]/span'
    ADVENTURE ='//*[@id="root"]/div/div/div/div[2]/div[8]/div[3]/div/div/a/button/span[1]/span'

    if str(category_name).upper() == "FICTION":
        driver.find_element_by_xpath(FICTION).click()
    elif str(category_name).upper() == "DRAMA":
        driver.find_element_by_xpath(DRAMA).click()
    elif str(category_name).upper() == "HUMOR":
        driver.find_element_by_xpath(HUMOR).click()
    elif str(category_name).upper() == "POLITICS":
        driver.find_element_by_xpath(POLITICS).click()
    elif str(category_name).upper() == "PHILOSOPHY":
        driver.find_element_by_xpath(PHILOSOPHY).click()
    elif str(category_name).upper() == "HISTORY":
        driver.find_element_by_xpath(HISTORY).click()
    elif str(category_name).upper() == "ADVENTURE":
        driver.find_element_by_xpath(ADVENTURE).click()
    else:
        print("Invalid category name")


    driver.implicitly_wait(10)
    tit = driver.find_element_by_xpath("//h1")
    seach_textbox = driver.find_element_by_xpath('//input')
    seach_textbox.send_keys(search_text)
    search_button = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/button/span[1]')
    search_button.click()
    time.sleep(10)
    if str(category_name).upper() == str(tit.text).upper():
        print(tit.text, " book category is verified and open")
        time.sleep(10)
        try:
            search_result = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[2]/div').is_displayed()
            if search_result == True:
                print("Search result is present")

        except:
            print("Search result is not present And there is no alert message")





test_search_book_by_nameAuther(cat)



