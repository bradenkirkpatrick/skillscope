import matplotlib.pyplot as plt
from wordcloud import WordCloud
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

def generate_wordcloud(df):
    text = ' '.join(df['column_name'].astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400).generate(text)
    plt.figure(figsize=(15, 7.5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def login_rit_site(driver, username, password):
    driver.get(os.getenv('LOGIN_URL'))  # Update with environment variable
    time.sleep(2)  # Wait for the login page to load

    # Enter username
    username_field = driver.find_element(By.ID, "ritUsername")  # Update with actual field ID
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element(By.ID, "ritPassword")  # Update with actual field ID
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    time.sleep(8)  # Wait for 2FA to complete

def scrape_rit_jobs(query, num_pages=5, username='', password=''):
    driver = webdriver.Chrome()
    login_rit_site(driver, username, password)
    job_descriptions = []
    
    for page in range(num_pages):
        url = f"https://rit-csm.symplicity.com/students/app/jobs/search?perPage=1&page={page}&sort=!kwmatch&keywords=software%2520engineer&currentJobId=9044d386ecc1f2f122daa296774c22e5"
        driver.get(url)
        time.sleep(5)  # Wait for the page to load
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # job_cards = soup.find_all('div', class_='job-card-class')  # Update with actual class name
        desc = soup.find('div', class_='form-col no-padding')  # Update with actual class name
        if desc:
                job_descriptions.append(desc.get_text(separator=' ', strip=True))
    
    driver.quit()
    df = pd.DataFrame({'job_description': job_descriptions})
    return df

def main():
    username = os.getenv('USERNAME')  # Replace with environment variable
    password = os.getenv('PASSWORD')  # Replace with environment variable
    df = scrape_rit_jobs("Software Engineer", username=username, password=password, num_pages=1762)
    # Save df to a CSV file
    df.to_csv('rit_jobs.csv', index=True)
    # generate_wordcloud(df)
    
if __name__ == "__main__":
    main()
