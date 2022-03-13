# kunai

My Python Package for Research and Utils.

## Install

```bash
pip install git+ssh://git@github.com/mjun0812/kunai.git

# upgrade
pip install git+ssh://git@github.com/mjun0812/kunai.git -U

# editable(recommend)
git clone https://github.com/mjun0812/kunai.git
cd kunai
pip install -e .
```

## API Overview

### kunai.Registry

```python
from kunai import Registry
```

### kunai.torch_utils

required `pip install torch torchinfo`

```python
from kunai.torch_utils import (
    cuda_info,
    set_device,
    time_synchronized,
    save_model,
    save_model_info,
    fix_seed,
    worker_init_fn,
)
```

### kunai.hydra_utils

required `pip install hydra-core`

```python
from kunai.hydra_utils import get_default_config, set_hydra, validate_config
```

### kunai.utils

```python
from kunai.utils import (
    get_cmd,
    get_git_hash,
    post_slack,
    image_viewer,
    setup_logger,
    numerical_sort,
    make_output_dirs,
    csv_to_list,
    fig_to_numpy,
    draw_image_graph,
)
```

## API Documentation

[Here](./docs/doc.md)
