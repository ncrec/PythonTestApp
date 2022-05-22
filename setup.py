import os
from setuptools import setup, find_packages

setup(name="ncrec_test",
      version="1.1.0",
      python_requires='>=3.4',
      description="Test API client",
      author="Ncrec",
      author_email="danil-kuptsov@yandex.ru",
      packages=find_packages(exclude=["*tests.*", "*test.*"]),
      license='MIT License',
      keywords="ncrec",
      zip_safe=True)
