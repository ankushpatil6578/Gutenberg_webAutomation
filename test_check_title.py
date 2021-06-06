from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver\chromedriver.exe")
website_url = "http://skunkworks.ignitesol.com:3000/"
driver.get(website_url)
driver.maximize_window()


def test_check_titles_heading():
    print("WebPage Title = ", driver.title)
    if driver.title== "React App":
        print("Webpage is open and title is correct")

    page_heading = "headingDiv"
    header_text=driver.find_element_by_class_name(page_heading)
    print("WebPage Heading =",header_text.text)

    if  header_text.text == "Gutenberg Project":
        print("Webpage have Gutenberg Project heading")


def test_list_of_buttons():
    buttton_class = driver.find_elements_by_class_name("btn_text")
    if len(buttton_class)==0:
        print("list of buttons is not present")

    else:
        print("\n List of buttons is present these are follows ")
        for i in buttton_class:
            print(i.text)


test_check_titles_heading()
test_list_of_buttons()

