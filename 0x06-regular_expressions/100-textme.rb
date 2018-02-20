#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=to:)\+[0-9]+|(?<=from:)[a-zA-Z]+|(?<=flags:)[^\]]*/).join(',')
