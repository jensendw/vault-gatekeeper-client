# vault-gatekeeper-client

[![Build Status](https://travis-ci.org/jensendw/vault-gatekeeper-client.svg?branch=master)](https://travis-ci.org/jensendw/vault-gatekeeper-client)

## Usage

```shell
pip install vault-gatekeeper-client
```

```python
from vault_gatekeeper_client import VaultGatekeeperClient

gatekeeper = VaultGatekeeperClient(task_id='marathon_app_id',
                                     gatekeeper_addr='https://my-vault-gatekeeper',
                                     vault_addr='https://my-vault:8200',
                                     secret_path='secret/test')


print(gatekeeper.secrets)
```

The statement above returns a dict of dicts based on the name of each file in the secret_path and the relevant keys within each file, for example:

```shell
secret/test/foo
      key1: value1
      key2: value2
secret/test/bar
      key1: value1
      key2: value2
```
Will return
```shell
{'foo': {'key1': 'value1', 'key2': 'value2'}, 'bar': {'key1': 'value1', 'key2': 'value2'}}
```

## Contributing

1. Fork it ( https://github.com/jensendw/vault-gatekeeper-client )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
