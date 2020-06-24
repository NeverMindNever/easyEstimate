from setuptools import setup

version="0.4.8"

setup(
    name='easyEstimate',
    version=version,
    packages=['easyEstimate'],
    package_data={
        'model': ['easyEstimate/Appartement_Estimation_2019_Cat_Boost.joblib'],
        'csv': ['easyEstimate/repertoire_code_adr.csv']
    },
    include_package_data=True,
    url='www.telecomazur.fr',
    license='Apache 2.0',
    author='A. Tounsadi',
    author_email='info@telecomazur.fr',
    description='AN easy way to estimate the price of habitation in France'
)
