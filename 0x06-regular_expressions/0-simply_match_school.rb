#!/usr/bin/env ruby

# Accept the argument
argument = ARGV[0]

# Define regular expression pattern
pattern = /School/

# Scan method to fin  instances of pattern
result = argument.scan(pattern)

# result is an array of strings is joined and printed
puts result.join
