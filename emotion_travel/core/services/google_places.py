import requests
from django.conf import settings

class GooglePlacesAPI:
    BASE_URL = "https://google-map-places.p.rapidapi.com"

    @staticmethod
    def get_places(query, location=None, radius=5000):
        """Search places based on query."""
        url = f"{GooglePlacesAPI.BASE_URL}/search"
        headers = {
            "X-RapidAPI-Key": settings.RAPIDAPI_KEY,
            "X-RapidAPI-Host": "google-map-places.p.rapidapi.com",
        }
        params = {
            "query": query,
            "radius": radius,
        }
        if location:
            params["location"] = location

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        return {"error": response.json(), "status_code": response.status_code}

    @staticmethod
    def get_place_details(place_id):
        """Retrieve detailed information about a place."""
        url = f"{GooglePlacesAPI.BASE_URL}/details"
        headers = {
            "X-RapidAPI-Key": settings.RAPIDAPI_KEY,
            "X-RapidAPI-Host": "google-map-places.p.rapidapi.com",
        }
        params = {
            "place_id": place_id,
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        return {"error": response.json(), "status_code": response.status_code}
