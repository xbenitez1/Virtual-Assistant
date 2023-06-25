import pyttsx4
import speech_recognition as sr
import pywhatkit
import pyjokes
import webbrowser
import datetime
import wikipedia


# Voice recognition to text
def transform_audio_to_text():
    # Save voice in a variable
    voice = sr.Recognizer()

    # Microphone configuration
    with sr.Microphone() as origin:

        # Time hold
        voice.pause_threshold = 0.8

        # inform Star Microphone
        print("YOU CAN SPEEK")

        # Save Audio
        voice_audio = voice.listen(origin)

        # Check text
        try:
            # Find in google
            google_check = voice.recognize_google(voice_audio, language="es-mx")

            # Text check
            print("Dijiste: " + google_check)

            return google_check

        # Posible errors
        except sr.UnknownValueError:

            # Check mistake
            print("Sorry i dont understand")

            # Return error
            return "TRY AGAIN"

        except sr.RequestError:

            # Check mistake
            print("Sorry i dont understand")

            # Return error
            return "TRY AGAIN"

        # unexpected error:
        except:
            # Check mistake
            print("Sorry i dont understand")

            # Return error
            return "SOMETHING GO RONG"


# Voice Assitant respond
def voice_assitant(text_assitant):
    id1_spanish = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
    id2_english = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

    # Start pyttsx4
    engine = pyttsx4.init()
    engine.setProperty("voice", id1_spanish)

    # Assitant tolk
    engine.say(text_assitant)
    engine.runAndWait()


# Check voice option and intall
def check_option_voices():
    engine = pyttsx4.init()
    for voice in engine.getProperty("voices"):
        print(voice)


# Inform today
def today_data():
    # Variable day
    day = datetime.date.today()

    # Week day
    week_day = day.weekday()

    # Diccionay days of de week, date and hour
    days_of_the_week = {0: "Lunes",
                        1: "Martes",
                        2: "Miercoles",
                        3: "Jueves",
                        4: "Viernes",
                        5: "Sabado",
                        6: "Domindo"}
    month_list = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "junio", "julio", "agosto",
                  "septiembre", "Octubre", "noviembre", "diciembre"]
    hour = datetime.datetime.now()

    # response vitual assistant
    hour_reed = f"Hola xavier. espero que estes bien, soy Jennifer.hoy es {days_of_the_week[week_day]}.{hour.day}" \
                f" de {month_list[hour.month - 1]} de {hour.year}. y son las {hour.hour} y {hour.minute}"

    voice_assitant(hour_reed)


# Virtual assitent engine
def virtual_assitent_brain():
    # initial greeting
    today_data()

    # Star assitent
    start = True

    while start:
        response = transform_audio_to_text().lower()
        print(response)

        if "abrir youtube" in response:
            voice_assitant(" Estoy abriendo youtube")
            webbrowser.open("https://www.youtube.com/")
            continue
        elif "abrir google" in response:
            voice_assitant("Habriendo navegador de google")
            webbrowser.open("https://www.google.com/")
            continue
        elif "que dia es hoy" in response:
            today_data()
            continue
        elif "buscar en wikipedia" in response:
            voice_assitant("buscando en wikipedia")
            response = response.replace("buscar en wikipedia", " ")
            wikipedia.set_lang("es")
            result = wikipedia.summary(response, sentences=1)
            voice_assitant("Wikipedia dice lo siguiente")
            voice_assitant(result)
            continue
        elif "busca en internet" in response:
            voice_assitant("Buscando en internet")
            response = response.replace("busca en internet", " ")
            pywhatkit.search(response)
            continue
        elif "cuentame un chiste" in response:
            voice_assitant(pyjokes.get_joke("es"))
            continue
        elif "reproducir" in response:
            voice_assitant("Reproduciendo")
            pywhatkit.playonyt(response)
            continue
        elif "salir" in response:
            voice_assitant("Espero que hayas escontrado lo que buscabas que pases un buen dia")
            start = False
            continue


# Star Virtual loop assitent
virtual_assitent_brain()
