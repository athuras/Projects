## Iterative (bs1) and Recursive (bs2) object-oriented implementations:
## Usage: array.search(X)

class Array
  def  binarySearch1(x) 
   min = 0
    max = ( self.length - 1 )
    until (min >  max ) 
       mid = (min + max)/2
       z = x <=> self[mid]
       if z == 0   then return mid end
       if z == -1  then max = mid - 1 end
       if z == 1   then min = mid + 1 end
     end
    z = self[mid]
     until self[mid] > z do
      mid += 1
    end
    return -mid
  end
  
  def binarySearch2(x, min = 0, max = self.length - 1)
    mid = (max + min)/2
    
    if min >  max then
      z = self[mid]
      until self[mid] > z do
        mid += 1
      end
      return -mid
    end

    z = x <=> self[mid]
    if z == 0  then return mid end
    if z == -1 then return self.binarySearch2(x, min, mid-1) end
    if z == 1  then return self.binarySearch2(x, mid + 1, max) end
  end
end

## Iterative (bs3) and Recursive (bs4) functional implementations
## Usage: search(array, X)

def binarySearch3(numbers,value)
  i, flag = 0
  count = 0
  min = 0
  max = numbers.length-1
  until (min > max) do
    i = ((min + max)/2)
    if (numbers[i]<value) then min = i - 1 end
    if (numbers[i]>value) then max = i + 1 end
    if (numbers[i]== value) then return i end
    count += 1
  end
  return -i
end

def binarySearch4(numbers, value, min = 0, max = numbers.length-1)
  i = (min+max)/2
  if numbers[i]==value
    return i 
  elsif min==max 
    return -(i) 
  elsif numbers[i]< value 
    return binarySearch4(numbers, value, i+1, max) 
  elsif numbers[i]> value 
    return binarySearch4(numbers, value, min, i-1) 
  end
end

puts 'test begin'
source = [0,1,2,3,3,5,6,7,9,11,12]
find = [1,2,3,4,5,6,7,8,9,10]

find.each do |a|
puts "#{a}:#{source.binarySearch2(a)}"
end
puts " done "
