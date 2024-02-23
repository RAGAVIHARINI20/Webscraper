from django.shortcuts import render
from bs4 import BeautifulSoup
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import io as StringIO
from django.core import serializers
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from .models import ProjectDetail,ContactDetail,ProjectOutputDetail
import json
from xlsxwriter.workbook import Workbook
import csv
import requests
import re
import pandas as pd
from sklearn.metrics import accuracy_score
from django.views.decorators.csrf import ensure_csrf_cookie
from autoscraper import AutoScraper

HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}

@ensure_csrf_cookie
def scrape(request):
  queryset = ProjectDetail.objects.all()
  context = {
    'queryset': queryset
  }
  return render(request, 'display.html', context)

#This function is to store the project and its url to the database
@ensure_csrf_cookie
def createProject(request):
  if request.method == 'POST':
    if request.POST.get('project') and request.POST.get('url'):
      post = ProjectDetail()
      post.project_name = request.POST.get('project')
      post.url = request.POST.get('url')
      post.save()

      return scrape(request)

  else:
    return render(request, 'form.html')

@ensure_csrf_cookie
def contactUs(request):
  if request.method == 'POST':
    if request.POST.get('name') and request.POST.get('email') and request.POST.get('message'):
      post = ContactDetail()
      post.name = request.POST.get('name')
      post.email = request.POST.get('email')
      post.message = request.POST.get('message')
      post.save()
      return HttpResponse('Your query is reported and the team will contact you soon!')


  else:
    return HttpResponse('Query not saved')

#This function is to export the result as excel/csv/JSON
@ensure_csrf_cookie
def exportResult(request):
  if request.method=='POST':
    data=json.loads(request.body)
    print(data)
    if data.get('format') and data.get('url'):
      format=data.get('format')
      url=data.get('url')
      textDict=data.get('elements')
      resHeader=textDict.keys()
      print(textDict.values())
      if format=='excel':
        results=scrapeWeb(url, list(textDict.values()))
        saveProject(request.get('url'), request.get('username'), request.get('project_name'), json.dumps(results,indent=2))
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = "attachment; filename=test.xlsx"
        book = Workbook(response, {'in_memory': True})
        sheet = book.add_worksheet('test')
        first_row = 0
        ordered_list=list(resHeader)
        for header in ordered_list:
          col = ordered_list.index(header)
          sheet.write(first_row, col, header)
        row = 1
        ordered_list=list(results[0].keys())
        for result in results:
          for _key, _value in result.items():
            col = ordered_list.index(_key)
            sheet.write(row, col, _value)
          row += 1
        book.close()
        calculateAccuarcy()
        return response
      elif format=='JSON':
        results=scrapeWeb(url, list(textDict.values()))
        data=json.dumps(results,indent=2)
        saveProject(request.get('url'),request.get('username'),request.get('project_name'),data)
        json_file = StringIO.StringIO()
        json_file.write(data)
        json_file.seek(0)
        wrapper = FileWrapper(json_file)
        response = HttpResponse(wrapper, content_type='application/json')
        response['Content-Disposition'] = 'attachement; filename=test.json'
        return response
      elif format=='csv':
        results=scrapeWeb(url, list(textDict.values()))
        saveProject(request.get('url'), request.get('username'), request.get('project_name'),
                    json.dumps(results, indent=2))
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="test.csv"'
        writer = csv.writer(response)
        header=list(results[0].keys())
        writer.writerow(header)
        header = list(results[0].keys())
        for result in results:
          result_list=[]
          for i in range(len(header)):
              result_list.append(result.get(header[i]))
          writer.writerow(result_list)
        return response
      else:
        return render(request,'scrape.html')
  else:
    return render(request, 'scrape.html')



