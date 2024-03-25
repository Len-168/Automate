import subprocess
import threading
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from controller import Controller



class Appium(Controller):

        def get_devices(self):
                adb_cmd = ['adb', 'devices', '-l']
                output = subprocess.check_output(adb_cmd).decode('utf-8').strip().split('\n')
                devices = []
                for line in output[1:]:
                        if 'emulator' in line:
                                device_info = line.split()
                                device_name = device_info[0]
                                device_udid = device_info[0]
                                platform_version = next((info for info in device_info if info.startswith('platform_version:')), None)
                                if platform_version:
                                        platform_version = platform_version.split(':')[1]
                                else:
                                        platform_version = '9'
                                devices.append({
                                        'device_name': device_name,
                                        'device_udid': device_udid,
                                        'platform_version': platform_version, 
                                })
                return devices


        def run_appium(self,device_name, device_udid, platform_version):


                desired_caps = {
                        'platformName': 'Android',
                        'deviceName': device_name,
                        'udid': device_udid,
                        'platformVersion': platform_version,
                        'appPackage':'com.facebook.lite',
                        'appActivity':'com.facebook.lite.MainActivity',
                }
                
                driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
                time.sleep(10)

                # try:

                self.skipAllowPermission(driver=driver)

                self.clickOnImage(driver=driver,file_location='images/btn_create.png',sleep=3)

                self.clickOnImage(driver=driver,file_location='images/next_btn.png',sleep=3)

                #Input Name
                name = self.inputName(driver=driver)
                print("Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
                print(str(name))

                #Input Phone Number
                phone = self.inputPhone(driver=driver)
                print(phone)

                # except BaseException:
                #         pass

        def startThread(self):

                devices = self.get_devices()

                threads = []
                for device in devices:
                        thread = threading.Thread(
                        target=self.run_appium,args=(device['device_name'], device['device_udid'], device['platform_version']))
                        threads.append(thread)
                for thread in threads:
                        thread.start()





if __name__=="__main__": 
    obj = Appium()

    obj.startThread()