from setuptools import setup, find_packages
setup(
    name="aski",
    packages=find_packages("код"),
    package_dir={"": "код"},
    install_requires=[
    ],
    extras_require={
        "dev": [
            "pytest",
        ],
    },
    scripts=[
        "скрипте/aski",
    ],
)
