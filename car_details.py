key = "AIzaSyD3kNDlEpRsF-Mb14oQfZNaqPF6ECnvKrA"

import pathlib
import textwrap

from googlesearch import search
import google.generativeai as genai

genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def to_markdown(text):
    
    return text

def others(text):
    tex =f""" you are in a conversational bot on a car website here is a user text -> {text} 
    answer him in less then 100 words
    """
    
    response = chat.send_message(tex)
    a = response.text
    return a

def photos_get():
    tex =f"""see this conversation {chat.history}  if you did'nt find any car just return None else only give the name of cars"""
    
    response = model.generate_content(tex, safety_settings={'HARASSMENT':'block_none'})
    if  "None" in response.text:
        print("none")
        return "None",chat.history
    else:
        photos_link = search_google(response.text)
        return photos_link ,chat.history



def search_google(query):
    p = f"Photos of {query} "
    return list(search(p, num_results=5))



