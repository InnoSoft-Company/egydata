from setuptools import setup, find_packages

setup(
  name="egydata",
  version="0.1.0",
  author="MidoGhanam",
  author_email="mghanam883@outlook.com",
  description="Python library for Egyptian data: cities, governorates, timezones, phone numbers, etc.",
  long_description=open("README.md", encoding="utf-8").read(),
  long_description_content_type="text/markdown",
  url="https://midoghanam2.pythonanywhere.com/",
  packages=find_packages(),
  python_requires=">=3.9",
  install_requires=[
    # أي مكتبات خارجية تحتاجها
  ],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
)