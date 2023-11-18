from celery import shared_task
from django.shortcuts import get_object_or_404, get_list_or_404
from utils.models_loads import get_phoneEvent_model, get_userPlanty_model, get_userPhone_model
from .celery import app
import requests
from datetime import datetime, timedelta
from django.forms.models import model_to_dict



@app.task(name="manage_notifications")
def manage_notifications():
    list_responses = []
    list_notifications = get_phoneEvent_model().objects.filter(event_type__icontains="Watering Reminder")
    for notification in list_notifications:
        if (notification.last_event_date + timedelta(days=notification.frequency - 1)) == datetime.today().date():
            notification_dict = model_to_dict(notification)
            status = send_notifications(expo_token=notification.user_phone.token, title=notification.event_type, body=notification.message)
            list_responses.append({"event": notification_dict, "response": status["data"]})
            if status == 200:
                notification.last_event_date = notification.last_event_date + timedelta(days=notification.frequency).date()
                notification.save()
    return list_responses


# @app.task(name="manage_status_plants")
# def manage_status_plants():
#     list_responses = []
#     list_notifications = get_phoneEvent_model().objects.filter(event_type__icontains="Temperature Alert")
#     for notification in list_notifications:
#         try:
#             user_device = notification.user_device
#             notification_dict = {}
#             title = f'Temperature Alert - {user_device.plant_name}'
#             if user_device.planty.actual_temperature[-1] + 6 < user_device.planty.plants_info.temperature:
#                 body = f'Your plant {user_device.plant_name} might be feeling cold. Make sure to maintain a warmer room temperature to promote healthy growth. Consider using gentle heating or thermal blankets if needed.'
#                 notification_dict = model_to_dict(notification)
#                 for token in get_list_or_404(get_userPhone_model(), user_id=notification.user_device.user.id):
#                     status = send_notifications(expo_token=token.token, title=title, body=body)
#             elif user_device.planty.actual_temperature[-1] - 8 > user_device.planty.plants_info.temperature:
#                 body = f'To keep your plant {user_device.plant_name} happy and healthy, we recommend adjusting the environmental temperature to a more suitable level. Ensure shade and, if possible, ventilate the area to reduce heat.'
#                 notification_dict = model_to_dict(notification)
#                 for token in get_list_or_404(get_userPhone_model(), user_id=notification.user_device.user.id):
#                     status = send_notifications(expo_token=token.token, title=title, body=body)
#             list_responses.append({"event": notification_dict["user_phone"], "response": status["data"]["details"]})
#         except:
#           pass
#     list_notifications = get_phoneEvent_model().objects.filter(event_type__icontains="Light Alert")
#     for notification in list_notifications:
#         try:
#             user_device = notification.user_device
#             notification_dict = {}
#             title = f'Light Alert - {user_device.plant_name}'
#             if user_device.planty.actual_light[-1] + 30 < user_device.planty.plants_info.light:
#                 body = f'Your plant {user_device.plant_name} need more light to efficiently carry out photosynthesis. Place them in a spot with bright indirect light or consider using grow lights to supplement natural light.'
#                 notification_dict = model_to_dict(notification)
#                 for token in get_list_or_404(get_userPhone_model(), user_id=notification.user_device.user.id):
#                     status = send_notifications(expo_token=token.token, title=title, body=body)
#             elif user_device.planty.actual_light[-1] - 30 > user_device.planty.plants_info.light:
#                 body = f'Too much direct sunlight can be harmful to some plants. Move your plant {user_device.plant_name} to a location with partial shade or use curtains to filter the light. This will prevent it from getting sunburned.'
#                 notification_dict = model_to_dict(notification)
#                 for token in get_list_or_404(get_userPhone_model(), user_id=notification.user_device.user.id):
#                     status = send_notifications(expo_token=token.token, title=title, body=body)
#             list_responses.append({"event": notification_dict["user_phone"], "response": status["data"]["details"]})
#         except:
#           pass
#     list_notifications = get_phoneEvent_model().objects.filter(event_type__icontains="Humidity Alert")
#     for notification in list_notifications:
#         try:
#             user_device = notification.user_device
#             notification_dict = {}
#             title = f'Humidity Alert - {user_device.plant_name}'
#             if user_device.planty.actual_watering[-1] + 30 < user_device.planty.plants_info.watering:
#                 body = f'Your plant {user_device.plant_name} is dehydrated. Make sure to water it adequately to keep the soil slightly moist. Watch for wilting signs and adjust the watering frequency accordingly.'
#                 notification_dict = model_to_dict(notification)
#                 status = send_notifications(expo_token=notification.user_phone.token, title=title, body=body)
#             elif user_device.planty.actual_watering[-1] - 30 > user_device.planty.plants_info.watering:
#                 body = f'It seems you are providing too much water to your plant {user_device.plant_name}. To avoid overwatering and root problems, reduce the amount of water you give and ensure the soil is dry before watering again.'
#                 notification_dict = model_to_dict(notification)
#                 for token in get_list_or_404(get_userPhone_model(), user_id=notification.user_device.user.id):
#                     status = send_notifications(expo_token=token.token, title=title, body=body)
#             list_responses.append({"event": notification_dict["user_phone"], "response": status["data"]["details"]})
#         except:
#           pass
#     return list_responses

