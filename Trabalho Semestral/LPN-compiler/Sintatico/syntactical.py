from Lexico.lexical_output import LEXICAL_OUTPUT as LEXOUT
from Sintatico.parsing_table import create_rules
from Lexico import gramatic as GRA # language gramatic

DEBUG = 1

class SyntacticalAnalyzer:
    def __init__(self, filepath=None): #class constructor
        self._SUCCESS = True
        self._FAILURE = False
        self._PARSING_TABLE = create_rules()
        self._LEVEL = ['main']
        self._INDEX = 0
        self._DCL_VAR = True
        self._DCL_FUNC = False
        self._DCL_CORPO = False
        self._DCL_EXP = False
        self._VARIABLES = []
        self._SYMBOL_TABLE = []
        self._COMMAND = []
        self._stack = ['$', 51]
        self._entry_vector =[]

        for tup in LEXOUT:
            self._entry_vector.append(tup[1])
    
    def push_to_stack(self, token):
        self._stack.append(token)
    
    def pop_from_stack(self):
        return self._stack.pop()

    def print_stack(self):
        print(self._stack)

    def search_rule(self, stack_token_id, entry_vector_id):
        try:
            if DEBUG:
                print(f'[DEBUG] Searching PARSING_TABLE[{stack_token_id}][{entry_vector_id}]')
                if stack_token_id - 50 < 0:
                    print("[DEBUG] stack_token_id - 50 < 0")
                    return self._FAILURE

                print(self._PARSING_TABLE[stack_token_id - 50][entry_vector_id])
            return self._PARSING_TABLE[stack_token_id - 50][entry_vector_id]['tokens'].copy()
        except IndexError:
            print(f"[ERROR] Erro sintático, regra não encontrada, PARSING_TABLE[{stack_token_id}][{entry_vector_id}].")
            return self._FAILURE

    def semantic(self, token, m_entry_vector):
        if DEBUG:
            print("[DEBUG] Iniciando execução da análise semântica...")
            print(f"[DEBUG] NIVEL = {self._LEVEL}")
            print(f"[DEBUG] TOKEN = {token}")

        if len(m_entry_vector) < 2:
            if DEBUG:
                print("[DEBUG] m_entry_vector < 2")
            return

            #token não é um tipo de variavel > varaivel > (: ou ;)
        if token not in GRA.TYPES_INDEX and m_entry_vector[1] == 7 and (m_entry_vector[2] == 43 or m_entry_vector[2] == 41):
            # isto não é uma declaração de função
            # porque não tem tipo de variável antes de 7 (nomevariavel)
            # isto é uma declaração de variável
            self._DCL_VAR = True
            self._DCL_CORPO = False

        if token in GRA.TYPES_INDEX and m_entry_vector[1] == 7:
            # token é algum tipo reservado (integer, float...) e o próximo item no vetor de entrada é 7 (nomevariavel)
            # exemplo: integer soma
            # início da declaração de uma função
            self._DCL_VAR = False
            self._DCL_FUNC = True
            self._DCL_CORPO = False

        elif token == 15: # 15 == inicio
            # início da declaração do CORPO
            self._DCL_VAR = False
            # fiz pq pode ter corpo dentro de func
            # self._DCL_FUNC = False
            self._DCL_CORPO = True

        if token == 7 and self._DCL_VAR == True: # token é 'nomevariavel' e a flag de declaração de variáveis é True
            # declaração de múltiplas variáveis
            # exemplo: var1 , var2 : integer ;
            self._VARIABLES.append(LEXOUT[self._INDEX][0])

        if token == 41: # ':'
            for variable in self._VARIABLES:

                for symbol in self._SYMBOL_TABLE:
                    if variable == symbol['name'] and self._LEVEL[-1] == symbol['level']:
                        if DEBUG:
                            print("[DEBUG] Symbol already in symbol table!")
                        #raise("[DEBUG] Symbol already in symbol table!")

                self._SYMBOL_TABLE.append(
                    {
                        'name': variable,
                        'category': 'VARIABLE',
                        'type': LEXOUT[self._INDEX+1][0],
                        'level': self._LEVEL[-1]
                    }
                )

            self._VARIABLES.clear()

        if self._DCL_FUNC and token in GRA.TYPES_INDEX and not self._DCL_VAR:
            self._SYMBOL_TABLE.append(
                    {
                        'name': LEXOUT[self._INDEX+1][0],
                        'category': 'PROCEDURE',
                        'type': LEXOUT[self._INDEX][0],
                        'level': self._LEVEL[-1]
                    }
                )
            self._DCL_FUNC = False

        try:
            if DEBUG:
                print(f"[DEBUG] ENTRY_VECTOR = {m_entry_vector[1]}")
        except:
            pass

        """
        Obter nível (escopo) para utilizar na tabela de símbolos 
        +-------------------------------------------------------+
        |    NOME   |    CATEGORIA    |    TIPO    |    NÍVEL   |
        +-------------------------------------------------------+
            var1        variavel        integer         main
        """
        if token == 40 and m_entry_vector[1] in GRA.TYPES_INDEX and m_entry_vector[2] == 7:
            if DEBUG:
                print("[DEBUG] token == 40 and self._entry_vector[0] in GRA.TYPES")
            #self._LEVEL.append(m_entry_vector[2])
                print(f"[DEBUG] {LEXOUT[self._INDEX+2][0]}")
            self._LEVEL.append(LEXOUT[self._INDEX+2][0])
        
        if self._DCL_CORPO:
            # início de uma análise semântica de uma expressão
            if token == 7 and self._DCL_EXP: # token é 'nomevariavel' 
                for index,symbol in enumerate(self._SYMBOL_TABLE):
                    if LEXOUT[self._INDEX][0] in symbol['name']: # variável existe na tabela de símbolos?
                        self._COMMAND.append(symbol['type']) # sim: então adiciona o tipo da variável na lista self._COMMAND
                        break
                    elif index == (len(self._SYMBOL_TABLE) - 1): # não: erro, variável não declarada
                        print(f"ERRO SEMANTICO: Variavel não declarada {LEXOUT[self._INDEX][0]}")
                        #raise

            # adiciona o tipo da variável na lista self._COMMAND
            if token == 5 and self._DCL_EXP:  self._COMMAND.append('integer')
            if token == 6 and self._DCL_EXP:  self._COMMAND.append('float')
            if token == 8 and self._DCL_EXP:  self._COMMAND.append('char')
            if token == 10 and self._DCL_EXP: self._COMMAND.append('string')

            if token == 7 and m_entry_vector[1] == 32: # token é 'nomevariavel' e a próxima posição do vetor de entrada é '='?
                self._DCL_EXP = True # sim: então é uma declaração de EXPRESSÃO
                for symbol in self._SYMBOL_TABLE:
                    if LEXOUT[self._INDEX][0] in symbol['name']: # variável existe na tabela de símbolos?
                        self._COMMAND.append(symbol['type']) # sim: então adiciona o tipo da variável na lista self._COMMAND
                        break
                if len(self._COMMAND) == 0: # algum tipo foi adicionado na lista self._COMMAND?
                    print(f"ERRO SEMANTICO: Variavel não declarada {LEXOUT[self._INDEX][0]}") # não: erro, variável não declarada
                    #raise

            #print(f"[DEBUG] self._DCL_EXP: {self._DCL_EXP}")
            if token == 40 and self._DCL_EXP: # 40 == ';'
                #print(f"[DEBUG] self._COMMAND: {self._COMMAND}")
                # float só recebe float, integer só recebe integer
                if all(x == self._COMMAND[0] for x in self._COMMAND): # verifica se os tipos são compatíveis
                    if DEBUG:
                        print("[DEBUG] All variables types are compatible (equal)!")
                else:
                    print(f"ERROR Semantico expressão, variables types are not compatible (different types): {LEXOUT[self._INDEX - 1][0]}.")
                self._DCL_EXP = False
                self._COMMAND.clear()
            # fim da análise semântica de uma EXPRESSÃO
            
            # início de análise de WHILE ou IF
            if token == 1 or token == 16 :
                if m_entry_vector[2] == 7: 
                    for symbol in self._SYMBOL_TABLE:
                        if LEXOUT[self._INDEX + 2][0] in symbol['name']:
                            self._COMMAND.append(symbol['type']) # integer
                            break
                if len(self._COMMAND) == 0:
                    print(f"ERRO SEMANTICO: Primeira variavel do if ou while não declarada {LEXOUT[self._INDEX + 2][0]}")
                if m_entry_vector[4] == 5:    self._COMMAND.append('integer')
                elif m_entry_vector[4] == 6:  self._COMMAND.append('float')
                elif m_entry_vector[4] == 8:  self._COMMAND.append('char')
                elif m_entry_vector[4] == 10: self._COMMAND.append('string')
                elif m_entry_vector[4] == 7:
                    for index,symbol in enumerate(self._SYMBOL_TABLE):
                        if LEXOUT[self._INDEX + 4][0] in symbol['name']:
                            self._COMMAND.append(symbol['type']) # integer
                            break
                        elif index == (len(self._SYMBOL_TABLE) - 1):
                            print(f"ERRO SEMANTICO: Segunda variavel do if ou while não declarada {LEXOUT[self._INDEX + 4][0]}")
                if all(x == self._COMMAND[0] for x in self._COMMAND):
                    if DEBUG:
                        print("[DEBUG] All items are equal!")
                else:
                    print((f"ERROR Semantico IF, variables types are not compatible (different types):{LEXOUT[self._INDEX][0]}."))
                self._COMMAND.clear()
            # fim de análise de WHILE ou IF

            # início de análise semântica de FOR
            if token == 18 : # 18 == 'for'
                if m_entry_vector[6] == 7: 
                    for index,symbol in enumerate(self._SYMBOL_TABLE):
                        if LEXOUT[self._INDEX + 6][0] in symbol['name']:
                            self._COMMAND.append(symbol['type']) # integer
                            break
                        elif index == (len(self._SYMBOL_TABLE) - 1):
                            print(f"ERRO SEMANTICO: Variavel de comparação 1 do for não declarada {LEXOUT[self._INDEX + 6][0]}")
                if m_entry_vector[8] == 5:    self._COMMAND.append('integer')
                elif m_entry_vector[8] == 6:  self._COMMAND.append('float')
                elif m_entry_vector[8] == 8:  self._COMMAND.append('char')
                elif m_entry_vector[8] == 10: self._COMMAND.append('string')
                elif m_entry_vector[8] == 7:
                    for index,symbol in enumerate(self._SYMBOL_TABLE):
                        if LEXOUT[self._INDEX + 8][0] in symbol['name']:
                            self._COMMAND.append(symbol['type']) # integer
                            break
                        elif index == (len(self._SYMBOL_TABLE) - 1):
                            print(f"ERRO SEMANTICO: Variavel de comparação 2 do for não declarada {LEXOUT[self._INDEX + 8][0]}")
                if m_entry_vector[11] == 5:    self._COMMAND.append('integer')
                else:
                    print(f"ERRO SEMANTICO: Variavel de incremento do for não é inteiro {LEXOUT[self._INDEX + 11][0]}")
                if all(x == self._COMMAND[0] for x in self._COMMAND):
                    if DEBUG:
                        print("[DEBUG] All items are equal!")
                else:
                    print((f"ERROR Semantico FOR, variables types are not compatible (different types):{LEXOUT[self._INDEX][0]}."))
                self._COMMAND.clear()
            # fim de análise semântica de FOR

            # início de análise semântica de COUT
            if token == 24 : # 24 == 'cout'
                for index_1, token in enumerate(m_entry_vector):
                    if token == 7:
                        for index_2,symbol in enumerate(self._SYMBOL_TABLE):
                            if LEXOUT[self._INDEX + index_1][0] in symbol['name']:
                                break
                            elif index_2 == (len(self._SYMBOL_TABLE) - 1):
                                print(f"ERRO SEMANTICO COUT: Variavel do cout não declarada {LEXOUT[self._INDEX + index_1][0]}")
            # fim de análise semântica de COUT

            # início de análise semântica de CIN
            if token == 25 : # 25 == 'cout'
                for index, symbol in enumerate(self._SYMBOL_TABLE):
                    if LEXOUT[self._INDEX + 2][0] in symbol['name']:
                        break
                    elif index == (len(self._SYMBOL_TABLE) - 1):
                        print(f"ERRO SEMANTICO: Variavel do cin não declarada {LEXOUT[self._INDEX + 2][0]}")
            # fim de análise semântica de CIN
                
            # início de análise semântica de RETURN
            if token == 4 : # 4 == 'return'
                for index, symbol in enumerate(self._SYMBOL_TABLE):
                    if LEXOUT[self._INDEX + 2][0] in symbol['name']:
                        break
                    elif index == (len(self._SYMBOL_TABLE) - 1): # or 
                        print(f"ERRO SEMANTICO: Variavel do return não declarada {LEXOUT[self._INDEX + 2][0]}")
            # fim de análise semântica de RETURN

            if token == 4: # 4 == return
                # fim da declaração de uma função (return)
                self._DCL_VAR = False
                self._DCL_FUNC = False
                self._DCL_CORPO = False
                #rever level de declaração e atribuição de variaveis 
                self._LEVEL.pop()

        if DEBUG:
            print(f"[DEBUG] self._VARIABLES = {self._VARIABLES}")
            print(f"[DEBUG] self._SYMBOL_TABLE = {self._SYMBOL_TABLE}")


    def parse(self):
        iteration_counter = 0
        
        if DEBUG:
            print("[DEBUG] Starting parsing process...")

        entry_vector = self._entry_vector.copy()

        while(True):
            if DEBUG:
                print("========================================")
                print(f"[DEBUG] ITERAÇÃO: {iteration_counter}")
                print(f"[DEBUG] ENTRADA: {entry_vector}")
                print(f"[DEBUG] STACK: {self._stack}")

            token_id = self.pop_from_stack() # get the element from the top of the stack
            
            self.semantic(token_id, entry_vector)

            if DEBUG:
                print(f"[DEBUG] STACK.pop() | token_id = {token_id}")

            if token_id == '$':
                if DEBUG:
                    print("[DEBUG] Análise sintática concluída. Nenhum erro sintático foi encontrado.")
                else:
                    print("\nSyntatic finished\n")
                return self._SUCCESS

            elif token_id == entry_vector[0]:
                if DEBUG:
                    print("[DEBUG] token_id == ENTRADA[0], removing first element from entry_vector.")
                entry_vector.pop(0) # removes the first element from entry_vector
                self._INDEX += 1
            
            else: # token_id != entry_vector[0] -> must search for rule in parsing PARSING_TABLE
                tokens = self.search_rule(token_id, entry_vector[0])
                if tokens:
                    if DEBUG:
                        print(f"[DEBUG] Tokens retornados pela regra: {tokens}")

                    if tokens[0] == 17: # if tokens == 17 (î) then do not push it to the stack
                        iteration_counter = iteration_counter + 1
                        continue

                    tokens.reverse()
                    if DEBUG:
                        print(f"[DEBUG] Tokens (reversed): {tokens}")

                    for token in tokens: # push tokens to stack
                        self.push_to_stack(token)

                else:
                    if DEBUG:
                        print("[DEBUG] Função search_rule() falhou (retornou False).")
                    return self._FAILURE
            
            if DEBUG:
                print(f"[DEBUG] ENTRADA: {entry_vector}")
                print(f"[DEBUG] STACK: {self._stack}")
                
            iteration_counter = iteration_counter + 1
    
    def final_print(self):
        print(f"Tabela de simbolos = {self._SYMBOL_TABLE}")

def Syntactical_Analyzer():
    syn = SyntacticalAnalyzer()
    syn.parse()
    syn.final_print()
    print("Semantic finished")