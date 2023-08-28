from pprint import pprint
from functools import wraps
import click

from aura.error_handler import UnsupportedOutputFormat, handle_error
from aura.format import format_table_output, format_text_output


def api_command(name: str, help_text: str, fixed_cmd_output: str = None):
    """
    Decorator for all API CLI commands.

    Adds CLI options that are shared by all API commands.

    Wraps the API call in a try-catch block, handles errors and formats the output.
    """

    def api_command_decorator(func):
        @click.command(name=name, help=help_text)
        @click.option("--output", help="Set the output format of a command")
        @click.option(
            "--include",
            "-i",
            is_flag=True,
            default=False,
            help="Display Headers of the API response",
        )
        @click.option(
            "--raw",
            is_flag=True,
            default=False,
            help="Display the raw API response body",
        )
        @wraps(func)
        def wrapper(output: str, include: bool, raw: bool, *args, **kwargs):
            try:
                api_response = func(*args, **kwargs)
                if not raw:
                    api_response.raise_for_status()

                response_data = api_response.json()
                data = None
                if "data" in response_data:
                    data = response_data["data"]
            # pylint: disable=broad-exception-caught
            except Exception as exception:
                handle_error(exception)
            else:
                if include:
                    print(api_response.headers, "\n")

                if raw:
                    print(response_data)
                    return click.get_current_context().exit(code=0)

                ctx = click.get_current_context()
                config = ctx.obj
                output_format = (
                    fixed_cmd_output or output or config.get_option("default-output") or "json"
                )

                if data is None:
                    print("Operation successful")
                elif output_format == "json":
                    pprint(data)
                elif output_format == "table":
                    out = format_table_output(data)
                    print(out)
                elif output_format == "text":
                    out = format_text_output(data)
                    print(out)
                else:
                    raise UnsupportedOutputFormat(output_format)

                return click.get_current_context().exit(code=0)

        return wrapper

    return api_command_decorator
