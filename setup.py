import os
from distutils.core import setup


def read_file_into_string(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file_into_string(name)
    return ''


setup(
    name='kb-kbsoftware-couk',
    packages=['web', 'web.tests', 'project', 'project.management', 'project.management.commands', 'project.migrations', 'dash', 'dash.tests', 'settings'],
    package_data={
        'project': [
            'static/*.*',
            'static/ico/*.*',
            'static/img/*.*',
            'static/img/project/*.*',
            'templates/*.*',
            'templates/project/*.*',
        ],

        'web': [
            'templates/*.*',
            'templates/web/*.*',
        ],

        'dash': [
            'templates/*.*',
            'templates/contact/*.*',
            'templates/dash/*.*',
        ],
    },
    version='0.0.39',
    description='KB Software Ltd',
    author='Patrick Kimber',
    author_email='code@pkimber.net',
    url='git@github.com:pkimber/kbsoftware_couk.git',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 1.8',
        'Topic :: Office/Business :: Scheduling',
    ],
    long_description=get_readme(),
)