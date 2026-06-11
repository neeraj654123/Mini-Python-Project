from plyer import notification
import time

while True:
    notification.notify(
        title="💧 Water Reminder",
        message="Please sip some water!",
        timeout=5
    )
    time.sleep(5)  # every 30 minutes
