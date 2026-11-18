# https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md
all
rule 'MD013', :line_length => 140, :tables => false # Line length
exclude_rule 'MD005' # Inconsistent indentation for list items at the same level
exclude_rule 'MD007' # Unordered list indentation
exclude_rule 'MD025' # Multiple top level headers in the same document
exclude_rule 'MD031' # Fenced code blocks should be surrounded by blank lines
exclude_rule 'MD009' # trailing spaces
exclude_rule 'MD024' # Multiple headers with the same content
exclude_rule 'MD027' # Multiple spaces after blockquote symbol
exclude_rule 'MD029' # Ordered list item prefix
exclude_rule 'MD040' # Fenced code blocks should have a language specified
rule 'MD026', :punctuation => '.,;:!'
