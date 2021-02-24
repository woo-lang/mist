from woolang.project.project import Project
import sys as sys

class WoolangArgumentParser(object):
    def __init__(self, command_line_argument):
        self.arguments = command_line_argument[1:]

        self.compiler_version = "1.0.0"



        self.parser_arguments(self.arguments)

    # parse the arguments
    def parser_arguments(self, arguments):
        if len(arguments) == 0:
            self.woolang_compiler()
        else:
            if arguments[0] == "-v" or arguments[0] == "--version":
                print(
                    f"Woolang Compiler {self.compiler_version} on {sys.platform}"
                )

            elif arguments[0] == "-h" or arguments[0] == "--help":
                self.show_help_message()

            elif arguments[0] == "init":
                project = Project()
            else:
                print("None")

    def woolang_compiler(self):
        console_output_texts = [
            f"Woolang Compiler {self.compiler_version} on {sys.platform}",
            "enter following command for show help :\n\twoolang --help"
        ]
        for output_text in console_output_texts:
            print(output_text)

    # show help message
    def show_help_message(self):
        console_output_texts = [
            f"Woolang Compiler {self.compiler_version} on {sys.platform}"
            "Enter following command in terminal to build a woo file :\nwoolang <inputfile.has>"
            "\nother commands :", "\t--help , -h , help : show help",
            "\t--version , -v , version : show compiler version"
        ]
        for output_text in console_output_texts:
            print(output_text)