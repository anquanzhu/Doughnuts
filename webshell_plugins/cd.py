from libs.config import alias, color, gset, gget
from libs.myapp import send

from base64 import b64encode


@alias(True, d="dir")
def run(directory: str = ''):
    """
    cd

    Change the working directory.
    """
    directory = b64encode(directory.encode()).decode()
    pwd = send(f"chdir(base64_decode('{directory}'));print(getcwd());").r_text.strip()
    gset("webshell.pwd", pwd, namespace="webshell")
    gset("webshell.prompt", f"doughnuts ({color.cyan(gget('webshell.netloc', 'webshell'))}) > ")
