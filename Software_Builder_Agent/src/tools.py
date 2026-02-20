from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_core.tools import tool
from typing import Tuple
import subprocess
import pathlib
import os


@tool()
def get_current_directory():
    """Returns the current working directory."""
    return os.getcwd()


# Initialize file management toolkit once and extract the actual tools
working_dir = os.getcwd()

toolkit = FileManagementToolkit(
    root_dir=str(working_dir)
)
file_management_tools = toolkit.get_tools()


@tool
def run_cmd(cmd: str, cwd: str = None, timeout: int = 30) -> Tuple[int, str, str]:
    """
    Runs a shell command in the specified directory and returns the result.

    Args:
        cmd (str): The shell command to run.
        cwd (str, optional): The directory to run the command in. Defaults to None (current directory).
        timeout (int, optional): The maximum time to wait for the command to complete in seconds. Defaults to 30.

    Returns:        
    Tuple[int, str, str]: A tuple containing the return code, standard output, and standard error of the command execution.
    """

    cwd_dir = pathlib.Path(cwd) if cwd else pathlib.Path.cwd()

    res = subprocess.run(cmd, shell=True, cwd=str(
        cwd_dir), capture_output=True, text=True, timeout=timeout)

    return res.returncode, res.stdout, res.stderr
