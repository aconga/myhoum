import requests
from urllib.parse import urlencode

api_key = "AIzaSyDVvn7oxPvO_UvIGsQrraTGWVYlqDFFCms"
def extract_lat_lng(address_or_postalcode, data_type = 'json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_postalcode, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299): 
        return {}
    latlng = {}
    try:
        latlng = r.json()['results'][0]['geometry']['location']
    except:
        pass
    return latlng.get("lat"), latlng.get("lng")


def get_lat_lng_model(model):
    try:
        obj = model.objects.all().order_by('-start_date')[0]
    except:
        return None, None, None, None
    return obj, obj.latitude, obj.longitude, obj.start_date