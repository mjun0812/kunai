# API

Update: 2021-12-31 14:09

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
