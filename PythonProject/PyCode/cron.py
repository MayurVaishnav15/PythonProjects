from apscheduler.schedulers.background import BackgroundScheduler
from code import quote, send_whatsapp_message, client
import time
scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start() 
job = scheduler.add_job(send_whatsapp_message,'cron',[client, quote], hour="15", minute="51")
print(job)

while True:
    time.sleep(1)