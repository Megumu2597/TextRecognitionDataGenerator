import os 
#print(os.path.basename(__file__),os.path.dirname(__file__))
def load_fonts(lang):
    """Load all fonts in the fonts directories
    """

    if lang in os.listdir(os.path.join(os.path.dirname(__file__), "fonts")):
        return [
            os.path.join(os.path.dirname(__file__), "fonts/{}".format(lang), font)
            for font in os.listdir(
                os.path.join(os.path.dirname(__file__), "fonts/{}".format(lang))
            )
        ]
    else:
        return [
            os.path.join(os.path.dirname(__file__), "fonts/latin", font)
            for font in os.listdir(
                os.path.join(os.path.dirname(__file__), "fonts/latin")
            )
        ]
print(load_fonts("ja"))
