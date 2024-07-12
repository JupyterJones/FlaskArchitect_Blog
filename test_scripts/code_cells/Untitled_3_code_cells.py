/home/jack/miniconda3/envs/bakup-clonebase/lib/python3.9/site-packages/PyQt6/Qt6/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/bakup-clonebase/lib/python3.9/site-packages/PySide2-5.15.2.1-py3.9-linux-x86_64.egg/PySide2/Qt/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/bakup-clonebase/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/cloned_base/lib/python3.9/site-packages/PyQt5/Qt5/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/cloned_base/lib/python3.9/site-packages/PyQt6/Qt6/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/cloned_base/lib/python3.9/site-packages/PySide2/Qt/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/cloned_base/lib/python3.9/site-packages/PySide6/Qt/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/cloned_base/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/cloned_py31/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/py31/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/py36/lib/python3.6/site-packages/PySide2/Qt/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/py37/lib/python3.7/site-packages/PyQt5_Qt5-5.15.2-py3.7-linux-x86_64.egg/PyQt5/Qt5/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/py37/lib/python3.7/site-packages/PyQt6/Qt6/plugins/platforms/libqvnc.so
/home/jack/miniconda3/envs/py37/plugins/platforms/libqvnc.so
/home/jack/miniconda3/lib/python3.9/site-packages/PySide2/Qt/plugins/platforms/libqvnc.so
/home/jack/miniconda3/pkgs/qt-5.12.9-hda022c4_4/plugins/platforms/libqvnc.so
/home/jack/miniconda3/pkgs/qt-main-5.15.2-h327a75a_7/plugins/platforms/libqvnc.so
/home/jack/miniconda3/plugins/platforms/libqvnc.so
/usr/lib/x86_64-linux-gnu/qt5/plugins/platforms/libqvnc.so


import NodeGraphQt
graph = NodeGraphQt.NodeGraph()

import NodeGraphQt

# create a node graph controller
graph = NodeGraphQt.NodeGraph()

# create two nodes
node1 = graph.create_node("NodeGraphQt.Nodes.Math.Add")
node2 = graph.create_node("NodeGraphQt.Nodes.Math.Multiply")

# connect the nodes by drag-and-drop
node1.output(0).connect_to(node2.input(0))

# show the node graph widget
graph.widget.show()


import os
import signal

from Qt import QtCore, QtWidgets

from NodeGraphQt import (
    NodeGraph,
    PropertiesBinWidget,
    NodesTreeWidget,
    NodesPaletteWidget
)
from nodes import basic_nodes, custom_ports_node, group_node, widget_nodes

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import signal

from Qt import QtCore, QtWidgets

from NodeGraphQt import (
    NodeGraph,
    PropertiesBinWidget,
    NodesTreeWidget,
    NodesPaletteWidget
)

# import example nodes from the "example_nodes" package
from nodes import basic_nodes, custom_ports_node, group_node, widget_nodes

if __name__ == '__main__':

    # handle SIGINT to make the app terminate on CTRL+C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QtWidgets.QApplication([])

    # create graph controller.
    graph = NodeGraph()

    # set up context menu for the node graph.
    graph.set_context_menu_from_file('../examples/hotkeys/hotkeys.json')

    # registered example nodes.
    graph.register_nodes([
        basic_nodes.BasicNodeA,
        basic_nodes.BasicNodeB,
        custom_ports_node.CustomPortsNode,
        group_node.MyGroupNode,
        widget_nodes.DropdownMenuNode,
        widget_nodes.TextInputNode,
        widget_nodes.CheckboxNode
    ])

    # show the node graph widget.
    graph_widget = graph.widget
    graph_widget.resize(1100, 800)
    graph_widget.show()

    # create node with custom text color and disable it.
    n_basic_a = graph.create_node(
        'nodes.basic.BasicNodeA', text_color='#feab20')
    n_basic_a.set_disabled(True)

    # create node and set a custom icon.
    n_basic_b = graph.create_node(
        'nodes.basic.BasicNodeB', name='custom icon')
    this_path = os.path.dirname(os.path.abspath(__file__))
    icon = os.path.join(this_path, 'examples', 'star.png')
    n_basic_b.set_icon(icon)

    # create node with the custom port shapes.
    n_custom_ports = graph.create_node(
        'nodes.custom.ports.CustomPortsNode', name='custom ports')

    # create node with the embedded QLineEdit widget.
    n_text_input = graph.create_node(
        'nodes.widget.TextInputNode', name='text node', color='#0a1e20')

    # create node with the embedded QCheckBox widgets.
    n_checkbox = graph.create_node(
        'nodes.widget.CheckboxNode', name='checkbox node')

    # create node with the QComboBox widget.
    n_combo_menu = graph.create_node(
        'nodes.widget.DropdownMenuNode', name='combobox node')

    # create group node.
    n_group = graph.create_node('nodes.group.MyGroupNode')

    # make node connections.

    # (connect nodes using the .set_output method)
    n_text_input.set_output(0, n_custom_ports.input(0))
    n_text_input.set_output(0, n_checkbox.input(0))
    n_text_input.set_output(0, n_combo_menu.input(0))
    # (connect nodes using the .set_input method)
    n_group.set_input(0, n_custom_ports.output(1))
    n_basic_b.set_input(2, n_checkbox.output(0))
    n_basic_b.set_input(2, n_combo_menu.output(1))
    # (connect nodes using the .connect_to method from the port object)
    port = n_basic_a.input(0)
    port.connect_to(n_basic_b.output(0))

    # auto layout nodes.
    graph.auto_layout_nodes()

    # crate a backdrop node and wrap it around
    # "custom port node" and "group node".
    n_backdrop = graph.create_node('Backdrop')
    n_backdrop.wrap_nodes([n_custom_ports, n_combo_menu])

    # fit nodes to the viewer.
    graph.clear_selection()
    graph.fit_to_selection()

    # Custom builtin widgets from NodeGraphQt
    # ---------------------------------------

    # create a node properties bin widget.
    properties_bin = PropertiesBinWidget(node_graph=graph)
    properties_bin.setWindowFlags(QtCore.Qt.Tool)

    # example show the node properties bin widget when a node is double clicked.
    def display_properties_bin(node):
        if not properties_bin.isVisible():
            properties_bin.show()

    # wire function to "node_double_clicked" signal.
    graph.node_double_clicked.connect(display_properties_bin)

    # create a nodes tree widget.
    nodes_tree = NodesTreeWidget(node_graph=graph)
    nodes_tree.set_category_label('nodeGraphQt.nodes', 'Builtin Nodes')
    nodes_tree.set_category_label('nodes.custom.ports', 'Custom Port Nodes')
    nodes_tree.set_category_label('nodes.widget', 'Widget Nodes')
    nodes_tree.set_category_label('nodes.basic', 'Basic Nodes')
    nodes_tree.set_category_label('nodes.group', 'Group Nodes')
    # nodes_tree.show()

    # create a node palette widget.
    nodes_palette = NodesPaletteWidget(node_graph=graph)
    nodes_palette.set_category_label('nodeGraphQt.nodes', 'Builtin Nodes')
    nodes_palette.set_category_label('nodes.custom.ports', 'Custom Port Nodes')
    nodes_palette.set_category_label('nodes.widget', 'Widget Nodes')
    nodes_palette.set_category_label('nodes.basic', 'Basic Nodes')
    nodes_palette.set_category_label('nodes.group', 'Group Nodes')
    # nodes_palette.show()

    app.exec_()




