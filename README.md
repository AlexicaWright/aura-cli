## Aura Command Line Interface

The Neo4j Aura CLI is an open source command line interface for interacting with the Aura cloud platform through the public Aura API.

You can sign up for Aura here: https://console.neo4j.io

To find out more about about the Aura API visit the documentation: https://neo4j.com/docs/aura/platform/api/overview/

## Installation

To install the CLI you need to have Python and `pip` installed. Then you can run:

`pip install aura-cli`

to download and install the CLI. As with other Python libraries, you should consider installing it in a virtual environemnt.

## Usage

After installation, the `aura` command will be available in your terminal. You can verify that the installation was successful by running `aura --version` or `aura --help`.

### Credentials

Aura API credentials need to be created in the console (see the [Aura API documentation](https://console.neo4j.io/?_gl=1*ab5vqi*_ga*ODA4NTgzMDE4LjE2NzkzOTY4NDk.*_ga_DL38Q8KGQC*MTY5NDM0NDI0NC44MS4xLjE2OTQzNDUzMjEuNTAuMC4w&_ga=2.169558053.548335101.1694344245-808583018.1679396849#account)). These can then be added to the CLI through the `aura credentials add` command. The credentials will then be saved locally in a config file. You can add multiple credentials and switch between them.

To add your first credentials run
`aura credentials add --name <NAME> --client-id <YOUR_CLIENT_ID> --client-secret <YOUR_CLIENT_SECRET> --use`

Here is a list of all credentials commands:

- `aura credentials add`
- `aura credentials list`
- `aura credentials current`
- `aura credentials use`
- `aura credentials delete`

Configured credentials will be overriden if environment variables for the Client ID or Client Secret are set.

### Environment Variables

There are 4 environment variables that can be set for use in the CLI:

- `AURA_CLI_AUTH_URL` - The url used for getting an auth token (default to https://api.neo4j.io/oauth/token)
- `AURA_CLI_BASE_URL` - The base url used for all API calls (defaults to https://api.neo4j.io/v1)
- `AURA_CLI_CLIENT_ID` - The client id used for authentication
- `AURA_CLI_CLIENT_SECRET` - The client secret used for authentication

Setting environment variables will override any configurations that were set with the `aura config set` command.

### Config

The `aura config` commands allows to set configurations and default values. Currently there are 4 options which can be set with the `aura config set` command:

- `default-tenant` - the default tenant which to use for commands like `aura instances create` (where a tenant-id is required)
- `output` - the default output format for API commands (json, text or table)
- `auth-url` - The url used for getting an auth token (default to https://api.neo4j.io/oauth/token)
- `base-url` - The base url used for all API calls (defaults to https://api.neo4j.io/v1)

List of all config commands:

- `aura config get`
- `aura config list`
- `aura config set`
- `aura config unset`

### API Commands

API commands are divided into 3 resources: `instances`, `tenants` and `snapshots`. Use the `--help` flag to get more information about each subcommand, e.g. `aura instances --help`.

Example commands:

`aura instances get --name DevInstance`

`aura instances create --name DevInstance --region europe-west1 --type professional-db --tenant-id my-tenant-123`

`aura snapshots list --instance-id=b25d4b9f`

### Output format

By default the output format is json. Using the `output` option the format can be changed to `table`, `text` or `yaml`, e.g.

`aura instances list --output table`

### Useful flags

All API commands have the following 3 flags:

- `--include, -i` : Print the API response headers
- `--raw` : Print the raw API response body
- `--verbose` : Print verbose output

### Logs

By default the CLI will collect logs in a `~/.aura/auracli.log` file.

## Development

To installing the CLI for developement, do the following:

In the root directory run `. venv/bin/activate` to active the virtual environment.

Next, run `pip install --editable .` to install the dependencies. Then you can run the cli `aura --help`.

When finished, run `deactivate` to deactivate the venv.

To run the unit tests, run `pytest tests/`.

For development you will need the following Python libraries installed:

- `pytest`
- `black`
- `pylint`
- `pre-commit`
- `pytest-cov`
