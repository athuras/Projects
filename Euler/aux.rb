module Aux
  include Math
  PHI = (1 + 5**0.5)/2

  # just so i remember, blocks ftw
  def sum( *splat ) return args.inject { |a,b| a += b } end

  class Array
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
