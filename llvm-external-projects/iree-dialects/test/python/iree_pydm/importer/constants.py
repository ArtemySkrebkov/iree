# RUN: %PYTHON %s | iree-dialects-opt | FileCheck --enable-var-scope --dump-input-filter=all %s

from typing import List
from mlir.dialects.iree_pydm.importer.test_util import *


# CHECK-LABEL: @const_integer
# CHECK: iree_pydm.constant 1 : si64 -> !iree_pydm.integer
@test_import_global
def const_integer():
  return 1


# CHECK-LABEL: @const_float
# CHECK: iree_pydm.constant 2.200000e+00 : f64 -> !iree_pydm.real
@test_import_global
def const_float():
  return 2.2


# CHECK-LABEL: @const_str
# CHECK: iree_pydm.constant "Hello" -> !iree_pydm.str
@test_import_global
def const_str():
  return "Hello"


# CHECK-LABEL: @const_bytes
# CHECK: iree_pydm.constant "Bonjour" -> !iree_pydm.bytes
@test_import_global
def const_bytes():
  return b"Bonjour"


# CHECK-LABEL: @const_none
# CHECK: iree_pydm.none -> !iree_pydm.none
@test_import_global
def const_none():
  return None


# CHECK-LABEL: @const_true
# CHECK: iree_pydm.constant true -> !iree_pydm.bool
@test_import_global
def const_true():
  return True


# CHECK-LABEL: @const_false
# CHECK: iree_pydm.constant false -> !iree_pydm.bool
@test_import_global
def const_false():
  return False