@app.task(name="manage_status_plants")
def manage_status_plants():
    list_responses = []

    # Manejo de alertas de temperatura
    temperature_notifications = get_phoneEvent_model().objects.filter(event_type__icontains="Temperature Alert")
    for notification in temperature_notifications:
        try:
            list_responses.extend(handle_sensors_alert(
            notification,
            type="temperature",
            threshold_high=6,
            threshold_low=8
            ))
        except Exception as e:
            pass
    light_notifications = get_phoneEvent_model().objects.filter(event_type__icontains="Light Alert")
    for notification in light_notifications:
        try:
            list_responses.extend(handle_sensors_alert(
            notification,
            type="light",
            threshold_high=30,
            threshold_low=30
            ))
        except Exception as e:
            pass
    humidity_notifications = get_phoneEvent_model().objects.filter(event_type__icontains="Humidity Alert")
    for notification in humidity_notifications:
        try:
            list_responses.extend(handle_sensors_alert(
            notification,
            type="humidity",
            threshold_high=30,
            threshold_low=30
            ))
        except Exception as e:
            pass
    return list_responses

def handle_sensors_alert(notification, type, threshold_high, threshold_low):
    user_device = notification.user_device
    sensors_dict = {
      "temperature": {
        "sensor_value": user_device.planty.actual_temperature[-1],
        "plant_value": user_device.planty.plants_info.temperature,
        "title": f'Temperature Alert - {user_device.plant_name}', 
        "low": f'Your plant {user_device.plant_name} might be feeling cold. Make sure to maintain a warmer room temperature to promote healthy growth. Consider using gentle heating or thermal blankets if needed.',
        "high": f'To keep your plant {user_device.plant_name} happy and healthy, we recommend adjusting the environmental temperature to a more suitable level. Ensure shade and, if possible, ventilate the area to reduce heat.'
      },
      "humidity": {
        "sensor_value": user_device.planty.actual_watering[-1],
        "plant_value": user_device.planty.plants_info.watering,
        "title": f'Humidity Alert - {user_device.plant_name}',
        "low": f'Your plant {user_device.plant_name} is dehydrated. Make sure to water it adequately to keep the soil slightly moist. Watch for wilting signs and adjust the watering frequency accordingly.',
        "high": f'It seems you are providing too much water to your plant {user_device.plant_name}. To avoid overwatering and root problems, reduce the amount of water you give and ensure the soil is dry before watering again.'
      },
      "light": {
        "sensor_value": user_device.planty.actual_light[-1],
        "plant_value": user_device.planty.plants_info.light,
        "title": f'Light Alert - {user_device.plant_name}',
        "low": f'Your plant {user_device.plant_name} need more light to efficiently carry out photosynthesis. Place them in a spot with bright indirect light or consider using grow lights to supplement natural light.',
        "high": f'Too much direct sunlight can be harmful to some plants. Move your plant {user_device.plant_name} to a location with partial shade or use curtains to filter the light. This will prevent it from getting sunburned.'
      }
    }
    response = {}
    #Low
    if sensors_dict[type]["sensor_value"] + threshold_high < sensors_dict[type]["plant_value"]:
        response = send_notification(sensors_dict[type]["title"], sensors_dict[type]["low"], get_list_or_404(get_userPhone_model(), user_id=notification.user_device.user.id))
    #High  
    elif sensors_dict[type]["sensor_value"] - threshold_low > sensors_dict[type]["plant_value"]:
        response = send_notification(sensors_dict[type]["title"], sensors_dict[type]["high"], get_list_or_404(get_userPhone_model(), user_id=notification.user_device.user.id))
    return response



def send_notification(title, body, tokens):
    responses = []
    for token in tokens:
        print(token.token)
        status = send_notifications(expo_token=token.token, title=title, body=body)
        responses.append({"event": token.user_phone, "response": status["data"]["details"]})
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