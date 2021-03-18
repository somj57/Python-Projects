# Importing Rocket Status Class for checking the data
from rocketLauncher import *
import time

class _launcher(rocket):
    def __init__(self):
        super().__init__()
    
    def state(self,i):
        state = super().checkData(i)
        if state == 1:
            return True
        else:
            return False

if __name__ =='__main__':
    choice  = input("Do you want to launch the rocket (Y/N) : ")
    # Creating the object of the class
    obj1 = _launcher()

    # Getting the status of the stages
    def _netlink():
        state = obj1.state(0)
        return state
    def _fuel():
        state = obj1.state(0)
        return state
    def _power():
        state = obj1.state(0)
        return state
    def _oxygen():
        state = obj1.state(0)
        return state
    def _engine():
        state = obj1.state(0)
        return state
    
    if choice == "Y":
        if _netlink():
            print("Step 5 : NetLink is Checked")
            time.sleep(1)
            if _fuel():
                print("Step 4 : Fuel is Checked")
                time.sleep(1) 
                if _power():
                    print("Step 3 : Power is Checked")
                    time.sleep(1)
                    if _oxygen():
                        print("Step 2 : Oxygen is Checked")
                        time.sleep(1)
                        if _engine():
                            print("Step 1 : Engine On is Checked")
                            time.sleep(1)
                            print("Rocket Launch Successfull")
                            time.sleep(1)
                            print("🚀")
                        else:
                            print("Launching Failed At Step 1 :Engine Failure")
                    else:
                        print("Launching Failed At Step 2 :Oxygen Failure")
                else:
                    print("Launching Failed At Step 3 :Power Failure");
            else:
                print("Launching Failed At Step 4 :Fule Failure")
        else:
            print("Launching Failed At Step 5 :NetLink Failure")
    else:
        print("Launch Cnacelled")

'''
This is concrete class
'''