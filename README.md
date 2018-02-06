# vault-gatekeeper-client

[![Build Status](https://travis-ci.org/jensendw/vault-gatekeeper-client.svg?branch=master)](https://travis-ci.org/jensendw/vault-gatekeeper-client)

## Usage

```shell
pip install vault-gatekeeper-client
```

```python
import vault-gatekeeper-client

gatekeeper = VaultGatekeeper(task_id='marathon_app_id',
                                     gatekeeper_addr='https://my-vault-gatekeeper',
                                     vault_addr='https://my-vault:8200',
                                     secret_path='secret/test')

secrets = gatekeeper.Client()
print(secrets)
```
