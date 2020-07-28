from setuptools import setup, find_packages

setup(
    name = 'marmot_client',
    version = '1.0.0',
    description = 'Python client interface to Marmot',
    author = 'Kang-Woo Lee',
    author_email = 'kwlee@etri.re.kr',
    url = 'https://github.com/kwlee0220/marmot.client.python',
    install_requires = [
        'protobuf',
        'grpcio'
    ],
    packages = find_packages(),
    python_requires = '>=3',
    zip_safe = False
)