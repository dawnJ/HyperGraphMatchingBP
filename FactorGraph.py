# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_FactorGraph', [dirname(__file__)])
        except ImportError:
            import _FactorGraph
            return _FactorGraph
        if fp is not None:
            try:
                _mod = imp.load_module('_FactorGraph', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _FactorGraph = swig_import_helper()
    del swig_import_helper
else:
    import _FactorGraph
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _FactorGraph.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _FactorGraph.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _FactorGraph.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _FactorGraph.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _FactorGraph.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _FactorGraph.SwigPyIterator_equal(self, x)

    def copy(self):
        return _FactorGraph.SwigPyIterator_copy(self)

    def next(self):
        return _FactorGraph.SwigPyIterator_next(self)

    def __next__(self):
        return _FactorGraph.SwigPyIterator___next__(self)

    def previous(self):
        return _FactorGraph.SwigPyIterator_previous(self)

    def advance(self, n):
        return _FactorGraph.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _FactorGraph.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _FactorGraph.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _FactorGraph.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _FactorGraph.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _FactorGraph.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _FactorGraph.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _FactorGraph.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _FactorGraph.new_intArray(nelements)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _FactorGraph.delete_intArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _FactorGraph.intArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _FactorGraph.intArray___setitem__(self, index, value)

    def cast(self):
        return _FactorGraph.intArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _FactorGraph.intArray_frompointer
    if _newclass:
        frompointer = staticmethod(_FactorGraph.intArray_frompointer)
intArray_swigregister = _FactorGraph.intArray_swigregister
intArray_swigregister(intArray)

def intArray_frompointer(t):
    return _FactorGraph.intArray_frompointer(t)
intArray_frompointer = _FactorGraph.intArray_frompointer

class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _FactorGraph.new_doubleArray(nelements)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _FactorGraph.delete_doubleArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _FactorGraph.doubleArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _FactorGraph.doubleArray___setitem__(self, index, value)

    def cast(self):
        return _FactorGraph.doubleArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _FactorGraph.doubleArray_frompointer
    if _newclass:
        frompointer = staticmethod(_FactorGraph.doubleArray_frompointer)
doubleArray_swigregister = _FactorGraph.doubleArray_swigregister
doubleArray_swigregister(doubleArray)

def doubleArray_frompointer(t):
    return _FactorGraph.doubleArray_frompointer(t)
doubleArray_frompointer = _FactorGraph.doubleArray_frompointer

class VecInt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecInt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecInt, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _FactorGraph.VecInt_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _FactorGraph.VecInt___nonzero__(self)

    def __bool__(self):
        return _FactorGraph.VecInt___bool__(self)

    def __len__(self):
        return _FactorGraph.VecInt___len__(self)

    def __getslice__(self, i, j):
        return _FactorGraph.VecInt___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _FactorGraph.VecInt___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _FactorGraph.VecInt___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _FactorGraph.VecInt___delitem__(self, *args)

    def __getitem__(self, *args):
        return _FactorGraph.VecInt___getitem__(self, *args)

    def __setitem__(self, *args):
        return _FactorGraph.VecInt___setitem__(self, *args)

    def pop(self):
        return _FactorGraph.VecInt_pop(self)

    def append(self, x):
        return _FactorGraph.VecInt_append(self, x)

    def empty(self):
        return _FactorGraph.VecInt_empty(self)

    def size(self):
        return _FactorGraph.VecInt_size(self)

    def swap(self, v):
        return _FactorGraph.VecInt_swap(self, v)

    def begin(self):
        return _FactorGraph.VecInt_begin(self)

    def end(self):
        return _FactorGraph.VecInt_end(self)

    def rbegin(self):
        return _FactorGraph.VecInt_rbegin(self)

    def rend(self):
        return _FactorGraph.VecInt_rend(self)

    def clear(self):
        return _FactorGraph.VecInt_clear(self)

    def get_allocator(self):
        return _FactorGraph.VecInt_get_allocator(self)

    def pop_back(self):
        return _FactorGraph.VecInt_pop_back(self)

    def erase(self, *args):
        return _FactorGraph.VecInt_erase(self, *args)

    def __init__(self, *args):
        this = _FactorGraph.new_VecInt(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _FactorGraph.VecInt_push_back(self, x)

    def front(self):
        return _FactorGraph.VecInt_front(self)

    def back(self):
        return _FactorGraph.VecInt_back(self)

    def assign(self, n, x):
        return _FactorGraph.VecInt_assign(self, n, x)

    def resize(self, *args):
        return _FactorGraph.VecInt_resize(self, *args)

    def insert(self, *args):
        return _FactorGraph.VecInt_insert(self, *args)

    def reserve(self, n):
        return _FactorGraph.VecInt_reserve(self, n)

    def capacity(self):
        return _FactorGraph.VecInt_capacity(self)
    __swig_destroy__ = _FactorGraph.delete_VecInt
    __del__ = lambda self: None
VecInt_swigregister = _FactorGraph.VecInt_swigregister
VecInt_swigregister(VecInt)

class VecVecInt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecVecInt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecVecInt, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _FactorGraph.VecVecInt_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _FactorGraph.VecVecInt___nonzero__(self)

    def __bool__(self):
        return _FactorGraph.VecVecInt___bool__(self)

    def __len__(self):
        return _FactorGraph.VecVecInt___len__(self)

    def __getslice__(self, i, j):
        return _FactorGraph.VecVecInt___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _FactorGraph.VecVecInt___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _FactorGraph.VecVecInt___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _FactorGraph.VecVecInt___delitem__(self, *args)

    def __getitem__(self, *args):
        return _FactorGraph.VecVecInt___getitem__(self, *args)

    def __setitem__(self, *args):
        return _FactorGraph.VecVecInt___setitem__(self, *args)

    def pop(self):
        return _FactorGraph.VecVecInt_pop(self)

    def append(self, x):
        return _FactorGraph.VecVecInt_append(self, x)

    def empty(self):
        return _FactorGraph.VecVecInt_empty(self)

    def size(self):
        return _FactorGraph.VecVecInt_size(self)

    def swap(self, v):
        return _FactorGraph.VecVecInt_swap(self, v)

    def begin(self):
        return _FactorGraph.VecVecInt_begin(self)

    def end(self):
        return _FactorGraph.VecVecInt_end(self)

    def rbegin(self):
        return _FactorGraph.VecVecInt_rbegin(self)

    def rend(self):
        return _FactorGraph.VecVecInt_rend(self)

    def clear(self):
        return _FactorGraph.VecVecInt_clear(self)

    def get_allocator(self):
        return _FactorGraph.VecVecInt_get_allocator(self)

    def pop_back(self):
        return _FactorGraph.VecVecInt_pop_back(self)

    def erase(self, *args):
        return _FactorGraph.VecVecInt_erase(self, *args)

    def __init__(self, *args):
        this = _FactorGraph.new_VecVecInt(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _FactorGraph.VecVecInt_push_back(self, x)

    def front(self):
        return _FactorGraph.VecVecInt_front(self)

    def back(self):
        return _FactorGraph.VecVecInt_back(self)

    def assign(self, n, x):
        return _FactorGraph.VecVecInt_assign(self, n, x)

    def resize(self, *args):
        return _FactorGraph.VecVecInt_resize(self, *args)

    def insert(self, *args):
        return _FactorGraph.VecVecInt_insert(self, *args)

    def reserve(self, n):
        return _FactorGraph.VecVecInt_reserve(self, n)

    def capacity(self):
        return _FactorGraph.VecVecInt_capacity(self)
    __swig_destroy__ = _FactorGraph.delete_VecVecInt
    __del__ = lambda self: None
VecVecInt_swigregister = _FactorGraph.VecVecInt_swigregister
VecVecInt_swigregister(VecVecInt)

class VecDouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecDouble, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _FactorGraph.VecDouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _FactorGraph.VecDouble___nonzero__(self)

    def __bool__(self):
        return _FactorGraph.VecDouble___bool__(self)

    def __len__(self):
        return _FactorGraph.VecDouble___len__(self)

    def __getslice__(self, i, j):
        return _FactorGraph.VecDouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _FactorGraph.VecDouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _FactorGraph.VecDouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _FactorGraph.VecDouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _FactorGraph.VecDouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _FactorGraph.VecDouble___setitem__(self, *args)

    def pop(self):
        return _FactorGraph.VecDouble_pop(self)

    def append(self, x):
        return _FactorGraph.VecDouble_append(self, x)

    def empty(self):
        return _FactorGraph.VecDouble_empty(self)

    def size(self):
        return _FactorGraph.VecDouble_size(self)

    def swap(self, v):
        return _FactorGraph.VecDouble_swap(self, v)

    def begin(self):
        return _FactorGraph.VecDouble_begin(self)

    def end(self):
        return _FactorGraph.VecDouble_end(self)

    def rbegin(self):
        return _FactorGraph.VecDouble_rbegin(self)

    def rend(self):
        return _FactorGraph.VecDouble_rend(self)

    def clear(self):
        return _FactorGraph.VecDouble_clear(self)

    def get_allocator(self):
        return _FactorGraph.VecDouble_get_allocator(self)

    def pop_back(self):
        return _FactorGraph.VecDouble_pop_back(self)

    def erase(self, *args):
        return _FactorGraph.VecDouble_erase(self, *args)

    def __init__(self, *args):
        this = _FactorGraph.new_VecDouble(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _FactorGraph.VecDouble_push_back(self, x)

    def front(self):
        return _FactorGraph.VecDouble_front(self)

    def back(self):
        return _FactorGraph.VecDouble_back(self)

    def assign(self, n, x):
        return _FactorGraph.VecDouble_assign(self, n, x)

    def resize(self, *args):
        return _FactorGraph.VecDouble_resize(self, *args)

    def insert(self, *args):
        return _FactorGraph.VecDouble_insert(self, *args)

    def reserve(self, n):
        return _FactorGraph.VecDouble_reserve(self, n)

    def capacity(self):
        return _FactorGraph.VecDouble_capacity(self)
    __swig_destroy__ = _FactorGraph.delete_VecDouble
    __del__ = lambda self: None
VecDouble_swigregister = _FactorGraph.VecDouble_swigregister
VecDouble_swigregister(VecDouble)

class VecVecdouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecVecdouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecVecdouble, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _FactorGraph.VecVecdouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _FactorGraph.VecVecdouble___nonzero__(self)

    def __bool__(self):
        return _FactorGraph.VecVecdouble___bool__(self)

    def __len__(self):
        return _FactorGraph.VecVecdouble___len__(self)

    def __getslice__(self, i, j):
        return _FactorGraph.VecVecdouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _FactorGraph.VecVecdouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _FactorGraph.VecVecdouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _FactorGraph.VecVecdouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _FactorGraph.VecVecdouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _FactorGraph.VecVecdouble___setitem__(self, *args)

    def pop(self):
        return _FactorGraph.VecVecdouble_pop(self)

    def append(self, x):
        return _FactorGraph.VecVecdouble_append(self, x)

    def empty(self):
        return _FactorGraph.VecVecdouble_empty(self)

    def size(self):
        return _FactorGraph.VecVecdouble_size(self)

    def swap(self, v):
        return _FactorGraph.VecVecdouble_swap(self, v)

    def begin(self):
        return _FactorGraph.VecVecdouble_begin(self)

    def end(self):
        return _FactorGraph.VecVecdouble_end(self)

    def rbegin(self):
        return _FactorGraph.VecVecdouble_rbegin(self)

    def rend(self):
        return _FactorGraph.VecVecdouble_rend(self)

    def clear(self):
        return _FactorGraph.VecVecdouble_clear(self)

    def get_allocator(self):
        return _FactorGraph.VecVecdouble_get_allocator(self)

    def pop_back(self):
        return _FactorGraph.VecVecdouble_pop_back(self)

    def erase(self, *args):
        return _FactorGraph.VecVecdouble_erase(self, *args)

    def __init__(self, *args):
        this = _FactorGraph.new_VecVecdouble(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _FactorGraph.VecVecdouble_push_back(self, x)

    def front(self):
        return _FactorGraph.VecVecdouble_front(self)

    def back(self):
        return _FactorGraph.VecVecdouble_back(self)

    def assign(self, n, x):
        return _FactorGraph.VecVecdouble_assign(self, n, x)

    def resize(self, *args):
        return _FactorGraph.VecVecdouble_resize(self, *args)

    def insert(self, *args):
        return _FactorGraph.VecVecdouble_insert(self, *args)

    def reserve(self, n):
        return _FactorGraph.VecVecdouble_reserve(self, n)

    def capacity(self):
        return _FactorGraph.VecVecdouble_capacity(self)
    __swig_destroy__ = _FactorGraph.delete_VecVecdouble
    __del__ = lambda self: None
VecVecdouble_swigregister = _FactorGraph.VecVecdouble_swigregister
VecVecdouble_swigregister(VecVecdouble)


_FactorGraph.FACTORGRAPH_H_swigconstant(_FactorGraph)
FACTORGRAPH_H = _FactorGraph.FACTORGRAPH_H
class CFactorGraph(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CFactorGraph, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CFactorGraph, name)
    __repr__ = _swig_repr

    def SetVerbost(self, verbose):
        return _FactorGraph.CFactorGraph_SetVerbost(self, verbose)

    def AddAuctionFactor(self):
        return _FactorGraph.CFactorGraph_AddAuctionFactor(self)
    __swig_destroy__ = _FactorGraph.delete_CFactorGraph
    __del__ = lambda self: None

    def GetNofNodes(self):
        return _FactorGraph.CFactorGraph_GetNofNodes(self)

    def __init__(self, NofNodes, NofStates):
        this = _FactorGraph.new_CFactorGraph(NofNodes, NofStates)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def AddNodeBelief(self, Nid, bi):
        return _FactorGraph.CFactorGraph_AddNodeBelief(self, Nid, bi)

    def AddEdge(self, ei, ej, data):
        return _FactorGraph.CFactorGraph_AddEdge(self, ei, ej, data)

    def AddSparseEdge(self, ei, ej, data, mi, mj, nnz, nnzIdx):
        return _FactorGraph.CFactorGraph_AddSparseEdge(self, ei, ej, data, mi, mj, nnz, nnzIdx)

    def AddSparseEdgeNZ(self, ei, ej, data, mi, mj, nnz, nnzIdx):
        return _FactorGraph.CFactorGraph_AddSparseEdgeNZ(self, ei, ej, data, mi, mj, nnz, nnzIdx)
    __swig_setmethods__["m_verbose"] = _FactorGraph.CFactorGraph_m_verbose_set
    __swig_getmethods__["m_verbose"] = _FactorGraph.CFactorGraph_m_verbose_get
    if _newclass:
        m_verbose = _swig_property(_FactorGraph.CFactorGraph_m_verbose_get, _FactorGraph.CFactorGraph_m_verbose_set)

    def Solve(self, MaxIter):
        return _FactorGraph.CFactorGraph_Solve(self, MaxIter)

    def UpdateMessages(self):
        return _FactorGraph.CFactorGraph_UpdateMessages(self)

    def GetBelief(self, Nid):
        return _FactorGraph.CFactorGraph_GetBelief(self, Nid)

    def ComputeObj(self, decode):
        return _FactorGraph.CFactorGraph_ComputeObj(self, decode)

    def GetDecode(self):
        return _FactorGraph.CFactorGraph_GetDecode(self)

    def PrintFactorInfo(self):
        return _FactorGraph.CFactorGraph_PrintFactorInfo(self)
CFactorGraph_swigregister = _FactorGraph.CFactorGraph_swigregister
CFactorGraph_swigregister(CFactorGraph)


_FactorGraph.FACTOR_H_swigconstant(_FactorGraph)
FACTOR_H = _FactorGraph.FACTOR_H

_FactorGraph.FACTOR_INVALID_swigconstant(_FactorGraph)
FACTOR_INVALID = _FactorGraph.FACTOR_INVALID

_FactorGraph.FACTOR_NODE_ID_swigconstant(_FactorGraph)
FACTOR_NODE_ID = _FactorGraph.FACTOR_NODE_ID

_FactorGraph.FACTOR_EDGE_ID_swigconstant(_FactorGraph)
FACTOR_EDGE_ID = _FactorGraph.FACTOR_EDGE_ID

_FactorGraph.FACTOR_SPARSEEDGE_ID_swigconstant(_FactorGraph)
FACTOR_SPARSEEDGE_ID = _FactorGraph.FACTOR_SPARSEEDGE_ID

_FactorGraph.FACTOR_GENERAL_ID_swigconstant(_FactorGraph)
FACTOR_GENERAL_ID = _FactorGraph.FACTOR_GENERAL_ID

_FactorGraph.FACTOR_GENERALSPARSE_ID_swigconstant(_FactorGraph)
FACTOR_GENERALSPARSE_ID = _FactorGraph.FACTOR_GENERALSPARSE_ID
class EdgeInternal(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, EdgeInternal, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EdgeInternal, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ei"] = _FactorGraph.EdgeInternal_ei_set
    __swig_getmethods__["ei"] = _FactorGraph.EdgeInternal_ei_get
    if _newclass:
        ei = _swig_property(_FactorGraph.EdgeInternal_ei_get, _FactorGraph.EdgeInternal_ei_set)
    __swig_setmethods__["ej"] = _FactorGraph.EdgeInternal_ej_set
    __swig_getmethods__["ej"] = _FactorGraph.EdgeInternal_ej_get
    if _newclass:
        ej = _swig_property(_FactorGraph.EdgeInternal_ej_get, _FactorGraph.EdgeInternal_ej_set)
    __swig_setmethods__["data"] = _FactorGraph.EdgeInternal_data_set
    __swig_getmethods__["data"] = _FactorGraph.EdgeInternal_data_get
    if _newclass:
        data = _swig_property(_FactorGraph.EdgeInternal_data_get, _FactorGraph.EdgeInternal_data_set)

    def __init__(self):
        this = _FactorGraph.new_EdgeInternal()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _FactorGraph.delete_EdgeInternal
    __del__ = lambda self: None
EdgeInternal_swigregister = _FactorGraph.EdgeInternal_swigregister
EdgeInternal_swigregister(EdgeInternal)

class SparseEdgeInternal(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SparseEdgeInternal, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SparseEdgeInternal, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ei"] = _FactorGraph.SparseEdgeInternal_ei_set
    __swig_getmethods__["ei"] = _FactorGraph.SparseEdgeInternal_ei_get
    if _newclass:
        ei = _swig_property(_FactorGraph.SparseEdgeInternal_ei_get, _FactorGraph.SparseEdgeInternal_ei_set)
    __swig_setmethods__["ej"] = _FactorGraph.SparseEdgeInternal_ej_set
    __swig_getmethods__["ej"] = _FactorGraph.SparseEdgeInternal_ej_get
    if _newclass:
        ej = _swig_property(_FactorGraph.SparseEdgeInternal_ej_get, _FactorGraph.SparseEdgeInternal_ej_set)
    __swig_setmethods__["data"] = _FactorGraph.SparseEdgeInternal_data_set
    __swig_getmethods__["data"] = _FactorGraph.SparseEdgeInternal_data_get
    if _newclass:
        data = _swig_property(_FactorGraph.SparseEdgeInternal_data_get, _FactorGraph.SparseEdgeInternal_data_set)
    __swig_setmethods__["mi"] = _FactorGraph.SparseEdgeInternal_mi_set
    __swig_getmethods__["mi"] = _FactorGraph.SparseEdgeInternal_mi_get
    if _newclass:
        mi = _swig_property(_FactorGraph.SparseEdgeInternal_mi_get, _FactorGraph.SparseEdgeInternal_mi_set)
    __swig_setmethods__["mj"] = _FactorGraph.SparseEdgeInternal_mj_set
    __swig_getmethods__["mj"] = _FactorGraph.SparseEdgeInternal_mj_get
    if _newclass:
        mj = _swig_property(_FactorGraph.SparseEdgeInternal_mj_get, _FactorGraph.SparseEdgeInternal_mj_set)
    __swig_setmethods__["nnz"] = _FactorGraph.SparseEdgeInternal_nnz_set
    __swig_getmethods__["nnz"] = _FactorGraph.SparseEdgeInternal_nnz_get
    if _newclass:
        nnz = _swig_property(_FactorGraph.SparseEdgeInternal_nnz_get, _FactorGraph.SparseEdgeInternal_nnz_set)
    __swig_setmethods__["nnzIdx"] = _FactorGraph.SparseEdgeInternal_nnzIdx_set
    __swig_getmethods__["nnzIdx"] = _FactorGraph.SparseEdgeInternal_nnzIdx_get
    if _newclass:
        nnzIdx = _swig_property(_FactorGraph.SparseEdgeInternal_nnzIdx_get, _FactorGraph.SparseEdgeInternal_nnzIdx_set)

    def __init__(self):
        this = _FactorGraph.new_SparseEdgeInternal()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _FactorGraph.delete_SparseEdgeInternal
    __del__ = lambda self: None
SparseEdgeInternal_swigregister = _FactorGraph.SparseEdgeInternal_swigregister
SparseEdgeInternal_swigregister(SparseEdgeInternal)

class CFactorBase(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CFactorBase, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CFactorBase, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_getmethods__["RegisterFactorCreator"] = lambda x: _FactorGraph.CFactorBase_RegisterFactorCreator
    if _newclass:
        RegisterFactorCreator = staticmethod(_FactorGraph.CFactorBase_RegisterFactorCreator)
    __swig_getmethods__["CreateFactor"] = lambda x: _FactorGraph.CFactorBase_CreateFactor
    if _newclass:
        CreateFactor = staticmethod(_FactorGraph.CFactorBase_CreateFactor)
    __swig_setmethods__["m_LocalMax"] = _FactorGraph.CFactorBase_m_LocalMax_set
    __swig_getmethods__["m_LocalMax"] = _FactorGraph.CFactorBase_m_LocalMax_get
    if _newclass:
        m_LocalMax = _swig_property(_FactorGraph.CFactorBase_m_LocalMax_get, _FactorGraph.CFactorBase_m_LocalMax_set)

    def Primal(self, decode):
        return _FactorGraph.CFactorBase_Primal(self, decode)

    def Dual(self):
        return _FactorGraph.CFactorBase_Dual(self)

    def UpdateMessages(self):
        return _FactorGraph.CFactorBase_UpdateMessages(self)

    def Print(self):
        return _FactorGraph.CFactorBase_Print(self)

    def IsGeneralFactor(self):
        return _FactorGraph.CFactorBase_IsGeneralFactor(self)

    def GetIncludedNodes(self, nodes):
        return _FactorGraph.CFactorBase_GetIncludedNodes(self, nodes)

    def size(self):
        return _FactorGraph.CFactorBase_size(self)
    __swig_destroy__ = _FactorGraph.delete_CFactorBase
    __del__ = lambda self: None
    FactorID = _FactorGraph.CFactorBase_FactorID
CFactorBase_swigregister = _FactorGraph.CFactorBase_swigregister
CFactorBase_swigregister(CFactorBase)

def CFactorBase_RegisterFactorCreator(ID, creator):
    return _FactorGraph.CFactorBase_RegisterFactorCreator(ID, creator)
CFactorBase_RegisterFactorCreator = _FactorGraph.CFactorBase_RegisterFactorCreator

def CFactorBase_CreateFactor(ID, nodes, data):
    return _FactorGraph.CFactorBase_CreateFactor(ID, nodes, data)
CFactorBase_CreateFactor = _FactorGraph.CFactorBase_CreateFactor

class NodeFactor(CFactorBase):
    __swig_setmethods__ = {}
    for _s in [CFactorBase]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NodeFactor, name, value)
    __swig_getmethods__ = {}
    for _s in [CFactorBase]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, NodeFactor, name)
    __repr__ = _swig_repr
    __swig_setmethods__["m_bi"] = _FactorGraph.NodeFactor_m_bi_set
    __swig_getmethods__["m_bi"] = _FactorGraph.NodeFactor_m_bi_get
    if _newclass:
        m_bi = _swig_property(_FactorGraph.NodeFactor_m_bi_get, _FactorGraph.NodeFactor_m_bi_set)
    __swig_setmethods__["m_NofStates"] = _FactorGraph.NodeFactor_m_NofStates_set
    __swig_getmethods__["m_NofStates"] = _FactorGraph.NodeFactor_m_NofStates_get
    if _newclass:
        m_NofStates = _swig_property(_FactorGraph.NodeFactor_m_NofStates_get, _FactorGraph.NodeFactor_m_NofStates_set)
    __swig_setmethods__["m_id"] = _FactorGraph.NodeFactor_m_id_set
    __swig_getmethods__["m_id"] = _FactorGraph.NodeFactor_m_id_get
    if _newclass:
        m_id = _swig_property(_FactorGraph.NodeFactor_m_id_get, _FactorGraph.NodeFactor_m_id_set)

    def __init__(self):
        this = _FactorGraph.new_NodeFactor()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _FactorGraph.delete_NodeFactor
    __del__ = lambda self: None

    def UpdateDual(self):
        return _FactorGraph.NodeFactor_UpdateDual(self)

    def Primal(self, decode):
        return _FactorGraph.NodeFactor_Primal(self, decode)

    def Dual(self):
        return _FactorGraph.NodeFactor_Dual(self)

    def UpdateMessages(self):
        return _FactorGraph.NodeFactor_UpdateMessages(self)

    def IsGeneralFactor(self):
        return _FactorGraph.NodeFactor_IsGeneralFactor(self)

    def GetIncludedNodes(self, nodes):
        return _FactorGraph.NodeFactor_GetIncludedNodes(self, nodes)

    def Print(self):
        return _FactorGraph.NodeFactor_Print(self)
NodeFactor_swigregister = _FactorGraph.NodeFactor_swigregister
NodeFactor_swigregister(NodeFactor)

class SparseEdgeFactor(CFactorBase):
    __swig_setmethods__ = {}
    for _s in [CFactorBase]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SparseEdgeFactor, name, value)
    __swig_getmethods__ = {}
    for _s in [CFactorBase]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SparseEdgeFactor, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
SparseEdgeFactor_swigregister = _FactorGraph.SparseEdgeFactor_swigregister
SparseEdgeFactor_swigregister(SparseEdgeFactor)

class SparseEdgeNZFactor(SparseEdgeFactor):
    __swig_setmethods__ = {}
    for _s in [SparseEdgeFactor]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SparseEdgeNZFactor, name, value)
    __swig_getmethods__ = {}
    for _s in [SparseEdgeFactor]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SparseEdgeNZFactor, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _FactorGraph.delete_SparseEdgeNZFactor
    __del__ = lambda self: None
SparseEdgeNZFactor_swigregister = _FactorGraph.SparseEdgeNZFactor_swigregister
SparseEdgeNZFactor_swigregister(SparseEdgeNZFactor)

class DenseEdgeFactor(CFactorBase):
    __swig_setmethods__ = {}
    for _s in [CFactorBase]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DenseEdgeFactor, name, value)
    __swig_getmethods__ = {}
    for _s in [CFactorBase]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DenseEdgeFactor, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def Primal(self, decode):
        return _FactorGraph.DenseEdgeFactor_Primal(self, decode)

    def Dual(self):
        return _FactorGraph.DenseEdgeFactor_Dual(self)

    def IsGeneralFactor(self):
        return _FactorGraph.DenseEdgeFactor_IsGeneralFactor(self)

    def UpdateMessages(self):
        return _FactorGraph.DenseEdgeFactor_UpdateMessages(self)

    def GetIncludedNodes(self, nodes):
        return _FactorGraph.DenseEdgeFactor_GetIncludedNodes(self, nodes)

    def Print(self):
        return _FactorGraph.DenseEdgeFactor_Print(self)
    __swig_destroy__ = _FactorGraph.delete_DenseEdgeFactor
    __del__ = lambda self: None
    FactorID = _FactorGraph.DenseEdgeFactor_FactorID
DenseEdgeFactor_swigregister = _FactorGraph.DenseEdgeFactor_swigregister
DenseEdgeFactor_swigregister(DenseEdgeFactor)

# This file is compatible with both classic and new-style classes.


