from contexts.types import ContextType
from finq import FINQ
from sr_collections.variable_storage import VariableStorage
from tree.node import TreeNode

bin_operations = ['+', '-', '*', '/', '**']


class AlgebraicExpressionNode(TreeNode):
    def interpret(self, variable_storage: VariableStorage):
        sub_vars = variable_storage.sub_storage()
        sub_vars.create_variable("$()", True)
        v = FINQ(self.children).map(lambda c: c.interpret(variable_storage)) \
            .map(lambda v: "\"" + v + "\"" if isinstance(v, str) and v not in bin_operations else v) \
            .map(str).join_str(' ')
        return eval(v)

    @staticmethod
    def get_type():
        return ContextType.algebraic_expression
