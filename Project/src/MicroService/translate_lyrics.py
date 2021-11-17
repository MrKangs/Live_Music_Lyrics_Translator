import googletrans as google

def translate_lyrics(language, lyrics_file, translated_lyrics_file):
    """
    This function will use Google Translate API based on the .txt file

    If the lyrics too large (limit of 5,000 characters), then it will do a split translation of Google Translator API

    Once the translation is complete, then it will write a new .txt file called TRANSLATED that will have the translated version of the lyrics

    Args:
        language: string value that indicates which language to be translated 
        lyrics_file = path of where the lyrics is stored
        translated_lyrics_file = path of where the translated lyrics will be saved
    """        
    translator = google.Translator()
    og_file = open(lyrics_file, 'r', encoding = 'utf-8')
    translated_file = open(translated_lyrics_file, 'w', encoding= 'utf-8')

    og_lyrics = og_file.read()

    if len(og_lyrics) > 5000:
        split_lyrics = []

        for i in range(0, len(og_lyrics), 4999):
            split_lyrics.append(og_lyrics[i: i + 5000])

        for i in range(len(split_lyrics)):
            result = translator.translate(split_lyrics[i], dest = language)
            translated_file.write(result.text)
            
        translated_file.close()
        og_file.close()
        
    else:

        result = translator.translate(og_lyrics, dest = language)
        translated_file.write(result.text)
        og_file.close()
        translated_file.close()
