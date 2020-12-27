import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
import unicodedata
import io
import re



import urllib.request, json 



global Data
global state_data
global district_data
global world_data

with urllib.request.urlopen("https://api.covid19india.org/data.json") as url:
    Data = json.loads(url.read().decode())



with urllib.request.urlopen("https://api.covid19india.org/v4/timeseries.json") as url:
    state_data = json.loads(url.read().decode())



with urllib.request.urlopen("https://coronavirus-19-api.herokuapp.com/countries") as url:
    world_data = json.loads(url.read().decode())
    #print(world_data)
    


with urllib.request.urlopen("https://api.covid19india.org/state_district_wise.json") as url:
    district_data = json.loads(url.read().decode())

#india total stats
india_daily_Data=Data['cases_time_series']
#print(india_daily_Data)
def india_total():

  india_total=Data['cases_time_series'][-1]
  india_total_confirmed=india_total['totalconfirmed']
  india_total_deceased=india_total['totaldeceased']
  india_total_recovery=india_total['totalrecovered']
  india_recovery_ratio=(int(india_total_recovery)/int(india_total_confirmed))*100

  print("India Total Confirmed: "+ india_total_confirmed)
  print("India Total Deceased: "+ india_total_deceased)
  print("India Total Recovered: "+ india_total_recovery)

  print("India Recovery Ratio: "+ str(india_recovery_ratio))


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



    
     


#india statewise


india_daily_data=Data['statewise']
dict_state_code={}
for val in india_daily_data:
    state_Data=val
    dict_state_code[state_Data['state']]=state_Data['statecode']




def india_statewise(state_name):


 state_code=dict_state_code[state_name]
 curr_date=(list(state_data[state_code]['dates'].keys())[-2])
 
 state_total=state_data[state_code]['dates'][curr_date]
 state_total_confirmed=state_total['total']['confirmed']
 state_total_deceased=state_total['total']['deceased']
 state_total_recovery=state_total['total']['recovered']
 state_recovery_ratio=(int(state_total_recovery)/int(state_total_confirmed))*100

 print(state_name + " Total Confirmed: "+ str(state_total_confirmed))
 print(state_name +" Total Deceased: "+ str(state_total_deceased))
 print(state_name +" Total Recovered: "+ str(state_total_recovery))

 print(state_name +" Recovery Ratio: "+ str(state_recovery_ratio))


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
 state_wise_data=district_data[State_Name]
 print()
 #district_name="Sawai Madhopur"
 for state in state_wise_data:
    if district_name in state_wise_data['districtData']:
        print(district_name,end='\t\t')
        print(state_wise_data['districtData'][district_name]["confirmed"],end='\t')
        print(state_wise_data['districtData'][district_name]["deceased"],end='\t')
        print(state_wise_data['districtData'][district_name]["recovered"])
        break

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
 for countries in world_data:
    if countries["country"]==country_name:
        print(country_name + " Total Confirmed Cases:  " + str(countries["cases"]))
        print(country_name + " Total Deceased Cases:  " + str(countries["deaths"]))
        print(country_name + " Total Recovered Cases:  " + str(countries["recovered"]))
        print(country_name + " Total Active Cases:  " + str(countries["active"]))
        print(country_name + " Recovery Ratio:  " + str(int(countries["recovered"])/int(countries["cases"])*100))




'''country_wise("India")
world_Data()
district_wise("Jaipur")
state_districewise("Tamil Nadu")
state_cases_bw_dates("Sikkim","2020-08-12","2020-08-30");
state_datewise("Rajasthan","2020-08-12");
india_statewise("Gujarat")
india_cases_bw_two_dates("2020-08-12","2020-08-30")
india_cases_single_date("2020-08-12")
india_total()'''


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


pd.set_option('max_colwidth', 1000)  # Increase column width

data = pd.read_csv('Covid_QA.csv',  encoding='latin-1')
module = hub.load('universal-sentence-encoder-qa_3')

#print(preprocess_sentences(data.Answers)).

response_encodings = module.signatures['response_encoder'](
        input=tf.constant(preprocess_sentences(data.Answers)),
        context=tf.constant(preprocess_sentences(data.Questions)))['outputs']


test_questions = [
"number of cases in tamil nadu",
"number of cases in iraq",
"covid cases in kenya",
"how many total covid cases in world",
]

# Create encodings for test questions
question_encodings = module.signatures['question_encoder'](
    tf.constant(preprocess_sentences(test_questions))
)['outputs']

# Get the responses
test_responses = data.Answers[np.argmax(np.inner(question_encodings, response_encodings), axis=1)]

pd.DataFrame({'Test Questions': test_questions, 'Test Responses':test_responses})
print(test_responses)
for i in test_responses:
    
    eval(i)
