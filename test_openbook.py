from selenium import webdriver
import time



driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver\chromedriver.exe")
website_url = "http://skunkworks.ignitesol.com:3000/"
driver.get(website_url)
driver.maximize_window()
def test_check_openBook():
    DRAMA = '//*[@id="root"]/div/div/div/div[2]/div[2]/div/div/a/button/span[1]/span'
    driver.find_element_by_xpath(DRAMA).click()
    time.sleep(5)
    poems_bookname = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div/a/h5')
    poems_bookname.click()
    time.sleep(5)
    print(driver.title)

    if str(driver.title).__contains__('The Project Gutenberg'):
        print("Book page is open ")
        assert True
    else:
        print("Book page is not open")
        assert False


test_check_openBook()
