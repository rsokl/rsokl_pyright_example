from setuptools import find_packages, setup

setup(
    name="rsokl_pyright_example",
    version="0.0.0",
    python_requires=">=3.7",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data = {
        'rsokl_pyright_example': ['py.typed'],
    }
)
