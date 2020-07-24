def translator(text, target="en"):
    from google.cloud import translate

    translate_client = translate.Client()

    translation = translate_client.translate(text, target_language="en")

    return translation['translatedText']

print(translator("bitte?"))
