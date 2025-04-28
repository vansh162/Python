import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import json

# ---------- Web Scraping Functions ----------

def scrape_blog():
    url = input("Enter blog URL: ")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('h2')
        data = []
        for article in articles:
            title = article.text.strip()
            link = article.find('a')['href'] if article.find('a') else ''
            data.append({'title': title, 'link': link})
        with open('blog_data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Blog data saved to blog_data.json")
    except Exception as e:
        print(f"Error: {e}")
    print("=============================")

def scrape_ecommerce():
    url = input("Enter e-commerce site URL: ")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div', class_='thumbnail')
        data = []
        for product in products:
            name = product.find('a', class_='title').text.strip()
            price = product.find('h4', class_='price').text.strip()
            rating = product.find('div', class_='ratings').find_all('span', class_='glyphicon-star')._len_()
            data.append({'name': name, 'price': price, 'rating': rating})
        df = pd.DataFrame(data)
        df.to_csv('ecommerce_data.csv', index=False)
        print("Product data saved to ecommerce_data.csv")
    except Exception as e:
        print(f"Error: {e}")
    print("=============================")

def scrape_weather():
    url = input("Enter weather URL: ")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        desc = soup.find('span', class_='phrase').text.strip()
        print(f"🌦 Current Weather: {desc}")
    except Exception as e:
        print(f"Error: {e}")
    print("=============================")

# ---------- Web Automation Functions ----------

def login_website():
    try:
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/login")
        username = input("Enter username (e.g. tomsmith): ")
        password = input("Enter password (e.g. SuperSecretPassword!): ")

        driver.find_element(By.ID, 'username').send_keys(username)
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.CSS_SELECTOR, 'button.radius').click()

        time.sleep(3)
        driver.save_screenshot('login_result.png')
        print("Login attempted. Screenshot saved as login_result.png")
        driver.quit()
    except Exception as e:
        print(f"Error: {e}")
    print("=============================")

def fill_form():
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        time.sleep(3)
        driver.find_element(By.NAME, 'firstname').send_keys('Dhruvi')
        driver.find_element(By.NAME, 'lastname').send_keys('Modha')
        driver.save_screenshot('form_filled.png')
        print("Form filled. Screenshot saved as form_filled.png")
        driver.quit()
    except Exception as e:
        print(f"Error: {e}")
    print("=============================")

def search_google():
    try:
        driver = webdriver.Chrome()
        keyword = input("Enter search keyword: ")
        driver.get("https://duckduckgo.com/")
        time.sleep(2)
        search_box = driver.find_element(By.ID, 'searchbox_input')
        search_box.send_keys(keyword)
        driver.find_element(By.ID, 'searchbox_homepage_button').click()
        time.sleep(3)
        driver.save_screenshot('search_result.png')
        print("Search done. Screenshot saved as search_result.png")
        driver.quit()
    except Exception as e:
        print(f"Error: {e}")
    print("=============================")


# ---------- Combined Scraping + Automation Task ----------

def scrape_and_open_links():
    try:
        response = requests.get("https://blog.scrapinghub.com")
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('h2')
        driver = webdriver.Chrome()
        for article in articles[:3]:  # open first 3 links
            link = article.find('a')['href']
            print(f"Opening: {link}")
            driver.get(link)
            time.sleep(2)
        driver.quit()
        print("Opened top 3 blog links in browser.")
    except Exception as e:
        print(f"Error: {e}")
    print("=============================")

# ---------- Main Menu ----------

def main():
    print("=============================")
    print("Welcome to Scraper & Bot")
    print("A Web Scraping and Automation Utility")
    print("=============================")
    while True:
        print("Choose an option:")
        print("1. Web Scraping")
        print("2. Web Automation")
        print("3. Combined Tasks (Scraping + Automation)")
        print("4. Exit")
        print("=============================")
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                print("Web Scraping Options:")
                print("1. Scrape Blog Data (Titles and Links)")
                print("2. Scrape E-commerce Products (Name, Price, Rating)")
                print("3. Scrape Weather Data (Temperature, Conditions)")
                print("4. Back to Main Menu")
                print("=============================")
                choice = input("Enter your choice: ")
                
                if choice == '1':
                    scrape_blog()
                elif choice == '2':
                    scrape_ecommerce()
                elif choice == '3':
                    scrape_weather()
                elif choice == '4':
                    break
                
        elif choice == '2':
            while True:
                print("Web Automation Options:")
                print("1. Login to a Website")
                print("2. Fill and Submit a Form")
                print("3. Search and Capture Google Results")
                print("4. Back to Main Menu")
                print("=============================")
                
                choice = input("Enter your choice: ")    
                
                if choice == '1':
                    login_website()
                elif choice == '2':
                    fill_form()
                elif choice == '3':
                    search_google()
                elif choice == '4':
                    break

        elif choice == '3':
            while True:
                print("Combined Tasks Options:")
                print("1. Scrape Search Results and Visit Links")
                print("2. Back to Main Menu")
                print("=============================")
                
                choice = input("Enter your choice: ")
                
                if choice == '1':
                    scrape_and_open_links()
                elif choice == '2':
                    break
                
        elif choice == '4':
            print("Exiting program. Thank you!")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
