import sys
import re
import platform
import requests
from pathlib import Path
from typing import Union, List

import spacy.util as util
from spacy import about
from spacy.errors import filter_warning
from wasabi import Printer

from . import pkg


def download(model: str) -> None:
    """Downloads a spaCyTurk trained model.

    Args:
        model (str): spaCyTurk model name
    """
    try:
        # check model name
        models = _fetch_model_names()
        if model not in models:
            models = ', '.join(models)
            msg = Printer()
            msg.fail(f'Model "{model}" does not exist.')
            msg.fail(f'Available models: {models}')
            return

        # first try to install compatible version
        # if it fails, install the latest version
        try:
            version = re.search(r'^\d+\.\d+', about.__version__).group()
            download_url = f'{pkg.__hf_url__}/{model}/resolve/v{version}.0/{model}-any-py3-none-any.whl'
            cmd = [sys.executable, "-m", "pip", "install"] + [download_url]
            util.run_command(cmd)
        except:
            download_url = f'{pkg.__hf_url__}/{model}/resolve/main/{model}-any-py3-none-any.whl'
            cmd = [sys.executable, "-m", "pip", "install"] + [download_url]
            util.run_command(cmd)
    except:
        _conn_fail_msg()


def info() -> None:
    """Prints info about spaCyTurk installation and models.
    """
    try:
        models_st = _fetch_model_names()

        # disable spaCy compatibility warnings
        filter_warning('ignore', '[W094]')
        filter_warning('ignore', '[W095]')

        models = {}
        for pkg_name in util.get_installed_models():
            package = pkg_name.replace("-", "_")
            if package in models_st:
                models[package] = util.get_package_version(pkg_name)

        data = {
            "spaCyTurk version": pkg.__version__,
            "Location": str(Path(__file__).parent),
            "Platform": platform.platform(),
            "spaCy version": about.__version__,
            "Python version": platform.python_version(),
            "spaCyTurk models": ", ".join(f"{n} ({v})" for n, v in models.items())
        }

        msg = Printer()
        msg.table(data, title='Info about spaCyTurk')
    except:
        _conn_fail_msg()


def _fetch_model_names() -> List[str]:
    """Fetchs spacyTurk model names from Hugging Face Hub.

    Returns:
        spacyTurk model names
    """
    res = requests.get(pkg.__hf_search_url__)
    res.raise_for_status()
    return [m['id'].split('/')[-1] for m in res.json()]


def _conn_fail_msg() -> None:
    """Prints connection failed message.
    """
    msg = Printer()
    msg.fail('Connection to Hugging Face Hub failed.')
    msg.fail('Please try again or make sure your Internet connection is on.')
