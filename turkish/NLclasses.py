# TURKISH

class Clause:
    pass

class Declarative: # Proposition ???
    def __init__(subject, predicate, properties = {'discourse function': ['IS_PROPOSITIONAL', 'REQUESTS_RESPONSE']}): # well figure this out better later

        




class Clause:

    def __init__(subject: NounPhrase, predicate: VerbPhrase, clausetype: ClauseType):

        self.subject = subject
        self.predicate = predicate
        self.clausetype = clausetype


    def tostring(): # "surface structure !"

        if self.clausetype == 'declarative':
            return LanguageObject(subject) + LanguageObject(predicate)

        if self.clausetype == 'open-interrogative':
            # its as if we can almost treat open interrogatives like declarative sentences .... we dont need the clausetype open interrogative? OR is it possible to combine open and closed, at all? 
            # if we unify this with some sort of symbolic "language of discourse" then we can greatly simplify this to "requesting confirmation" vs. not - any element tagged as a "blank" is understood as a question WITHOUT a tag "requesting confirmation".

            if isQuestionWord(subject):


            # this gets complicated - there is a rule depending on if the subject vs. something underneath the verb... is the Wh-question...
            # maybe this is a reason to make them separate classes after all, it honestly gets pretty complicated.

            # im stumped, just choose something arbitrary.....
            # the weird thing is that if the subject is the question word, it is identical to a declarative sentence.
            # and if its the argument of literaly any other part of the sentence - a subordinated complement, an adjective - then it has this particular question-word form - questionword AUX rest of sentnece normal plus "trace" where the element moved from.... MOVEMENT

        




class Clause:
    def __init__(self, subject, predicate, clause_type='declarative'):
        self.subject = subject
        self.predicate = predicate
        self.clause_type = clause_type

        if self.clause_type == 'declarative':
            self.construct_declarative()
        elif self.clause_type == 'interrogative':
            self.construct_interrogative()
        # ... handle other clause types ...

    def construct_declarative(self):
        # Logic for declarative clause construction
        pass

    def construct_interrogative(self):
        # Logic for interrogative clause construction
        pass

    # ... other methods ...

# Usage
declarative_clause = Clause("I", "am coding", "declarative")
interrogative_clause = Clause("Are", "you coding", "interrogative")



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




class NounProperties:
    self.number = ""
    self.





def main():
    np1 = NounPhrase('DOG', 'determined')
    vp1 = VerbPhrase('RUN', 'present', 'habitual', 'possible')
    clause1 = Clause(declarative, np1, vp1)


if __name__ == 'main':
    main()



