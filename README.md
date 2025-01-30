
# Formal Verification: Securing ERC-4626 Vaults with Certora Prover 

This repository provides an example of how to use Certora Prover for formal verification of smart contracts. Follow the steps below to install Certora, obtain an API key, and execute `certoraRun` on the configuration file.

## Prerequisites

Ensure you have the following installed:
- Python 3 and `pip3`
- A Solidity compiler compatible with your contract version

---

## Installation

### Step 1: Install Certora CLI

You need to install the Certora CLI to interact with the Certora Prover. Run the following command:

```sh
pip3 install certora-cli
```

Verify the installation:

```sh
certoraRun --help
```

---

## Obtaining an API Key from Certora

To use Certora Prover, you must have an API key. Sign up or log in to [Certora's website](https://certora.com/). Finally, set up your API key in your environment variables:

```sh
export CERTORAKEY=<your_api_key>
```


---

## Running Certora Prover

To verify the smart contract, execute `certoraRun` with the provided configuration file:

```sh
certoraRun certora/VaultERC.conf
```

If you are using a Solidity contract, ensure your configuration file correctly specifies the contract paths and verification rules.



