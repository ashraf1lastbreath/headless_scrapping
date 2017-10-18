import time
from selenium import webdriver
from pyvirtualdisplay import Display

def start_driver():
    """Open headless chromedriver"""
    print 'Starting Web driver...'
    display = Display(visible=0, size=(800, 600))
    display.start()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('/root/headless_scrapping/chromedriver', chrome_options=chrome_options)
    #driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    # print "Sleeping for 4 ..."
    time.sleep(4)
    return driver, display

def close_driver(driver, display):
    """Close chromedriver"""
    print "Closing Web driver..."
    display.stop()
    driver.quit()
    print "Chrome driver closed successfully. "


def get_page(url, driver):
    """Tell the browser to get a page"""
    print "Please wait, getting your webpage ..."
    driver.get(url)
    # print "Sleeping for 20..."
    time.sleep(20)
    return driver
    # return driver

def generate_report(page, xp):
    """Parse the webage to get selected div"""
    print""
    print "Element text from your selected Xpath : "
    print "======================================================================"
    result = page.find_element_by_xpath(xp)    #find first element
    print result.text
    print ""


def parse_url(url, xp):
    """Calling function which calls all other fucntions to parse html"""

    driver, display = start_driver()
    page = get_page(url, driver)
    generate_report(page, xp)
    close_driver(driver, display)


if __name__ == '__main__':
    # url = "https://www.whoisthisip.com/ipblock"
    print "Please enter the URL for whose div you want to track :"
    url = raw_input()
    print "Please enter the Xpath of the div you want to track . Follow the below steps to find out the xpath :"
    print "     1. Open Webpage on Chrome "
    print "     2. Right click on page > Inspect"
    print "     3. Select pointer icon, and point click the word you want to track on the webpage"
    print "     4.  Right click on selected (blue) part in Inspector  >  Copy > Copy XPath"
    xp = raw_input()
    

    parse_url(url, xp)
