"""
translator functions
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION='2019-04-03'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    """
    translate english to french
    """
    try:
        res = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        french_text = res['translations'][0]['translation']
    except:
        french_text = ''
    return french_text

def french_to_english(french_text):
    """
    translate french to english
    """

    try:
        res = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        english_text = res['translations'][0]['translation']
    except:
        english_text=''
        
    return english_text
