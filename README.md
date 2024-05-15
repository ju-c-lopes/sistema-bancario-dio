# Sistema Bancario DIO
Desafio DIO para criação de um sistema bancário utilizando Python

---
## Requisitos

### Operações
---
---
1. Depósito

#### Detalhe sobre operação depósito
* [x] Ser possível depositar _**valores positivos**_ na conta bancária
* [x] Depósitos devem ser armazenados em uma **variável** e exibidos na **Operação Extrato** _[3]_
---

2. Saque

#### Detalhe sobre operação saque
* [x] Permitir _3 saques diários_ com **limite máximo** de _R$ 500,00_
* [x] Exibir **mensagem de falta de saldo** se não tiver saldo em conta
* [x] Saques devem ser armazenados em uma **variável** e exibidos na **Operação Extrato** _[3]_
---
3. Extrato

#### Detalhe sobre operação extrato
* [x] Listar **TODOS** _depósitos_ e _saques_
* [x] Exibir **saldo atual** no _fim da listagem_
* [x] Exibir mensagem em branco caso não haja movimentações
---

### Formato dos valores
* [x] R$ #.##
    * Exemplo: R$ 20.50
---

## Extras

* Limpa a tela ao iniciar a aplicação e a cada operação bem sucedida
* Validação de inputs do usuário, não permitindo ele inserir um ```> ENTER``` ou uma string vazia, que apresentará um ValueError, para isso, utilizamos _**try**_ | _**except**_ para conferir se o input será válido.
