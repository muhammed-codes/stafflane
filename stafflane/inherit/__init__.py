"""
stafflane/inherit/

Extension infrastructure for Stafflane — model field injection and CBV replacement.

Key public symbols re-exported here for convenience:

    from stafflane.inherit import StafflaneViewInheritMixin   # view extension
    from stafflane.inherit import StafflaneModelBase           # model metaclass
    from stafflane.inherit import INJECTION_MAP              # migration routing
    from stafflane.inherit import VIEW_REGISTRY              # registered views
"""

from stafflane.inherit.extension_registry import INJECTION_MAP
from stafflane.inherit.model_inherit import EXTENSION_REGISTRY, StafflaneModelBase
from stafflane.inherit.view_inherit import StafflaneViewInheritMixin
from stafflane.inherit.view_registry import VIEW_REGISTRY

__all__ = [
    "StafflaneViewInheritMixin",
    "StafflaneModelBase",
    "INJECTION_MAP",
    "EXTENSION_REGISTRY",
    "VIEW_REGISTRY",
]
