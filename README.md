## Screen Capture to PDF Tool
This tool captures screenshots of a specified area of your screen and converts them into a PDF document. It’s ideal for creating a PDF from digital books, slide decks, or any paginated content that can be navigated with a "Next" button.
________________________________________________________________________________________________________________________
### Installation
Clone this repository.
Run the main.py script, and it will install the necessary packages if they are not already installed.

### Usage
1. Run the script: python main.py
2. Follow the on-screen prompts to set the:
- Top-left and bottom-right coordinates of the capture area.
- Position of the "Next" button (used to advance pages).
- Total number of pages to capture.
- The tool will automatically capture screenshots of each page and save them in a temporary directory. Once done, it will combine these images into a single PDF named book.pdf in the current directory.

### Features
- Allows users to specify the top-left and bottom-right corners of the capture area.
- Automatically advances pages and captures each one.
- Converts all captured screenshots into a single PDF document.

### Requirements
This project requires the following Python packages: The script will automatically install any missing packages!
- os
- tempfile
- time
- argparse
- pyautogui
- mss
- Pillow
- img2pdf
________________________________________________________________________________________________________________________

### Updates
- Fixed bugs and added features 
- coordination calculator
- wait time to allow loading
- TO DO: apply OCR when converting to PDF

