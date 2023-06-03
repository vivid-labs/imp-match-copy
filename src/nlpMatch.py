from src.helpers import splitAllCamel

# Word2vec returns dictionary of codeComponent matched to most likely figmaComponent (no repeats)
def nlpMatch(codeArr, figmaArr, model):

  # Preprocess the names
  codeCamelSplits = splitAllCamel(codeArr, model)
  figmaCamelSplits = splitAllCamel(figmaArr, model)

  codeComponentMap = []
  figmaComponentMap = []
  alreadyMatched = set()

  for c in codeArr:
    c = tuple(c)
    cSplits = codeCamelSplits[c]
    bestPercentMatch, bestWordMatch = 0, ()
    for f in figmaArr:
      f = tuple(f)
      fSplits = figmaCamelSplits[f]
      # Match each of the parts of the code and figma component names to each other. 
      if f not in alreadyMatched:
        if len(fSplits) == 0 and bestPercentMatch == 0:
          bestWordMatch = f
        percentMatch, norm = 0,0
        for cs in cSplits:
          for fs in fSplits:
            simScore = model.similarity(cs, fs)
            percentMatch += simScore
            norm += 1
        if norm > 0 and percentMatch / norm > bestPercentMatch:
          bestPercentMatch = percentMatch / norm
          bestWordMatch = f

    codeComponentMap.append(c)
    figmaComponentMap.append(bestWordMatch)
    alreadyMatched.add(bestWordMatch)
  return [codeComponentMap, figmaComponentMap]
