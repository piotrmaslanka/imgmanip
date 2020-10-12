from setuptools import setup, find_packages
from satella import __version__


setup(keywords=['image', 'manipulation', 'imaging', 'png', 'bmp'],
      packages=find_packages(include=['imgmanip.*', 'imgmanip']),
      version=__version__,
      install_requires=[
            'pillow', 'satella'
      ],
      python_requires='!=2.7.*,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
      entry_points={
          'console_scripts': [
              'imgmanip = imgmanip.script:command',
          ],
      },
      )
