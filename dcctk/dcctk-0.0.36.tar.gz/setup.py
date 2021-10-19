from setuptools import setup
from itertools import chain

with open("README.md", encoding="utf-8") as f:
      long_description = f.read().strip()


with open("VERSION") as f:
      v = int(f.read().strip()) + 1

EXTRAS_REQUIRE = {
      'sense': ['transformers', 'torch', 'opencc', 'umap-learn', 'yellowbrick>=1.3'],
      'colab': ['datashader', 'bokeh', 'holoviews', 'scikit-image', 'colorcet'],
}
EXTRAS_REQUIRE['all'] = list(set(chain(*EXTRAS_REQUIRE.values())))

setup(name='dcctk',
      version=f'0.0.{v}',
      description="Diachronic Character-based Corpus toolkit",
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/liao961120/dcctk',
      author='Yongfu Liao',
      author_email='liao961120@github.com',
      license='MIT',
      packages=['dcctk'],
      install_requires=['scikit-learn', 'scipy', 'gdown>=3.10.2', 'pyyaml', 'cqls', 'tqdm'],
      dependency_links=[
            'https://github.com/liao961120/CompoTree/tarball/main',
            'https://github.com/liao961120/hanziPhon/tarball/main',
      ],  
      extras_require=EXTRAS_REQUIRE,
      # tests_require=['deepdiff'],
      zip_safe=False)


with open("VERSION", "w") as f:
      f.write(str(v))
