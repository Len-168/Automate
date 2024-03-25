import random
import secrets
import string
import time
import cv2
import names
import numpy as np
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy

class AppConstant:

    def getFirstName(self):
        FirstName = names.get_first_name(gender='female')
        return FirstName

    def getLastName(self):
        LastName = names.get_last_name()
        return LastName

    def getRandomPassword(self):
        return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for n in range(12))
    
    def getPhoneNumber(self):
        first = ['88','99']
        kk = random.choice(first)
        diget = random.randint(1111111,9999999)
        fullPhone = "+855"+str(kk)+str(diget)

        return fullPhone

    def skipAllowPermission(self,driver):
        for _ in range(4):
            try:
                    permis = driver.find_element(by=AppiumBy.ID,value='com.android.packageinstaller:id/permission_deny_button')
                    if permis.is_displayed() == True:
                            permis1 = driver.find_element(by=AppiumBy.ID,value='com.android.packageinstaller:id/permission_deny_button')
                            permis1.click(),time.sleep(3)
                    else:
                            pass
            except:
                    break
            pass

    def clickOnImage(self,driver,file_location,sleep):
            
            screenshot = driver.get_screenshot_as_png()
            screenshot = np.array(bytearray(screenshot), dtype=np.uint8)
            screenshot = cv2.imdecode(screenshot, cv2.IMREAD_COLOR)

            image_to_click = cv2.imread(file_location)

            result = cv2.matchTemplate(screenshot, image_to_click, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            top_left = max_loc

            image_height, image_width, _ = image_to_click.shape
            center_x = top_left[0] + image_width // 2
            center_y = top_left[1] + image_height // 2

            action = TouchAction(driver)
            action.tap(x=center_x, y=center_y).perform()

            time.sleep(sleep)



