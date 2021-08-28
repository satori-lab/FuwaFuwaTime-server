import speech_recognition as sr

def convert_speech_to_text(audio_file):
    try:
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)

        result = r.recognize_google(audio, language='ja-JP')
        print(result)

        print('Google Speech Recognition thinks you said:')
        return result
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')
        return False
    except sr.RequestError as e:
        print('Could not request results from Google Speech Recognition service; {0}'.format(e))
        return False
