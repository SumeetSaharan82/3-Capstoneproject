import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from google import genai
from google.genai import types

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

load_dotenv()

# def load_config (config_path: str = "config.json") -> dict:
#     """
#     Load the configuration from a JSON file.

#     Args:
#         config_path (str): Path to the configuration file.

#     Returns:
#         dict: The loaded configuration.
#     """
with open("config.json", "r") as f:
        CONFIG = json.load(f)
  

# Open AI function
def run_openai (message):
    client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=CONFIG["openai"]["model"],
        messages=message,
        temperature=CONFIG["openai"].get("temperature", 0.7),
        max_tokens=CONFIG["openai"].get("max_tokens", 150),
        top_p=CONFIG["openai"].get("top_p", 1.0)

    )
    return response.choices[0].message.content.strip()

# Gemini AI function
def run_gemini (message):
    client = genai.Client()
    config = types.GenerateContentConfig(
        temperature=CONFIG["gemini"].get("temperature", 0.7),
        max_output_tokens=CONFIG["gemini"].get("max_output_tokens", 150),
        top_p=CONFIG["gemini"].get("top_p", 1.0)

    
    )
    response = client.models.generate_content(
        model=CONFIG["gemini"]["model"],
        contents=message,
        config=config
    )
    return response.text.strip()

# Router Function
def run_llm (history):
     provider = CONFIG.get("provider", "openai").lower()
     if provider == "openai":
          return run_openai(history)
     elif provider == "gemini":
          conversation = "\n".join([f"{msg['role']}: {msg['content']}" for msg in history])
          return run_gemini(conversation)
     else:
          raise ValueError(f"Unsupported provider: {provider}")