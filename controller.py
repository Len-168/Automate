import time
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from contstant import AppConstant

class Controller(AppConstant):

    def inputName(self,driver):
        
        FirstName = self.getFirstName()
        LastName = self.getLastName()

        firstName = driver.find_element(by=AppiumBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.widget.MultiAutoCompleteTextView[1]")
        firstName.send_keys(FirstName),time.sleep(2)

        lastName = driver.find_element(by=AppiumBy.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.widget.MultiAutoCompleteTextView[2]')
        lastName.click(),time.sleep(3)
        lastName.send_keys(LastName),time.sleep(5)

        self.clickOnImage(driver=driver,file_location='images/next_btn.png',sleep=5)

        self.skipAllowPermission(driver=driver)

        full_name = FirstName+lastName
        return full_name

    def  inputPhone(self,driver):
        
        Phone = self.getPhoneNumber()

        txtPhoneNumber = driver.find_element(by=AppiumBy.CLASS_NAME,value='android.widget.MultiAutoCompleteTextView')
        txtPhoneNumber.click(),time.sleep(3)
        txtPhoneNumber.send_keys(Phone),time.sleep(2)

        self.clickOnImage(driver=driver,file_location='images/next_btn.png',sleep=5)

        while True:
            try:
                errorPhone = driver.find_element(by=AppiumBy.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.view.View')
                if errorPhone.is_displayed():
                        Phone = self.getPhoneNumber()
                        txtPhoneNumber.clear(),time.sleep(3)
                        txtPhoneNumber.send_keys(Phone),time.sleep(2)
                        self.clickOnImage(driver=driver,file_location='images/next_btn.png',sleep=5)
                else:
                        break
            except BaseException:
                    break
            pass
        
        return Phone