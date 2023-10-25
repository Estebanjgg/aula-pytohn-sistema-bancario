### **README - Sistema Bancário "Banco Esteban"**

Este projeto é uma implementação simples de um sistema bancário em Python. O usuário pode criar uma conta, depositar dinheiro, sacar dinheiro, ver um extrato de transações, transferir dinheiro e consultar o saldo.

---

#### **Funções Principais:**

1. **Depositar:** O usuário pode depositar uma quantia específica na sua conta.
2. **Sacar:** O usuário pode sacar uma quantia específica, desde que tenha saldo suficiente.
3. **Ver Extrato:** O usuário pode ver todas as transações realizadas e o saldo final.
4. **Transferir Dinheiro:** É possível transferir dinheiro entre contas registradas no sistema.
5. **Ver Saldo:** O usuário pode consultar o saldo atual da sua conta.
6. **Sair:** Sair do sistema.

---

#### **Estrutura do Código:**

- **Classe `BankAccount`**: Esta classe representa uma conta bancária e contém métodos para depositar, sacar, obter um extrato, transferir dinheiro e verificar o saldo.
  
- **Função `input_float(prompt)`**: Função que solicita ao usuário que insira um número flutuante e trata erros se o usuário não inserir um número válido.

- **Função `clear_console()`**: Função para limpar o console. Adaptar-se-á dependendo do sistema operacional em uso.

- **Função `main_menu()`**: Função que exibe o menu principal ao usuário e gerencia a lógica principal do sistema.

---

#### **Como executar o sistema:**

Para executar o sistema bancário "Banco Esteban", siga estes passos:

1. Certifique-se de ter Python instalado no seu computador.
2. Abra o terminal ou linha de comando na localização do arquivo `app.py` (ou qualquer nome que tenha dado ao arquivo).
3. Execute o comando `python app.py`.
4. Siga as instruções na tela para interagir com o sistema.

---

#### **Notas adicionais:**

- A implementação atual salva as contas em uma lista chamada `accounts_list`. No entanto, esta lista e seus dados são perdidos assim que o programa é encerrado. Se desejar uma solução persistente, considere implementar um banco de dados ou guardar os dados em um arquivo.
  
- Ao retornar ao menu principal, o programa limpará o console para melhorar a experiência do usuário.

---
