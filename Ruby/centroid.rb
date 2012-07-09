# Related to an interview question which effectively required finding the optimal place to 
# locate a store given the location and size of customers. So I decided to make it more general!
# 1-D: Location on a line
# 2-D: Location in a plane (i.e. Manhatten)
# 3-D: Location within Cloud City
# 4-D: Location within Cloud City, in the optimal era
# 5-D: ...

class Point 
  attr_accessor :weight, :vector

  def initialize(w, v)
    @weight = w
    @vector = v
    return self
  end
end

class PointGroup < Point
  attr_accessor :points, :bounds, :centroid
  
  def initialize(pointList)

    ################################
    
    points = {}
    pointList.each_with_index do |e, i|
     points[i] = e
    end
    
    maxSize = 0
    points.keys.each do |k|
      if points[k].vector.size > maxSize
        maxSize = points[k].vector.size
      end
    end
   
    @points = points    

    ################################
    
    min = points[0].vector
    max = points[0].vector
    sums = Array.new(maxSize){ |e| 0 }

    aux  = {}
    maxSize.times do |e|
      aux[e] = []
    end

    points.keys.each do |k|
      points[k].vector.each_with_index do |e, i|
        if min[i] > e then min[i] = e end
        if max[i] < e then max[i] = e end
        sums[i] += points[k].weight
        aux[i].push( [e, points[k].weight] )
      end
    end

    @bounds = [min, max]

    centroid = Array.new(maxSize)
    aux.keys.each do |k|
      aux[k].sort!{ |a, b| a[1] <=> b[1] }
    end
    aux.keys.each do |k|
      puts "key: #{k}"
      partialSum = sums[k] / 2.to_f
      j = 0
      until partialSum <= 0 or j > 100 do
        partialSum -= aux[k][j][1]
        j += 1
      end
      centroid[k] = aux[k][j][0]
    end

    @centroid = centroid

    return self
  end

end
        
module TestSuite

  def ps1(x=4, dim=2, range=10)
    points = []
    x.times do 
      w = rand(range)
      v = []
      dim.times do 
        v.push(rand(range))
      end
      points.push( Point.new(w,v))
    end
    return points
  end

end
