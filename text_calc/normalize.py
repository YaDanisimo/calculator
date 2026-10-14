def normalize(text):
    text = text.lower()
    text = text.replace('ё', 'е')
    return text