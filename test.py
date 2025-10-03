from google import genai

client = genai.Client(api_key="GOOGLE_API_KEY")



# List available models
for model in client.models.list():  # Pager object is iterable
    print(model.name)

