import re
pattern = args[0]
filename = rwd+format_path(args[1])
with open(filename, 'r') as f:
  for line in f:
    if re.search(pattern, line):
      print(line)