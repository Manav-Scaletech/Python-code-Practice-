import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from io import BytesIO
from PIL import Image

URL = "https://scaletech.xyz"

# Folder to save images
SAVE_FOLDER = "Downloaded_Images"
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Get HTML
response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

image_urls = set()


def add_url(url):
    if url:
        image_urls.add(urljoin(URL, url.strip()))


# ------------------------
# Find <img> tags
# ------------------------
for img in soup.find_all("img"):

    add_url(img.get("src"))

    if img.get("srcset"):
        for item in img["srcset"].split(","):
            add_url(item.strip().split()[0])

    add_url(img.get("data-src"))

    if img.get("data-srcset"):
        for item in img["data-srcset"].split(","):
            add_url(item.strip().split()[0])


# ------------------------
# Find <source> tags
# ------------------------
for source in soup.find_all("source"):

    add_url(source.get("src"))

    if source.get("srcset"):
        for item in source["srcset"].split(","):
            add_url(item.strip().split()[0])


# ------------------------
# Find CSS background images
# ------------------------
for tag in soup.find_all(style=True):

    matches = re.findall(
        r'url\(["\']?(.*?)["\']?\)',
        tag["style"]
    )

    for match in matches:
        add_url(match)


print(f"\nFound {len(image_urls)} images.\n")

# ------------------------
# Download and Convert
# ------------------------
count = 1

headers = {
    "User-Agent": "Mozilla/5.0"
}

for url in image_urls:

    try:

        r = requests.get(url, headers=headers, timeout=20)

        if r.status_code != 200:
            continue

        image = Image.open(BytesIO(r.content))

        # Convert to RGB if needed
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        filename = f"image_{count}.jpg"

        save_path = os.path.join(SAVE_FOLDER, filename)

        image.save(save_path, "JPEG", quality=95)

        print(f"Downloaded -> {filename}")

        count += 1

    except Exception as e:
        print(f"Skipped: {url}")
        print(e)

print("\nDone!")
print(f"Saved {count-1} images in '{SAVE_FOLDER}' folder.")