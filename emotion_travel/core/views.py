import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from deepface import DeepFace
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from urllib.parse import quote

API_KEY = "f2d2025b23244d73bdb142145251703"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

@csrf_exempt
def home(request):
    if request.method == "POST":
        try:
            # Parse the JSON data manually
            image_data = request.POST.get("imageData")
            if not image_data:
                return JsonResponse({"error": "No image data received"}, status=400)

            # Analyze the image using DeepFace's emotion detector
            analysis = DeepFace.analyze(image_data, actions=["emotion"])
            print(analysis)

            # Extract the detected emotion with the highest probability
            detected_emotion = analysis[0]["dominant_emotion"]
            # detected_emotion = "neutral"
            with open("./emotion_mapping.json", "r") as f:
                data = f.read()
                parsed_data = json.loads(data)

            emotion_info = parsed_data.get(detected_emotion)
            return render(
                request,
                "core/Homepage.html",
                context={
                    "data": emotion_info,
                    "emotion": detected_emotion,
                },
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except ValueError:
            return render(
                request,
                "core/Homepage.html",
                context={"error_message": "Face not detected! Align your face properly."},
            )
    else:
        return render(request, "core/Homepage.html")

def landing(request):
    emotion = request.GET.get("emotion") #emotion from the previous page
    category = request.GET.get("category")
    print(f"emotion recieved : {emotion}")
    # print(f"category recieved : {category}")
    with open("./emotion_mapping.json" , "r") as f :
        data = f.read()
        emotion_data = json.loads(data)
        
    # #extract relevant data
    selected_data =  emotion_data.get(emotion , {})
    categories = selected_data.get("categories" , [])
    
    category_data = None
    for cat in categories :
        if cat["name"] == category:
            category_data = cat
            break     
    
    places = []
    
    if category_data: 
        for option in category_data.get("options" , [] ):        
            name = option.get("name")
            places.append({
                "name" : name ,
                "desc" : option.get("description"),
                "image" : option.get("image"),
                "loc" : option.get("location")
                # "weather" : get_weather("kozhikode")
            })
    # print(f"Places: {places}")
        
    return render(request, "core/Landing_page.html" , {"places" : places})

def get_weather(city) :
    params = {
        "key": API_KEY, 
        "q": city
    }
    
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Weather in {location}: {temperature}°C, {condition}")


#e-mail setup

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("suggestion")

        email_body = f"Sender Email: {email}\n\n{message}"

        try:
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=email_body,
                from_email="adhunash@gmail.com",  # Your sender email
                recipient_list=["adhunash@gmail.com"],  # Receiver email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

        return redirect("contact")

    return render(request, "core/contact.html")

