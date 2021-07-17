from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Education",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: Turkish",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS",
    "Programming Language :: Python :: 3.8",
]

setup(
    name="PyPerspective",
    version="1.0.0",
    description="A Library For Perspective API Usage",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="",
    author="Tunay Ada Karacan",
    author_email="tunayada@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keyword="Perspective Py PyPerspective Py Perspective API Perspective API",
    packages = find_packages(),
    py_modules=["datetime","warnings","json"],
    install_requires=["requests"]
)
