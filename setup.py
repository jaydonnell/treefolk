from setuptools import setup

setup(name='treefolk',
      version='0.1',
      description='An experiment in knowledge graphs',
      url='https://github.com/jaydonnell/treefolk',
      author='Jay Donnell',
      author_email='jay.donnell@hey.com',
      license='Apache License 2.0',
      packages=['treefolk'],
      install_requires=[
            'airtable-python-wrapper >= 0.13.0',
      ],
      zip_safe=False)