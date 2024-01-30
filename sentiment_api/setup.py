#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="João Victor Lopes de Paula",
    author_email='joaovictorlopesld@hotmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Construção de API via FastAPI e Streamlit com API do Hugging Face para predição de sentimento",
    entry_points={
        'console_scripts': [
            'sentiment_api=sentiment_api.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='sentiment_api',
    name='sentiment_api',
    packages=find_packages(include=['sentiment_api', 'sentiment_api.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jvlopesdp/sentiment_api',
    version='0.1.0',
    zip_safe=False,
)
