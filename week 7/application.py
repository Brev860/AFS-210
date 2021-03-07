
import pandas as pd
import plotly.express as px
 
covid_data= pd.read_csv('https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports/03-06-2021.csv')
us_data = covid_data[covid_data['Country_Region']=='US'].drop(['Country_Region','Lat', 'Long_','Last_Update','FIPS','Incident_Rate','Total_Test_Results','People_Hospitalized','Case_Fatality_Ratio','UID','ISO3','Testing_Rate','Hospitalization_Rate'], axis=1)
us_data = us_data[us_data.sum(axis = 1) > 0]
 
us_data = us_data.groupby(['Province_State'])['Recovered'].sum().reset_index()
us_data_death = us_data[us_data['Recovered'] > 0]
state_fig = px.bar(us_data_death, x='Province_State', y='Recovered', title='State wise Recovery cases of COVID-19 in USA', text='Recovered')

state_fig.show()
