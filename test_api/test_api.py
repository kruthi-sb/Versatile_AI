import os
import google.generativeai as genai

key = os.getenv('gemini_pro')

# to see available gemini models:
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

txt_model = genai.GenerativeModel('gemini-pro')
response = txt_model.generate_content("give project ideas for generative ai")

print(response.text)

# for vision model:
import PIL.Image as Image

img = Image.open('C:\\Users\\kruth\\OneDrive\\Desktop\\Versatile_AI\\test_api\\sample_img.png')
img_model = genai.GenerativeModel('gemini-pro-vision')
response = img_model.generate_content(["Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.", img], stream=True)
response.resolve()
print(response.text)






