import requests, re
from bs4 import BeautifulSoup as bs

PATTERN = r'jobs/view/[^/]+-(\d+)'
URL = "https://www.linkedin.com/jobs/search?keywords=Security%20Engineer&location=Washington%2C%20United%20States&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
TEMPLATE_JOB_URL = "https://www.linkedin.com/jobs/view/__JOB_ID__"



def retrieve_jobs_urls(url):
    '''
        Retrieve the urls of the job postings from a given url
    '''
    
    # Send a GET request to the URL
    response = requests.get(url)

    # Convert the response content to soup object
    soup = convert_to_bs_object(response.content)

    # Find all the a tags with a specified class "base-card__full-link"
    a_tags = soup.find_all("a", class_="base-card__full-link")

    urls = list()

    for tag in a_tags:
        urls.append(tag["href"])
 
    return urls

def convert_to_bs_object(content):
    '''
        Convert response.content() into bs object
    '''
    return bs(content,"html.parser")



if __name__ == "__main__":
    url_list = retrieve_jobs_urls(URL)
    with open("description.txt", 'a') as txt_file:
        for url in url_list:
            '''
                Sample URL: https://www.linkedin.com/jobs/view/junior-security-engineer-at-aapc-3911563572?position=1&pageNum=0&refId=iJVtEtgGgs%2BOCD7QPRC8zg%3D%3D&trackingId=HqWOFnbH%2B3Uzpske6fMTAg%3D%3D&trk=public_jobs_jserp-result_search-card
                The numbers before the ?position parameter is the job id. We extract this one and insert into the template.
            '''
            # Expected match='jobs/view/junior-security-engineer-at-aapc-391026
            match = re.search(PATTERN, url)        

            # match.group(0) returns 'jobs/view/junior-security-engineer-at-aapc-391026 while match.group(1) returns 391026
            job_url = TEMPLATE_JOB_URL.replace("__JOB_ID__", match.group(1)) 

            visit_job = requests.get(job_url)
            job_content = convert_to_bs_object(visit_job.content)
            job_description = job_content.find("div", class_="show-more-less-html__markup")
            description = job_description.get_text(separator="\n")
            txt_file.write(description)
