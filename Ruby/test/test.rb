class Array
  def swap(i,j)
    set = self.dup
    set[i], set[j] = set[j], set[i]
    return set
  end
  def swap!(i,j)
    self[i], self[j] = self[j], self[i]
    return self
  end

  def permute0(set, x=0, result=[])
    if x == set.length - 2
      return result.push(set).push(set.swap(x, x+1))
    end
    n = 0
    until n == set.length - x do
      permute( set.swap(n,x), x + 1, result)
      n+=1
    end
    return result
  end
  
  def permute1(
end

class String
  def toCharList
    result = []
    i = 0
    until i == self.length 
      result.push(self[i].chr)
      i+=1
    end
    return result
  end

end
