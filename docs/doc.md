# API

Update: 2022-03-13 13:52

## <kbd>module</kbd> Registry

### <kbd>class</kbd> `Registry`

The registry that provides name -> object mapping,to support third-party users' custom modules.

To create a registry (e.g. a backbone registry):
```python
BACKBONE_REGISTRY = Registry('BACKBONE')

```

To register an object:
```python
@BACKBONE_REGISTRY.register()
class MyBackbone():

```or
```python
BACKBONE_REGISTRY.register(MyBackbone)

To get an object from registry

```pythonBACKBONE_REGISTRY.get("MyBackbone")
```

### <kbd>function</kbd> `Registry.get`

```python
get(self, name: str) → object
```

get object from Registry

#### Args:

 - <b>`name`</b> (str):  Object Name

#### Raises:

- *`KeyError`*:  No object from registry

#### Returns:

- *`object`*:  Registred Object

### <kbd>function</kbd> `Registry.register`

```python
register(self, obj: object = None) → Optional[object]
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

 - <b>`cfg`</b> (OmegaConf.omegaconf):  Hydra config obj.

### <kbd>function</kbd> `hydra_utils.get_default_config`

```python
get_default_config(config_dir_path, config_name='config.yaml')
```

hydraを使わずにディレクトリに分割されたyamlの設定ファイルをOmegaConfに変換する

２つ以上の設定ファイルを比較するときに必要

#### Args:

 - <b>`config_dir_path`</b> (str):  config群があるディレクトリ
 - <b>`config_name`</b> (str, optional):  configのファイル名. Defaults to "config.yaml".

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

 - <b>`cfg`</b> (OmegaConf.omegaconf):  ロードしたconfigファイル

#### Returns:

- *`OmegaConf.omegaconf`*:  マージされたconfigファイル

### <kbd>function</kbd> `hydra_utils.enum_dict_keys`

```python
enum_dict_keys(base, base_name='')
```

dictのkeyを再帰的に列挙したリストを取得する

#### Args:

 - <b>`base`</b> (dict):  列挙するリスト
 - <b>`base_name`</b> (str, optional):  親の階層のkey．再起実行用. Defaults to "".

#### Returns:

- *`list`*:  dictのkeyのリスト

## <kbd>module</kbd> torch_utils
kunai.torch

## <kbd>module</kbd> torch_utils.cuda

### <kbd>function</kbd> `torch_utils.set_device`

```python
set_device(global_gpu_index, is_cpu=False, pci_device_order=True)
```

Set use GPU or CPU Device

set using GPU or CPU Device(instead of CUDA_VISIBLE_DEVICES).set also CUDNN.

#### Args:

 - <b>`global_gpu_index`</b> (int):  using gpu number in all gpu.
 - <b>`is_cpu`</b> (bool, optional):  use cpu or not. Defaults to False.
 - <b>`pci_device_order`</b> (bool, optional):  . Defaults to True.

#### Returns:

- *`torch.device`*:  use device object.

### <kbd>function</kbd> `torch_utils.cuda_info`

```python
cuda_info(global_cuda_index=0)
```

show using GPU Info

#### Args:

 - <b>`global_cuda_index`</b> (int, optional):  using GPU number in all GPU number. Defaults to 0.

### <kbd>function</kbd> `torch_utils.time_synchronized`

```python
time_synchronized()
```

return time at synhronized CUDA and CPU. CUDAとCPUの計算が非同期なため，同期してから時間計算する．

#### Returns:

- *`time`*:  関数呼び出し時の時刻

## <kbd>module</kbd> torch_utils.model_util

### <kbd>function</kbd> `torch_utils.save_model`

```python
save_model(model, file_path)
```

Save PyTorch ModelPyTorchのモデルを保存するParallelにも対応

#### Args:

 - <b>`model`</b> (torch.nn.Module):  モデルオブジェクト
 - <b>`file_path`</b> (str):  保存先

### <kbd>function</kbd> `torch_utils.save_model_info`

```python
save_model_info(output_dir, model, input_size, prefix='')
```

Output PyTorch Model Summary to log.

#### Args:

 - <b>`output_dir`</b> (string):  output log dir
 - <b>`model`</b> (torch.nn.Module):  PyTorch Model Class
 - <b>`input_size`</b> (List):  input tensor size
 - <b>`prefix`</b> (str, optional):  log file prefix output_dir/model_summary_{prefix}.log. Defaults to "".

### <kbd>function</kbd> `torch_utils.check_model_parallel`

```python
check_model_parallel(model)
```

check model is parallel or single

#### Args:

 - <b>`model`</b> (torch.nn.Module):  Model file

#### Returns:

