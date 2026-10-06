from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Vaibhav',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    package_dir={'': 'src'},
    packages=find_packages(where='src')
)