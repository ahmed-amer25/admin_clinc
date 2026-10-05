import os
from google import genai

class AIHealer:
    def __init__(self, driver):
        self.driver = driver

    def heal(self):
        pass

    def heal_locator(self, broken_selector: str, page_source: str) -> str:
        prompt = f"""
        An automated Selenium test failed because the CSS Selector '{broken_selector}' was not found.
        Here is a snippet of the page's HTML DOM:
        
        {page_source[:4000]}
        
        Analyze the HTML and provide ONLY the fixed valid CSS selector for the element.
        Do not output any explanation or extra text, output ONLY the CSS selector string.
        """
        try:
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return response.text.strip()
        except Exception as e:
            print(f"[AI Error] Failed to generate healing selector: {e}")
            return broken_selector