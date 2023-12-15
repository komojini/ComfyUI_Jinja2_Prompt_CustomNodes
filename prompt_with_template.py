import sys
import os
import comfy.sd
import comfy.utils

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

class PromptWithTemplate:
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

    CATEGORY = "komojini/Text"
    FUNCTION = "process"
    RETURN_TYPES = ("STRING",)

    def process(self, text, **vars):
        for key, value in vars.items():
            text = text.replace(key, value)

        return (text,)


class ObjectPromptWithTemplate(PromptWithTemplate):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True}),
            },
            "optional": {
                "instance_prompt": ("STRING", {"default": ""}),
                "class_prompt": ("STRING", {"default": ""}),
                "gender_prompt": ("STRING", {"default": ""}),
            },
        }
    

NODE_CLASS_MAPPINGS = {
    "PromptWithTemplate": PromptWithTemplate,
    "ObjectPromptWithTemplate": ObjectPromptWithTemplate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptWithTemplate": "Prompt with Template",
    "ObjectPromptWithTemplate": "Object Prompt Template"
}