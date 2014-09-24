from setuptools import setup


def desc():
    with open("README.md") as f:
        return f.read()

def reqs():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='frasco-users-avatar',
    version='0.1',
    url='http://github.com/frascoweb/frasco-users-avatar',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="Avatars for Frasco-Users",
    long_description=desc(),
    py_modules=['frasco_users_avatar'],
    platforms='any',
    install_requires=[
        'frasco',
        'frasco-users'
    ]
)