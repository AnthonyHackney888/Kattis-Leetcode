=begin

=end
class Circle

  @@pi = 3.14
  
  def initialize(radius)
    @radius = radius
  end	
  
  def radius
    @radius
  end
  def pi 
    @@pi
  end
  
  
  def get_area
    @@pi * @radius ** 2
  end
  
end

def main
  calc = Circle.new(15)
  puts calc.pi
  puts calc.get_area
  
  
end

main