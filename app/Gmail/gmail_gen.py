import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL = os.getenv("GEMINI_MODEL","gemini-3,5-flash")

def generate_email_with_gemini(command):
    if not API_KEY:
        raise RuntimeError("gemini_api_key is missing.")

    prompt = f"""
  You are a professional Gmail email writing assistant.

  Conver the user's voice command into a professional email.

  rules:
  - Do not copy the command literally.
  - Do not explain anything.
  - Do not invent names, dates, prices, comapnies, attachments, or facts.
  - Keep the email natural and concise.
  - Include an appropriate greeting and closing.
  
