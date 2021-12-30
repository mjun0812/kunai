# API

Update: 2021-12-30 19:33

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

configファイルを標準出力し，Current Dirを実行スクリプトの場所に戻す．

hydraは使用時にカレントディレクトリを変更するため，hydra.utils.get_original_cwdを使って実行ディレクトリを取得してもとに戻す．

#### Args:

- *`cfg`*: OmegaConf.omegaconf

### <kbd>function</kbd> `hydra_utils.get_default_config`

```python
get_default_config(config_dir_path, config_name='config.yaml')
```

hydraを使わずにディレクトリに分割されたyamlの設定ファイルをOmegaConfに変換する

２つ以上の設定ファイルを比較するときに必要

#### Args:

- *`config_dir_path`*: str
- *`config_name`*: str, optional

#### Returns:

- *`OmegaConf.omegaconf`*:  omegaconf

### <kbd>function</kbd> `hydra_utils.validate_config`

```python
validate_config(cfg)
```

2つのOmegaConfをマージする．

main関数でロードしたものと，デフォルトで使っているものをマージする．開発中にデフォルトのconfigに追加があった場合に，既に生成されたconfigに追加した項目をロードしたconfigに追加するために使う


```yaml

# load config
HOGE: 3

# default config
HOGE: 2
HUGA: 1

# merged config
HOGE: 3
HUGA: 1

```

#### Args:

- *`cfg`*: OmegaConf.omegaconf

#### Returns:

- *`OmegaConf.omegaconf`*:  マージされたconfigファイル

### <kbd>function</kbd> `hydra_utils.enum_dict_keys`

```python
enum_dict_keys(base, base_name='')
```

dictのkeyを再帰的に列挙したリストを取得する

#### Args:

- *`base`*: dict
- *`base_name`*: str, optional

#### Returns:

- *`list`*:  dictのkeyのリスト

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

slackにメッセージを送る. send slack message

#### Args:

- *`token`*: str
- *`channel`*: str, optional
- *`username`*: str, optional
- *`message`*: str, optional

#### Returns:

- *`int`*:  http status code

### <kbd>function</kbd> `utils.setup_logger`

```python
setup_logger(rank, log_path)
```

loggerのセットアップをする

#### Args:

- *`rank`*: int
- *`log_path`*: str

#### Example:

```python

    # write first on python script file

    import logging

    logger = logging.getLogger()


    # logging

    logger.info("test log")


    # output

    [2021-12-22 19:48:45,027][INFO] test log

    ```
