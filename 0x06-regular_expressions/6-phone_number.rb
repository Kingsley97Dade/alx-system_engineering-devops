#!/usr/bin/env ruby
# Ruby script to match a 10-digit phone number using regular expression

# Method to check if the argument matches the regular expression for a 10-digit phone number
def match_phone_number(argument)
  regex = /^\d{10}$/ # Regular expression to match exactly 10 digits
  if argument.match?(regex)
    puts "The argument is a 10-digit phone number."
  else
    puts "The argument is not a 10-digit phone number."
  end
end

# Accept argument from command line
argument = ARGV[0]

# Check if an argument is provided
if argument.nil?
  puts "Please provide a phone number as an argument."
else
  match_phone_number(argument)
end
