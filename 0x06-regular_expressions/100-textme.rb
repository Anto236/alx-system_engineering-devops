#!/usr/bin/env ruby
def extract_info(input_string)
	sender = input_string[/from:(.*?)\s/, 1]
	receiver = input_string[/to:(.*?)\s/, 1]
	flags = input_string[/flags:(.*?)\s/, 1]
	"#{sender},#{receiver},#{flags}"
end

input_string = ARGV[0]
puts extract_info(input_string)

