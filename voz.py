import pyttsx3

#Voy a iniciar el motor de la voz 
motor = pyttsx3.init()

#Quiero obtener las voces que estan disponibles 
voces = motor.getProperty('voices')

# print("VOCES DISPONIBLES:")
# for i, voz in enumerate(voces):
    # print(i, voz.name)
for voz in voces:
        if "sabina" in voz.name.lower():
            motor.setProperty('voice', voz.id)
            break

    #Acomodaremos la velocidad y el volumen
motor.setProperty('rate', 165)
motor.setProperty('volume', 5.0)

    # #Las primeras pruebas de la voz
    # motor.say("De vuelta a casa jefa. Iniciando los sistemas.")
    # motor.runAndWait()

    #Funcion para hablar
def hablar(texto):
    motor.say(texto)
    motor.runAndWait()


  #Segunda prueba de voz
hablar ("De vuelta a casa jefa, Iniciando los sistemas. Todos mis sistemas estan funcionando correctamente.")
