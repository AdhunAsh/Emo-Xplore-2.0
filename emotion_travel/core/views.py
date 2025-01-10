import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from deepface import DeepFace
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

@csrf_exempt
def home(request):
    if request.method == "POST":
        try:
            #Parse the JSON data manually
            image_data = request.POST.get("imageData")
            if not image_data:
                return JsonResponse({"error": "No image data received"}, status=400)

            # Analyze the image using DeepFace's emotion detector
            analysis = DeepFace.analyze(image_data, actions=["emotion"])

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
    else:
        return render(request, "core/Homepage.html")




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('subject')

        try:
            send_mail(
                f'Contact Form Submission from {name}',
                message,
                email, # sender email
                ['adhunash@gmail.com'],  # Reciever email
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
        
        return redirect('contact')

    return render(request, 'core/contact.html')

def suggest(request):
    return render(request,'core/suggest_place.html')