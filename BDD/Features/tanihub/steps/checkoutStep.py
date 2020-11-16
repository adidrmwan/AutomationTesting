from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@given('I am on TaniHub Home page')
def openHomePage(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tanihub.com/")
    context.driver.find_element_by_xpath("//*[@id='app-layout']/nav/div[2]/div[2]/div/div[2]/section/div/div[2]/div[1]/label").click()
    context.driver.implicitly_wait(2)

@when('I Click Login Button')
def LoginButton(context):
    context.driver.find_element_by_id("button-1").click()
    context.driver.implicitly_wait(2)

@then('I See Login Page')
def VerifyLoginPage(context):
    login_title = context.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/p").text
    assert (login_title == "Masuk")
    context.driver.implicitly_wait(2)

@then('I See Email Field')
def VerifyEmailField(context):
    email_title = context.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[1]/label/span/i").text
    assert (email_title == "Email Anda")

@when('I Enter "{email}" to Email Field')
def InputEmail(context,email):
    context.driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
    context.driver.implicitly_wait(2)

@when('I Click Selanjutnya Button')
def ClickNextButton(context):
    context.driver.find_element_by_xpath("//button[@type='submit']").click()
    context.driver.implicitly_wait(2)

@then('I See "{password}" Field')
def VerifyEmailField(context,password):
    password_title = context.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[2]/label/p").text
    assert (password_title == password)

@when('I Enter "{password}" to Password Field')
def InputEmail(context,password):
    context.driver.find_element_by_id("input-password-3").send_keys(password)
    context.driver.implicitly_wait(2)

@when('I Click Masuk Button')
def ClickSubmitButton(context):
    context.driver.find_element_by_xpath("//button[@type='submit']").click()
    context.driver.implicitly_wait(2)

@then('I See "{account}" in Home Page')
def VerifyMyAccount(context,account):
    context.driver.find_element_by_xpath("//*[@id='app-layout']/nav/div[4]/div/div[2]/div/div[1]/button").click()
    context.driver.implicitly_wait(2)
    account_title = context.driver.find_element_by_xpath("//*[@id='dropdown-menu']/div/div[1]/span[1]/p").text
    assert (account_title == account)

