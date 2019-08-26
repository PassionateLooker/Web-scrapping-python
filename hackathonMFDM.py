# import requests,csv,time,os
# from bs4 import BeautifulSoup
# pages=[10]
#
#
# with open('E:/hackathon MDFM/marveldata.csv','a',encoding='utf8',newline='')as f_output:
#     csv_print=csv.writer(f_output)
#
#     file_is_empty=os.stat('E:/hackathon MDFM/marveldata.csv').st_size==0
#     if file_is_empty:
#         # csv_print.writerow(['name','id','align','eye','hair','sex','alive','appearance','year'])
#         csv_print.writerow(['Name','identity'])
#     for page in pages:
#         source=requests.get("http://marvel-ironman.surge.sh".format(page)).text
#         soup=BeautifulSoup(source,'lxml')
#         for characters in soup.select('.h2'):
#
#             name=characters.text
#             csv_print.writerow([name])
#
#         for characters in soup.select('.h4'):
#
#             identity=characters.text
#
#
#
#             csv_print.writerow([identity])




# html=urlopen("http://marvel-ironman.surge.sh")
# bsObj=BeautifulSoup(html,'lxml')
# table=bsObj.findAll()

#WEB SCRAPPING---------------

from bs4 import BeautifulSoup
import requests,time,os,csv
pages=[10,20]

with open('E://hackathon MDFM//indeed.csv','a',encoding='utf-8',newline='')as f_output:
    csv_print=csv.writer(f_output)

    file_is_empty=os.stat('E://hackathon MDFM//indeed.csv').st_size==0
    if file_is_empty:

        csv_print.writerow(['company','job title','location','summary','salary'])

    for page in pages:
        source=requests.get('https://www.indeed.co.in/jobs?q=python+developer&l=Bengaluru%2C+Karnataka&start={}'.format(page)).text
        soup=BeautifulSoup(source,'lxml')
        # jobs=soup.find(class_='result')
        # print(jobs.prettify())
        for jobs in soup.find_all(class_='result'):
            # print(jobs.prettify())
            # print("**************")
            try:
                company=jobs.span.text.strip()
            except Exception as e:
                company=None
            print(company)

            try:
                jobTitle=jobs.a.text.strip()
            except Exception as e:
                jobTitle=None
            print(jobTitle)

            try:
                location=jobs.find(text='Bengaluru, Karnataka').strip()
            except Exception as e:
                location=None
            print(location)

            try:
                summary=jobs.find('div',class_='summary').text.strip()
            except Exception as e:
                summary=None
            print(summary)

            try:
                salary=jobs.find('span',class_='salary no-wrap').text.strip()
            except Exception as e:
                salary=None
            print(salary)
            time.sleep(2)
            csv_print.writerow([company,jobTitle,location,summary,salary])

            print("********")

# jobTitle=jobs.a.text.strip()
# print(jobTitle)
# company=jobs.span.text.strip()
# print(company)
# location=jobs.find(text='Bengaluru, Karnataka').strip()
# print(location)
# summary=jobs.find('div',class_='summary').text.strip()
# print(summary)