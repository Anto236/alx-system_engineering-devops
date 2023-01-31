#!/usr/bin/env ruby

#htn and hbtn

#Accept the argument
argument = ARGV[0]

#regex pattern starts with digit and range of 10
pattern = /^\d{10}$/

#scan for instances of the pattern
result = argument.scan(pattern)

#print result
puts result.join
