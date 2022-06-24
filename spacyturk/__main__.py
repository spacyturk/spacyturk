import argparse

from .api import download


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'command', 
        choices=['download'], 
        help='downloads spaCyTurk model'
    )
    parser.add_argument(
        'model_name', 
        help='spaCyTurk model name'
    )
    args = parser.parse_args()
    download(args.model_name)