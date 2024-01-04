#!/usr/bin/env ruby
# Ruby script to match a string that starts with 'h', ends with 'n', and has any single character in between

# Method to check if the argument matches the regular expression criteria
def match_pattern(argument)
  regex = /^h.n$/ # Regular expression to match the described pattern
  if argument.match?(regex)
    puts "The argument matches the pattern 'h_n'."
  else
    puts "The argument does not match the pattern 'h_n'."
  end
end

# Accept argument from command line
argument = ARGV[0]

# Check if an argument is provided
if argument.nil?
  puts "Please provide an argument."
else
  match_pattern(argument)
end
