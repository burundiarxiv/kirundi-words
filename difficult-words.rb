# frozen_string_literal: true

require 'csv'
require 'pry'

words = File.read('amajambo_5.txt').split("\n")

# keep words with only 2 vowels
with_2_vowels = words.select { |word| word.count('aeiou') == 2 }

# keep startinng and finishing with a vowels
start_ending_vowels = with_2_vowels.select { |word| word.start_with?('a', 'e', 'i', 'o', 'u') && word.end_with?('a', 'e', 'i', 'o', 'u') }
