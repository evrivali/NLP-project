import sqlite3
from nltk import grammar, parse

def execute_query(conn,q):
 cur = conn.cursor()
 cur.execute(q)
 rows = cur.fetchall()
 for row in rows:
  print(row)

g = """
% start S
# ###################
# Grammar Productions
# ###################
S[SEM=('SELECT'+?q + 'FROM knowledge WHERE' + ?p)] -> Q[SEM=?q] P[SEM=?p]
P[SEM=(?v+' AND '+?n)] -> V[SEM=?v] N[SEM=?n]
P[SEM=?v] -> V[SEM=?v]
P[SEM=?adj] -> ADJ[SEM=?adj]
P[SEM=?iv] -> IV[SEM=?iv]
P[SEM=(?iv+' AND '+?adv)] -> IV[SEM=?iv] ADV[SEM=?adv]
P[SEM=?tv] -> TV[SEM=?tv]
P[SEM=(?tv+' AND '+?n)] -> TV[SEM=?tv] N[SEM=?n]
P[SEM=(?tv+' AND '+?r)] -> TV[SEM=?tv] R[SEM=?r]
# ###################
# Lexical Productions
# ###################
Q[SEM='Name'] -> 'who'
Q[SEM='Noun'] -> 'what' | 'what is'
Q[SEM='Adverb'] -> 'how'
Q[SEM='Receiver'] -> 'who is'
R[SEM=("Receiver='john'")] -> 'to john'
R[SEM=("Receiver='mary'")] -> 'to mary'
R[SEM=("Receiver='tomy'")] -> 'to tomy'
N[SEM=("Noun='dog'")]-> 'dog' | 'dogs'
N[SEM=("Noun='food'")]-> 'food' | 'foods'
N[SEM=("Noun='cat'")]-> 'cat' | 'cats'
N[SEM=("Noun='book'")]-> 'book' | 'books'
V[SEM="Verb='need'"]-> 'need' | 'needs'
V[SEM="Verb='hate'"]-> 'hate' | 'hates'
V[SEM="Verb='chase'"]-> 'chase' | 'chases'
V[SEM="Verb='love'"]-> 'love' | 'loves'
V[SEM="Verb='have'"]-> 'have' | 'has'
ADJ[SEM="Adjective='scary'"]-> 'scary'
ADJ[SEM="Adjective='tall'"]-> 'tall'
ADJ[SEM="Adjective='short'"]-> 'short'
ADJ[SEM="Adjective='blonde'"]-> 'blonde'
ADJ[SEM="Adjective='slim'"]-> 'slim'
ADJ[SEM="Adjective='fat'"]-> 'fat'
AV[SEM='-'] -> 'are' | 'is' | 'do' | 'does'| 'to' | 'a' | 'is mary' | 'is john' | 'is tomy' | 'the' | 'does mary'
IV[SEM="Intransitive_Verb='run'"]-> 'run' | 'runs' | 'running'
TV[SEM="Transitive_Verb='give'"]-> 'give' | 'gives' | 'giving' | 'gave'
ADV[SEM="Adverb='quickly'"]-> 'quickly'
 """
grammar = grammar.FeatureGrammar.fromstring(g)
tokens= 'who gives dog'.split()
parser = parse.FeatureEarleyChartParser(grammar)
trees = list(parser.parse(tokens))
if (len(trees)==0):
 print("There's no answer for your question")
else:
 answer = trees[0].label()['SEM']
 answer = [s for s in answer if s]
 q = ' '.join(answer)
 print(q)
 execute_query(sqlite3.connect('semantic_analysis.db'),q)

