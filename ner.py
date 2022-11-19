import nltk
from nltk.tag.stanford import StanfordNERTagger

def ner_tagging(inp):
#sentence = u"Twenty miles east of Reno, Nev., " \
#    "where packs of wild mustangs roam free through " \
#    "the parched landscape, Tesla Gigafactory 1 " \
#    "sprawls near Interstate 80."

	jar = './stanford-ner-tagger/stanford-ner.jar'
	model = './stanford-ner-tagger/english.all.3class.distsim.crf.ser.gz'

	# Prepare NER tagger with english model
	ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

	ner_out = []
	for words in inp:	
		# Run NER tagger on words
		ner_out = ner_tagger.tag(words)
		#print(ner_out)
	return ner_out
