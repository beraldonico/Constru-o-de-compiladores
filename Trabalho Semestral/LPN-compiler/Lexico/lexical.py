from Lexico import gramatic as GRA # language gramatic
import sys

DEBUG = 0

class LexicalAnalyzer:
    def __init__(self, filepath=None): #class constructor
        self._source_code_filepath = filepath
        self._source_code_vector = None
        self._tokens_vector = []
        self._tokens_tuple_vector = []
        self._token_delimiters = [' ', '\n', '\r', '\t']

        if filepath: #If file is defined, read file data
            self.read_source_code_file(filepath)

    def read_source_code_file(self, filepath=None):
        if filepath:
            self._source_code_filepath = filepath
            with open(self._source_code_filepath) as f: #Read file data
                self._source_code_vector = f.read()
            return True
        else:
            return False

    #Remove comments from source code
    def remove_comments(self):
        comment = False #If inside a comment

        #For each token in a comment change with ''
        #Increment index counter to continue relating with gramatic 
        for index, token in enumerate(self._tokens_vector):
            #print(token)
            if token["token"] == '*/':
                if not comment:
                    raise Exception("Não foi encontrado uma abertura de comentário '/*'")
                else:
                    self._tokens_vector[index]["token"] = ''
                    comment = False
            if comment:
                self._tokens_vector[index]["token"] = ''
            if token["token"] == '/*':
                comment = True
                self._tokens_vector[index]["token"] = ''
        if comment:
            raise Exception("Não foi encontrado um fechamento de comentário '*/'")

        
        #Remove all '' to reduce final executable 
        tmp_tokens_vector = []
        for token in self._tokens_vector:
            if token["token"] != '':
                tmp_tokens_vector.append(token)

        self._tokens_vector = tmp_tokens_vector.copy()

    # Parsing token of source code
    def extract_tokens(self):
        line = 1
        literal = False
        string = False
        char = False
        token = ''
        for symbol in self._source_code_vector:
            if symbol in self._token_delimiters and not literal and not string and not char:
                if token != '':
                    self._tokens_vector.append({"token": token, "line":line})
                token = ''
                if symbol == '\n':
                    line = line + 1
            else:
                token = token + symbol

            if symbol == '~':
                literal = not literal

            if symbol == '\"':
                string = not string

            if symbol == '\'':
                char = not char
            
        if literal:
            raise Exception(f"Literal não finalizado na linha {line}")
        
        if char:
            raise Exception(f"Char não finalizado na linha {line}")
        
        if string:
            raise Exception(f"String não finalizado na linha {line}")

    # Print with new line (\n)
    def print_tokens_vector(self):
        vector = self._tokens_vector

        print("#======================================================================================================#")
        print("| INDEX |                       TOKEN                       |      TYPE      |    CODE    |    LINE    |")
        print("|------------------------------------------------------------------------------------------------------|")
        for index in range(len(vector)):
            print(
                '|{message:{fill}{align}{width}}|'.format(message=index,fill=' ',align='^',width=7),
                '{message:{fill}{align}{width}}|'.format(message=vector[index]["token"],fill=' ',align='^',width=50),
                '{message:{fill}{align}{width}}|'.format(message=vector[index]["type"],fill=' ',align='^',width=15),
                '{message:{fill}{align}{width}}|'.format(message=vector[index]["code"],fill=' ',align='^',width=11),
                '{message:{fill}{align}{width}}|'.format(message=vector[index]["line"],fill=' ',align='^',width=11),
                )
            print("|--------------------------------------------------------------------------------------------------|")
            #print(f"| {index} | {vector[index]['token']}")
        print("#==================================================================================================#")
    
    # Print with new line (\n)
    def print_tokens_tuple(self):
        vector = self._tokens_tuple_vector
        
        print("#========================================================================#")
        print("| INDEX |                       TOKEN                       |    CODE    |")
        print("|------------------------------------------------------------------------|")
        for index in range(len(vector)):
            print(
                '|{message:{fill}{align}{width}}|'.format(message=index,fill=' ',align='^',width=7),
                '{message:{fill}{align}{width}}|'.format(message=vector[index][0],fill=' ',align='^',width=50),
                '{message:{fill}{align}{width}}|'.format(message=vector[index][1],fill=' ',align='^',width=11),
                )
            print("|------------------------------------------------------------------------|")
        print("#========================================================================#")

    @property
    def source_code_filepath(self):
        return self._source_code_filepath

    @source_code_filepath.setter
    def source_code_filepath(self, filepath):
        self._source_code_filepath = filepath

    # Check integer
    def is_integer(self, number):
        try:
            int(number)
            return True
        except:
            return False
    
    # Check caracter
    def is_character(self, c):
        try:
            return c.encode('ascii').isalpha()
        except:
            return False

    # Check float
    def is_float(self, number):
        try:
            return number.replace(".", "", 1).isdigit()
        except:
            return False

    # Relate token to each token cod
    def define_tokens(self):
        index = 0
        while index < len(self._tokens_vector):
            token = self._tokens_vector[index]["token"]
            # Literal
            if token[0] == '~' and token[-1] == '~':
                self._tokens_tuple_vector.append((token[2:-2], 12))
                self._tokens_vector[index]["type"] = "Literal"
                self._tokens_vector[index]["code"] = 12
            # Char
            elif token[0] == '\'' and token[-1] == '\'':
                self._tokens_tuple_vector.append((token[2], 8))
                self._tokens_vector[index]["type"] = "nomedochar"
                self._tokens_vector[index]["code"] = 8
            # String
            elif token[0] == '\"' and token[-1] == '\"':
                self._tokens_tuple_vector.append((token[2:-2], 10))
                self._tokens_vector[index]["type"] = "nomedastring"
                self._tokens_vector[index]["code"] = 10
            # Reserved words
            elif token in GRA.TOKENS:
                self._tokens_tuple_vector.append((token, GRA.TOKENS_INDEX[GRA.TOKENS.index(token)]))
                self._tokens_vector[index]["type"] = "Reserved"
                self._tokens_vector[index]["code"] = GRA.TOKENS_INDEX[GRA.TOKENS.index(token)]
            # Variable Types
            elif token in GRA.TYPES:
                self._tokens_tuple_vector.append( (token, GRA.TYPES_INDEX[GRA.TYPES.index(token)]))
                self._tokens_vector[index]["type"] = "Type"
                self._tokens_vector[index]["code"] = GRA.TYPES_INDEX[GRA.TYPES.index(token)]
            # Code symbols
            elif token in GRA.SYMBOLS:
                self._tokens_tuple_vector.append((token, GRA.SYMBOLS_INDEX[GRA.SYMBOLS.index(token)]))
                self._tokens_vector[index]["type"] = "Symbol"
                self._tokens_vector[index]["code"] = GRA.SYMBOLS_INDEX[GRA.SYMBOLS.index(token)]
            # tratar identificador
            elif self.is_character(token[0]): 
                self._tokens_tuple_vector.append((token, 7))
                self._tokens_vector[index]["type"] = "Variable"
                self._tokens_vector[index]["code"] = 7
            elif self.is_integer(token): # tratar identificador
                self._tokens_tuple_vector.append((token, 5))
                self._tokens_vector[index]["type"] = "numerointeger"
                self._tokens_vector[index]["code"] = 5
            elif self.is_float(token): # tratar identificador
                self._tokens_tuple_vector.append((token, 6))
                self._tokens_vector[index]["type"] = "numerofloat"
                self._tokens_vector[index]["code"] = 6
            else:
                sys.exit(f"Token não identificado na linha {self._tokens_vector[index]['line']}: {token}")
            index += 1
    
    def generate_file(self):
        with open("Lexico/lexical_output.py", "w") as f:
            f.write("LEXICAL_OUTPUT = [\n")
            for index in range(len(self._tokens_tuple_vector)):
                f.write(str(self._tokens_tuple_vector[index]) + ",\n")
            f.write("]")
        print("File Generated")

    def final_print(self):
        print(f"Tabela de simbolos = {self._tokens_tuple_vector}")


def lexical_analyzer(argv=None):
    lexa = LexicalAnalyzer(argv)
    #lexa = LexicalAnalyzer('test.lpn')
        
    lexa.extract_tokens()
    lexa.remove_comments()
    lexa.define_tokens()
    
    if DEBUG:
        lexa.print_tokens_vector()
        print()
        lexa.print_tokens_tuple()

    lexa.generate_file()

    lexa.final_print()
    print("Lexical finished")