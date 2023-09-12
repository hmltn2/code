# TURKISH WORD, SENTENCE AND LANGUAGE ANALYZER !!!!!!!!!!!!!!!!!!!!!!!!

"""
class Word:
    self.arguments = "" # complement, children.. ?
    self.properties = "" # Inflection, Morphology ?
"""

# use OPERATOR OVERLOADING ????? to handle different constructors for different kinds of clauses?????? seems more elegant????
class Clause:
# TODO: remove this boilerplate?
    def __init__(subject: NounPhrase, predicate: VerbPhrase, clausetype: ClauseType):
        self.subject = subject
        self.predicate = predicate
        self.clausetype = clausetype

class NounPhrase: # determinerphrase ??????
    def __init__(determiner: Determiner, noun: Noun):
        self.determiner = determiner
        self.noun = noun

# perhaps OPERATOR OVERLOADING IS THE TRICK HERE??? to keep the grammar pythonic????
class Noun:
    def __init__(adjective, noun: Noun):

class VerbPhrase:
    def __init__(verb: Verb, parameters, args):
        self.verb = verb
        self.parameters = parameters
        self.args = args

class DeterminerPhrase:
    def __init__(determination, number):
        self.determination = determination
        self.number = number


class Noun:
    def __init__(inflection: Inflection, noun_properties: [number, case])

class Verb:
    def __init__(morphology: Morphology, arguments: [*NounPhrase]):
        self.morphology = morphology
        self.args = args

class Morphology:
    pass


# to be moved eventually to a different file
# PROPERTIES
class NounProperties:
    self.number = ""
    self.





def main():
    np1 = NounPhrase('DOG', 'determined')
    vp1 = VerbPhrase('RUN', 'present', 'habitual', 'possible')
    clause1 = Clause(declarative, np1, vp1)


if __name__ == 'main':
    main()



