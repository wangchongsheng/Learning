import win32com.client

speaker = win32com.client.Dispatch("SAPI.APVOICE")
speaker.Speak("啦啦啦啦啦")