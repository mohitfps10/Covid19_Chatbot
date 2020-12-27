import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
import unicodedata
import io
import re



import urllib.request, json 





def func1():
 global Data
 global state_data
 global district_data
 global world_data
 global dict_state_code
 with urllib.request.urlopen("https://api.covid19india.org/data.json") as url:
    Data = json.loads(url.read().decode())
 
 
 
 with urllib.request.urlopen("https://api.covid19india.org/v4/timeseries.json") as url:
     state_data = json.loads(url.read().decode())
 
 
 
 with urllib.request.urlopen("https://coronavirus-19-api.herokuapp.com/countries") as url:
     world_data = json.loads(url.read().decode())
     #print(world_data)
     
 
 
 with urllib.request.urlopen("https://api.covid19india.org/state_district_wise.json") as url:
     district_data = json.loads(url.read().decode())

  #india statewise
 
 
 india_daily_data=Data['statewise']
 dict_state_code={}
 for val in india_daily_data:
     state_Data=val
     dict_state_code[state_Data['state']]=state_Data['statecode']
 
 #india total stats
 india_daily_Data=Data['cases_time_series']
 #print(india_daily_Data)
def india_total():
 
   india_total=Data['cases_time_series'][-1]
   india_total_confirmed=india_total['totalconfirmed']
   india_total_deceased=india_total['totaldeceased']
   india_total_recovery=india_total['totalrecovered']
   india_recovery_ratio=(int(india_total_recovery)/int(india_total_confirmed))*100

   res=[]
   res.append("India Total Confirmed: "+ str(india_total_confirmed))
   res.append("India Total Deceased: "+ str(india_total_deceased))
   res.append("India Total Recovered: "+ str(india_total_recovery))
 
   res.append("India Recovery Ratio: "+ str(india_recovery_ratio))
 
   return res
 
 #india datewise
def india_cases_single_date(Date_to_be_calculated):
 
   #Date_to_be_calculated="2020-10-28"
   print(india_daily_Data)
   
   for day in india_daily_Data:
     if(day['dateymd']==Date_to_be_calculated):
         
       print("India Total Confirmed on " + Date_to_be_calculated+ " :  "+ day['dailyconfirmed'])
       print("India Total Deceased on " + Date_to_be_calculated+ " :  "+ day['dailydeceased'])
       print("India Total Recovered on " + Date_to_be_calculated+ " :  "+ day['dailyrecovered'])
 
    
 #india between two dates
 
 
def india_cases_bw_two_dates(india_start_date,india_end_date):
     #india_start_date="2020-06-19"
     #india_end_date="2020-09-25"
     confirmed_count1=0
     deceased_count1=0
     recovered_count1=0
     confirmed_count2=0
     deceased_count2=0
     recovered_count2=0
     for day in india_daily_Data:
 
      
       if(day['dateymd']==india_start_date):
         
         confirmed_count1=int(day['totalconfirmed'])
         deceased_count1=int(day['totaldeceased'])
         recovered_count1=int(day['totalrecovered'])
         
 
       if(day['dateymd']==india_end_date):
         
         confirmed_count2=int(day['totalconfirmed'])
         deceased_count2=int(day['totaldeceased'])
         recovered_count2=int(day['totalrecovered'])
 
 
     print("India Total Confirmed bw " + india_end_date+ " and "+ india_start_date + " is:  " + str(confirmed_count2-confirmed_count1))
     print("India Total Deceased bw " + india_end_date+ " and "+ india_start_date + " is:  " + str(deceased_count2-deceased_count1))
     print("India Total Recovered bw " + india_end_date+ " and "+ india_start_date + " is:  " + str(recovered_count2-recovered_count1))
 
 
 
     
      
 
 

 
 
 
 
