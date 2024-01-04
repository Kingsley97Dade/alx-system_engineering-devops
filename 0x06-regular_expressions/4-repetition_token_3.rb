#!/usr/bin/env ruby
# Ruby script to match the word "School" using regular expression without square brackets

# Method to check if the argument matches the regular expression for "School"
def match_school(argument)
  regex = /\bSchool\b/ # Regular expression to match "School" as a whole word
  if argument.match?(regex)
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
