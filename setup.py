from setuptools import setup

setup(
    name="pyHelperKennedyRodrigue",
    version="0.2.0",
    description="python functions to help access Dr. Kennedy's and Dr. Rodrigue's data",
    url="",
    author="Ekarin E. Pongpipat",
    author_email="epongpipat@gmail.com",
    license="MIT",
    packages=["pyHelperKennedyRodrigue"],
    install_requires=["numpy", "pandas"],
    zip_safe=False,
    package_data={'pyHelperKennedyRodrigue': ['data/*']},
    include_package_data=True,
)
