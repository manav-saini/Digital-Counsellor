import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to be scraped
URL = "https://counselchat.com/"

# Make a GET request to the URL
response = requests.get(URL)

# # Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
# # Find all topics
# topic = soup.find("div", class_="topics")
# topics =[]
# for t in topic.find_all("a"):
#     topics.append(t.text)

# #Remove all element with \xa0
# topics = [x.strip() for x in topics if x != '\xa0']

# url_2 = "https://counselchat.com/therapists#?keyword="
# for t in topics:
#     u = url_2 + t
#     response = requests.get(u)
#     soup = BeautifulSoup(response.content, "html.parser")
#     # Find all therapists
#     counselors_data = soup.find("div", class_="directory-results")
#     print(counselors_data)
#     c_d_ = counselors_data.find_all("div", class_="row directory-result ng-scope")
#     urls =[]
#     for c in c_d_:
#         l = c.find("div", class_="col-sm-2 text-center mb-15")
#         urls.append(l.find("a").get("href"))
#     print(urls)
#     break
 
topics = soup.find("div",class_="row recently-answered mt-10")
topics = topics.find("div", class_="col-sm-8")
topics = topics.find_all("div", class_="row")
urls = []
for t in topics:
    urls.append(URL[:-1]+t.find("a").get("href"))
questions_link=[]
for u in urls:
    for p in range(1, 40):
        url = u+"?page="+str(p)
        print(url)
        response = requests.get(u)
        soup = BeautifulSoup(response.content, "html.parser")
        q = soup.find("div", class_="content-answers mt-20")
        q = q.find_all("div", class_="list-item")
        for i in q:
            questions_link.append(URL[:-1]+i.find("a").get("href"))

DATA = pd.DataFrame(columns=["topic", "question", "answer", "therapist", "link"])
for q in questions_link:
    response = requests.get(q)
    soup = BeautifulSoup(response.content, "html.parser")
    topic = q.split("?")[0].split("/")[-1]
    question = soup.find("div", class_="page-description")
    question = question.find_all("p")
    question_description = ""
    for i in question:
        question_description += i.text
    data = soup.find_all("div", class_="item-answer")
    for d in data:
        therapist = d.find("div", class_="therapist-summary")
        for t in therapist:
            name = t.find('a').text.strip()
            link = URL[:-1]+str(t.find('a').get("ng-href"))
        
        answer = d.find("div", class_="description")
        answer = answer.find_all("p")
        answer_description = ""
        for i in answer:
            answer_description += i.text
        upvote = d.find("div", class_="actions")
        upvote = upvote.find("a")
        upvote = upvote["ng-init"].split("=")[1].strip()
        DATA = DATA.append({"topic": topic, "question": question_description, "answer": answer_description, "therapist": name, "link": link}, ignore_index=True)

DATA.to_csv("scrapped_data.csv", index=False)

