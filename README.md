# kunai

My Python Package

## API

### kunai.torch

required `pip install torch torchinfo`

```python
from kunai.torch import (
    cuda_info,
    set_device,
    time_synchronized,
    save_model,
    save_model_info,
    fix_seed,
    worker_init_fn,
)
```

### kunai.hydra

required `pip install hydra-core`

```python
from kunai.hydra import (
    set_hydra, validate_config, get_default_config
)
```

### kunai.utils

```python
from kunai.utils import (
    get_cmd, get_git_hash, post_slack
)
```
