#!/usr/bin/env ruby

#expression to match hbtttn

# Accept the argument
argument = ARGV[0]

# Define the regex pattern
pattern = /hbt+n/

# Scan method to find instance of pattern
result = argument.scan(pattern)

# Print result and join array to string
puts result.join
