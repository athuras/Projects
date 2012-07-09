module Aux
  include Math
  PHI = (1 + 5**0.5)/2

  class Array
    def sum
      sum = 0
      self.each do |e|; sum += e; end;
      return sum
    end

    def containsFactor(x)
      state = false
      self.each do |e|
        if x % e == 0
          return true
        end
      end
      return false
    end
  end

  def fib(n); return (PHI**n/sqrt(5) + 0.5).floor; end;
  def invFib(f); return log( f * sqrt(5) + 0.5 , PHI).floor; end;

end