- *`bool`*:  parallel = True, single = False

## <kbd>module</kbd> torch_utils.seed

### <kbd>function</kbd> `torch_utils.worker_init_fn`

```python
worker_init_fn(worker_id)
```

Reset numpy random seed in PyTorch Dataloader

#### Args:

 - <b>`worker_id`</b> (int):  random seed value

### <kbd>function</kbd> `torch_utils.fix_seed`

```python
fix_seed(seed)
```

fix seed on random, numpy, torch module

#### Args:

 - <b>`seed`</b> (int):  seed parameter

#### Returns:

- *`int`*:  seed parameter

## <kbd>module</kbd> utils

## <kbd>module</kbd> utils.graph

### <kbd>function</kbd> `utils.draw_image_graph`

```python
draw_image_graph(images, captions, filename, row, col, all_title='', dpi=150)
```

matplotlibで画像を並べたグラフを保存する

#### Args:

 - <b>`images`</b> (list[np.ndarray]):  画像のリスト
 - <b>`captions`</b> (list[str]):  各画像につけるキャプションのリスト
 - <b>`filename`</b> (str):  図を保存するPath
 - <b>`row`</b> (int):  行
 - <b>`col`</b> (int):  列
 - <b>`all_title`</b> (str, optional):  図全体のキャプション. Defaults to "".
 - <b>`dpi`</b> (int, optional):  保存する図のDPI. Defaults to 150.

### <kbd>function</kbd> `utils.fig_to_numpy`

```python
fig_to_numpy(fig)
```

Matplotlibのfigureをnumpy arrayに変換

#### Args:

 - <b>`fig`</b> (fig):  MatplotlibのFigure

#### Returns:

- *`numpy.ndarray`*:  画像

## <kbd>module</kbd> utils.image_utils

### <kbd>function</kbd> `utils.image_viewer`

```python
image_viewer(image_list)
```

OpenCV Base Image Viewer

 Next Image: key m, d, right key Previous Image: key n, a, left key Quit: q

#### Args:

 - <b>`image_list`</b> (list[str]):  Image path list

### <kbd>function</kbd> `utils.csv_to_list`

```python
csv_to_list(path, head=False)
```

csv to 2D List

#### Args:

 - <b>`path`</b> (str):  csv path
 - <b>`head`</b> (bool, optional):  Skip CSV header. Defaults to False.

#### Returns:

- *`List`*:  2D List

### <kbd>function</kbd> `utils.get_cmd`

```python
get_cmd()
```

実行コマンドを取得する

#### Returns:

- *`string`*:  実行コマンド

#### Examples:

get_cmd()
    -> python hoge.py --huga

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

 - <b>`token`</b> (str):  Slack Token
 - <b>`channel`</b> (str, optional):  メッセージを送る通知先. Defaults to "#通知".
 - <b>`username`</b> (str, optional):  メッセージを送るユーザーの名前. Defaults to "通知".
 - <b>`message`</b> (str, optional):  send message. Defaults to "".

#### Returns:

- *`int`*:  http status code

### <kbd>function</kbd> `utils.setup_logger`

```python
setup_logger(rank, log_path)
```

loggerのセットアップをする
```python

# write first on python script file
import logging
logger = logging.getLogger()

# logging
logger.info("test log")

# output
[2021-12-22 19:48:45,027][INFO] test log

```

#### Args:

 - <b>`rank`</b> (int):  ログを記録するプロセスのランク．masterなら-1か0を設定．
 - <b>`log_path`</b> (str):  ログの保存先

### <kbd>function</kbd> `utils.make_output_dirs`

```python
make_output_dirs(output_base_path: str, prefix='', child_dirs=None) → str
```

mkdir YYYYMMDD_HHmmSS (+ _prefix)

#### Args:

 - <b>`output_base_path`</b> (str):  make output dir path.
 - <b>`prefix`</b> (str, optional):  add prefix mkdir. Defaults to "".
 - <b>`child_dirs`</b> ([type], optional):  mkdir child dir list. Defaults to None.

#### Returns:

- *`str`*:  YYYYMMDD_HHmmSS

#### Examples:

```python
out = make_output_dirs("./result", prefix="MODEL", child_dirs=["models", "figs"])

./result/21010812_120000
├── models
└── figs

```

### <kbd>function</kbd> `utils.atoi`

```python
atoi(text)
```

### <kbd>function</kbd> `utils.natural_keys`

```python
natural_keys(text)
```

### <kbd>function</kbd> `utils.numerical_sort`

```python
numerical_sort(list)
```

Numerical sort

#### Args:

 - <b>`list`</b> (list[str]):  sort elements

#### Returns:

- *`list`*:  sorted list
