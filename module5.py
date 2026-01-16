from translate import Translator

data = ["salom", "dastur", 2.5, "yordam", 34, "kitob"]

translator = Translator(from_lang="uz", to_lang="en")


result = {}

for item in data:
    if isinstance(item, str): 
        result[item] = translator.translate(item)
print(result)
