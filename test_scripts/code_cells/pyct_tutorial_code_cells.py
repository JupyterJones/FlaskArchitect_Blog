!pip install tf-nightly

import gast
from tensorflow.python.autograph.pyct import transformer

class BasicCppCodegen(transformer.CodeGenerator):

  def visit_Name(self, node):
    self.emit(node.id)

  def visit_arguments(self, node):
    self.visit(node.args[0])
    for arg in node.args[1:]:
      self.emit(', ')
      self.visit(arg)

  def visit_FunctionDef(self, node):
    self.emit('void {}'.format(node.name))
    self.emit('(')
    self.visit(node.args)
    self.emit(') {\n')
    self.visit_block(node.body)
    self.emit('\n}')

  def visit_Call(self, node):
    self.emit(node.func.id)
    self.emit('(')
    self.visit(node.args[0])
    for arg in node.args[1:]:
      self.emit(', ')
      self.visit(arg)
    self.emit(');')


import gast
from tensorflow.python.autograph.pyct import transpiler

class PyToBasicCpp(transpiler.GenericTranspiler):

  def transform_ast(self, node, ctx):
    codegen = BasicCppCodegen(ctx)
    codegen.visit(node)
    return codegen.code_buffer

def f(x, y):
  print(x, y)

code, _ = PyToBasicCpp().transform(f, None)
print(code)

def get_node_and_ctx(f):
  node, source = parser.parse_entity(f, ())
  f_info = transformer.EntityInfo(
    name='f',
    source_code=source,
    source_file=None,
    future_features=(),
    namespace=None)
  ctx = transformer.Context(f_info, None, None)
  return node, ctx

from tensorflow.python.autograph.pyct import anno
from tensorflow.python.autograph.pyct import parser
from tensorflow.python.autograph.pyct import qual_names
from tensorflow.python.autograph.pyct.static_analysis import annos
from tensorflow.python.autograph.pyct.static_analysis import activity


def f(a):
  b = a + 1
  return b


node, ctx = get_node_and_ctx(f)

node = qual_names.resolve(node)
node = activity.resolve(node, ctx)

fn_scope = anno.getanno(node, annos.NodeAnno.BODY_SCOPE)  # Note: tag will be changed soon.


print('read:', fn_scope.read)
print('modified:', fn_scope.modified)

from tensorflow.python.autograph.pyct import cfg


def f(a):
  if a > 0:
    return a
  b = -a

node, ctx = get_node_and_ctx(f)

node = qual_names.resolve(node)
cfgs = cfg.build(node)
cfgs[node]

from tensorflow.python.autograph.pyct import anno
from tensorflow.python.autograph.pyct import cfg
from tensorflow.python.autograph.pyct import qual_names
from tensorflow.python.autograph.pyct.static_analysis import annos
from tensorflow.python.autograph.pyct.static_analysis import reaching_definitions
from tensorflow.python.autograph.pyct.static_analysis import reaching_fndefs
from tensorflow.python.autograph.pyct.static_analysis import liveness


def f(a):
  b = a + 1
  return b


node, ctx = get_node_and_ctx(f)

node = qual_names.resolve(node)
cfgs = cfg.build(node)
node = activity.resolve(node, ctx)
node = reaching_definitions.resolve(node, ctx, cfgs)
node = reaching_fndefs.resolve(node, ctx, cfgs)
node = liveness.resolve(node, ctx, cfgs)

print('live into `b = a + 1`:', anno.getanno(node.body[0], anno.Static.LIVE_VARS_IN))
print('live into `return b`:', anno.getanno(node.body[1], anno.Static.LIVE_VARS_IN))

from tensorflow.python.autograph.pyct import transpiler


class NoopTranspiler(transpiler.PyToPy):

  def get_caching_key(self, ctx):
    # You may return different caching keys if the transformation may generate
    # code versions.
    return 0

  def get_extra_locals(self):
    # No locals needed for now; see below.
    return {}

  def transform_ast(self, ast, transformer_context):
    return ast

tr = NoopTranspiler()

def f(x, y):
  return x + y


new_f, module, source_map = tr.transform(f, None)

new_f(1, 1)

from tensorflow.python.autograph.pyct import parser


class HelloTranspiler(transpiler.PyToPy):

  def get_caching_key(self, ctx):
    return 0

  def get_extra_locals(self):
    return {'name': 'you'}

  def transform_ast(self, ast, transformer_context):
    print_code = parser.parse('print("Hello", name)')
    ast.body = [print_code] + ast.body
    return ast


def f(x, y):
  pass

new_f, _, _ = HelloTranspiler().transform(f, None)

_ = new_f(1, 1)

import inspect

print(inspect.getsource(new_f))

