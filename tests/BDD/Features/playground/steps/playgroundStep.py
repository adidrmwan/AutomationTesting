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

@then(u'I See "{message}" for First Number')
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

# ===================================================================

@when(u'I Select "Sci-Fi Author" to The Occupation Field')
def SelectOccupation(context):
    context.driver.find_element_by_xpath("//select[@name='occupation']/option[text()='Science Fiction Author']").click()


@then(u'I See "{message}" for Third Number')
def ThirdNumber(context,message):
    result = context.driver.find_element_by_id("ok_3").text
    assert (message == result)

# ===================================================================

@when(u'I Count the Number of Blue Boxes')
def CountNumber(context):
    count = len(context.driver.find_elements_by_class_name("bluebox"))
    print (count)

@when(u'I Enter The Count to The Answer Slot')
def AnswerFourthQuestion(context):
    count = len(context.driver.find_elements_by_class_name("bluebox"))
    context.driver.find_element_by_id("answer4").send_keys(count)


@then(u'I See "{message}" for Fourth Number')
def FourthNumber(context,message):
    result = context.driver.find_element_by_id("ok_4").text
    assert (message == result)

# ===================================================================

@when(u'I Click Link that Says "click me"')
def ClickLink(context):
    context.driver.find_element_by_xpath("//a[@onclick=\"link_clicked();return false\"]").click()


@then(u'I See "{message}" for Fifth Number')
def FifthNumber(context,message):
    result = context.driver.find_element_by_id("ok_5").text
    assert (message == result)

# ===================================================================

@when(u'I Get The Class of Red Box')
def GetClass(context):
    class_name = context.driver.find_element_by_id("redbox").get_attribute("class")
    print (class_name)


@when(u'I Enter The Class to The Answer Slot')
def AnswerClass(context):
    class_name = context.driver.find_element_by_id("redbox").get_attribute("class")
    context.driver.find_element_by_id("answer6").send_keys(class_name)

@then(u'I See "{message}" for Sixth Number')
def SixthNumber(context,message):
    result = context.driver.find_element_by_id("ok_6").text
    assert (message == result)

# ===================================================================

@when(u'I Run JavaScript Function "ran_this_js_function()"')
def RunJs(context):
    context.driver.execute_script('ran_this_js_function();')


@then(u'I See "{message}" for Seventh Number')
def SeventhNumber(context,message):
    result = context.driver.find_element_by_id("ok_7").text
    assert (message == result)

# ===================================================================

@when(u'I Run JavaScript Function "got_return_from_js_function()"')
def GetReturnJS(context):
    return_text = context.driver.execute_script('return got_return_from_js_function();')

@when(u'I Enter The Return Value to The Answer Slot')
def AnswerTheQuestion(context):
    return_text = context.driver.execute_script('return got_return_from_js_function();')
    context.driver.find_element_by_id("answer8").send_keys(return_text)

@then(u'I See "{message}" for Eight Number')
def EightNumber(context,message):
    result = context.driver.find_element_by_id("ok_8").text
    assert (message == result)

# ===================================================================

@when(u'I Select written book on Form')
def SelectWrittenBook(context):
    context.driver.find_element_by_xpath("//input[@name='wrotebook']").click()

@then(u'I See "{message}" for Nineth Number')
def NinenthNumber(context,message):
    result = context.driver.find_element_by_id("ok_9").text
    assert (message == result)

# ===================================================================

@when(u'I Get The Text of Red Box')
def GetText(context):
    get_text = context.driver.find_element_by_id("redbox").text

@when(u'I Enter The Text to The Answer Slot')
def AnswerTheQuestion(context):
    get_text = context.driver.find_element_by_id("redbox").text
    context.driver.find_element_by_id("answer10").send_keys(get_text)


@then(u'I See "{message}" for Ten Number')
def TenNumber(context,message):
    result = context.driver.find_element_by_id("ok_10").text
    assert (message == result)

# ===================================================================

@when(u'I Get The Box on Top')
def GetTheBox(context):
    orange_box =  context.driver.find_element_by_id("orangebox")
    green_box =   context.driver.find_element_by_id("greenbox")

    if orange_box.location["y"] < green_box.location["y"] :
        result = 'orange'
    else:
        result = 'green'
    
    print(result)


@when(u'I Enter The Box to The Answer Slot')
def AnswerTheQuestionBox(context):
    orange_box =  context.driver.find_element_by_id("orangebox")
    green_box =   context.driver.find_element_by_id("greenbox")

    if orange_box.location["y"] < green_box.location["y"] :
        result = 'orange'
    else:
        result = 'green'

    context.driver.find_element_by_id("answer11").send_keys(result)


@then(u'I See "{message}" for Eleventh Number')
def EleventhNumber(context,message):
    result = context.driver.find_element_by_id("ok_11").text
    assert (message == result)

# ===================================================================

@when(u'I Set The Browser to 850 and 650')
def SetBrowserSize(context):
    context.driver.set_window_size(850, 650)


@then(u'I See "{message}" for Twelve Number')
def TwelveNumber(context,message):
    result = context.driver.find_element_by_id("ok_12").text
    assert (message == result)

# ===================================================================

@when(u'I Enter The Answer of ID to The Answer Slot')
def GetDisplayingID(context):
    item = len(context.driver.find_elements_by_id("ishere"))

    if item > 0:
        rest = 'yes'
    else:
        rest = 'no'
    
    context.driver.find_element_by_id("answer13").send_keys(rest)

@then(u'I See "{message}" for Thirteen Number')
def GetTheResult(context,message):
    result = context.driver.find_element_by_id("ok_13").text
    assert (result == message )

# ===================================================================

@when(u'I Enter The Item is Visible to The Answer Slot')
def PurplerBoxVisible(context):
    purple = context.driver.find_element_by_id("purplebox").is_displayed()

    if purple is True:
        rest = 'yes'
    else:
        rest = 'no'
    
    print(rest)
    
    context.driver.find_element_by_id("answer14").send_keys(rest)


@then(u'I See "{message}" for Fourteen Number')
def GetTheResult(context,message):
    result = context.driver.find_element_by_id("ok_14").text
    assert (result == message )

# ===================================================================

@when(u'I Click the Link')
def ClickTheLink(context):
    wait = WebDriverWait(context.driver, 10)
    context.driver.find_element_by_xpath("//a[@onclick=\"show_new_link_after_wait();return false;\"]").click()
    wait.until(EC.presence_of_element_located((By.XPATH,"//a[@onclick=\"click_after_wait();return false;\"]"))).click()
    

@when(u'I Click Submit Button')
def SubmitButton(context):
    context.driver.switch_to.alert.accept()
    context.driver.find_element_by_id("submitbutton").click()


@then(u'I See "{message}" for the Last Question')
def step_impl(context,message):
    result = context.driver.find_element_by_id("ok_15").text
    result16 = context.driver.find_element_by_id("ok_16").text
    result_last = context.driver.find_element_by_id("ok_17").text
    assert (result16 == message )
    assert (result == message )
    assert (result_last == message )
