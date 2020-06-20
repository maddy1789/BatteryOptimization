import psutil
import time
from win10toast import ToastNotifier
# import pyttsx3
# import threading

notification = ToastNotifier()

def display_notification(title, message, icon):
    notification.show_toast(
                            title="Battery Indicator", 
                            msg=message, 
                            icon_path=icon, 
                            duration=10
                           )

    while notification.notification_active():
        time.sleep(0.1)

def battery_monitor():
    while(True):
        time.sleep(10)

        battery = psutil.sensors_battery()
        percent = int(battery.percent)
        power_plugged = battery.power_plugged
        title = "BATTERY POWER: {}%".format(percent)

        if power_plugged == False:
            if percent < 15:
                msg = "PLEASE PLUG-IN THE POWER CABLE, YOUR BATTERY IS LESS THAN 15%"
                display_notification(title, msg, "icons/big_drain.ico")
            elif percent < 40:
                msg = "Please plug-in the power cable, your battery is draining"
                display_notification(title, msg, "icons/big_discharged.ico")
        elif power_plugged == True:
            if percent == 100:
                msg = "PLEASE PLUG-OUT THE POWER CABLE, YOUR BATTERY IS FULL"
                display_notification(title, msg, "icons/big_full_charging.ico")
            elif percent > 80:
                msg = "Please plug-out the power cable, your battery is charged for than 80%"
                display_notification(title, msg, "icons/big_charged.ico")


if __name__ == "__main__":
    battery_monitor()