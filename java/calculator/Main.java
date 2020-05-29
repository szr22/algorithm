package java.calculator;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 一个使用样例
        Calculator calc = new Calculator();

        // 中间的数字是优先级（precedence），数字越小优先级越高
        // 这里限定二元运算符是left associative，一元运算符是right associative
        calc.registerOperation("+", 500, (a,b) -> a+b);
        calc.registerOperation("-", 500, (a,b) -> a-b);
        calc.registerOperation("*", 400, (a,b) -> a*b);
        calc.registerOperation("/", 400, (a,b) -> a/b);
        calc.registerOperation("^", 200, (a,b) -> (int) Math.pow(a,n));
        calc.registerOperation("-", 100, (a) -> -a);

        // 某道Calculator变形题，重定义了"&"和"|"的语义
        calc.registerOperation("&", 600, (a,b) -> Math.max(a,b));
        calc.registerOperation("|", 800, (a,b) -> Math.min(a,b));

        calc.registerFunction("abs", (int ...a) -> Math.abs(a[0]));
        calc.registerFunction("min", (int ...a) -> Arrays.stream(a).min().getAsInt());
        calc.registerFunction("max", (int ...a) -> Arrays.stream(a).max().getAsInt());

        System.out.println(calc.evaluate("1 + 2 * 3 ^ abs(6 - 3 * 3) + (-8) / (-2)"));
        System.out.println(calc.evaluate("min(-3 * 2, -4, -5) * max(5, 6, 7, min(8, 9))"));
    }
}

class Calculator{
    private Map<String, OperationInfo<UnaryOperation>> unaryOperations;
    private Map<String, OperationInfo<BinaryOperation>> binaryOperations;
    private Map<String, Function> functions;

    public Calculator() {
        this.unaryOperations = new HashMap<String, OperationInfo<UnaryOperation>>();
        this.binaryOperations = new HashMap<String, OperationInfo<BinaryOperation>>();
        this.functions = new HashMap<String, Function>();
    }

    public void registerOperation(String operator, int precedence, UnaryOperation operation) {
        unaryOperations.put(
            operator, new OperationInfo<UnaryOperation>(precedence, operation)
        );
    }

    public void registerOperation(String operator, int precedence, BinaryOperation operation) {
        binaryOperations.put(
            operator, new OperationInfo<BinaryOperation>(precedence, operation)
        );
    }

    public void registerFunction(String name, Function function) {
        functions.put(name, function);
    }

    public int evaluate(String expression) {
        CalculatorExecutor executor = CalculatorExecutor(unaryOperations, binaryOperations, functions, expression);
        return executor.run();
    }
}

// 对一元运算符的抽象
interface UnaryOperation{
    public int apply(int operand);
}

// 对二元运算符的抽象
interface BinaryOperation  {
    public int apply(int lhs, int rhs);
}

// 对函数的抽象
interface Function {
    public int apply(int ...operands);
}

// 用于打包operation和对应的precedence信息的小类
class OperationInfo<T> {
    public final int precedence;
    public final T operation;
    public OperationInfo(int precedence, T operation){
        this.precedence = precedence;
        this.operation = operation;
    }
}

// LL(1) Recursive Descent Syntax Directed Translator
class CalculatorExecutor {
    private final Map<String, OperationInfo<UnaryOperation>> unaryOperations;
    private final Map<String, OperationInfo<BinaryOperation>> binaryOperations;
    private final Map<String, Function> functions;

    private final String stream;
    private int position;

    // 词法部分也合并到这个类里了
    private enum TokenType {
        INTEGER,
        NAME,
        OPERATOR,
        LPAREN,
        RPAREN,
        COMMA,
        EOS,
        ERROR
    }

    private class Token {
        public final TokenType type;
        public final Object payload;
        public final int columnNumber;
        public Token(TokenType type, int columnNumber) {
          this(type, columnNumber, null);
        }
        public Token(TokenType type, int columnNumber, Object payload) {
          this.type = type;
          this.payload = payload;
          this.columnNumber = columnNumber;
        }
    }

    private Stack<Token> tokens;

    public CalculatorExecutor(
        Map<String, OperationInfo<UnaryOperation>> unaryOperations,
        Map<String, OperationInfo<BinaryOperation>> binaryOperations,
        Map<String, Function> functions,
        String stream) {
        this.unaryOperations = unaryOperations;
        this.binaryOperations = binaryOperations;
        this.functions = functions;
        this.stream = stream;
        this.position = 0;
        this.tokens = new Stack<Token>();
    }

