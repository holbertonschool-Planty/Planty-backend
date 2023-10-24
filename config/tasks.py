from celery import shared_task
from django.shortcuts import get_object_or_404
from utils.models_loads import get_phoneEvent_model
from .celery import app
import requests
from datetime import datetime, timedelta




@app.task(name="manage_notifications")
def manage_notifications():
    list_responses = []
    list_notifications = get_phoneEvent_model().objects.all()
    for notification in list_notifications:
        if (notification.last_event_date + timedelta(days=notification.frequency - 1)).date() == datetime.today().date():
            status = send_notifications(expo_token=notification.user_phone.token, title=notification.event_type, body=notification.message)
            list_responses.append({"event": notification, "response": status})
            if status == 200:
                notification.last_event_date = notification.last_event_date + timedelta(days=notification.frequency).date()
                notification.save()
    return list_responses


@app.task(name="manage_status_plants")
def manage_status_plants():
    # Waiting until exists the Users_planties model.
    pass


def send_notifications(expo_token: str, title: str, body: str):
    url = "https://exp.host/--/api/v2/push/send"
    headers = {
        "host": "exp.host",
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "content-type": "application/json"
    }
    data = {
        "to": expo_token,
        "sound": "default",
        "title": title,
        "body": body
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()