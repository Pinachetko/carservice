from services.models import ServiceType

class Translite():
  def __init__(self, entry):
    self.entry = entry
  @staticmethod
  def get_transtable():
      return ((u"Э", u"EE"),(u"э", u"ee"),(u"Щ", u"Sch"),(u"Щ", u"SCH"),(u"Ё", u"Yo"),(u"Ё", u"YO"),(u"Ж", u"Zh"),(u"Ж", u"ZH"),(u"Ц", u"Ts"),(u"Ц", u"TS"),(u"Ч", u"Ch"),(u"Ч", u"CH"),(u"Ш", u"Sh"),\
      (u"Ш", u"SH"),(u"Ы", u"Yi"),(u"Ы", u"YI"),(u"Ю", u"Yu"),(u"Ю", u"YU"),(u"Я", u"Ya"),(u"Я", u"YA"),(u"А", u"A"),(u"Б", u"B"),(u"В", u"V"),(u"Г", u"G"),(u"Д", u"D"),\
      (u"Е", u"E"),(u"З", u"Z"),(u"И", u"I"),(u"Й", u"J"),(u"К", u"K"),(u"Л", u"L"),(u"М", u"M"),(u"Н", u"N"),(u"О", u"O"),(u"П", u"P"),(u"Р", u"R"),(u"С", u"S"),(u"Т", u"T"),\
      (u"У", u"U"),(u"Ф", u"F"),(u"Х", u"H"),(u"Ъ", u"`"),(u"Ь", u"'"),(u"щ", u"sch"),(u"ё", u"yo"),(u"ж", u"zh"),(u"ц", u"ts"),(u"ч", u"ch"),(u"ш", u"sh"),\
      (u"ы", u"yi"),(u"ю", u"yu"),(u"я", u"ya"),(u"а", u"a"),(u"б", u"b"),(u"в", u"v"),(u"г", u"g"),(u"д", u"d"),(u"е", u"e"),(u"з", u"z"),(u"и", u"i"),(u"й", u"j"),(u"к", u"k"),\
      (u"л", u"l"),(u"м", u"m"),(u"н", u"n"),(u"о", u"o"),(u"п", u"p"),(u"р", u"r"),(u"с", u"s"),(u"т", u"t"),(u"у", u"u"),(u"ф", u"f"),(u"х", u"h"))

  @staticmethod
  def get_supported_language():
    supported_language = ["en", "ru"]
    return supported_language

  def translite(self, lang='ru'):
    transtable = self.get_transtable()
    if lang == 'en':
      for symb_in, symb_out in transtable:
        self.entry = self.entry.replace(symb_in, symb_out)
    elif lang == "ru":
      for symb_out, symb_in in transtable:
        self.entry = self.entry.replace(symb_in, symb_out)
    return self

  def get_link(self):
    self.entry = self.entry.replace(" ", "-").lower()
    return self.entry

  def normalize(self):
    self.entry = self.entry.replace("-", " ").capitalize()
    return self.entry
