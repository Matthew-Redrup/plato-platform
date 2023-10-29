import argparse
import sys


def cli(args=None):
    if not args:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", help="Prompt to pass the agent")
    args = parser.parse_args(args)

    if not args.prompt:
        print("Prompt not provided. Exiting...")
        return

    print("Prompt:", args.prompt)
