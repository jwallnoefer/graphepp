# GraphEPP

[![PyPI](http://img.shields.io/pypi/v/graphepp.svg)](https://pypi.python.org/pypi/graphepp)
[![Docs](https://readthedocs.org/projects/graphepp/badge/?version=latest)](https://graphepp.readthedocs.io)
[![Tests, Artifacts and Release](https://github.com/jwallnoefer/graphepp/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/jwallnoefer/graphepp/actions/workflows/ci.yaml)

**GraphEPP is a collection of functions for multipartite entanglement
purification protocols (EPP) on noisy graph states.**

![GHZ](https://user-images.githubusercontent.com/11145016/114246620-59c11380-9993-11eb-9b38-abd067d2363f.png)

## Installation

You can install GraphEPP into your python environment from the
[Python Package Index](https://pypi.org/project/graphepp/):

```
pip install graphepp
```

If you encounter any problems, you can try installing it the exact versions of
GraphEPP's dependencies that were used to develop it
(specified in `Pipfile.lock`). This assumes Python 3.8 and
[`pipenv`](https://github.com/pypa/pipenv) are installed on your system:

```
git clone https://github.com/jwallnoefer/graphepp.git
cd graphepp
git checkout main
pipenv sync
pipenv install graphepp
```
and then use `pipenv shell` to activate the virtual environment

## Scope

This project provides functions for operations on quantum states that are
diagonal in the graph state basis corresponding to a chosen graph state.
(for an introduction to graph states see e.g. [arXiv:quant-ph/0602096](https://arxiv.org/abs/quant-ph/0602096))
These include:

* Local Pauli-diagonal noise channels that are applied on qubits of the graph state.
* Distance measures for states given in the same graph state basis.
* The ADB protocol for two-colorable graph states introduced in [Phys. Rev. Lett. **91**, 107903 (2003)](https://doi.org/10.1103/PhysRevLett.91.107903) and [Phys. Rev. A **71**, 012319 (2005)](https://doi.org/10.1103/PhysRevA.71.012319).
* The protocol for all graph states introduced in [Phys. Rev. A **74**, 052316 (2006)](https://doi.org/10.1103/PhysRevA.74.052316).

as well as auxiliary functions like local complementation of graphs.

Example use case: Perform multiple rounds of EPP on a noisy linear cluster state
of 5 qubits when the CNOT operations used in the EPP are themselves imperfect
(e.g. modeled by local depolarizing noise).


## Publications
An earlier (unreleased) version of GraphEPP was used for these publications:

> Two-dimensional quantum repeaters <br>
> J. Wallnöfer, M. Zwerger, C. Muschik, N. Sangouard, and W. Dür <br>
> [Phys. Rev. A **94**, 052307 (2016)](https://doi.org/10.1103/PhysRevA.94.052307) <br>
> Preprint: [arXiv:1604.05352 \[quant-ph\]](https://arxiv.org/abs/1604.05352)

> Measurement-based quantum communication with resource states generated by entanglement purification <br>
> J. Wallnöfer and W. Dür <br>
> [Phys. Rev. A **95**, 012303 (2017)](https://doi.org/10.1103/PhysRevA.95.012303) <br>
> Preprint: [arXiv:1609.05754 \[quant-ph\]](https://arxiv.org/abs/1609.05754)
