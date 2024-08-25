from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import time
import re

# Set up the ChromeDriver
service = Service(executable_path='C:/Users/Shivam Gangal/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')  # Update the path
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode (no UI)
driver = webdriver.Chrome(service=service, options=options)

# URL of the Airbnb page
url = "https://www.airbnb.com/rooms/1084274096011847923"

# Open the webpage
driver.get(url)

# Wait for the page to load fully
time.sleep(5)  # Adjust the sleep time as necessary

# Extract the page source after JavaScript execution
page_source = driver.page_source

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Convert HTML to Markdown using markdownify
markdown_content = md(str(soup))

# Save the output to a Markdown file
with open("airbnb_scraped_content.md", "w", encoding="utf-8") as file:
    file.write(markdown_content)

# Close the browser
driver.quit()

print("The page content has been successfully scraped and saved as 'airbnb_scraped_content.md'.")

# Define a function to clean and structure the content
def clean_and_structure_md(file_path):
    # Read the raw markdown content
    with open(file_path, 'r', encoding='utf-8') as file:
        raw_content = file.read()
    
    # Remove unwanted whitespace and new lines
    cleaned_content = re.sub(r'\n\s*\n', '\n\n', raw_content)  # Remove excessive new lines
    cleaned_content = cleaned_content.strip()  # Remove leading/trailing whitespace

    # Ensure that headings are correctly formatted
    cleaned_content = re.sub(r'^\s*#+\s*', '# ', cleaned_content, flags=re.MULTILINE)
    
    # Example: Reformat list items if needed
    cleaned_content = re.sub(r'\*\s+', '* ', cleaned_content)  # Ensure consistent list formatting

    # Save the cleaned content to a new file
    structured_file_path = 'C:/Users/Shivam Gangal/Desktop/Python Programs/Projects/Web_Scraping/structured_airbnb_content.md'
    with open(structured_file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)
    
    return structured_file_path


# File path to the .md file
file_path = 'C:/Users/Shivam Gangal/Desktop/Python Programs/Projects/Web_Scraping/airbnb_scraped_content.md'
structured_file_path = clean_and_structure_md(file_path)

# Print out the path to the cleaned and structured file
print(f"Structured content saved to: {structured_file_path}")


