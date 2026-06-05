from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import dotenv_values
from utils import get_key
envs=dotenv_values()

(BASE_URL,)=[dotenv_values()[x] for x in dotenv_values().keys()]
API_KEY=get_key("API_KEY")

if API_KEY is None:
    raise EnvironmentError("尚未配置api key")
if BASE_URL is None:
    raise EnvironmentError("尚未配置Base Url")

llm=ChatOpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
)


def get_weather(city:str)->str:
    return f"{city}总是阳光明媚"

agent=create_agent(
    model="deepseek-v4-flash",
    tools=[get_weather],
    system_prompt="You are a helpful assistant."
)

def main():
    agent


if __name__ == "__main__":
    main()
