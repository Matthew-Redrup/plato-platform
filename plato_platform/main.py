import os
import dotenv
from plato_platform.utils.cli import cli
from plato_platform.agents import agents
from plato_platform.modules import llm

dotenv.load_dotenv()

assert os.environ.get("OPENAI_API_KEY"), "OPENAI_API_KEY not found in .env file"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


def main():
    prompt = cli()
    prompt = llm.add_cap_ref(
        prompt,
        prompt_suffix="",
        cap_ref="",
        cap_ref_content="",
    )
    agents.user_proxy.initiate_chat(agents.host, message=prompt)


if __name__ == "__main__":
    main()
