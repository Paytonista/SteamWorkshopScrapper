from selenium.webdriver import Edge, EdgeOptions
from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation

data_object = open("data.txt", "w")
driver_option = webdriver.EdgeOptions()
# set options as desired
driver_option.add_argument('--headless')
driver_option.add_argument('--disable-gpu')
driver_option.add_argument('--ignore-certificate-errors')
# set path to Edge driver executable
def create_webdriver():
    chromedriver_path = 'C:\\Users\\kenne\\OneDrive\\Desktop\\SeleniumScrapper\\msedgedriver.exe' # change path as needed
    # create Edge driver with options
    return webdriver.Edge(executable_path=chromedriver_path, options=driver_option)


browser = create_webdriver()
browser.get("https://steamcommunity.com/workshop/browse/?appid=294100&browsesort=trend&section=readytouseitems&actualsort=trend&p=2&days=-1") # change URL as needed

projects = browser.find_elements("xpath", "//div[@class='workshopItem' and @data-panel='{\"type\":\"PanelGroup\"}']")

project_list = {}
for proj in projects:
    proj_name = proj.text # Project name
    proj_url = proj.find_element(By.TAG_NAME, "a").get_attribute("href") # Project URL
    #project_list[proj_name] = proj_url
    print(proj_name)
    open("data.txt", "a").write(proj_name + "\n")
    open("data.txt", "a").write(proj_url + "\n")
    


browser.quit()