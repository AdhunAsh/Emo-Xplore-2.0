import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from deepface import DeepFace
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from urllib.parse import quote


@csrf_exempt
def home(request):
    if request.method == "POST":
        try:
            # Parse the JSON data manually
            image_data = request.POST.get("imageData")
            if not image_data:
                return JsonResponse({"error": "No image data received"}, status=400)

            # Analyze the image using DeepFace's emotion detector
            # analysis = DeepFace.analyze(image_data, actions=["emotion"])

            # Extract the detected emotion with the highest probability
            # detected_emotion = analysis[0]["dominant_emotion"]
            detected_emotion = "neutral"
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
    else:
        return render(request, "core/Homepage.html")

def suggest(request):
    emotion = request.GET.get("emotion") #emotion from the previous page
    print(f"emotion recieved : {emotion}")
    with open("./emotion_mapping.json" , "r") as f :
        data = f.read()
        emotion_data = json.loads(data)
        
    #extract relevant data
    selected_data =  emotion_data.get(emotion , {})
    categories = selected_data.get("categories" , [])
    # print(selected_data)
    # print(categories)
    
    #link for next page
    link = f"{reverse('more_details')}"
    
    #flatten data to send only lat, lng, name, and a link
    places = []
    
    for category in categories : 
        for option in category.get("options" , [] ):
            #get lat and lng
            lat = option.get("lat")
            lng = option.get("lng")
            
            if not lat or not lng:
                print(f"Warning: Missing coordinates for {option.get('name')}. lat: {lat}, lng: {lng}")
                continue  # Skip this place if coordinates are missing

            try:
                # Convert lat and lng to float
                lat = float(lat)
                lng = float(lng)
            except ValueError:
                # If conversion fails, log an error and skip this place
                print(f"Error: Invalid coordinates for {option.get('name')}. lat: {lat}, lng: {lng}")
                continue
             
            places.append({
                "name" : option.get("name"), 
                "lat" : float(lat),
                "lng" : float(lng),
                "img" : option.get("image"),
                "link": f"{link}?emotion={emotion}&place={quote(option.get('name'))}" #append the query param for each place
            })
    print(f"Places: {places}")
    place_json = json.dumps(places)
            
    return render(request, "core/suggest_place.html" , {"places" : place_json})


def details(request):
    emotion = request.GET.get("emotion") #emotion from the previous page
    print(f"emotion recieved : {emotion}")
    with open("./emotion_mapping.json" , "r") as f :
        data = f.read()
        emotion_data = json.loads(data)
        
    #extract relevant data
    selected_data =  emotion_data.get(emotion , {})
    categories = selected_data.get("categories" , [])
    # print(selected_data)
    # print(categories)
    
    #flatten data to send details about the places
    place_name = request.GET.get("place")
    
    for category in categories : 
        for option in category.get("options" , [] ):
            if option.get("name") == place_name:
                print(f"Match found: {option.get('name')}") 
                return render(
                    request,
                    "core/place.html",
                    context= {
                        "name" : option.get("name"),
                        "description" : option.get("description"),
                        "attraction" : option.get("attraction"),
                        "images" : option.get("images"),
                        "backgroundImage" : option.get("background-img")
                    }
                )
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("subject")

        try:
            send_mail(
                f"Contact Form Submission from {name}",
                message,
                email,  # sender email
                ["adhunash@gmail.com"],  # Reciever email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

        return redirect("contact")

    return render(request, "core/contact.html")
