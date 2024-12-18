import json
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from deepface import DeepFace
from django.views.decorators.csrf import csrf_exempt
from deepface import DeepFace


@csrf_exempt
def home(request):
    return render(request, "core/home.html")


def video(request):
    if request.method == "POST":
        try:
            # Parse the JSON data manually
            image_data = request.POST.get("imageData")
            if not image_data:
                return JsonResponse({"error": "No image data received"}, status=400)

            # Analyze the image using DeepFace's emotion detector
            analysis = DeepFace.analyze(image_data, actions=["emotion"])

            # Extract the detected emotion with the highest probability
            detected_emotion = analysis[0]["dominant_emotion"]
            print(detected_emotion)
            with open("emotion_mapping.json", "r") as f:
                data = f.read()
                parsed_data = json.loads(data)

            emotion_info = parsed_data[detected_emotion]

            return render(request, "core/suggested_place.html", context={"data": data})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    else:
        return render(request, "core/video.html")
