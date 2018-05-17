from setuptools import setup, find_packages


setup(
    name='pyaclg',
    version='0.3.0',
    description='Auomatic Changelog Git',
    author='Santiago Blanco Ventas',
    license='MIT',
    project_urls={
        'Source': 'https://github.com/sblancov/pyaclg'
    },
    packages=find_packages(),
    install_requires=['gitpython==2.1.9'],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': ['pyaclg = pyaclg.main:main']
    }
)
