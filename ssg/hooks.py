from typing import Any, Dict

_callbacks: Dict[Any, Any] = {}


def register(hook, order: int = 0) -> Any:
    def register_callback(func):
        _callbacks.setdefault(hook, {}).setdefault(order, []).append(func)
        return func

    return register_callback


def event(hook, *args) -> None:
    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[hook][order]:
            func(*args)


def filter(hook, value, *args) -> Any:
    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[hook][order]:
            value = func(value, *args)
    return value
