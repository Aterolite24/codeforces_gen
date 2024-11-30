from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def fetch_problem_statement_selenium(contest_id, problem_index):
    url = f"https://codeforces.com/contest/{contest_id}/problem/{problem_index}"
    
    # Set up the browser
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Run in headless mode (no GUI)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the URL
    driver.get(url)

    try:
        # Wait for the problem statement to load (max 15 seconds)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "problem-statement")))

        # Check if the problem exists
        if "Problem not found" in driver.page_source:
            print(f"Problem {contest_id}{problem_index} does not exist.")
            return None, None

        # Extract problem title (adjust the CSS selector if necessary)
        title = driver.find_element(By.CSS_SELECTOR, ".title").text.strip()

        # Extract problem statement
        statement = driver.find_element(By.CLASS_NAME, "problem-statement")
        paragraphs = statement.find_elements(By.TAG_NAME, "p")
        problem_text = "\n".join(p.text.strip().replace("\xa0", " ") for p in paragraphs)

        return title, problem_text
    except Exception as e:
        print(f"Error fetching problem {contest_id}{problem_index}: {e}")
        return None, None
    finally:
        driver.quit()

# Example usage
contest_id = 1851
problem_index = "A"
title, problem_statement = fetch_problem_statement_selenium(contest_id, problem_index)

if title and problem_statement:
    print(f"Title: {title}")
    print("Problem Statement:")
    print(problem_statement)
