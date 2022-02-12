# Grammar rules

expression      : logic_or;

logic_or        : logic_and (OR logic_and)*;

logic_and       : equality (AND equality)*;

equality        : comparison ((EQ_EQ | NOT_EQ) comparison)*;

comparison      : term ((GREATER | GREATER_EQ | LESS | LESS_EQ) term)*;

term            : factor ((PLUS|MINUS) factor)*;

factor          : unary ((MUL|DIV) unary)*;

unary           : (MINUS) unary | atom;

atom            : NUMBER;