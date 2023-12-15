import sys
import comfy.sd
import comfy.utils

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

class Format:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True}),
            },
            "optional": {
                "var_1": ("STRING", {"default": ""}),
                "var_2": ("STRING", {"default": ""}),
                "var_3": ("STRING", {"default": ""}),
                "var_4": ("STRING", {"default": ""}),
                "var_5": ("STRING", {"default": ""}),
            },
        }

    CATEGORY = "Zuellni/Text"
    FUNCTION = "process"
    RETURN_TYPES = ("STRING",)

    def process(self, text, **vars):
        for key, value in vars.items():
            text = text.replace(key, value)

        return (text,)