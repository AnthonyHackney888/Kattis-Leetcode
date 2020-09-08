=begin
	author: Anthony Hackney	
=end

filename = 'test.txt'
puts "opening '#{filename}'"

fh = open filename
=begin
while (line = fh.gets)
  puts line
end
=end
=begin
fh.each do |line|
  puts line
end
=end

fh.readlines('test.txt').each do |line|
  puts line
end
fh.close

