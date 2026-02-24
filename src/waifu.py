import requests
import json

class WaifuDownloaderAPI:
	def __init__(self):
		self.url = f"https://gelbooru.com//index.php?page=dapi&s=post&q=index&api_key=da94a99fb256765d2f354b28af5d875ad2c3f235d362381acb2cab173e9deecb3b04fd5abfa8c73c754325aafde62fed4038cfab446247a296f470f32d18e380&user_id=1923595&json=1&limit=1&limit=42&pid={random.randint(1, 139)}&tags=lappland_(arknights)"
	def generate_random_image():

    # Send GET request
    response = requests.get(self.url)
    data = response.json()

    image_url = data["post"][random.randint(0, 41)]["file_url"]

    print("Downloading:", image_url)

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://gelbooru.com/"
    }

    response = requests.get(
        image_url,
        headers=headers,
        stream=True,
        timeout=30
    )

    response.raise_for_status()

    # check what you actually got
    print(response.headers.get("Content-Type"))
    return response.content
