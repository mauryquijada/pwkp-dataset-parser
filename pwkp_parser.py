import argparse

def parse_pwkp_file(pwkp_source_file, complex_sentences_file):
	translations = []

	"""
	Code expects pwkp_source_file to be of the form:

	Complex sentence <newline>
	Simple translation, sentence 1 <newline>
	Simple translation, sentence 2 <newline>
	<newline>
	Complex sentence <newline>
	...
	"""
	with open(pwkp_source_file) as pwkp_file:
		translation_beginning = True
		translation = None
		for line in pwkp_file:
			if translation_beginning:
				translation = (line.strip(), "")
				translation_beginning = False
			else:
				if line == "\n":
					translation_beginning = True
					translations.append(translation)
				else:
					source, target = translation
					translation =\
						(source, target + line.strip() + " ")


	with open(complex_sentences_file, "w") as pwkp_source:
		pwkp_source.writelines("%s\n" % l for l, _ in translations)



if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Parses the simple-complex " +
		"sentence pair dataset for Simplified Wikipedia as provided by Zhu" +
		" et al.")
	parser.add_argument("pwkp_source_file", help="The input simple-complex " +
		"sentence pair dataset file.")
	parser.add_argument("complex_sentences_file",  help="The filename to " +
		"write all complex sentences to, each separated by a newline.")

	args = parser.parse_args()
	parse_pwkp_file(args.pwkp_source_file, args.complex_sentences_file)