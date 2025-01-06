from setuptools import setup, find_packages

setup(
    name='teleglog',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'numpy>=1.21.0',
        'pyTelegramBotAPI>=4.26.0'
    ],
    author='w1tnessbtwwwww (Alexey Surovtsev)',
    author_email='work.w1tnessbtw@mail.ru',
    description='Teleglog Library for make your telegram logging easier.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/w1tnessbtwwwww/teleglog',
    classifiers=[
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
