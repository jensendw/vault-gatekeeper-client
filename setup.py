from distutils.core import setup


setup(name='vault-gateway-client',
      version='0.0.1',
      description='vault-gateway-client for interacting with mesos-vault-gateway service',
      url='https://github.com/jensendw/vault-gateway-client',
      author='Daniel Jensen',
      author_email='jensendw@gmail.com',
      license='Apache',
      packages=['vault_gatekeeper_client'],
      install_requires=[
          'hvac',
          'requests'
      ],
      zip_safe=False)
