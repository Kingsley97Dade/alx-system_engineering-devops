#!/usr/bin/env ruby
# Ruby script to match only capital letters using regular expression

# Method to check if the argument contains only capital letters
def match_capital_letters(argument)
  regex = /^[A-Z]+$/ # Regular expression to match only capital letters
  if argument.match?(regex)
    puts "The argument contains only capital letters."
  else
    puts "The argument contains other characters besides capital letters."
  end
end

# Accept argument from command line
argument = ARGV[0]

# Check if an argument is provided
if argument.nil?
  puts "Please provide an argument."
else
  match_capital_letters(argument)
end
