import re
import pickle
from caseconverter import camelcase

# Converts camelStr -> ["camel", "Str"]
def splitCamelCase(camelStr):
  matches = re.finditer(".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)", camelStr)
  return [m.group(0) for m in matches]

# Returns dictionary with {"[codeComponent, filePath]": ["code", "component"]...}
def splitAllCamel(arr, model):
  nameToSplit = {}
  for c in arr:
    split = splitCamelCase(camelcase(c[1]))
    validSplit = []
    for word in split: #dont include words that aren't in the corpus
      word = word.lower()
      if word in model.key_to_index:
        validSplit.append(word)

    nameToSplit[tuple(c)] = validSplit
  return nameToSplit