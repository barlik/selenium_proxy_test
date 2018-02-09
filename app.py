from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

import time

PROXY = "http://owasp-zap-openshift.zap-rhel.svc:8080"

webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}

SELENIUM_HUB_URL = 'http://selenium-hub.tuesday3001.svc:4444/wd/hub'

driver = webdriver.Remote(command_executor=SELENIUM_HUB_URL,
                          desired_capabilities=webdriver.DesiredCapabilities.CHROME)


# driver.get('http://google.com')
# driver.quit()


print("Selenium hub: {}".format(SELENIUM_HUB_URL))
print("Using proxy: {}".format(PROXY))

TARGET = "http://www.python.org"

while True:
    print("Connecting to: {}".format(TARGET))

    driver.get(TARGET)
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
    print("DONE")
    print("Sleeping for 10 seconds...")
    time.sleep(10)
