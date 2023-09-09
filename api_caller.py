import requests
def caloric_intake(age,weight,height,gender,activity_level,goal):


    url = "https://health-calculator-api.p.rapidapi.com/dcn"

    querystring = {"age":age,"weight":weight,"height":height,"gender":gender,"activity_level":activity_level,"goal":goal,"equation":"mifflin"}

    headers = {
        "X-RapidAPI-Key": "50bc718d42mshab627403e178300p1cec14jsn7b5f62c565f8",
        "X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()
#caloric_intake(27,104,181,"male","moderately_active","weight_loss")