import { ArgumentParser } from "./arguments/parser"
import * as process from 'process'

const runWoolangSource = (sourceFileName) => {
    console.log(sourceFileName)
}

// the interpreter version
export const WOOLANG_INTERPRETER_VERSION = "1.0.0"

// all available command line arguments
export const WOOLANG_CLI_ARGUMENTS = {
    "run": runWoolangSource
}


const argumentParser = new ArgumentParser(process.argv)

argumentParser.parseCommandArguments()