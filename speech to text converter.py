import speech_recognition as sr

def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Please speak.")

        try:
            # Capture the audio
            audio = recognizer.listen(source, timeout=5)
            print("Processing your speech...")

            # Convert speech to text using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as ex:
            print(f"An error occurred: {ex}")

# Call the function
speech_to_text()