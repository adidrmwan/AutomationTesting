from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@given(u'I use the Chrome Browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@given(u'I Navigate to TaniHub Homepage')
def NavigateToTanihub(context):
    context.driver.get("https://tanihub.com/")
    context.driver.find_element_by_xpath("//*[@id='app-layout']/nav/div[2]/div[2]/div/div[2]/section/div/div[2]/div[1]/label").click()
    context.driver.implicitly_wait(2)
    context.driver.find_element_by_id("button-1").click()
    context.driver.implicitly_wait(2)
    login_title = context.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/p").text
    assert (login_title == "Masuk")
    context.driver.implicitly_wait(2)

@given(u'I am logged in as "{email}"')
def LoggedInAsUser(context,email):
    context.driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
    context.driver.implicitly_wait(2)
    context.driver.find_element_by_xpath("//button[@type='submit']").click()
    context.driver.implicitly_wait(2)
    context.driver.find_element_by_id("input-password-3").send_keys('admin123')
    context.driver.implicitly_wait(2)
    context.driver.find_element_by_xpath("//button[@type='submit']").click()
    context.driver.implicitly_wait(2)

@when(u'I Enter "{product}" to Search Field')
def SearchingProduct(context,product):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))).send_keys(product)
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='input-icon-2']"))).send_keys(Keys.RETURN)
    context.driver.implicitly_wait(2)

@then(u'I See the Result of "{result}" on Page')
def SearchingResult(context,result):
    wait = WebDriverWait(context.driver, 10)
    result_text = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app-layout']/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p"))).text
    assert (result_text == result)
    context.driver.implicitly_wait(5)

@when(u'I Add The Item to Cart')
def AddItem(context):
    context.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[5]/button[1]").click()
    context.driver.implicitly_wait(2)

@when(u'I Click Checkout Button')
def ClickCheckout(context):
    wait = WebDriverWait(context.driver, 10)
    context.driver.find_element_by_xpath("//*[@id='app-layout']/nav/div[4]/button[2]").click()
    context.driver.implicitly_wait(2)
    context.driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div[3]/div[2]/div/button").click()
    context.driver.implicitly_wait(2)

@then(u'I See The Summary Page of Checkout')
def SummaryPage(context):
    wait = WebDriverWait(context.driver, 10)
    address = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app-layout']/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/p[2]"))).text 
    item = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app-layout']/div[2]/div/div[2]/div[1]/div[3]/div/div"))).is_displayed()
    assert item is True
    payment = context.driver.find_element_by_xpath("//*[@id='app-layout']/div[2]/div/div[2]/div[2]/div").is_displayed()
    assert payment is True