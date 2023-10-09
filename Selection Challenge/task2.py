#Task2: API Automated test using
import requests
from jsonschema import validate

#This the schema of the response json from the API
schema={
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "topLevelDomain": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "alpha2Code": {
      "type": "string"
    },
    "alpha3Code": {
      "type": "string"
    },
    "callingCodes": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "capital": {
      "type": "string"
    },
    "altSpellings": {
      "type": "array",
      "items": [
        {
          "type": "string"
        },
        {
          "type": "string"
        },
        {
          "type": "string"
        }
      ]
    },
    "region": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "topLevelDomain",
    "alpha2Code",
    "alpha3Code",
    "callingCodes",
    "capital",
    "altSpellings",
    "region"
  ]
}

#We call the API for the US and validate the response has the correct schema with the validate function from the jsonschema library
PARAMS = {'access_key':'9c6b1761dc407d17aa15ad1e5290d159', 'fullText':'true'}
url = "http://api.countrylayer.com/v2/name/United States of America"
response = requests.get(url = url, params = PARAMS)
response_json = response.json()
validate(instance={"name" : "United States of America", "topLevelDomain" : ['.us'],"alpha2Code":"US","alpha3Code":"USA","callingCodes":['1'],"capital":"Washington, D.C.","altSpellings":['US', 'USA', 'United States of America'],"region":"Americas"}, schema=schema)

#We do the same for Germany
PARAMS = {'access_key':'9c6b1761dc407d17aa15ad1e5290d159', 'fullText':'true'}
url = "http://api.countrylayer.com/v2/name/Germany"
response = requests.get(url = url, params = PARAMS)
response_json = response.json()
validate(instance={"name" : "Germany", "topLevelDomain" : ['.de'],"alpha2Code":"DE","alpha3Code":"DEU","callingCodes":['49'],"capital":"Berlin","altSpellings":['DE', 'Federal Republic of Germany', 'Bundesrepublik Deutschland'],"region":"Europe"}, schema=schema)

#Lastly, we do it for the UK
PARAMS = {'access_key':'9c6b1761dc407d17aa15ad1e5290d159', 'fullText':'true'}
url = "https://api.countrylayer.com/v2/name/United Kingdom of Great Britain and Northern Ireland"
response = requests.get(url = url, params = PARAMS)
response_json = response.json()
validate(instance={"name" : "United Kingdom of Great Britain and Northern Ireland", "topLevelDomain" : ['.uk'],"alpha2Code":"GB","alpha3Code":"GBR","callingCodes":['44'],"capital":"London","altSpellings":['GB', 'UK', 'Great Britain'],"region":"Europe"}, schema=schema)

#Now, we do it for a fake country, expecting an error
PARAMS = {'access_key':'9c6b1761dc407d17aa15ad1e5290d159', 'fullText':'true'}
url = "https://api.countrylayer.com/v2/name/Lotharingia"
response = requests.get(url = url, params = PARAMS)
response_json = response.json()
validate(instance={"name" : "Lotharingia", "topLevelDomain" : ['.lo'],"alpha2Code":"KL","alpha3Code":"KOL","callingCodes":['99'],"capital":"Aachen","altSpellings":['KOL', 'Middle Francia', 'Austrasia'],"region":"Europe"}, schema=schema)

#Now, we will test thye POST function of the API

#This is the schema for the json given as an example
new_schema={
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "alpha2_code": {
      "type": "string"
    },
    "alpha3_code": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "alpha2_code",
    "alpha3_code"
  ]
}

#Here, we validate the json given follows the schema required and make the POST request to the API 
example_json= {'name': 'Test Country', 'alpha2_code': 'TC', 'alpha3_code': 'TCY'}
PARAMS = {'access_key':'9c6b1761dc407d17aa15ad1e5290d159'}
url = 'https://api.countrylayer.com/v2/addcountry'
newcountry = {'country': example_json}
validate(instance={"name" : "Test Country", "alpha2_code" : "TC","alpha3_code":"TCY"}, schema=new_schema)
x = requests.post(url, params = PARAMS, json = newcountry)

#This is the text from the response from the POST with the response codes. This can be used for further validations
print(x.text)