def india_statewise(state_name):
 
 
  state_code=dict_state_code[state_name]
  curr_date=(list(state_data[state_code]['dates'].keys())[-2])
  
  state_total=state_data[state_code]['dates'][curr_date]
  state_total_confirmed=state_total['total']['confirmed']
  state_total_deceased=state_total['total']['deceased']
  state_total_recovery=state_total['total']['recovered']
  state_recovery_ratio=(int(state_total_recovery)/int(state_total_confirmed))*100
  res=[]

  res.append(state_name + " Total Confirmed: "+ str(state_total_confirmed))
  res.append(state_name +" Total Deceased: "+ str(state_total_deceased))
  res.append(state_name +" Total Recovered: "+ str(state_total_recovery))
 
  res.append(state_name +" Recovery Ratio: "+ str(state_recovery_ratio))
 
  return res
#state datewise
 
 
def state_datewise(state_name,Date_to_be_calculated):
 
  #Date_to_be_calculated="2020-07-30"
  state_code=dict_state_code[state_name]
  state_daily_data=state_data[state_code]['dates'][Date_to_be_calculated]
 
  print(state_name +" Total Confirmed on " + Date_to_be_calculated+ " :  "+ str(state_daily_data['delta']['confirmed']))
  print(state_name +" Total Deceased on " + Date_to_be_calculated+ " :  "+ str(state_daily_data['delta']['deceased']))
  print(state_name +" Total Recovered on " + Date_to_be_calculated+ " :  "+ str(state_daily_data['delta']['recovered']))
 
    
#state between two dates

def state_cases_bw_dates(state_name,state_start_date,state_end_date):
 
 
  #state_start_date="2020-06-19"
  #state_end_date="2020-09-25"
  
  state_code=dict_state_code[state_name]
  confirmed_count1=0
  deceased_count1=0
  recovered_count1=0
  confirmed_count2=0
  deceased_count2=0
  recovered_count2=0
  state_daily_data_datewise=state_data[state_code]['dates']
  
  confirmed_count1=int(state_daily_data_datewise[state_start_date]['total']['confirmed'])
  deceased_count1=int(state_daily_data_datewise[state_start_date]['total']['deceased'])
  recovered_count1=int(state_daily_data_datewise[state_start_date]['total']['recovered'])
  
  confirmed_count2=int(state_daily_data_datewise[state_end_date]['total']['confirmed'])
  deceased_count2=int(state_daily_data_datewise[state_end_date]['total']['deceased'])
  recovered_count2=int(state_daily_data_datewise[state_end_date]['total']['recovered'])
 
 
  print(state_name +" Total Confirmed bw " + state_end_date+ " and "+ state_start_date + " is:  " + str(confirmed_count2-confirmed_count1))
  print(state_name +" Total Deceased bw " + state_end_date+ " and "+ state_start_date + " is:  " + str(deceased_count2-deceased_count1))
  print(state_name +" Total Recovered bw " + state_end_date+ " and "+ state_start_date + " is:  " + str(recovered_count2-recovered_count1))
      
 
#State Districe Wise data
def state_districewise(State_Name):
 
 
 
  #State_Name="Rajasthan"
  state_district_wise_data=district_data[State_Name]['districtData']
 
  print(state_district_wise_data.keys())
 
  for districts in state_district_wise_data:
     print(districts[0:min(len(districts),6)],end='\t\t')
     print(state_district_wise_data[districts]["confirmed"],end='\t')
     print(state_district_wise_data[districts]["deceased"],end='\t')
     print(state_district_wise_data[districts]["recovered"])
 
 
 #district name wise
 
def district_wise(district_name):
  #state_wise_data=district_data[State_Name]
  #print()
  #district_name="Sawai Madhopur"
  res=[]
  for state_name in district_data:
   
     if district_name in district_data[state_name]['districtData']:
         res.append(district_name)
         res.append((district_name + " Total Confirmed: "+ str( district_data[state_name]['districtData'][district_name]["confirmed"])))
         res.append((district_name + " Total Deceased: "+ str( district_data[state_name]['districtData'][district_name]["deceased"])))
         res.append((district_name + " Total Recovered: "+ str( district_data[state_name]['districtData'][district_name]["recovered"])))
         
         break
  return res
#world data
 
