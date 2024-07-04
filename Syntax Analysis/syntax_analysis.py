import nltk
cgrammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> PN | Det N | N 
VP -> IV | IV ADV | AV ADJ | TV PN NP | V NP
Det -> 'the' | 'a' | 'an'
ADJ -> 'scary' | 'tall' | 'short' | 'blonde' | 'slim' | 'fat'
N -> 'cat' | 'dog' | 'cats' | 'food' | 'book' | 'books'
AV -> 'is' | 'does' | 'are' | 'do'
IV -> 'runs' | 'run' | 'running' | 'hurts' | 'hurt' | 'hurting' | 'walks' | 'walk' | 'walking' | 'jumps' | 'jump' | 'jumping' | 'shoots' | 'shoot' | 'shooting'
TV -> 'gives' | 'give' | 'gave' | 'giving'
V -> 'chased' | 'chase' | 'needs' | 'need' | 'hates' | 'hate' | 'has' | 'have' | 'loves' | 'love' | 'kicks' | 'kick' | 'jumps' | 'jump'
PN -> 'mary' | 'john' | 'tomy' 
ADV -> 'quickly' | 'slowly' | 'independently'
""")
sent = ['mary', 'runs', 'quickly']
# Using Chart Parser
cparser = nltk.ChartParser(cgrammar)
for tree in cparser.parse(sent):
  print(tree)
  tree.draw()