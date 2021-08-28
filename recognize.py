import speech_recognition as sr

def convert_speech_to_text(audio_file_path: str):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = r.record(source)

    result = r.recognize_google(audio, language='ja-JP')

    try:
        print('Google Speech Recognition thinks you said:')
        print(result)
        return result
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')
        return False
    except sr.RequestError as e:
        print('Could not request results from Google Speech Recognition service; {0}'.format(e))
        return False
