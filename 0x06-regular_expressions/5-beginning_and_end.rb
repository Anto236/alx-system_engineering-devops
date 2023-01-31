#!/usr/bin/env ruby

#htn and hbtn

#Accept the argument
argument = ARGV[0]

#regex pattern starts with h ends with n and
#can have any single character in between
pattern = /^h\wn$/

#scan for instances of the pattern
result = argument.scan(pattern)

#print result
puts result.join
