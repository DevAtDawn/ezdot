from setuptools import setup
setup(
    name='ezdot',
    version='0.0.1',
    packages=['ezdot'],
    entry_points={
        'console_scripts': [
            'ezdot=ezdot.ezdot:main'
        ]
    }
)
