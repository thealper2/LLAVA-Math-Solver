import requests
import json
import base64

class LLAVACalculator:
    def __init__(self, url='http://localhost:11434/api/generate'):
        self.url = url
        self.prompt = (
            "Examine the image and find any mathematical expressions."
            "If an expression has no answer after the equal sign, calculate and return only the numerical result, with no additional text, explanation, or punctuation."
            "Do not mention the expression itself—just provide the number."
            "Only respond with numbers."
        )

    def get_answer(self, image_data):
        try:
            payload = {
                "model": "llava",
                "prompt": self.prompt,
                "stream": False,
                "images": [base64.b64encode(image_data).decode('utf-8')]
            }
            response = requests.post(self.url, data=json.dumps(payload))
            print(response.text)
            response_json = response.json()

            answer = response_json.get('response')
            if not answer:
                print("No 'response' field found in response:", response_json)
            return answer
        
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)

        except ValueError as e:
            print("Failed to parse JSON:", e)
        
        return None
