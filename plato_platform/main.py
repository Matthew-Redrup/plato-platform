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
        prompt_suffix="Follow the RULES below to generate a comprehensive yet concise mini-course for rapid learning. The course should contain chapters that teach me about these SUB_TOPICS. Make sure the chapters fit my level, profession and topic. Ask for clarification if you need more information about my knowledge",
        cap_ref="Use concrete examples to explain every concept. Use emojis to add expression. Generate Generate one chapter at a time. Ask for feedback at the end of each chapter. Ask if I need clarification at the end of each chapter. With each concept, explain real world use cases. After we complete every sub topic, present a list of additional topics we can explore that align with my level, profession, topic and objective.",
        cap_ref_content="architechure, design and maintanability",
    )
    agents.user_proxy.initiate_chat(agents.host, message=prompt)


if __name__ == "__main__":
    main()
