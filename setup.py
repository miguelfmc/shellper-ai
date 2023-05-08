from setuptools import setup

setup(
    name="shellper-ai",
    version="0.1.0",
    packages=["shellper"],
    install_requires=["click", "openai"],
    extras_requires=["black"],
    entry_points="""
        [console_scripts]
        shellper=shellper.shellper:search
    """,
)
