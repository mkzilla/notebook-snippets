"""
Setup module for the jupyterlab-latex
"""
import setuptools
from setupbase import (
    create_cmdclass, ensure_python, find_packages, get_version
    )

data_files_spec = [(
    'etc/jupyter/jupyter_notebook_config.d',
    'jupyter-config/jupyter_notebook_config.d',
    'notebook_snippets.json'
),]

cmdclass = create_cmdclass(data_files_spec=data_files_spec)

setup_dict = dict(
    name='notebook_snippets',
    version=get_version('notebook_snippets/_version.py'),
    description='code snippets integration for JupyterLab',
    packages=find_packages(),
    cmdclass=cmdclass,
    author='chengtian',
    author_email='792400644@qq.com',
    url='https://github.com/mkzilla/notebook-snippets',
    license='MIT',
    platforms='Linux, Mac OS X, Windows',
    keywords=['Jupyter', 'JupyterLab', 'snippets'],
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'notebook'
    ],
    package_data={'notebook_snippets':['api/*']},
)

try:
    ensure_python(setup_dict["python_requires"].split(','))
except ValueError as e:
    raise  ValueError("{:s}, to use {} you must use python {} ".format(
                          e,
                          setup_dict["name"],
                          setup_dict["python_requires"])
                     )

setuptools.setup(**setup_dict)