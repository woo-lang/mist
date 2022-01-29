import sys
import os

from typing import Dict, Tuple

from globals import global_symbol_table
from lang.lexer.lexer import Lexer
from lang.parser.parser import Parser
from lang.interpreter.interpreter import Interpreter, Context


def parse_args(args) -> Tuple[str, Dict[str, str]]:
    command, params = None, {}
    previous = None
    for index, argument in enumerate(args):
        if index == 0:
            command = argument
            continue
        if argument.startswith("--"):
            if previous:
                params[previous] = "true"
            previous = argument
        else:
            if previous:
                params[previous] = argument
                previous = None
            else:
                print(f"Invalid parameter {argument}")
                sys.exit(1)

    return command, params


def start_interpreter(fn, text, dump_ast=False):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error

    interpreter = Interpreter()
    context = Context("<program>")
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)
    if dump_ast:
        print(ast.node)
    return result.value, result.error


def run(filename, dump_ast):
    with open(filename, "r") as reader:
        content = reader.read().strip()
    if len(content) == 0:
        return
    result, error = start_interpreter("<stdin>", content, dump_ast)
    if error:
        print(error.as_string())
        sys.exit(1)


def main():
    command, params = parse_args(sys.argv[1:])
    if command == "help":
        print(f"Usage: mist <command> <params>")
    else:
        if not os.path.exists(command):
            print(f"{command} not found")
            sys.exit(1)
        run(command, params.get("--dump-ast") == "true")


if __name__ == "__main__":
    main()
