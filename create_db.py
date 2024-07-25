import sqlite3

# Conecte-se ao banco de dados (será criado se não existir)
conn = sqlite3.connect('palavras.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS palavras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palavra TEXT NOT NULL
)
''')

palavras = [
    "sagaz", "âmago", "negro", "termo", "êxito", "mexer", "nobre", "senso", "afeto", 
    "algoz", "ética", "plena", "fazer", "tênue", "assim", "mútua", "vigor", "sobre", 
    "aquém", "sutil", "porém", "seção", "poder", "fosse", "sanar", "ideia", "cerne", 
    "audaz", "moral", "inato", "desde", "muito", "justo", "quiçá", "honra", "sonho", 
    "torpe", "razão", "amigo", "ícone", "etnia", "fútil", "égide", "anexo", "tange", 
    "dengo", "haver", "lapso", "expor", "então", "tempo", "seara", "mútuo", "boçal", 
    "hábil", "casal", "saber", "ávido", "pesar", "ardil", "graça", "dizer", "óbice", 
    "causa", "dever", "sendo", "genro", "coser", "xibiu", "tenaz", "pária", "estar", 
    "posse", "brado", "crivo", "ainda", "prole", "comum", "temor", "ápice", "corja", 
    "ânimo", "detém", "pauta", "ceder", "assaz", "ânsia", "culto", "fugaz", "censo", 
    "digno", "mundo", "atroz", "forte", "gleba", "vício", "vulgo", "cozer", "valha", 
    "criar", "mesmo", "saúde", "revés", "denso", "neném", "pudor", "dogma", "jeito", 
    "todos", "regra", "louco", "atrás", "ordem", "mercê", "homem", "feliz", "impor", 
    "pedir", "banal", "round", "clava", "limbo", "coisa", "usura", "juízo", "sábio", 
    "apraz", "forma", "servo", "prosa", "tenro", "desse", "falar", "pífio", "presa", 
    "certo", "ajuda", "posso", "cunho", "ontem", "viril", "vendo", "legal", "devir", 
    "herói", "manso", "falso", "meiga", "valor", "reaça", "fácil", "visar", "mágoa", 
    "ébrio", "sério", "acaso", "puder", "fluir", "guisa", "afago", "platô", "linda", 
    "lugar", "ímpio", "temer", "abrir", "garbo", "afins", "praxe", "obter", "gerar", 
    "óbvio", "cisma", "matiz", "burro", "bruma", "união", "pleno", "crise", "êxodo", 
    "havia", "fluxo", "vênia", "senil", "tédio", "ritmo", "morte", "enfim", "levar", 
    "tomar", "olhar", "visão", "álibi", "casta", "brega", "gênio", "prumo", "parvo", 
    "vital", "bravo", "favor", "reles", "cabal", "pulha", "falta", "ouvir", "vivaz", 
    "reter", "parco", "tecer", "calma", "valia", "sábia", "outro", "ameno", "laico", 
    "grato", "viver", "tendo", "terra", "possa", "noção", "carma", "passo", "força", 
    "único", "achar", "nicho", "ranço", "pobre", "noite", "façam", "prime", "rogar", 
    "rever", "fardo", "farsa", "fator", "óbito", "ativo", "selar", "coeso", "épico", 
    "dúbio", "anelo", "citar", "sinto", "papel", "nossa", "leigo", "cisão", "sesta", 
    "claro", "sonso", "ciúme", "adiar", "cesta", "líder", "haste", "velho", "deter", 
    "tende", "gente", "humor", "atuar", "revel", "sulco", "ideal", "vemos", "exato", 
    "árduo", "ponto", "ficar", "igual", "amplo", "vazio", "fonte", "marco", "labor", 
    "feixe", "lavra", "terno", "débil", "hiato", "remir", "senão", "cauda", "capaz", 
    "gesto", "ótica", "tanto", "imune", "ambos", "varão", "inata", "jovem", "relva", 
    "vácuo", "toada", "tenra", "sonsa", "ciclo", "apoio", "caçar", "coçar", "velar", 
    "raiva", "algum", "vimos", "pouco", "série", "xeque", "chuva", "farão", "horda", 
    "leito", "fusão", "advém", "entre", "feito", "sente", "probo", "coesa", "doido", 
    "minha", "frase", "carro", "cruel", "anuir", "trama", "torço", "verso", "brisa", 
    "ímpar", "rigor", "botar", "chata", "massa", "blasé", "lazer", "prece", "maior", 
    "dorso", "pegar", "sorte", "signo", "moção", "seita", "fauna", "covil", "preso", 
    "credo", "furor", "casto", "morar", "livro", "flora", "vetor", "adeus", "dócil", 
    "peste", "liame", "ambas", "comer", "plano", "faina", "houve", "senda", "ocaso", 
    "nunca", "pecha", "árido", "saiba", "setor", "praia", "aliás", "manha", "vírus", 
    "peixe", "ardor", "meses", "agora", "visse", "mudar", "salvo", "beata", "aceso", 
    "antro", "vulto", "rezar", "vasto", "breve", "pajem", "parte", "saída", "morro", 
    "junto", "banzo", "risco", "campo", "ótimo", "reger", "prado", "avaro", "sinal", 
    "grupo", "áureo", "birra", "anais", "segue", "andar", "lenda", "serão", "antes", 
    "motim", "opção", "acima", "chulo", "estão", "fugir", "áurea", "leite", "nação", 
    "conta", "rapaz", "átomo", "brava", "treta", "vilão", "fruir", "oxalá", "parar", 
    "verbo", "ídolo", "texto", "fitar", "índio", "tirar", "tenso", "jazia", "prazo", 
    "reino", "gerir", "puxar", "festa", "alude", "norma", "traga", "tosco", "exame", 
    "época", "prova", "filho", "átrio", "bando", "malta", "turba", "corpo", "psico", 
    "anciã", "arcar", "preto", "sinhá", "cheio", "aonde", "acesa", "avião", "voraz", 
    "manhã", "fatal", "fatos", "sarça", "quase", "cópia", "praga", "venal", "certa", 
    "ligar", "quota", "logro", "nosso", ]


for palavra in palavras:
    cursor.execute('INSERT INTO palavras (palavra) VALUES (?)', (palavra,))

conn.commit()
conn.close()
