import requests

def req():
    name = "Daniel"
    message = "I want to follow you to your country"

r = requests.get("https://maker.ifttt.com/trigger/Message/with/key/2Kud4E0CUmxZX3JAbrzbl",{"value1":"name","value2":"message"})
print(r)

req()

