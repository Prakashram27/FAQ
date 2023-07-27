# # from googletrans import Translator

# # def detect_language(text):
# #     # Implement language detection logic here (you can use external libraries/APIs)
# #     # For this example, we'll assume English is the default language
# #     return 'en'

# # def translate_text(text, target_language):
# #     translator = Translator()
# #     translated_text = translator.translate(text, dest=target_language).text
# #     return translated_text

# from typing import Dict, Text, Any, List

# from rasa.engine.graph import GraphComponent, ExecutionContext
# from rasa.engine.recipes.default_recipe import DefaultV1Recipe
# from rasa.engine.storage.resource import Resource
# from rasa.engine.storage.storage import ModelStorage
# from rasa.shared.nlu.training_data.message import Message
# from rasa.shared.nlu.training_data.training_data import TrainingData

# from googletrans import Translator

# class LanguageChangeComponent(GraphComponent):

#     # The component name
#     name = "language_change"
#     # The component requires a language key in the pipeline configuration
#     requires = ["language"]
#     # The component provides an updated language key to be used in subsequent components
#     provides = ["language"]
#     # We do not need to persist this component's state
#     # Therefore, we can set it to `True` to save space in the model
#     defaults = {}
#     # We do not need to load anything to initialize the component
#     # So, this method remains empty
#     language_list = ["af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "ny", "zh-cn", "co",
#                       "hr", "cs", "da", "nl", "en", "eo", "et", "tl", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu",
#                       "ht", "ha", "haw", "iw", "he", "hi", "hmn", "hu", "is", "ig", "id", "ga", "it", "ja", "jv", "kn",
#                       "kk", "km", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi",
#                       "mr", "mn", "my", "ne", "no", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr",
#                       "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tg", "ta", "tt", "te", "th",
#                       "tr", "tk", "ug", "uk", "ur", "uz", "vi", "cy", "xh", "yi", "yo", "zu"]

#     def __init__(self, component_config=None):
#         super().__init__(component_config)
#         self.translator = Translator()

#     def translate_to_english(self, message, target_language):
#         if target_language != "en" and target_language in self.language_list:
#             translation = self.translator.translate(message, dest="en")
#             return translation.text
#         return message

#     def process(self, message: Message, **kwargs: Any) -> None:
#         target_language = message.get("language")
#         text = message.get("text")
#         translated_text = self.translate_to_english(text, target_language)

#         # Update the language key for subsequent components
#         message.set("language", "en", add_to_output=True)
#         message.set("text", translated_text, add_to_output=True)