    public int run() {
        int value = evalExpr(Integer.MAX_VALUE);
        passNextToken(TokenType.EOS);
        return value;
    }

    // 语法处理部分
    private int evalExpr(int precedence) {
        int value = evalFactor(precedence);

        // 二元运算符，注意这里对优先级的处理方法
        while (hasNextToken(TokenType.OPERATOR)) {
          Token token = nextToken();
          OperationInfo<BinaryOperation> info =
              binaryOperations.get((String)token.payload);
          if (info == null || info.precedence >= precedence) {
            pushBack(token);
            break;
          }
          value = info.operation.apply(value, evalExpr(info.precedence));
        }
        return value;
    }

    private int evalFactor(int precedence) {
        Token token = nextToken();

        // Case 1. 数字自身
        if (token.type == TokenType.INTEGER) {
          return (Integer)token.payload;
        }

        // Case 2. 一元运算符
        if (token.type == TokenType.OPERATOR) {
            OperationInfo<UnaryOperation> info =
                unaryOperations.get((String)token.payload);
            if (info == null || info.precedence > precedence) {
                error(token);
            }
            return info.operation.apply(evalExpr(info.precedence));
        }

        // Case 3. 函数调用
        if (token.type == TokenType.NAME) {
            Function func = functions.get((String)token.payload);
            if (func == null) {
                error(token);
            }
            ArrayList<Integer> args = new ArrayList<Integer>();
            passNextToken(TokenType.LPAREN);
            while (!hasNextToken(TokenType.RPAREN)) {
                args.add(evalExpr(Integer.MAX_VALUE));
                if (!hasNextToken(TokenType.COMMA)) {
                break;
                }
                nextToken();
            }
            passNextToken(TokenType.RPAREN);
            return func.apply(args.stream().mapToInt(x -> x).toArray());
            }

        // Case 4. 括号表达式
        if (token.type == TokenType.LPAREN) {
            int value = evalExpr(Integer.MAX_VALUE);
            Token rp = nextToken();
            if (rp.type != TokenType.RPAREN) {
                error(token);
            }
            return value;
        }

        error(token);
        return 0;
    }

    // 词法处理部分
    private boolean hasNextToken(TokenType ...expected) {
        Token token = nextToken();
        boolean status = Arrays.stream(expected).anyMatch(x -> x == token.type);
        pushBack(token);
        return status;
    }

    private void passNextToken(TokenType ...expected) {
        Token token = nextToken();
        if (!Arrays.stream(expected).anyMatch(x -> x == token.type)) {
            error(token);
        }
    }

    private void pushBack(Token token) {
        tokens.add(token);
    }

    private Token nextToken() {
        if (!tokens.isEmpty()) {
            return tokens.pop();
        }
        while (position < stream.length() && Character.isWhitespace(stream.charAt(position))) {
            ++position;
        }

        if (position >= stream.length()) {
            return new Token(TokenType.EOS, position);
        }

        final int start = position;
        final char ch = stream.charAt(position++);

        switch (ch) {
            case '(': return new Token(TokenType.LPAREN, start);
            case ')': return new Token(TokenType.RPAREN, start);
            case ',': return new Token(TokenType.COMMA, start);
            default:  --position; break;
        }

        if (Character.isDigit(ch)) {
            return nextNumber();
        }
        if (Character.isAlphabetic(ch)) {
            return nextName();
        }
        return nextOperator();
    }

    private Token nextNumber() {
        final int start = position;
        while (position < stream.length() && Character.isDigit(stream.charAt(position))) {
            ++position;
        }
        return new Token(TokenType.INTEGER, start,
                     Integer.parseInt(stream.substring(start, position)));
    }

    private Token nextName() {
        final int start = position;
        while (position < stream.length() && Character.isAlphabetic(stream.charAt(position))) {
            ++position;
        }
        return new Token(TokenType.NAME, start,
                     stream.substring(start, position));
    }

    private Token nextOperator() {
        final int start = position;
        while (position < stream.length()) {
            final char ch = stream.charAt(position);
            if (
                Character.isWhitespace(ch) ||
                Character.isDigit(ch) ||
                Character.isAlphabetic(ch) ||
                ch == '(' || ch == ')' || ch == ','
                ) {
                break;
            }
            ++position;
        }
        return new Token(TokenType.OPERATOR, start,
                     stream.substring(start, position));
    }

    private void error(Token token) {
        throw new RuntimeException(
            "Syntax error: unexpected token at column " +
            (token.columnNumber+1) + " -- " + token.type.name() +
            (token.payload == null ? "" : " (" + token.payload.toString() + ")")
        );
    }
}