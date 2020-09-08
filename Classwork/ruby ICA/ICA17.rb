=begin

=end


class Student
  def initialize(fname, lname, max_score, list_of_scores)
    @fname = fname
	@lname = lname
	@grade = set_grade(max_score, list_of_scores)
  end
    def fname
    @fname
  end
  
  def lname
    @lname
  end
  def grade
    @grade
  end
  
  def set_grade(max_score, list_of_scores)
    total_points = 0
	for i in list_of_scores
	  total_points = total_points+ i.to_i
	  
	end
	grade = total_points/max_score.to_f
	puts grade
	return get_letter_grade(grade)
  end
  
  def get_letter_grade(grade)
    letter_grade = ""
	if grade > 0.92
	  letter_grade ="A"
	end
	if grade > 0.80
	  letter_grade ="B"
	end
	if grade > 0.70
	  letter_grade ="C"
	end
	if grade > 0.60
	  letter_grade ="D"
	end
	
  def <=>(other)
    @lname <=> other.lname
  end
  
  def to_s
	return "#{@fname} #{@lname}: #{@grade}"
  end 
end  
end

def main
  
  student_list = Array.new
  filename = 'Grades.txt'
  fh = open filename
  file_writer = File.new('Graded.txt', 'w')
  fh.readlines('test.txt').each do |line|
    line = line.tr('"','')
    line = line.split(',').to_s
	student_list << line
	s = Student.new(line[0],line[1],line[2],line[3..])
    student_list << s

  end
  student_list = student_list.sort
  for s in student_list
    file_writer.puts(s)
  end
  fh.close
  
end
main()