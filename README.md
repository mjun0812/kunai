# kunai

My Python Package for Research and Utils.

## Install

```bash
pip install git+ssh://git@github.com/mjun0812/kunai.git

# upgrade
pip install git+ssh://git@github.com/mjun0812/kunai.git -U

# editable(recommend)
pip install -e .
```

## API Overview

### Registory

```python
from kunai import Registry
```

### kunai.torch_utils

required `pip install torch torchinfo`

```python
from .cuda import cuda_info, set_device, time_synchronized
from .model_util import save_model, save_model_info
from .seed import fix_seed, worker_init_fn
```

### kunai.hydra_utils

required `pip install hydra-core`

```python
from .hydra_utils import get_default_config, set_hydra, validate_config

```

### kunai.utils

```python
from .utils import get_cmd, get_git_hash, post_slack, setup_logger, numerical_sort, make_output_dirs, csv_to_list
from .graph import draw_image_graph, fig_to_numpy
```

## API Documentation

[Here](./docs/doc.md)