def world_Data():
 
 
  
  
 
  world_info= world_data[0]
  print("World Total Confirmed Cases:  " + str(world_info["cases"]))
  print("World Total Deceased Cases:  " + str(world_info["deaths"]))
  print("World Total Recovered Cases:  " + str(world_info["recovered"]))
  print("World Total Active Cases:  " + str(world_info["active"]))
 
 
  print()
 
 
 #country data
 
def country_wise(country_name):
 
  #country_name="USA"
 
  print(country_name)
  res=[]
  for countries in world_data:
     if countries["country"]==country_name:
         res.append(country_name + " Total Confirmed Cases:  " + str(countries["cases"]))
         res.append(country_name + " Total Deceased Cases:  " + str(countries["deaths"]))
         res.append(country_name + " Total Recovered Cases:  " + str(countries["recovered"]))
         res.append(country_name + " Total Active Cases:  " + str(countries["active"]))
         res.append(country_name + " Recovery Ratio:  " + str(int(countries["recovered"])/int(countries["cases"])*100))
 
  return res
  
def unicode_to_ascii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s))

def preprocess_sentences(w):
      l=[]
      for i in w:
          l.append(preprocess_sentence(i))
      return l
  
def preprocess_sentence(w):
   w = unicode_to_ascii(w.lower().strip())
   #separating punctuation
   w = re.sub(r"([?.!,¿])", r" \1 ", w)
   w = re.sub(r'[" "]+', " ", w)
   # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
   w = re.sub(r"[^a-zA-Z?.!,¿]+", " ", w)
   w = w.rstrip().strip()
   w = '<start> ' + w + ' <end>'
   return w
  
def func2():
 
 global data
 pd.set_option('max_colwidth', 1000)  # Increase column width
 data = pd.read_csv('Covid_QA.csv',  encoding='latin-1')
 global module
 module = hub.load("C:\\Users\\Mohit\\Desktop\\universal-sentence-encoder-qa_3")
 
 #print(preprocess_sentences(data.Answers)).
 global response_encodings
 response_encodings = module.signatures['response_encoder'](
        input=tf.constant(preprocess_sentences(data.Answers)),
        context=tf.constant(preprocess_sentences(data.Questions)))['outputs']
  



 
 
 
 
from flask import Flask, render_template, request
import pprint 

app = Flask(__name__)



@app.route('/')
def index():
   func1()
   func2()
   return render_template("index2.html")



def solve_query(question): 

   
   

 global flag   
 test_questions = [
    question
  ]
  
 # Create encodings for test questions
 question_encodings = module.signatures['question_encoder'](
      tf.constant(preprocess_sentences(test_questions))
  )['outputs']
  
 # Get the responses
 test_responses = data.Answers[np.argmax(np.inner(question_encodings, response_encodings), axis=1)]
  
 pd.DataFrame({'Test Questions': test_questions, 'Test Responses':test_responses})
 print(test_responses)

 l=[]
 l.append("india_")
 l.append("country_")
 l.append("world_")
 l.append("district_")
 
 
 l1=[]
 for i in test_responses:
      
      check1=i[0:6]
      check2=i[0:8]
      check3=i[0:9]


      if(check1 in l or check2 in l or check3 in l):
          flag=0
          return (eval(i))
      flag=1
      l1.append(i)
 return l1
     





@app.route('/result1',methods = ['GET','POST'])

def result1():

  return render_template("index.html")


@app.route('/result',methods = ['GET','POST'])

def result():
  
    if request.method == 'POST':
      question = request.form["Channel Id"]
      details=[]
      flag=0
     
      details=solve_query(question)
      quotes=["Stay Home...Stay Safe..!!!","The Threat is The Virus,Not the People","Stay Home...Stay Safe..!!!","Stay Home...Stay Safe..!!!","Stay Home...Stay Safe..!!!"]
      p=0
      if(flag==0):
       while(len(details)<5):
          details.append(quotes[p])
          p+=1
       return render_template("pass.html",subscriber_count = details[0],channel_name=details[1], channel_created_date=details[2],video_count=details[3],view_count=details[4])
      
    
if __name__ == "__main__": 

 app.run(debug = True)
  
  
