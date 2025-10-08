import requests
from bs4 import BeautifulSoup


import csv
# Step 1: Send HTTP request to the website
#base_url = 'https://stackoverflow.com/questions?page={}&sort=newest'
base_url = 'https://stackoverflow.com/questions?tab=newest&page={}' 
questions_data = []
# Function to get all pages of StackOverflow questions
def get_all_pages():
    page_num = 1
    
    while page_num < 100 :
            url = base_url.format(page_num)
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Failed to retrieve page {page_num}. Status code: {response.status_code}")
                continue
            
            print(f"Processing page {page_num}")
            soup = BeautifulSoup(response.content, 'html.parser')
            questions = soup.find_all('div', class_='s-post-summary')
            if not questions: 
                print("No more pages found.")
                break
            
            for question in questions:
                title = question.find('a', class_='s-link')
                question_title = title.get_text() if title else 'No title found'
                questions_data.append([question_title])
                question_link = 'https://stackoverflow.com' + title['href'] if title else ''
                date = question.find('span', class_='s-post-summary--meta-item')
                question_date = date.get_text(strip=True) if date else 'No date found'
                votes = question.find('div', class_='s-post-summary--stats-item')
                question_votes = votes.get_text(strip=True) if votes else 'No votes found'
                print(f"Question: {question_title}")
                print(f"Date Posted: {question_date}")
                print(f"Votes: {question_votes}")
                print(f"Link: {question_link}")
                get_answers(question_link)
            
            # Go to the next page
            
        
    # Save questions to a CSV file
    save_to_csv(questions_data)

def get_answers(question_url):
    response = requests.get(question_url)
    if response.status_code != 200:
        print(f"Failed to retrieve answers for {question_url}. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract answers
    answers = soup.find_all('div', class_='s-post-answer')
    
    if not answers:
        print(f"No answers found for {question_url}")
        return

    for answer in answers:
        # Extract answer text
        answer_text = answer.find('div', class_='s-prose')
        answer_text = answer_text.get_text(strip=True) if answer_text else 'No text found'
        questions_data.append([answer_text])
        # Extract answer author (user who posted the answer)
        answer_author = answer.find('div', class_='user-details')
        answer_author = answer_author.get_text(strip=True) if answer_author else 'No author found'
        
        # Extract answer votes
        answer_votes = answer.find('span', class_='vote-count-post')
        answer_votes = answer_votes.get_text(strip=True) if answer_votes else 'No votes found'
        
        # Print answer details
        print(f"Answer by: {answer_author}")
        print(f"Answer Votes: {answer_votes}")
        print(f"Answer Text: {answer_text}")
        print("-" * 50)

# Function to save questions data to CSV
def save_to_csv(data):
    # Define the header for the CSV
    header = ['Question Title']
    
    # Open or create a CSV file to save the data
    with open('stackoverflow_questions.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header
        writer.writerows(data)   # Write all question data

    print("Questions saved to 'stackoverflow_questions.csv'")
# Run the function


get_all_pages()
