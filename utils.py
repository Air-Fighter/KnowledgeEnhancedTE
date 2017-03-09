"""

    Utility functions.

"""

import torch
import torch.nn as nn

# list comprehension operator
# COMP = require("pl.comprehension").new()


def printerr(msg):
    print '\033[1;31;40m',
    print msg,
    print '\033[0m'



def get_tensor_size(tensor, separator):
    sep = separator or " "
    ret = []
    for i in xrange(0, tensor.dim()):
        ret[i] = tensor.size(i)
    return sep + str(ret)


# share module parameters
def share_params(cell, src):
    for c_param, s_param in zip(cell.parameters(), src.parameters()):
        c_param.data.copy_(s_param.data)

"""
def share_params(cell, src)
  if torch.type(cell) == 'nn.gModule' then
    for i = 1, #cell.forwardnodes do
      local node = cell.forwardnodes[i]
      if node.data.module then
        node.data.module:share(src.forwardnodes[i].data.module,
                               'weight', 'bias', 'gradWeight', 'gradBias')
      end
    end
  elseif torch.isTypeOf(cell, 'nn.Module') then
    cell:share(src, 'weight', 'bias', 'gradWeight', 'gradBias')
  else
    error('parameters cannot be shared for this input')
  end
end
"""

def get_tensor_data_address(x):
    pass

"""
function getTensorDataAddress(x)
  return string.format("%x+%d", torch.pointer(x:storage():data()), x:storageOffset())
end
"""

def get_tensor_table_norm(t):
    pass

"""
function getTensorTableNorm(t)
  local ret = 0
  for i, v in ipairs(t) do
    ret = ret + v:norm()^2
  end
  return math.sqrt(ret)
end
"""

def inc_counts(counter, key):
    if counter[key] is None:
        counter[key] = 1
    else:
        counter[key] += 1

def table_length(tab):
    pass

"""
function tableLength(tab)
  local count = 0
  for _ in pairs(tab) do count = count + 1 end
  return count
end
"""

def repeat_tensor_as_table(tensor, count):
    pass

"""
function repeatTensorAsTable(tensor, count)
  local ret = {}
  for i = 1, count do ret[i] = tensor end
  return ret
end
"""

def flatten_table(tab):
    pass

"""
function flattenTable(tab)
  local ret = {}
  for _, t in ipairs(tab) do
    if torch.type(t) == "table" then
      for _, s in ipairs(flattenTable(t)) do
        ret[#ret + 1] = s
      end
    else
      ret[#ret + 1] = t
    end
  end
  return ret
end
"""

def get_tensor_table_size(tab, separator):
    pass

"""
function getTensorTableSize(tab, separator)
  local sep = separator or " "
  local ret = {}
  for i, t in ipairs(tab) do
    ret[i] = getTensorSize(t, "x")
  end
  return stringx.join(sep, ret)
end
"""

def vector_string_compact(vec, separator):
    pass

"""
function vectorStringCompact(vec, separator)
  local sep = separator or " "
  local ret = {}
  for i = 1, vec:size(1) do
    ret[i] = string.format("%d:%.4f", i, vec[i])
  end
  return stringx.join(sep, ret)
end
"""

def tensor_size(tensor):
    pass

"""
function tensorSize(tensor)
  local size = 1
  for i=1, tensor:dim() do size = size * tensor:size(i) end
  return size
end
"""

# http://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html
StopWords = ["a", "an", "and", "are", "as", "at", "be", "by",
            "for", "from", "has", "in", "is", "of", "on", "that",
            "the", "to", "was", "were", "will", "with", "."]

def is_stop_word(word):
  return word in StopWords