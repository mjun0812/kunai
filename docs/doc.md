# API

Update: 2021-12-30 18:32

## <kbd>module</kbd> Registry

### <kbd>class</kbd> `Registry`

The registry that provides name -> object mapping, to support third-partyusers' custom modules.

To create a registry (e.g. a backbone registry):

.. code-block:: python

 BACKBONE_REGISTRY = Registry('BACKBONE')

To register an object:

.. code-block:: python

 @BACKBONE_REGISTRY.register() class MyBackbone(): ...

Or:

.. code-block:: python

 BACKBONE_REGISTRY.register(MyBackbone)

### <kbd>function</kbd> `Registry.get`

```python
get(self, name: str) → object
```

### <kbd>function</kbd> `Registry.register`

```python
register(self, obj: object = None) → Union[object, NoneType]
```

Register the given object under the the name `obj.__name__`.Can be used as either a decorator or not. See docstring ofthis class for usage.

## <kbd>module</kbd> hydra_utils

### <kbd>function</kbd> `hydra_utils.set_hydra`

```python
set_hydra(cfg)
```

### <kbd>function</kbd> `hydra_utils.get_default_config`

```python
get_default_config(config_dir_path, config_name='config.yaml')
```

### <kbd>function</kbd> `hydra_utils.validate_config`

```python
validate_config(cfg)
```

### <kbd>function</kbd> `hydra_utils.enum_dict_keys`

```python
enum_dict_keys(base, base_name='')
```

## <kbd>module</kbd> utils

### <kbd>function</kbd> `utils.get_cmd`

```python
get_cmd()
```

実行コマンドを取得する

#### Returns:

- *`string`*:  実行コマンド

#### Examples:

> get_cmd()
python hoge.py --huga

### <kbd>function</kbd> `utils.get_git_hash`

```python
get_git_hash()
```

gitハッシュを取得する

#### Returns:

- *`string`*:  Gitのハッシュ値

### <kbd>function</kbd> `utils.post_slack`

```python
post_slack(token, channel='#通知', username='通知', message='')
```

### <kbd>function</kbd> `utils.setup_logger`

```python
setup_logger(rank, log_path)
```
