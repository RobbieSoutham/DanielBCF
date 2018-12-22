from setuptools import find_packages, setup

try:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:
    from pip.req import parse_requirements
    from pip.download import PipSession

install_reqs = parse_requirements('./requirements.txt', session = PipSession())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='DanielBCF',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=reqs,
)
