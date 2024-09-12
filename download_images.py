import requests
import os
from urllib.parse import urlparse, unquote

def sanitize_filename(url):
    """Sanitize the filename extracted from the URL."""
    path = urlparse(url).path
    filename = os.path.basename(path)
    sanitized_filename = "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_')).rstrip()
    return sanitized_filename

def download_images(url_file, download_folder):
    # Ensure the download folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    with open(url_file, 'r') as file:
        urls = file.readlines()
    
    for i, url in enumerate(urls):
        url = url.strip()
        if url:
            try:
                response = requests.get(url)
                response.raise_for_status()
                # Sanitize the image name from the URL
                image_name = sanitize_filename(url)
                image_path = os.path.join(download_folder, image_name)
                
                # Save the image
                with open(image_path, 'wb') as img_file:
                    img_file.write(response.content)
                
                print(f"Downloaded {image_name} from {url}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    url_file = 'image_urls.txt'  # The file containing the list of image URLs
    download_folder = 'downloaded_images'  # The folder where images will be saved
    download_images(url_file, download_folder)
