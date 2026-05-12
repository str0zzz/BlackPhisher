from setuptools import setup, find_packages

setup(
    name="BlackPhisher",
    version="1.1",
    author="str0zzz",
    author_email="str0zzz@github.com",
    description="An advanced phishing tool with multiple templates and tunneling support.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/str0zzz/BlackPhisher",
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'blackphisher=blackphisher:main_menu',
        ],
    },
)
