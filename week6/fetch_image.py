import os
import requests
from urllib.parse import urlparse
from datetime import datetime

# Prompt user for image URL
image_url = input("Enter the image URL: ").strip()

# Create directory for fetched images
output_dir = "Fetched_Images"
os.makedirs(output_dir, exist_ok=True)

def get_filename_from_url(url):
    """Extract filename from URL or generate one if missing."""
    parsed_url = urlparse(url)
    basename = os.path.basename(parsed_url.path)
    if basename and "." in basename:
        return basename
    # Fallback: generate timestamp-based filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"image_{timestamp}.jpg"

try:
    # Fetch the image
    response = requests.get(image_url, timeout=10)
    response.raise_for_status()  # Raise HTTPError for bad responses

    # Determine filename
    filename = get_filename_from_url(image_url)
    filepath = os.path.join(output_dir, filename)

    # Save image in binary mode
    with open(filepath, "wb") as f:
        f.write(response.content)

    print(f"Successfully fetched: {filename}")
    print(f"Image saved to: {filepath}")

    print("Connection strengthened. Community enriched.")

except requests.exceptions.HTTPError as http_err:
    print(f" HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError:
    print("Connection error. Please check your internet or the URL.")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
except Exception as err:
    print(f"An unexpected error occurred: {err}")