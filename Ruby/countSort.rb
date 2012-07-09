# =>implementation of counting sort
class Array
  def cSort # first attempt
    aux = Array.new(self.max + 1){ |i| 0 } # aux is full of 0
    self.each do |e| # aux is now a histogram of self
      aux[e] += 1
    end 

    out = []
    aux.each_with_index do |e, i|
      until aux[i] == 0 do
        out.push(i)
        aux[i] -= 1
      end
    end
    return out
  end

  def cSort2 # now with better memory management
    aux = Array.new(self.max + 1){ |i| 0 }
    self.each do |e|
      aux[e] += 1
    end

    j = 0
    aux.each_with_index do |e, i|
      until aux[i] == 0 do
        self[j] = i
        j += 1
        aux[i] -= 1
      end
    end
    return self
  end

end
