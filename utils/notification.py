from celery import shared_task

@shared_task
def send_watering_notifications():
    print("Hello Word")