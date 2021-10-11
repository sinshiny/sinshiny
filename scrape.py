# import requests

# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)

# print(page.text)
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
results = soup.find(id="ResultsContainer")
# print(results)
# print(results.prettify())
job_elements = results.find_all("div", class_="card-content")
# print(job_elements)
# for job_element in job_elements:
#print(job_element, end="\n"*2)

# for job_element in job_elements:
# title_element = job_element.find("h2", class_="title")
# company_element = job_element.find("h3", class_="company")
# location_element = job_element.find("p", class_="location")
# print(title_element)
# print(company_element)
# print(location_element)
# print()

# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text)
#     print(company_element.text)
#     print(location_element.text)
#     print()

# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()

# python_jobs = job_elements.find_all("h2", string="Python")
# print(python_jobs)

python_jobs = results.find_all(
    "h2", string=lambda text: "PYTHON" in text.upper()
)
# print(python_jobs)

# print(len(python_jobs))
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
fo = open("ope.txt", "w")
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    fo.write(title_element.text.strip()+'\n')
    print(company_element.text.strip())
    fo.write(company_element.text.strip()+'\n')
    print(location_element.text.strip())
    fo.write(location_element.text.strip()+'\n'*2)
    print()
fo.close()
