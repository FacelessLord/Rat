from typing import Dict, Any

from finq import FINQ
from sr_collections.readonlydict import readonlydict
from sr_collections.variable import Variable


class VariableStorage:
    def __init__(self, base: Dict[str, Variable], referenced_global=None, proxy=False):
        self.global_storage: Dict[str, Variable] = base
        self.local_storage: Dict[str, Variable] = {}
        if not referenced_global:
            self.referenced_global = []
        self.is_proxy = proxy

    def sub_proxy_storage(self):
        return VariableStorage(readonlydict({**self.global_storage, **self.local_storage}),
                               self.referenced_global, True)

    def sub_storage(self):
        return VariableStorage({**self.global_storage, **self.local_storage}, self.referenced_global, False)

    def get_variable(self, key):
        if key in self.local_storage:
            return self.local_storage[key]
        elif key in self.global_storage:
            return self.global_storage[key]
        return None

    def get_value(self, key):
        variable = self.get_variable(key)
        if variable:
            return variable.get_value()
        else:
            raise ValueError(f"Variable '{key}' is referenced before assignment")

    def reference_global(self, key):
        self.referenced_global.append(key)

    def set_value(self, key, value):
        if not self.is_proxy:
            if key in self.referenced_global:
                self.global_storage[key].set_value(value)
            elif key in self.local_storage:
                self.local_storage[key].set_value(value)
            else:
                raise ValueError(f"Variable '{key}' does not exist")
        else:
            raise ValueError(f"Variable '{key}' is not mutable in this scope")

    def create_variable(self, name: str, value):
        if self.variable_locally_bound(name):
            return self.get_variable(name)
        self.local_storage[name] = Variable(name, value)

    def bind_variable(self, variable: Variable):
        if not self.variable_bound(variable.name):
            self.local_storage[variable.name] = variable
            variable.storage = self
        else:
            raise ValueError(f"Redefined varialble '{variable.name}'")

    def variable_bound(self, variable_name: str):
        return self.variable_locally_bound(variable_name) or self.variable_globally_bound(variable_name)

    def variable_locally_bound(self, variable_name: str):
        return variable_name in self.local_storage

    def variable_globally_bound(self, variable_name: str):
        return variable_name in self.global_storage

    def __str__(self):
        return "g[" + FINQ(self.global_storage.values()) \
            .map(lambda v: str(v.name) + ':' + str(v.value)).join_str(';\n') + "]\n" + \
               "l[" + FINQ(self.local_storage.values()) \
                   .map(lambda v: str(v.name) + ':' + str(v.value)).join_str(';\n') + "]"
