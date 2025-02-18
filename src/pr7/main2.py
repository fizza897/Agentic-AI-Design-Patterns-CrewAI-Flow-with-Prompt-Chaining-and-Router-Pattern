from crewai.flow.flow import Flow, start, listen
from litellm import completion


API_KEY = "AIzaSyCI0h48GE7fVmXxO1uBv_mGGjlu-4lr7Qg"

class CityFunFact(Flow):
    @start()
    def generate_random_city(self):
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{"content": "Return any random city name.", "role": "user"}],
        )
        city=result["choices"][0]["message"]["content"]
        print(city)
        return city
    
    @listen(generate_random_city)
    def generate_fun_fact(self,city_name):
        result = completion(
            model="gemini/gemini-2.0-flash-exp",
            api_key=API_KEY,
            messages=[{"content":f"write some of fun fact about {city_name}", "role": "user"}],
        )
        fun_fact=result["choices"][0]["message"]["content"]
        print(fun_fact)
        self.state["fun_fact"]=fun_fact


def kickoff():
    obj = CityFunFact()
    obj.kickoff()