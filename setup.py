from setuptools import setup, find_packages

setup(name='cart',
        version='0.1',
        description='Django pluggable shopping cart',
        author='Eric Woudenberg',
        packages=find_packages(),
        classifiers=['Development Status :: r8 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Utilities'],
    include_package_data=True,
    install_requires=['setuptools'],
)