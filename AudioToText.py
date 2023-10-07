from googletrans import Translator
import speech_recognition as sr


def translator(text,lang):
    try:
        translator = Translator()
        translation = translator.translate(text, src=lang, dest='en')
        return translation.text
    except Exception as e:
        return str(e)


def speech_to_text(audio_file, lang="en-US"):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

        try:
            # Recognize the speech using the Google Web Speech API
            recognized_text = recognizer.recognize_google(audio_data, language=lang)
            if(lang!="en-US"):
                recognized_text = translator(recognized_text,lang[:2])
            return recognized_text
        except sr.UnknownValueError:
            return "Speech recognition could not understand the audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

