from setuptools import setup
from easyEstimate import __version__

setup(
    name='easyEstimate',
    version=__version__,
    packages=['easyEstimate'],
    package_data={'': ['Appartement_Estimation_2019_Cat_Boost.joblib', 'repertoire_code_adr.csv']},
    include_package_data=True,
    url='www.telecomazur.fr',
    license='Apache 2.0',
    author='A. Tounsadi',
    author_email='info@telecomazur.fr',
    description='AN easy way to estimate the price of habitation in France'
)
