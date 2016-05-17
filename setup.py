"""
Flask-Session
-------------

Flask-Session is an extension for Flask that adds support for
Server-side Session to your application.

"""
from setuptools import setup


setup(
    name='Flask-Session',
    version='0.3.0',
    url='https://github.com/SiQLuxe/flask_session',
    license='BSD',
    author='Lucas',
    author_email='csq@qstrategy.cn',
    description='Add server-side session support for Flask application',
    long_description=__doc__,
    packages=['flask_session'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.8'
    ],
    test_suite='test_session',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)