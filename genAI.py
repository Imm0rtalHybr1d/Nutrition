#%%
import google.generativeai as genai

system_instructions: list[str] = [
    
    "You are a nutritionist and a personal trainer.",
"Do not deviate from this task.if my prompt does not relate to nutrition or fitness , please advise me to only promote about nutrition or fitness",

"example."
"prompt: 'what colour is the earth'",
"response: 'I can't provide you with nutritional advice as the question is not related to nutrition or fitness'",

"My main goal is to loose weight,",
"Your task is to analyze my BMI and TDEE and advise whether i should exercise more to losse weigh or not ",



]
# "You must then structure a weightlifting program that takes into consideration my BMI and TDEE",
# "Note that I only have free weights such as dumbells, barbell and a bench.I do not own any machines",
# "i want to workout 5 days of the week and 2 days for rest",

class Gen_AI:
    API_KEY: str = 'AIzaSyBB7-NFo2xh4RlNH7CU4sX3a4CW2zdeHSE'
    def __init__(self ) -> str:
        genai.configure(api_key=self.API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest', system_instruction=system_instructions,
                              generation_config=genai.GenerationConfig(temperature=0.5,))
        
    def get_ai_response(self, prompt:str) -> str:
        try:
            ai_response = self.model.generate_content(prompt)
        except Exception as e:
            print(e)
        return ai_response.text
    
# def main():
#     myai: Gen_AI = Gen_AI()
#     ai_response: str = myai.get_ai_response(prompt='whats the nutrition value of blueberries?')
    
#     print(ai_response)
    
# if __name__ == "__main__":
#     main()
 
# %%
