import sys
from typing import Any

if sys.version_info < (3, 7):
    from typing import Callable as Callable

    NoArgAnyCallable = Callable[[], Any]
else:
    from collections.abc import Callable as Callable
    from typing import Callable as TypingCallable

    NoArgAnyCallable = TypingCallable[[], Any]
