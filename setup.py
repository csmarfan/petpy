from setuptools import setup

setup(name='petpy',
        version='0.1',
        description='Petrophysics utilities',
        url='https://example.com/',
        author = 'Fan',
        author_email='yuanzhong.fan@shell.com',
        license = 'Apache 2',
        pakages=['petpy'],
        install_requires=['numpy'],
        test_require = ['pytest','pytest-cov'],
        entry_points={'console_scripts':
                ['gardner=petpy.__main__:main',
                 ]}
        )