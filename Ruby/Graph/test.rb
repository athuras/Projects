require 'stream'
require 'rgl/Adjacency'
require 'rgl/dot'

class Array
  def swap(i,j)
    set = self.dup
    set[i], set[j] = set[j], set[i]
    return set
  end
  def swap!(i, j)_
    self[i], self[j] = self[j], self[i]
    return self
  end
end

# => Returns a list of all permutations of the set
def permute(set, x=0, result=[])
  if x == set.length - 2
    return result.push(set).push(set.swap(x, x+1))
  end
  n = 0
  until n == set.length - x do
    permute( set.swap(n, x), x + 1, result )
    n+=1
  end
  return result
end

def initAdjGraph(setOfEdges)
  adjGraph = RGL::DirectedAdjacencyGraph[]

  setOfEdges.each do |e|
    adjGraph.add_edge(e[0], e[1])
  end
  
  return adjGraph
end

#  The Goal here is to generate an adjacency graph (in list form)
def atog(set, x = 0, result = [], adjacentVertex = set)
  if x == set.length - 2
      pairA = set
      pairB = set.swap(x, x+1)
      result.push([adjacentVertex, pairA])
      result.push([adjacentVertex, pairB])
      result.push([pairA, pairB])
  end
  n = 0
  until n == set.length - x do
    atog( set.swap( n, x ),  x + 1, result, set )
    result.push([set, set.swap(n, x)])
    n += 1
  end
  
  return result
end
