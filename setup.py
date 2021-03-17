import setuptools
import subprocess

setuptools.setup(
    name="hello",
    version=subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"]).strip(),
    description="Hello",
    packages=setuptools.find_packages(),
)
