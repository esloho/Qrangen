# Qrangen [Quantum Random Generator]

This project aims to build an easy-to-use application for generation of random numbers using measurements over Quantum circuits. This measurements are requested to Q-IBM servers. 


## Setting up

In order to do your own simulations with IBM servers, you need to obtain a personal token (See Qiskit Documentation for more info). Once you have this key, it needs to be stored in a file named `key.json` with the following structure:

```
{
	"api_token":<your_api_token>
}
```

A sample of this structure can be found in `example_key.json`.

## Usage

In order to run the generator, one should clone this repo, install the requirement packages in a Python environment, set a personal token and run `app.py`:

```
python app.py --mode 2 --number_amount 70 -bits 4
```

where `mode` flag is set to 2 in order to run in IBM servers and not in local (0), `number_amount` is the amount of numbers one wants to get and `bits` refers to the number of qubits used in the simulation (output numbers range from 0 to 2^{bits-1}).

There is also a benchmark feature, where some randomness comparaison is performed. By running 
```
python benchmark_app.py --mode 2 --number_amount 70 -bits 4
```

numpy pseudo-random number are generated as well. Different statistical moments of the distributions are compared.


## License

[Apache License 2.0](LICENSE)
