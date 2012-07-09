module ProjectEuler

  require_relative 'Aux'
  include 'Aux'

  # => 1
  # Add all the natural numbers below one thousand that are multiples of 3 or 5
  # Generalised
  def e1(max=1000, *mods = [3,5])
    sum = 0
    (max + 1).times do |i|
      if not mods.containsFactor(i)
        sum += e
      end
    end
    return sum
  end

  # => 2
  # By considering the terms in the Fibonacci sequece whose values do not exceed four million, find the sum of the even-valued terms
  def e2(bound=4*10**6)
    sum = 0
    i == invFib(bound)
    until i % 3 == 0 do; maxIndex -= 1; end;
    until i == 0 do
      sum += fib(i)
      i -= 3
    end
    return sum
  end

  # => 3    
  # Find the largest Prime Factor of a composite number -nontrivial
  def e3(n)
    return true
    # Options include Quadratic Sieve, Pollard's Rho Algorithm
  end

  # => 4
  # Find the largest palindrone made from the product of two 3-digit numbers
end
