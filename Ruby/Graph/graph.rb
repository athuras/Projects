require 'stream'
require 'rgl/Adjacency'
require 'rgl/dot'

class Array
  def swap(i,j)
    set = self.dup
    set[i]. set[j] = set[j], set[i]
    return set    
  end
  def swap!(i,j)
    self[i], self[j] = self[j], self[i]
    return self
  end

  def permute(set, x=0, result[])
    if x == set.length - 2
      return result.push(set).push(set.swap(x, x+1))
    end
    n = 0
    until n == set.length - x do
      permute( set.swap(n,x), x + 1, result)
      n += 1
    end
    return result
  end
  
  # =>Direction is based on bitwise AND. 
  def directedAdjacencyGraph(edges)
    graph = RGL::DirectedAdjacencyGraph[]

    edges.each do |e|
      order = (e[0]&e[1]? true: false)
      if order
        graph.add_edge(e[0], e[1])
      else
        graph.add_edge(e[1], e[0])
      end
    end
    return graph
  end

end
