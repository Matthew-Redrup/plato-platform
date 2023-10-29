import os
import dotenv
from plato_platform.utils.cli import cli

dotenv.load_dotenv()

assert os.environ.get("OPENAI_API_KEY"), "OPENAI_API_KEY not found in .env file"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


def main():
    output = cli()
    return output


if __name__ == "__main__":
    main()
