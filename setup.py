import setuptools

REQUIRED_PACKAGES = [
    "pytest==6.2.5",
    "requests==2.26.0",
]

setuptools.setup(
    name="smhi",
    version="0.0.1",
    description="ML Model for SMHI",
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
    author="Trustly ML Team",
)
