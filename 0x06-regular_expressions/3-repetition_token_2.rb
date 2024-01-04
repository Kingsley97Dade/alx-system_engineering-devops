#!/usr/bin/env ruby
# Ruby script to match the word "School" using regular expression

# Method to check if the argument matches the regular expression for "School"
def match_school(argument)
  regex = /School/ # Regular expression to match "School"
  if argument =~ regex
    puts "The argument contains the word 'School'."
  else
    puts "The argument does not contain the word 'School'."
  end
end

# Accept argument from command line
argument = ARGV[0]

# Check if an argument is provided
if argument.nil?
  puts "Please provide an argument."
else
  match_school(argument)
end
