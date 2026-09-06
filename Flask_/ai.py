import google.generativeai as genai

# Paste your API key here
genai.configure(api_key="AIzaSyAE2OvDN4fn86cwJpi5bpO9NvgmvS0V4Is")

# Choose model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate response
response = model.generate_content("Explain recursion in simple words")

print(response.text)