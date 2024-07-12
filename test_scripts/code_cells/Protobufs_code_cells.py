from onnx import *

# Int Attibute
arg = helper.make_attribute("this_is_an_int", 1701)
print("\nInt attribute:\n")
print(arg)

#NBVAL_IGNORE_OUTPUT
# Float Attribute
arg = helper.make_attribute("this_is_a_float", 3.14)
print("\nFloat attribute:\n")
print(arg)

# String Attribute
arg = helper.make_attribute("this_is_a_string", "string_content")
print("\nString attribute:\n")
print(arg)

# Repeated Attribute
arg = helper.make_attribute("this_is_a_repeated_int", [1, 2, 3, 4])
print("\nRepeated int attribute:\n")
print(arg)

# node
node_proto = helper.make_node("Relu", ["X"], ["Y"])

print("\nNodeProto:\n")
print(node_proto)

# node with args
node_proto = helper.make_node(
    "Conv", ["X", "W", "B"], ["Y"],
    kernel=3, stride=1, pad=1)

# This is just for making the attributes to be printed in order
node_proto.attribute.sort(key=lambda attr: attr.name)
print("\nNodeProto:\n")
print(node_proto)

print("\nMore Readable NodeProto (no args yet):\n")
print(helper.printable_node(node_proto))

# graph
graph_proto = helper.make_graph(
    [
        helper.make_node("FC", ["X", "W1", "B1"], ["H1"]),
        helper.make_node("Relu", ["H1"], ["R1"]),
        helper.make_node("FC", ["R1", "W2", "B2"], ["Y"]),
    ],
    "MLP",
    [
        helper.make_tensor_value_info('X' , TensorProto.FLOAT, [1]),
        helper.make_tensor_value_info('W1', TensorProto.FLOAT, [1]),
        helper.make_tensor_value_info('B1', TensorProto.FLOAT, [1]),
        helper.make_tensor_value_info('W2', TensorProto.FLOAT, [1]),
        helper.make_tensor_value_info('B2', TensorProto.FLOAT, [1]),
    ],
    [
        helper.make_tensor_value_info('Y', TensorProto.FLOAT, [1]),
    ]
)

print("\ngraph proto:\n")
print(graph_proto)

print("\nMore Readable GraphProto:\n")
print(helper.printable_graph(graph_proto))

# An node that is also a graph
graph_proto = helper.make_graph(
    [
        helper.make_node("FC", ["X", "W1", "B1"], ["H1"]),
        helper.make_node("Relu", ["H1"], ["R1"]),
        helper.make_node("FC", ["R1", "W2", "B2"], ["Y"]),
    ],
    "MLP",
    [
        helper.make_tensor_value_info('X' , TensorProto.FLOAT, [1]),
        helper.make_tensor_value_info('W1', TensorProto.FLOAT, [1]),
        helper.make_tensor_value_info('B1', TensorProto.FLOAT, [1]),
        helper.make_tensor_value_info('W2', TensorProto.FLOAT, [1]),
        helper.make_tensor_value_info('B2', TensorProto.FLOAT, [1]),
    ],
    [
        helper.make_tensor_value_info('Y', TensorProto.FLOAT, [1]),
    ]
)

# output = ThisSpecificgraph([input, w1, b1, w2, b2])
node_proto = helper.make_node(
    "graph",
    ["Input", "W1", "B1", "W2", "B2"],
    ["Output"],
    graph=[graph_proto],
)

print("\nNodeProto that contains a graph:\n")
print(node_proto)

