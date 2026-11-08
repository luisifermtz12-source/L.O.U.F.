import speech_recognition as sr
import pyttsx3


voz = pyttsx3.init()
voz.setProperty('rate', 170)

def hablar(mensaje):
    print("L.O.U.F.:", mensaje)
    voz.say(mensaje)
    voz.runAndWait()

reconocedor = sr.Recognizer()

with sr.Microphone() as fuente:
    print("L.O.U.F. está iniciando...")
    reconocedor.adjust_for_ambient_noise(fuente)

    hablar("De vuelta a casa jefa. ¿Que tiene pensado para hoy?.")

    print("La estoy escuchando...")
    audio = reconocedor.listen(fuente)

    try:
        texto = reconocedor.recognize_google(
            audio, language="es-MX"
        )

        print("Tú:", texto)
        hablar("He entendido lo que dijo: " + texto)

    except sr.UnknownValueError:
        hablar("No pude entenderle. ¿Puede repetirlo jefa?")

    except sr.RequestError:
        hablar("Tengo problemas de conexión.")









# print("Iniciando L.O.U.F...")
#reconocedor = sr.Recognizer()
# with sr.Microphone() as fuente:
#       print("L.O.U.F. esta escuchando...")
#       reconocedor.adjust_for_ambient_noise(fuente)
#       audio = reconocedor.listen(fuente)

#       print("Procesando tu voz...")
#       try:
#             texto = reconocedor.recognize_google(audio, language="es-MX")
#             print("Has ducho:", texto)
            
#       except sr.UnknownValueError:
#             print("No pude entener lo que dijo jefa.")

#       except sr.RequestError:
#             print("Error de conexion con el servicio de reconocimiento.")
      
# # print("Activando microfono...")

# def escuchar():
#      with sr.Microphone() as microfono:
#          print("La estoy escuchando jefa...")
#          audio = reconocedor.listen(microfono)
#          print("Audio recibido.")
        
#      try: 
#              texto = reconocedor.recognice_google (audio, lenguaje="es-MX")
#              print("Tu dijiste:", texto)
#      except Exception as e:
#              print("No pude reconocer su voz jefa.")
# escuchar()

 