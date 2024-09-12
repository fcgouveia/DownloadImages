# README

## Image Downloader Script

This Python script allows you to download images from a list of URLs provided in a text file. Each image is saved to a specified download folder with a sanitized filename extracted from the URL.

### Features
- Downloads images from a list of URLs.
- Saves the images in a specified folder.
- Sanitizes filenames to avoid invalid characters.

### Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using pip:
```bash
pip install requests
```

### How to Use

1. **Prepare the URL List**:  
   Create a text file (e.g., `image_urls.txt`) containing the image URLs you want to download. Each URL should be on a new line.

   Example `image_urls.txt`:
   ```
   https://example.com/image1.jpg
   https://example.com/image2.png
   ```

2. **Run the Script**:  
   Execute the script with the default settings or modify the file paths as needed.

   ```bash
   python download_images.py
   ```

   By default:
   - The script expects the file `image_urls.txt` to contain the image URLs.
   - It saves the downloaded images to a folder named `downloaded_images`.

3. **Customizing File Paths**:  
   You can modify the following variables in the script:
   - `url_file`: Path to the file containing the image URLs.
   - `download_folder`: Path to the folder where images will be saved.

### How It Works

- The script reads the URLs from the provided text file.
- It sends an HTTP request to each URL to download the image.
- The filename is sanitized to remove any unwanted characters.
- Each image is saved to the specified folder.

### Example

Given a URL `https://example.com/path/to/image1.jpg`, the script will:
1. Sanitize the filename to `image1.jpg`.
2. Download the image and save it to the folder `downloaded_images`.

### Error Handling

If any URL fails to download, the script will display an error message with the specific URL and reason for failure.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute, submit issues, or suggest improvements!
