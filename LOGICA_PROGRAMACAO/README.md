# 🐍 Lógica de Programação com Python, Git e Clean Code

Este documento serve como material didático para as aulas de introdução à programação, controle de versão e boas práticas de desenvolvimento de software.

---

## 💻 1. Conteúdo de Aula: Python Básica e Lógica

Python é uma linguagem de alto nível, com sintaxe limpa e focada na legibilidade do código.

### Estruturas Fundamentais
* **Variáveis e Tipos:** Armazenamento de dados em memória (`int`, `float`, `str`, `bool`).
* **Estruturas Condicionais:** Tomada de decisão no fluxo do código usando `if`, `elif` e `else`.
* **Estruturas de Repetição:** Blocos de execução demarcados por laços de repetição `while` e `for`.
* **Funções (`def`):** Modularização de blocos de código reaproveitáveis com parâmetros e retornos.

---

## 🛠️ 2. Controle de Versão: Git

O Git é um sistema de controle de versão distribuído que rastreia o histórico de alterações nos arquivos.

### Ciclo de Vida dos Arquivos
* **Working Directory:** Pasta local onde os arquivos do projeto são modificados diretamente.
* **Staging Area:** Zona de preparação onde as alterações são selecionadas para o próximo registro.
* **Local Repository:** Banco de dados local onde os commits confirmados ficam armazenados de forma segura.

### Comandos Essenciais
* `git init`: Inicializa um novo repositório Git local na pasta atual.
* `git status`: Exibe o estado atual das modificações nos arquivos do projeto.
* `git add .`: Adiciona todas as modificações atuais para a zona de preparação (Staging).
* `git commit -m "mensagem"`: Grava o snapshot das alterações salvas com uma mensagem explicativa.

---

## 🚀 3. Plataforma de Colaboração: GitHub

O GitHub é uma plataforma de hospedagem de código baseada em nuvem que integra fluxos de trabalho com o Git.

### Conceitos Chave
* **Remote Repository:** Cópia do projeto hospedada nos servidores da nuvem do GitHub.
* **Fork:** Criação de uma cópia idêntica de um repositório alheio na sua própria conta.
* **Pull Request (PR):** Solicitação formal para enviar suas alterações de código para o projeto principal.

### Comandos de Integração
* `git clone <url>`: Baixa um repositório remoto existente para a sua máquina local.
* `git remote add origin <url>`: Vincula o seu repositório local a um repositório remoto.
* `git push origin main`: Envia os commits locais para o ramo principal no GitHub.
* `git pull`: Atualiza o repositório local trazendo as alterações recentes do servidor remoto.

---

## ✨ 4. Boas Práticas: Clean Code em Python

Clean Code consiste em escrever códigos fáceis de ler, fáceis de entender e fáceis de manter.

### Regras de Ouro
* **Nomes Significativos:** Variáveis e funções devem revelar explicitamente a sua real intenção.
* **Funções Pequenas:** Cada função deve realizar apenas uma tarefa e fazê-la de forma excelente.
* **Evite Comentários Óbvios:** O código limpo deve ser autoexplicativo através de sua estrutura.
* **Padrão PEP 8:** Guia de estilo oficial para escrita de código idiomático em Python.

### Exemplo Prático: Ruim vs. Limpo

**Código Ruim:**
```python
def calc(a, b):
    # multiplica as duas variáveis
    x = a * b
    return x
```

**Código Limpo (Clean Code):**
```python
def calcular_area_retangulo(largura: float, altura: float) -> float:
    return largura * altura
```

---

## 📁 5. Projetos Práticos Sugeridos

Aplicações práticas para fixação dos conceitos de lógica, Git, GitHub e Clean Code.

### Projeto 1: Calculadora de Terminal com Histórico
* **Conceitos:** Funções, loops `while`, estruturas condicionais e manipulação de listas em Python.
* **Desafio Git:** Criar commits separados para cada operação matemática implementada no sistema.

### Projeto 2: Simulador de Caixa Eletrônico (ATM)
* **Conceitos:** Controle de fluxo rigoroso, validação de entradas de dados e escopo de variáveis.
* **Desafio GitHub:** Publicar o código no GitHub e documentar a execução no arquivo `README.md`.

