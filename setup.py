from setuptools import setup, find_packages

setup(
  name="egydata",
  version="1.1.0",
  author="InnoSoft Company",                # ← change to your company
  author_email="midoghanam@hotmail.com",        # ← company email
  description="Python library for Egyptian data: cities, governorates, timezones, phone numbers, etc.",
  long_description=open("README.md", encoding="utf-8").read(),
  long_description_content_type="text/markdown",
  url="https://www.midoghanam.site/",        # can be your homepage or GitHub
  project_urls={
    "Source Code": "https://github.com/InnoSoft-Company/egydata",
    "Bug Tracker": "https://github.com/InnoSoft-Company/egydata/issues",
    "Documentation": "https://github.com/InnoSoft-Company/egydata#readme",
  },
  packages=find_packages(),
  entry_points={"console_scripts": ["egydata=egydata.cli:main", ],},
  python_requires=">=3.9",
  install_requires=[],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
)