# This function is the generic api is used to scrape the website
# url is the website url which is to be scraped
# textArray is the array which contains the example detail to be scraped and it will be selected by the user.
def scrapeWeb(url,textArray):
  # content=requests.get(url)
  # soup = BeautifulSoup(content.content, "html.parser")
  tagDetails=[]
  for i in range(len(textArray)):
    tagDetails.append(getPattern(textArray[i],url))
  scrapedResult=scrapeWithPattern(tagDetails,url)
  return scrapedResult

# This function is used to finding the patterns to extract the other data which can be scraped.
def getPattern(text,url):
  content = requests.get(url,headers=HEADERS)
  soup = BeautifulSoup(content.content, "html.parser")
  tagDict={}
  for tag in soup.find_all():
    if tag.text.strip()==text.strip():
     tagDict['text']=text.strip()
     if " " in str(tag):
       tagname = str(tag).split()[0]
       tagDict["tag"] = re.split('<', tagname, 1)[1]
     else:
       str1="<"
       str2=">"
       idx1 = str(tag).index(str1)
       idx2 = str(tag).index(str2)
       res = str(tag)[idx1 + len(str1) + 1: idx2]
       tagDict["tag"] =res
     if "class" in str(tag):
       x = re.findall("class=.*\"", str(tag).strip())
       classname = re.findall('"([^"]*)"', x[0])
       tagDict['class'] = classname[0]
     else:
       tagDict['class']=" "

     break

  return tagDict


def scrapeWithPattern(tagdetails,url):
  content = requests.get(url,headers=HEADERS)
  soup = BeautifulSoup(content.content, "html.parser")
  tagList=[]
  scrapedList = []
  for i in range(len(tagdetails)):
    tagname=tagdetails[i].get("tag")
    tagclass=tagdetails[i].get("class")
    tagList.append(soup.find_all(tagname,tagclass))
  if len(tagList)>0:
    listLen=[]
    for i in tagList:
      listLen.append(len(i))
    print(listLen)
    minNum=max(listLen)
    # print(minNum)
    # print(tagList)

    for i in range(len(tagList)):
      if len(tagList[i])!=minNum:
        n=minNum-len(tagList[i])
        for j in range(n):
          tagList[i].append(' ')

    print(tagList)

    for i in range(minNum):
      scrapedict={}
      for j in range(len(tagList)):
        # print(tagList[j][i])
        str1=BeautifulSoup(str(tagList[j][i]),'html.parser')
        # print(str1)
        scrapedict[str(j)]=str1.text.strip()
        # print(scrapedList)
      if len(scrapedict)>0:
        scrapedList.append(scrapedict)
      # print(scrapedList)
  return scrapedList

def getTagName(htmlLine):
  x= str(htmlLine).strip()
  x=x.split()
  if "<" in x[0]:
    return re.split('<',x[0],1)[1]
  else:
    return ""

def getClassName(htmlLine):
  if "class" in htmlLine:
    x = re.findall("class=.*\"", str(htmlLine).strip())
    classname = re.findall('"([^"]*)"', x[0])
    return classname


def calculateAccuarcy():
  df=pd.read_excel(r'C:\Users\welcome\Downloads\test (10).xlsx')
  df1=pd.read_excel(r'C:\Users\welcome\Downloads\test (9).xlsx')
  accuracy_score_1=accuracy_score(df['0'].values,df1["0"].values)
  # precision_score_1=precision_score(df['0'].values,df1["0"].values)
  print(accuracy_score_1)
  # print("Precision:"+precision_score_1)


def exportProject(request):
  # response=ProjectOutputDetail.objects.get(username=request.username)
  data = serializers.serialize('json', ProjectOutputDetail.objects.get(username=request.username))
  return HttpResponse(data, content_type='application/json')



def importProject(username,url,project_name,project_output):
  post = ProjectOutputDetail()
  post.username=username
  post.project_output=project_output
  post.project_name = project_name
  post.url = url
  post.save()

def saveProject(username,url,project_name,project_output):
  post = ProjectOutputDetail()
  post.username=username
  post.project_output=project_output
  post.project_name = project_name
  post.url = url
  post.save()



