from celery import shared_task
from django.shortcuts import get_object_or_404, get_list_or_404
from utils.models_loads import get_phoneEvent_model, get_userPlanty_model, get_userPhone_model
from .celery import app
import requests
from datetime import datetime, timedelta
from django.forms.models import model_to_dict
from datetime import datetime
import pytz


@app.task(name="manage_notifications")
def manage_notifications():
    responses = []

    watering_notifications = get_phoneEvent_model().objects.filter(event_type__icontains="Watering Reminder")
    for notification in watering_notifications:
        if (notification.last_event_date + timedelta(days=notification.frequency - 1)) == datetime.today().date():
            notification_dict = model_to_dict(notification)
            status = send_notifications(expo_token=notification.user_phone.token, title=notification.event_type, body=notification.message)
            responses.append({"event": notification_dict, "response": status["data"]})
            if status == 200:
                notification.last_event_date = notification.last_event_date + timedelta(days=notification.frequency).date()
                notification.save()

    return responses


@app.task(name="manage_status_plants")
def manage_status_plants():
    responses = []

    alerts = [
        {"type": "temperature", "threshold_high": 6, "threshold_low": 8, "event_type": "Temperature Alert"},
        {"type": "light", "threshold_high": 30, "threshold_low": 30, "event_type": "Light Alert"},
        {"type": "humidity", "threshold_high": 30, "threshold_low": 30, "event_type": "Humidity Alert"},
    ]

    for alert in alerts:
        notifications = get_phoneEvent_model().objects.filter(event_type__icontains=alert["event_type"])
        for notification in notifications:
            try:
                current_time = datetime.now(pytz.timezone(f"Etc/GMT{notification.user_device.planty.timezone}"))
                if 6 <= current_time.hour < 22:
                    responses.extend(handle_sensors_alert(notification, **alert))
            except Exception as e:
                pass

    return responses


def handle_sensors_alert(notification, type, threshold_high, threshold_low, event_type):
    user_device = notification.user_device
    sensors_dict = {
        "temperature": {"sensor_value": user_device.planty.actual_temperature[-1],
                        "plant_value": user_device.planty.plants_info.temperature,
                        "title": f'Temperature Alert - {user_device.plant_name}'},
        "humidity": {"sensor_value": user_device.planty.actual_watering[-1],
                     "plant_value": user_device.planty.plants_info.watering,
                     "title": f'Humidity Alert - {user_device.plant_name}'},
        "light": {"sensor_value": user_device.planty.actual_light[-1],
                  "plant_value": user_device.planty.plants_info.light,
                  "title": f'Light Alert - {user_device.plant_name}'},
    }

    response = {}
    if sensors_dict[type]["sensor_value"] + threshold_high < sensors_dict[type]["plant_value"]:
        response = send_notification(sensors_dict[type]["title"], f'Your plant {user_device.plant_name} might be feeling {event_type.lower()}.', get_list_or_404(get_userPhone_model(), user_id=notification.user_device.user.id))
    elif sensors_dict[type]["sensor_value"] - threshold_low > sensors_dict[type]["plant_value"]:
        response = send_notification(sensors_dict[type]["title"], f'To keep your plant {user_device.plant_name} happy and healthy, adjust the {event_type.lower()} conditions.', get_list_or_404(get_userPhone_model(), user_id=notification.user_device.user.id))

    return response


def send_notification(title, body, tokens):
    responses = []
    for token in tokens:
        status = send_notifications(expo_token=token.token, title=title, body=body)
        responses.append({"to": token.user.email, "token": token.token, "body": title, "response": status["data"]["status"]})
    return responses


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
    
