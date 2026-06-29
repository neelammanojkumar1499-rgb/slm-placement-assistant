"""
main.py

Central Entry Point

Usage:

python main.py preprocess
python main.py train
python main.py evaluate
python main.py chat
"""

import argparse

from src.preprocess import preprocess
from src.train import train
from src.evaluate import run_evaluation
from src.inference import chat


def main():

    parser = argparse.ArgumentParser(
        description="Placement SLM Project"
    )

    parser.add_argument(
        "command",
        choices=[
            "preprocess",
            "train",
            "evaluate",
            "chat",
        ],
        help="Operation to execute"
    )

    args = parser.parse_args()

    if args.command == "preprocess":

        preprocess()

    elif args.command == "train":

        train()

    elif args.command == "evaluate":

        run_evaluation()

    elif args.command == "chat":

        chat()


if __name__ == "__main__":

    main()
