import setuptools

from searchhide import __version__


with open('README.md', 'r') as fh:
    DESCRIPTION = fh.read()


setuptools.setup(
    name='django-search-hide',
    version=__version__,
    author='Denis Anikin',
    author_email='ad@xfenix.ru',
    description='Seo hide helper template tags for django',
    python_requires='>=3.5.0',
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/xfenix/django-search-hide',
    packages=setuptools.find_packages(),
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
