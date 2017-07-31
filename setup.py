from setuptools import setup, find_packages

setup(
    name='bigchaindb_print_on_console',
    version='0.1.0',
    description='Sample plugin',
    author='BigchainDB devs',
    packages=find_packages(),
    entry_points={
        'bigchaindb.block_publisher': [
            'console_print=bigchaindb_print_on_console'
        ]
    }
)
