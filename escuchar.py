import speech_recognition as sr
import pyttsx3


voz = pyttsx3.init()
voz.setProperty('rate', 170)

def hablar(mensaje):
    print("L.O.U.F.:", mensaje)
    voz.say(mensaje)
    voz.runAndWait()

reconocedor = sr.Recognizer()

hablar("Esta de vuelta en casa jefa. Puedo escucharla continuamente.")

while True:
    try: 
      with sr.Microphone() as fuente:
       print("\nL.O.U.F. está escuchando...")

       reconocedor.adjust_for_ambient_noise(
          fuente, duration=0.5
       )
       audio = reconocedor.listen(
          fuente, phrase_time_limit=8
          )
       texto = reconocedor.recognize_google(
          audio, language="es-MX"
       ).lower()
       print("Tu:", texto)
       if "adios" in texto or "apagate" in texto:
          hablar("Hasta pronto jefa. Cerrando mis sistemas.")
          break

       hablar("He escuchado lo que dice:" + texto)

    except sr.UnknownValueError:
       hablar("No eh podido conectarme al servicio de reconocimiento.")
       continue
    
    except sr.RequestError as error:
       print("Error de conexion:", error)
       continue

    except KeyboardInterrupt:
     print("\nL.O.U.F. detenido.")
     break
   




 