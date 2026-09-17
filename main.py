import os
import base64
import threading
import textwrap
from datetime import datetime

import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.image import Image as KivyImage
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.metrics import dp

API_KEY = (
    "AQ.Ab8RN6JiKQwzdeInYSe6SD"
    + "i7QCI4HWN_kvOELwOjEPGQHJDZkg"
)

# Endpoint oficial de Gemini Flash
URL_TEXTO = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

def _pedir_respuesta(self):
    try:
        contenidos = [
            {"role": "user" if m["role"] == "user" else "model",
             "parts": [{"text": m["content"]}]}
            for m in self.historial
        ]
        payload = {
            "contents": contenidos,
            "systemInstruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        }
        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": API_KEY
        }
        
        # Enviar con headers explícitos
        r = requests.post(URL_TEXTO, json=payload, headers=headers, timeout=30)
        data = r.json()

        # Si la API reporta un fallo, mostramos el mensaje real en vez de que truene Python
        if "error" in data:
            respuesta = f"(Error API: {data['error'].get('message', 'desconocido')})"
        elif "candidates" in data and len(data["candidates"]) > 0:
            respuesta = data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            respuesta = "(Gemini no devolvió texto de respuesta)"

    except Exception as e:
        respuesta = f"(No pude hablar con Gemini: {e})"

    self.historial.append({"role": "assistant", "content": respuesta})
    Clock.schedule_once(lambda dt: self._agregar_burbuja(respuesta, False), 0)
