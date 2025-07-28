# deepseek版本
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
import tool
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.markdown import Markdown

console = Console()
load_dotenv()

model = OpenAIModel(
    "deepseek-chat",
    provider=OpenAIProvider(
        api_key=os.getenv("OPENAI_API_KEY"),  # 从环境变量加载API密钥
        base_url="https://api.deepseek.com",
    ),
)
agent = Agent(
    model,
    system_prompt="You are an experienced programmer and you are especially good at os.",
    tools=[tool.read_file, tool.list_files, tool.rename_file, tool.write_file],
)


def main():
    history = []
    while True:
        user_input = input("Input:")
        print("🤖 Thinking...")
        resp = agent.run_sync(user_input, message_history=history)
        history = list(resp.all_messages())
        console.print(Markdown(resp.output))  # 用Markdown格式打印AI的回复


if __name__ == "__main__":
    main()
