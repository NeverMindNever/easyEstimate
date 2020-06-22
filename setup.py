from setuptools import setup

setup(
    name='easyEstimate',
    version='0.4.2',
    packages=[''],
    package_data={'': ['Appartement_Estimation_2019_Cat_Boost.joblib', 'repertoire_code_adr.csv']},
    include_package_data=True,
    url='api.telecomazur.fr',
    license='Apache 2.0',
    author='A. Tounsadi',
    author_email='info@telecomazur.fr',
    description='Estimate habitation in France easily'
)

#To create the package run python setup.py bdist_wheel
