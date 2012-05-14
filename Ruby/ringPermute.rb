require "stream"
require "rgl/Adjacency"
require "rgl/dot"

class Array
  #  swaps two elements in a list.
  def swap(i,j)
    set = self.dup
    set[i], set[j] = set[j], set[i]
    return set
  end
  def swap!
    self[i], self[j] = self[j], self[i]
    return self
  end

  # cyclic leftshift (with variable size), not the best way by far, but this isn't C.
  def leftRotate(left=0, right=self.length-1)
    set = self.dup
    if not left <= right
      left, right = right, left
    end
    temp = set[left]
    until left == right do
      set[left] = set[left + 1]
      left +=1
    end
    set[right] = temp
    return set
  end

  def leftRotate!(left=0, right=self.length-1)
    if not left <= right
      left, right = right, left
    end
    temp = self[left]
    until left == right do
      self[left] = self[left + 1]
      left +=1
    end
    self[right] = temp
    return self
  end
  
  #  Generates a cyclically connected (unidirectional) set of edges, for use with RingPermute module
  def spawnLeftRing(i=0)
    edgeList = []
    j = i
    until j == self.length do 
      edgeList.push(self.dup, self.leftRotate(i))
      self.leftRotate!(i)
      j += 1
    end
    return edgeList
  end

end

module RingPermutation
  # => a set of funtions (mainly for use in irb) to generate permute-structures. 
  # Typical usage would be
  #   x = formGraph([1,2,3,4,5])
  #   x.write_to_graphic_file('arbitrary string')
  #   then open the graph.dot file in Gephi and TADA (after some expansion): glory.
  require 'Time'

  class String
    def toA
      return self.scan(/./)
    end
  end

  def ringPermute(set, index=0, edges=[], graph=nil)
    if edges.length >= 2
      until edges.length == 0 do
        x = edges.pop
        graph.add_edge(edges.pop, x)
      end
    end

    if index == set.length - 2 then
      return set.spawnLeftRing(index)
    else
      (set.length - index).times do 
        edges += ringPermute2( set.leftRotate( index ), index + 1, edges, graph )
        graph.add_edge(set.dup, set.leftRotate( index ))
        set.leftRotate!( index )
      end
      return edges
    end
  end

  def formGraph2(set)
    t0 = Time.new
    graph = RGL::DirectedAdjacencyGraph[]
    edges = []
    residuals = ringPermute2(set, 0,edges, graph)
    if residuals.length >= 2
      until residuals.length == 0 do
        x = residuals.pop
        graph.add_edge( residuals.pop, x )
      end
    end
    puts "n:V:E #{set.length} : #{graph.length} : #{graph.edges.length} in #{Time.new - t0}"
    return graph
  end

  def initAdjGraph(edges) # edges: list of tuples
    graph = RGL::DirectedAdjacencyGraph[]
    i = 0
    until i >= (edges.length - 1) do
      graph.add_edge(edges[i], edges[i+1])
      i += 2
    end
    return graph
  end

end
