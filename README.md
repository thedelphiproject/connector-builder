# Delphi Project Connector Builder
Ergo oracle-core connector builder service.

Creates and compiles a connector executable for the Oracle to access the required datapoints.

### Running

To run the Github actions workflow, enter:

```
curl \
-u $username:$token \
-H "Accept: application/vnd.github.v3+json" \
https://api.github.com/repos/thedelphiproject/connector-builder/actions/workflows/main.yml/dispatches \
-d '{"ref":"main", "inputs":{"apiurl":"https://api.coingecko.com/api/v3/simple/price?ids=ergo&vs_currencies=USD"}}'
```

Where $username is your Github username and $token is a Github personal access token.

To run the python program on your own machine, enter:

```
python3 main.py '"https://api.coingecko.com/api/v3/simple/price?ids=ergo&vs_currencies=USD"'
```

### Output

The program will create a new executable called *connector-builder*. This is a program that the Oracle needs in order ot retrived the information to post on chain.

The program also creates a new directory called *templates*. In this directory, there will be two new files: *main.rs* and *Cargo.toml*. This is the source code that the program used to compile a the executable.

### Executable Connector
- [X] Coingecko ticker URL, eg `https://api.coingecko.com/api/v3/simple/price?ids=ergo&vs_currencies=USD`
- [ ] Number of decimals or conversion factor to turn float price into int.

### Connector Builder
- [X] Generates Rust source for a custom oracle-core connector by adapting the [erg-usd connector](https://github.com/ergoplatform/oracle-core/blob/master/connectors/erg-usd-connector/src/main.rs).
- [X] Compiles the connector, possibly for different targets (x86, arm).
- [X] Makes resulting binaries available for download
- [X] Makes generated source publicly available

Ideally, generated source and binaries would be hosted on github, making use of Actions. Perhaps in a separate repo, using a eparate branch for each connector variant.

To consider:
- Connectors should be uniquely identifyable
- Connectors should not be duplicated (i.e. no two connectors for same Coingecko ticker)
- Adding support for coinmarketcap api or alternative source