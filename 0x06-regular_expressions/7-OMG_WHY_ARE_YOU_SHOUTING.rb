#!/usr/bin/env ruby

#htn and hbtn

#Accept the argument
argument = ARGV[0]

#regex pattern must be only matching: capital letters
pattern = /[A-Z]*/

#scan for instances of the pattern
result = argument.scan(pattern)

#print result
puts result.join
