"""Module translator"""
from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    """Translate English to French"""
    frenchText = MyMemoryTranslator(source='english', target='french').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    """Translate French to English"""
    englishText = MyMemoryTranslator(source='french', target='english').translate(frenchText)
    return englishText
