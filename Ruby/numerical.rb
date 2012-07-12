module Numerical
  def compTrapezoid(a, b, n, &func) # sing even sub-intervals
    # supply a function as a block. i.e. compTrapezoid(0,PI,100) { |x| sin(x) }
    sum, i = 0, 1
    h = (b-a)/n.to_f
    until n == i do
      p, q = (i-1)*h + a, i*h + a
      sum += h*(func.call(p) + func.call(q))/2
      i += 1
    end
    return sum
  end
  def newtonCotes(a, b, k)
    # integrate a lagrange interpolating polynomial of degree k from a to b.  
  end
  def convergeTest(n)
    printf "n \t\t I(n)\tROC\n"
    sum, a = 1,1
    n.times do |i|
      k = 2**i
      sum = yield(2**i)
      printf "#{2**i}\t\t #{sum}\t#{sum/a}\n"
      a = sum
    end
  end
  
  def eulersMethod1(t, ic, n) # expects block slope function
    ti, wi = ic[0].to_f, ic[1].to_f
    h = (t-ti)/n.to_f
    puts "n = #{n}, h = #{h}"
    until ti >= t do
      puts "#{ti}, #{wi}"
      wi += h*(yield(ti,wi))
      ti += h
    end
    return wi
  end

  

end
