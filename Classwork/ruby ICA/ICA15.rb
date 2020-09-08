=begin
author Anthony Hackney
=end

#problem 1
=begin
num_one = gets
num_one = num_one.to_i 
num_two = gets
num_two = num_two.to_i
puts (num_one + num_two)

#problem 2 and 3
puts "what is your favorite color" 
x = gets

puts "Your favorite color is " + x
file_writer = File.new("YouSayIWrite.txt",'w')
puts"Writing to a file"
file_writer.puts("You told me #{x}")
file_writer.close

data = File.read("YouSayIWrite.txt")
puts data

#problem 4

grade = gets.to_i
if grade >= 90
  puts "A"
elsif grade >=80  
  puts "B" 
elsif grade >=70 
  puts "C"
elsif grade >=60 
  puts "D"
else 
  puts "F"
end


#problem 5
p "Enter a string"
string_one = gets

p "Enter another string"
string_two = gets.chomp

p string_one
p string_two


#problem 6
puts 'enter your age: '
age = gets.to_i
puts age >=60 ? "old" : "young"


#
#problem 7 
user_input = gets.to_i
counter = 0
while counter < user_input
  if counter % 5 == 0
	puts counter
	end
  counter +=1	
end

#problem 8
range = (1..10)
for i in range
   puts i if i % 2 == 0
  end
end



#problem 9
array = [1,2,3,'a','b','c']

for i in array  
  puts i
end

#problme 10
counter = 0

loop do counter
  puts counter
  counter +=1
break if counter > 5

end

#priblem 12
def sum_two(a,b)
  return (a+b)
end
puts sum_two(1,2)

#problem 13
def function1(a)
  return puts a
end
function1(5)

#problem 14

def read_file(name)
  check = gets.chomp
  while check != 'exit'
    file_writer = File.new(name,'w')
    puts"Writing to a file"
    file_writer.puts("You told me #{check}")
   end
end

#problem 14
my_array = []
while true
  input = gets.chomp
  if input.downcase == 'exit'
    break
  end
  my_array<<input
end
puts (my_array.to_a).to_s

#problem 15
my_hash = Hash.new
while true
  puts "Enter in a value: "
  input = gets.chomp
  if input.downcase == 'exit'
    break
  end
  input = input.split(',')
  my_hash.store(input[0], input[1])
  puts my_hash
end


#problem 16
def nameer(filename)
  file_writer = File.new(filename,'w')
  puts"Writing to a file:"
  input = gets.chomp
  while input.downcase != 'exit'
    file_writer.puts("You told me #{input}")
	puts'enter a line of text'
	input = gets.chomp
  end      
  file_writer.close
end
nameer('test.txt')


#probelm 17
class My_class
  def initialization(my_num)
    @my_num = 5
  end
  
  def my_num
    @my_num
  end

end

m1 = My_class.new
puts m1.my_num
=end
#probelm 18
class Employee
  def initialize(name, salary)
    @name = name
	@salary = salary
  end
  
  def name
    @name
  end
  def salary
    @salary
  end
  def <=>(other)
    @salary <=> other.salary
  end
  
  def to_s
    "Name: #{@name}, Salary: #{@salary}"
  end
end

e1 = Employee.new("john",5)
e2 = Employee.new("smith",2)
e3 = Employee.new("james",3)

employe_array = [e1,e2,e3]

for e in employe_array
  puts e
end

