from setuptools import setup, find_packages

setup(
    name='better-dash-callback',
    version='0.1.0',
    description='Runs clientside callback functions in Dash applications using Python syntax, eliminating the need for inline JavaScript.',
    author='Richard Barella Jr.',
    author_email='codingwithricky@gmail.com',
    url='https://github.com/ribab/better-dash-callback',
    packages=find_packages(exclude=['tests', 'examples']),
    install_requires=[
        'dash>=2.0.0',
        'javascripthon==0.13'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    include_package_data=True,
)
