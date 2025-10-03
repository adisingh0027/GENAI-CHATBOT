from google import genai

client = genai.Client(api_key="AIzaSyBqmcOUimDaB6-CmCGwlY9AoqJlEinh7-Y")



# List available models
for model in client.models.list():  # Pager object is iterable
    print(model.name)
