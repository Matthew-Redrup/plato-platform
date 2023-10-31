import os
import dotenv
from plato_platform.utils.cli import MenuCLI
from plato_platform.agents import agents

dotenv.load_dotenv()

assert os.environ.get("OPENAI_API_KEY"), "OPENAI_API_KEY not found in .env file"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


def main():
    cli = MenuCLI()

    while True:
        cli.display_menu()
        cli.parse_input()
        cli.action()

        prompt = cli.user_input
        agents.user_proxy.initiate_chat(agents.host, message=prompt)


if __name__ == "__main__":
    main()
