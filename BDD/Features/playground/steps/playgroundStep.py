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

@given(u'I Navigate to Playground Homepage')
def NavigateToPlayground(context):
    context.driver.get("http://timvroom.com/selenium/playground/")
    context.driver.implicitly_wait(2)

@when(u'I Get the Title of Page')
def GetTitle(context):
    title = context.driver.title

@when(u'I Enter The Title to The Answer Slot')
def AnswerTheQuestion(context):
    title = context.driver.title
    context.driver.find_element_by_id("answer1").send_keys(title)
    context.driver.implicitly_wait(2)

@when(u'I Click Check Results Button')
def CheckResult(context):
    context.driver.find_element_by_id("checkresults").click()
    context.driver.implicitly_wait(2)

@then(u'I See "{message}" for First Question')
def FirstQuestion(context,message):
    result = context.driver.find_element_by_id("ok_1").text
    assert (message == result)

# ===================================================================

@when(u'I Enter "{name}" to The Name Field')
def EnterName(context,name):
    context.driver.find_element_by_id("name").send_keys(name)
    context.driver.implicitly_wait(2)


@then(u'I See "{message}" for Second Number')
def SecondNumber(context,message):
    result = context.driver.find_element_by_id("ok_2").text
    assert (message == result)