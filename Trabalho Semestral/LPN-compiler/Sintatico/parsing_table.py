#Linha de 51 a 82
#coluna de 1 a 50
def create_rules():
    parsing_table = []
    for i in range(33):
        parsing_table.append([])
        for j in range(51):
            parsing_table[i].append([])
    for i in range(33):
        for j in range(51):
            parsing_table[i][j] = {'value': -1, 'GRA': '', 'tokens':[-1]}

    parsing_table[1][2]   = {'value': 1, 'GRA': "BLOCO", 'tokens':[2, 11, 39, 52, 53, 54, 38]}

    parsing_table[2][2]   = {'value': 3, 'GRA': "DCLVAR VAZIO", 'tokens':[17]}
    parsing_table[2][3]   = {'value': 3, 'GRA': "DCLVAR VAZIO", 'tokens':[17]}
    parsing_table[2][7]   = {'value': 2, 'GRA': "DCLVAR", 'tokens':[7, 55, 41, 56, 40, 57]}
    parsing_table[2][13]  = {'value': 3, 'GRA': "DCLVAR VAZIO", 'tokens':[17]}
    parsing_table[2][15]  = {'value': 3, 'GRA': "DCLVAR VAZIO", 'tokens':[17]}
    parsing_table[2][19]  = {'value': 3, 'GRA': "DCLVAR VAZIO", 'tokens':[17]}
    parsing_table[2][26]  = {'value': 3, 'GRA': "DCLVAR VAZIO", 'tokens':[17]}

    parsing_table[3][2]   = {'value': 13, 'GRA': "DCLFUNC VOID", 'tokens':[60, 7, 61, 39, 52, 53, 54, 4, 46, 62, 45, 38, 53]}
    parsing_table[3][3]   = {'value': 13, 'GRA': "DCLFUNC STRING", 'tokens':[60, 7, 61, 39, 52, 53, 54, 4, 46, 62, 45, 38, 53]}
    parsing_table[3][13]  = {'value': 13, 'GRA': "DCLFUNC INTRIRO", 'tokens':[60, 7, 61, 39, 52, 53, 54, 4, 46, 62, 45, 38, 53]}
    parsing_table[3][15]  = {'value': 19, 'GRA': "DCLFUNC VAZIO", 'tokens':[17]}
    parsing_table[3][19]  = {'value': 13, 'GRA': "DCLFUNC FLOAT", 'tokens':[60, 7, 61, 39, 52, 53, 54, 4, 46, 62, 45, 38, 53]}
    parsing_table[3][26]  = {'value': 13, 'GRA': "DCLFUNC CHAR", 'tokens':[60, 7, 61, 39, 52, 53, 54, 4, 46, 62, 45, 38, 53]}

    parsing_table[4][15]  = {'value': 31, 'GRA': "CORPO", 'tokens':[15, 65, 40, 66, 20]}

    parsing_table[5][41]  = {'value': 4, 'GRA': "REPIDENT VAZIO", 'tokens':[17]}
    parsing_table[5][43]  = {'value': 5, 'GRA': "REPIDENT", 'tokens':[43, 7, 55]}

    parsing_table[6][3]   = {'value': 8, 'GRA': "TIPO STRING", 'tokens':[3]}
    parsing_table[6][13]  = {'value': 6, 'GRA': "TIPO INTEIRO", 'tokens':[13]}
    parsing_table[6][19]  = {'value': 7, 'GRA': "TIPO FLOAT", 'tokens':[19]}
    parsing_table[6][26]  = {'value': 9, 'GRA': "TIPO CHAR", 'tokens':[26]}

    parsing_table[7][2]   = {'value': 10, 'GRA': "LDVAR VAZIO", 'tokens':[17]}
    parsing_table[7][3]   = {'value': 10, 'GRA': "LDVAR VAZIO", 'tokens':[17]}
    parsing_table[7][7]   = {'value': 11, 'GRA': "LDVAR", 'tokens':[59, 41, 56, 40, 57]}
    parsing_table[7][13]  = {'value': 10, 'GRA': "LDVAR VAZIO", 'tokens':[17]}
    parsing_table[7][15]  = {'value': 10, 'GRA': "LDVAR VAZIO", 'tokens':[17]}
    parsing_table[7][19]  = {'value': 10, 'GRA': "LDVAR VAZIO", 'tokens':[17]}
    parsing_table[7][26]  = {'value': 10, 'GRA': "LDVAR VAZIO", 'tokens':[17]}

    parsing_table[9][7]   = {'value': 12, 'GRA': "LID", 'tokens':[7, 55]}

    parsing_table[10][2]  = {'value': 15, 'GRA': "TIPO_RETORNO VOID", 'tokens':[2]}
    parsing_table[10][3]  = {'value': 18, 'GRA': "TIPO_RETORNO STRING", 'tokens':[3]}
    parsing_table[10][13] = {'value': 14, 'GRA': "TIPO_RETORNO INTEIRO", 'tokens':[13]}
    parsing_table[10][19] = {'value': 17, 'GRA': "TIPO_RETORNO FLOAT", 'tokens':[19]}
    parsing_table[10][26] = {'value': 16, 'GRA': "TIPO_RETORNO CHAR", 'tokens':[26]}

    parsing_table[11][39] = {'value': 26, 'GRA': "DEFPAR VAZIO", 'tokens':[17]}
    parsing_table[11][46] = {'value': 27, 'GRA': "DEFPAR", 'tokens':[46, 63, 45]}
    
    parsing_table[12][5]  = {'value': 20, 'GRA': "VALORRETORNO INTEIRO", 'tokens':[5]}
    parsing_table[12][6]  = {'value': 21, 'GRA': "VALORRETORNO FLOAT", 'tokens':[6]}
    parsing_table[12][7]  = {'value': 22, 'GRA': "VALORRETORNO VARIAVEL", 'tokens':[7]}
    parsing_table[12][8]  = {'value': 23, 'GRA': "VALORRETORNO CHAR", 'tokens':[8]}
    parsing_table[12][10] = {'value': 24, 'GRA': "VALORRETORNO STRING", 'tokens':[10]}
    parsing_table[12][45] = {'value': 25, 'GRA': "VALORRETORNO VAZIO", 'tokens':[17]}

    parsing_table[13][3]  = {'value': 28, 'GRA': "PARAM", 'tokens':[56, 64]}
    parsing_table[13][13] = {'value': 28, 'GRA': "PARAM", 'tokens':[56, 64]}
    parsing_table[13][19] = {'value': 28, 'GRA': "PARAM", 'tokens':[56, 64]}
    parsing_table[13][26] = {'value': 28, 'GRA': "PARAM", 'tokens':[56, 64]}

    parsing_table[14][40] = {'value': 29, 'GRA': "LPARAM", 'tokens':[40, 56, 64]}
    parsing_table[14][45] = {'value': 30, 'GRA': "LPARAM VAZIO", 'tokens':[17]}

    parsing_table[15][1]  = {'value': 52, 'GRA': "COMANDO WHILE", 'tokens':[1, 46, 7, 71, 45, 39, 65, 40, 66, 38]}
    parsing_table[15][7]  = {'value': 34, 'GRA': "COMANDO", 'tokens':[7, 32, 67]}
    parsing_table[15][16] = {'value': 49, 'GRA': "COMANDO IF", 'tokens':[16, 46, 7, 71, 45, 39, 65, 40, 66, 38, 72]}
    parsing_table[15][18] = {'value': 64, 'GRA': "COMANDO FOR", 'tokens':[18, 46, 7, 32, 73, 40, 7, 71, 40, 74, 45, 39, 65, 40, 66, 38]}
    parsing_table[15][23] = {'value': 67, 'GRA': "COMANDO DO", 'tokens':[23, 39, 65, 40, 66, 38, 1, 46, 7, 71, 45]}
    parsing_table[15][24] = {'value': 69, 'GRA': "COMANDO COUT", 'tokens':[24, 34, 12, 75]}
    parsing_table[15][25] = {'value': 68, 'GRA': "COMANDO CIN", 'tokens':[25, 28, 7]}
    parsing_table[15][27] = {'value': 39, 'GRA': "COMANDO FUNC", 'tokens':[27, 7, 68]}
    parsing_table[15][40] = {'value': 38, 'GRA': "COMANDO VAZIO", 'tokens':[17]}

    parsing_table[16][1]  = {'value': 33, 'GRA': "REPCOMANDO", 'tokens':[65, 40, 66]}
    parsing_table[16][3]  = {'value': 33, 'GRA': "REPCOMANDO", 'tokens':[65, 40, 66]}
    parsing_table[16][7]  = {'value': 33, 'GRA': "REPCOMANDO", 'tokens':[65, 40, 66]}
    parsing_table[16][16] = {'value': 33, 'GRA': "REPCOMANDO", 'tokens':[65, 40, 66]}
    parsing_table[16][18] = {'value': 33, 'GRA': "REPCOMANDO", 'tokens':[65, 40, 66]}
    parsing_table[16][20] = {'value': 32, 'GRA': "REPCOMANDO VAZIO", 'tokens':[17]}
    parsing_table[16][23] = {'value': 33, 'GRA': "REPCOMANDO", 'tokens':[65, 40, 66]}
    parsing_table[16][24] = {'value': 33, 'GRA': "REPCOMANDO", 'tokens':[65, 40, 66]}
    parsing_table[16][25] = {'value': 33, 'GRA': "REPCOMANDO", 'tokens':[65, 40, 66]}
    parsing_table[16][26] = {'value': 33, 'GRA': "REPCOMANDO", 'tokens':[65, 40, 66]}
    parsing_table[16][27] = {'value': 33, 'GRA': "REPCOMANDO", 'tokens':[65, 40, 66]}
    parsing_table[16][38] = {'value': 32, 'GRA': "REPCOMANDO VAZIO", 'tokens':[17]}
    parsing_table[16][40] = {'value': 33, 'GRA': "REPCOMANDO", 'tokens':[65, 40, 66]}

    parsing_table[17][5]  = {'value': 75, 'GRA': "EXPRESSAO", 'tokens':[79, 80]}
    parsing_table[17][6]  = {'value': 75, 'GRA': "EXPRESSAO", 'tokens':[79, 80]}
    parsing_table[17][7]  = {'value': 75, 'GRA': "EXPRESSAO", 'tokens':[79, 80]}
    parsing_table[17][8]  = {'value': 75, 'GRA': "EXPRESSAO", 'tokens':[79, 80]}
    parsing_table[17][10] = {'value': 75, 'GRA': "EXPRESSAO", 'tokens':[79, 80]}
    parsing_table[17][27] = {'value': 76, 'GRA': "EXPRESSAO FUNC", 'tokens':[27, 7, 68]}
    parsing_table[17][46] = {'value': 75, 'GRA': "EXPRESSAO", 'tokens':[79, 80]}

    parsing_table[18][40] = {'value': 40, 'GRA': "PARAMETROS VAZIO", 'tokens':[17]}
    parsing_table[18][45] = {'value': 40, 'GRA': "PARAMETROS VAZIO", 'tokens':[17]}
    parsing_table[18][46] = {'value': 41, 'GRA': "PARAMETROS", 'tokens':[46, 69, 70, 45]}

    parsing_table[19][5]  = {'value': 44, 'GRA': "TPARAM INTEIRO", 'tokens':[5]}
    parsing_table[19][6]  = {'value': 46, 'GRA': "TPARAM FLOAT", 'tokens':[6]}
    parsing_table[19][7]  = {'value': 48, 'GRA': "TPARAM VARIAVEL", 'tokens':[7]}
    parsing_table[19][8]  = {'value': 47, 'GRA': "TPARAM CHAR", 'tokens':[8]}
    parsing_table[19][10] = {'value': 45, 'GRA': "TPARAM STRING", 'tokens':[10]}

    parsing_table[20][43] = {'value': 43, 'GRA': "REPPAR", 'tokens':[43, 69, 70]}
    parsing_table[20][45] = {'value': 42, 'GRA': "REPPAR VAZIO", 'tokens':[17]}

    parsing_table[21][29] = {'value': 56, 'GRA': "COMPARACAO >=", 'tokens':[29, 73]}
    parsing_table[21][30] = {'value': 55, 'GRA': "COMPARACAO >", 'tokens':[30, 73]}
    parsing_table[21][31] = {'value': 53, 'GRA': "COMPARACAO ==", 'tokens':[31, 73]}
    parsing_table[21][33] = {'value': 58, 'GRA': "COMPARACAO <=", 'tokens':[33, 73]}
    parsing_table[21][35] = {'value': 57, 'GRA': "COMPARACAO <", 'tokens':[35, 73]}
    parsing_table[21][48] = {'value': 54, 'GRA': "COMPARACAO !=", 'tokens':[48, 73]}

    parsing_table[22][21] = {'value': 50, 'GRA': "ELSEPARTE", 'tokens':[21, 39, 65, 40, 66, 38]}
    parsing_table[22][40] = {'value': 51, 'GRA': "ELSEPARTE VAZIO", 'tokens':[17]}

    parsing_table[23][5]  = {'value': 59, 'GRA': "CONTCOMPARACAO", 'tokens':[5]}
    parsing_table[23][6]  = {'value': 60, 'GRA': "CONTCOMPARACAO", 'tokens':[6]}
    parsing_table[23][7]  = {'value': 63, 'GRA': "CONTCOMPARACAO", 'tokens':[7]}
    parsing_table[23][8]  = {'value': 62, 'GRA': "CONTCOMPARACAO", 'tokens':[8]}
    parsing_table[23][10] = {'value': 61, 'GRA': "CONTCOMPARACAO", 'tokens':[10]}
    
    parsing_table[24][36] = {'value': 65, 'GRA': "INCREMENTO ++", 'tokens':[36, 5]}
    parsing_table[24][49] = {'value': 66, 'GRA': "INCREMENTO --", 'tokens':[49, 5]}

    parsing_table[25][12] = {'value': 72, 'GRA': "SEQCOUT LITERAL", 'tokens':[34, 12, 75]}
    parsing_table[25][34] = {'value': 71, 'GRA': "SEQCOUT VARIAVEL", 'tokens':[34, 7, 76, 75]}
    parsing_table[25][40] = {'value': 70, 'GRA': "SEQCOUT VAZIO", 'tokens':[17]}
    #falta o literal vazio!!!

    parsing_table[26][34] = {'value': 73, 'GRA': "SEQUENCIA VAZIO", 'tokens':[17]}
    parsing_table[26][40] = {'value': 73, 'GRA': "SEQUENCIA VAZIO", 'tokens':[17]}
    parsing_table[26][43] = {'value': 74, 'GRA': "SEQUENCIA ,", 'tokens':[43, 7, 76]}

    parsing_table[29][5]  = {'value': 80, 'GRA': "TERMO", 'tokens':[81, 82]}
    parsing_table[29][6]  = {'value': 80, 'GRA': "TERMO", 'tokens':[81, 82]}
    parsing_table[29][7]  = {'value': 80, 'GRA': "TERMO", 'tokens':[81, 82]}
    parsing_table[29][8]  = {'value': 80, 'GRA': "TERMO", 'tokens':[81, 82]}
    parsing_table[29][10] = {'value': 80, 'GRA': "TERMO", 'tokens':[81, 82]}
    parsing_table[29][46] = {'value': 80, 'GRA': "TERMO", 'tokens':[81, 82]}

    parsing_table[30][37] = {'value': 77, 'GRA': "REPEXP +", 'tokens':[37, 79, 80]}
    parsing_table[30][40] = {'value': 79, 'GRA': "REPEXP VAZIO", 'tokens':[17]}
    parsing_table[30][45] = {'value': 79, 'GRA': "REPEXP VAZIO", 'tokens':[17]}
    parsing_table[30][50] = {'value': 78, 'GRA': "REPEXP -", 'tokens':[50, 79, 80]}

    parsing_table[31][5]  = {'value': 84, 'GRA': "FATOR INTEIRO", 'tokens':[5]}
    parsing_table[31][6]  = {'value': 85, 'GRA': "FATOR FLOAT", 'tokens':[6]}
    parsing_table[31][7]  = {'value': 86, 'GRA': "FATOR VARIAVEL", 'tokens':[7]}
    parsing_table[31][8]  = {'value': 88, 'GRA': "FATOR CHAR", 'tokens':[8]}
    parsing_table[31][10] = {'value': 87, 'GRA': "FATOR STRING", 'tokens':[10]}
    parsing_table[31][46] = {'value': 89, 'GRA': "FATOR EXPRESSAO", 'tokens':[46, 67, 45]}
    
    parsing_table[32][37] = {'value': 81, 'GRA': "REPTERMO VAZIO", 'tokens':[17]}
    parsing_table[32][40] = {'value': 81, 'GRA': "REPTERMO VAZIO", 'tokens':[17]}
    parsing_table[32][42] = {'value': 83, 'GRA': "REPTERMO /", 'tokens':[42, 81, 82]}
    parsing_table[32][44] = {'value': 82, 'GRA': "REPTERMO *", 'tokens':[44, 81, 82]}
    parsing_table[32][45] = {'value': 81, 'GRA': "REPTERMO VAZIO", 'tokens':[17]}
    parsing_table[32][50] = {'value': 81, 'GRA': "REPTERMO VAZIO", 'tokens':[17]}

    return parsing_table