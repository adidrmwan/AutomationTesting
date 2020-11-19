from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
    "platformName": "Android",
    "version" : "capabilities.setCapability(CapabilityType.VERSION, device.getProductVersion());",
    "deviceName" : "capabilities.setCapability('udid', device.getUniqueDeviceID());",
    "appPackage" : "com.tanihub.vaesdothrak",
    "appActivity" : "com.tanihub.vaesdothrak.MainActivity",
}
@given(u'I Open The Application')
def LaunchApp(context):
    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

@when(u'I Select Jabodetabek Area')
def SelectArea(context):
    explore_btn = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]'))
    )
    explore_btn.click()

    select_jabodetabek = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, '(//android.view.ViewGroup[@content-desc="btnListArea"])[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'))
    )
    select_jabodetabek.click()

@when(u'I Search the Product')
def SearchProduct(context):
    search_button = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="btnSearch"]/android.widget.TextView[2]'))
    )
    search_button.click()
    
    search_field = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText'))
    )
    search_field.send_keys("Minyak Goreng Rose Brand 2 L Karton")

    context.driver.press_keycode(66);

    # enter_search = WebDriverWait(context.driver, 30).until(
    #     EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup'))
    # )
    # enter_search.click()

@then(u'I See the Result of search')
def SeeResult(context):
    rest_search = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView[2]'))
    ).text

    assert (rest_search == "Rose Brand Minyak Goreng 2 L Karton")

    product = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]'))
    ).is_displayed()

    assert product is True

    directory = 'BDD/Features/tanihub/screenshoot/'
    file_name = 'search_product'+context.driver.current_activity
    context.driver.save_screenshot( directory + file_name + ".png")
# inputB = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputB"))
# )
# inputB.send_keys("5")

# sum = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "sum"))
# )

# if sum!=None and sum.text=="15":
#   assert True
# else:
#   assert False

# driver.quit()



# explore_btn=     xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]
# jabodetabek=    xpath=(//android.view.ViewGroup[@content-desc="btnListArea"])[1]/android.view.ViewGroup/android.view.ViewGroup

# search_field=   xpath=//android.view.ViewGroup[@content-desc="btnSearch"]/android.widget.TextView[2]
# search_fileds=  xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText
# enter_iput      xpath=xpath	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup
#result = /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView[2]
# /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]
