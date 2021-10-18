import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prescaling",
    version="0.0.1",
    author="Ryo Kamoi",
    author_email="ryokamoi.jp@google.com",
    description="prescaling is a package for scaling of preprocessing for machine learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryokamoi/ml-preprocessing-scalers",
    project_urls={
        "Bug Tracker": "https://github.com/ryokamoi/ml-preprocessing-scalers/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
