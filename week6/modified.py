import os
import requests
from urllib.parse import urlparse
from datetime import datetime
import hashlib

# 🌍 Welcome message
print("Welcome to the Ubuntu Image Fetcher")
print("A tool for mindfully collecting images from the web\n")

# 📁 Create directory for fetched images
output_dir = "Fetched_Images"
os.makedirs(output_dir, exist_ok=True)

# 🧠 Track downloaded image hashes to avoid duplicates
downloaded_hashes = set()

def get_filename_from_url(url):
    """Extract filename from URL or generate one if missing."""
    parsed_url = urlparse(url)
    basename = os.path.basename(parsed_url.path)
    if basename and "." in basename:
        return basename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"image_{timestamp}.jpg"

def is_image_content(headers):
    """Check if the response is likely an image."""
    content_type = headers.get("Content-Type", "")
    return content_type.startswith("image/")

def hash_content(content):
    """Generate a hash of the image content to detect duplicates."""
    return hashlib.sha256(content).hexdigest()

def fetch_image(url):
    """Download and save image from a single URL with safety checks."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # 🔍 Check content type
        if not is_image_content(response.headers):
            print(f"✗ Skipped (Not an image): {url}")
            return

        # 🛡️ Security precaution: hash content to detect duplicates
        content_hash = hash_content(response.content)
        if content_hash in downloaded_hashes:
            print(f"✗ Skipped (Duplicate image): {url}")
            return
        downloaded_hashes.add(content_hash)

        # 📝 Determine filename
        filename = get_filename_from_url(url)
        filepath = os.path.join(output_dir, filename)

        # 💾 Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"✗ HTTP error: {http_err}")
    except requests.exceptions.ConnectionError:
        print(f"✗ Connection error: {url}")
    except requests.exceptions.Timeout:
        print(f"✗ Timeout: {url}")
    except Exception as err:
        print(f"✗ Unexpected error: {err}")

def main():
    # 📥 Accept multiple URLs from user
    urls = input("Enter image URLs separated by commas:\n").split(",")

    for url in map(str.strip, urls):
        if url:
            fetch_image(url)

    print("\n🌐 Connection strengthened. Community enriched.")
    print("🗂️ Images organized for sharing. Errors handled with respect.")

if __name__ == "__main__":
    main()