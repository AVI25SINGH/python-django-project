base_url='https://www.timesjobs.com/candidate/job-search.html?from=submit&searchType=Home_Search&luceneResultSize=25&postWeek=60&cboPresFuncArea=35&pDate=Y&sequence=1&startPage='
all_in=[]

for i in range (1,41):
    all_in.append(base_url+str(i))
    
all_job_info=[]
import requests
from bs4 import BeautifulSoup

for url in all_in:
    base=requests.get(url).text
    all_bs4=BeautifulSoup(base,'lxml')
    all_li=all_bs4.find_all('li',class_='clearfix job-bx wht-shd-bx')
    
    for item in all_li:
        job=item.find('h2').text
        job=job.lstrip()
        
        company=item.find('h3',class_='joblist-comp-name').text
        company_n=company.lstrip().split()[0]
        
        exp=item.find('li').text
        import re
        patteren='\d+\s+[-]\s+\d+\s+\w+'
        exp1=re.findall(patteren,exp)
        
        location=item.find('span').text
        all_location=location.lstrip()
        
        job_description=val.find('ul',class_='list-job-dt1 clearfix').text
        job_description=job_description.splitlines()[3:4]
        job_description=','.join(job_description)
        
        all_skil=item.find('span',class_='srp-skills').text
        all_skill=all_skil.strip()
        all_link=item.find('a')['href'].strip()
        
        all_job={
        'job title': job,
        'company':company_n,
        'experience':exp1,
        'location':all_location,
        'job description':job_description,
        'key skill':all_skill,
        'job detail link':all_link
        }
        all_job_info.append(all_job)
    import pandas as pd
    
    df1=pd.DataFrame(all_job_info)
    print(df1)
    df1.to_excel('all_scrapp_data.xlsx')
        