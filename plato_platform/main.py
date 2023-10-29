import os
import dotenv
import argparse

dotenv.load_dotenv()

assert os.environ.get("OPENAI_API_KEY"), "OPENAI_API_KEY not found in .env file"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", help="Prompt to pass the agent")
    args = parser.parse_args()

    if not args.prompt:
        print("Prompt not provided. Exiting...")
        return

    print("Hello, World!", args.prompt)


if __name__ == "__main__":
    main()
