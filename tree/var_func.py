from Logger import warn
from finq import FINQ
from sr_collections.variable_storage import VariableStorage
from tree.node import TreeNode


class VarFunctionNode(TreeNode):
    def interpret(self, variable_storage: VariableStorage):
        func_var = self.children[0].interpret(variable_storage)
        args = self.children[1].interpret(variable_storage)

        argNames = FINQ(func_var.func_args).map(lambda n: n.name).to_list()
        modifiers = func_var.func_modifiers

        sub_variable_storage = variable_storage.sub_storage() if 'mut' in modifiers \
            else variable_storage.sub_proxy_storage()

        if len(args) < len(argNames):
            raise ValueError(f"Mismatched argument count: expected {len(argNames)}, got {len(args)}")
        if len(args) > len(argNames):
            warn(f"Excess arguments found: expected {len(argNames)}, got {len(args)}")

        FINQ(args).zip(argNames) \
            .for_each(lambda v: sub_variable_storage.create_variable(v[1], v[0]))

        return func_var(sub_variable_storage)
