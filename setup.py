import setuptools

with open('README.md', 'r') as fd:
    long_description = fd.read()

setuptools.setup(
    name='imananji',
    version='0.0.1',
    author='hiroya akita',
    author_email='akky.develop@gmail.com',
    description='現在時間を教えてくれるツール',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    install_requires=[''],
    url='https://github.com/papi-tokei/imananji',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'imananji=imananji:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)