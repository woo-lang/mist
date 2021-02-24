import { WOOLANG_INTERPRETER_VERSION } from "../index"
import { WOOLANG_CLI_ARGUMENTS } from "../index"
import { red } from "chalk"

// the command line argument parser

export class ArgumentParser {
    private readonly arguments: Array<string>

    constructor(readonly parameters: Array<string>) {
        // slice the command line arguments
        // and remove ["node", "filename"] from
        // the array
        this.arguments = parameters.slice(
            2, parameters.length
        )

    }

    /**
     * Take all the keys from the WOOLANG_CLI_ARGUMENTS
     * if no arguments are passed in along with node,
     * simply print out the version of woolang interpreter
     * 
     * if it contains arguments, make sure it contains
     * two arguments, and check for it in the 
     * WOOLANG_CLI_ARGUMENTS, and execute the
     * corresponding function ot throw out an error
     * 
     * else,throw an insufficient arguments
     * error
     */

    parseCommandArguments = () => {
        // let parseItemIndex = 0;
        const commandKeys = Object.keys(WOOLANG_CLI_ARGUMENTS)

        if (this.arguments.length == 0) {
            console.log(`Woolang ${WOOLANG_INTERPRETER_VERSION}`)
        } else if (this.arguments.length == 2) {
            const command = this.arguments[0]

            if (commandKeys.includes(command)) {
                WOOLANG_CLI_ARGUMENTS[
                    command
                ](this.arguments[1])
            } else {
                console.error(red(`Unknown command : ${command}`))
            }
        } else {
            console.error(red("Insufficient arguments"))
        }
    }

}
