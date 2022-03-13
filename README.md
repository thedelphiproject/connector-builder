# connector-builder
Ergo oracle-core connector builder service.

### Running 

```
python3 main.py '"https://api.coingecko.com/api/v3/simple/price?ids=ergo&vs_currencies=USD"'
```

Will create a new executable called connector-builder. To run that 

```
./connector-builder
```

Puts code into new folder called source-code.


Given these inputs:
- Coingecko ticker URL, eg `https://api.coingecko.com/api/v3/simple/price?ids=ergo&vs_currencies=USD`
- Number of decimals or conversion factor to turn float price into int.

Does the following:
- [X] Generates Rust source for a custom oracle-core connector by adapting the [erg-usd connector](https://github.com/ergoplatform/oracle-core/blob/master/connectors/erg-usd-connector/src/main.rs).
- [X] Compiles the connector, possibly for different targets (x86, arm).
- [X] Makes resulting binaries available for download
- [X] Makes generated source publicly available

Ideally, generated source and binaries would be hosted on github, making use of Actions. Perhaps in a separate repo, using a eparate branch for each connector variant.

To consider:
- Connectors should be uniquely identifyable
- Connectors should not be duplicated (i.e. no two connectors for same Coingecko ticker)
- Adding support for coinmarketcap api or alternative source