import sys
import subprocess

required_packages = ["os", "tempfile", "time", "argparse", "pyautogui", "mss", "Pillow", "img2pdf"]

def install_packages(packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_packages(required_packages)

import os
import tempfile
import time
import argparse
import pyautogui
import mss
from PIL import Image
import img2pdf

def get_mouse_position(prompt):
    print(prompt)
    time.sleep(5)
    return pyautogui.position()

def capture_screenshots(top_left, bottom_right, next_page, total_pages):
    rect_size = (bottom_right[0] - top_left[0], bottom_right[1] - top_left[1])
    images = []
    temp_dir = tempfile.mkdtemp()

    with mss.mss() as sct:
        for i in range(total_pages):
            page_num = str(i).zfill(len(str(total_pages)))
            file_name = os.path.join(temp_dir, f'book-page-{page_num}.png')
            images.append(file_name)

            pyautogui.moveTo(*next_page, duration=1)
            pyautogui.click()
            time.sleep(1)  

            monitor = {
                "top": top_left[1],
                "left": top_left[0],
                "width": rect_size[0],
                "height": rect_size[1]
            }
            screenshot = sct.grab(monitor)

            img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
            img.save(file_name)
            print(f"Saved: {file_name}")
        
        return images

top_left = get_mouse_position("Move your mouse to the top-left position of the file. You have 5 seconds...")
print(f"Top-left Coordinates: ({top_left.x}, {top_left.y})")

bottom_right = get_mouse_position("Move your mouse to the bottom-right position. You have 5 seconds...")
print(f"Bottom-right Coordinates: ({bottom_right.x}, {bottom_right.y})")

next_page = get_mouse_position("Move your mouse to the 'Next' button position. You have 5 seconds...")
print(f"Next button Coordinates: ({next_page.x}, {next_page.y})")

try:
    total_pages = int(input("Enter the total number of pages to capture: "))
except ValueError:
    print("Invalid input. Setting total pages to 10 by default.")
    total_pages = 10
    

def image2pdf(images):
    with open("book.pdf", "wb") as f:
        f.write(img2pdf.convert(images))


images = capture_screenshots((top_left.x, top_left.y), (bottom_right.x, bottom_right.y), (next_page.x, next_page.y), total_pages)
image2pdf(images)


print("Done, book saved in book.pdf.")
