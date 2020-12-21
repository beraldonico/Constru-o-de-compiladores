from Lexico.lexical_output import LEXICAL_OUTPUT as LEXOUT
from Sintatico.parsing_table import create_rules

DEBUG = 1

class SyntacticalAnalyzer:
    def __init__(self, filepath=None): #class constructor
        self._SUCCESS = True
        self._FAILURE = False
        self._PARSING_TABLE = create_rules()
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
                print(self._PARSING_TABLE[stack_token_id - 50][entry_vector_id])
            return self._PARSING_TABLE[stack_token_id - 50][entry_vector_id]['tokens'].copy()
        except IndexError:
            print("[ERROR] Erro sintático, regra não encontrada.")
            return self._FAILURE

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

            if DEBUG:
                print(f"[DEBUG] STACK.pop() | token_id = {token_id}")

            if token_id == '$':
                if DEBUG:
                    print("[DEBUG] Análise sintática concluída. Nenhum erro sintático foi encontrado.")
                else:
                    print("Syntatic finished")
                return self._SUCCESS

            elif token_id == entry_vector[0]:
                if DEBUG:
                    print("[DEBUG] token_id == ENTRADA[0], removing first element from entry_vector.")
                entry_vector.pop(0) # removes the first element from entry_vector
            
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

def Syntactical_Analyzer():
    syn = SyntacticalAnalyzer()
    syn.parse()