import google.generativeai as genai

def getai_response() -> None:

    genai.configure(api_key='AIzaSyBbUEkAOeey7Lq68yswWbb8oCSAHFZh73Q')

    model = genai.GenerativeModel('models/gemini-pro')

    result = model.generate_content('Tell me a story about a magic backpack')

    print(result.text)
    
def main():
    getai_response()
 
if __name__ == "__main__":
    main()
     