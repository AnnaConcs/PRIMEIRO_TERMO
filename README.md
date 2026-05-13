# 📑 Plano Integrado de Aulas: Engenharia, Sistemas e IoT

Este documento reúne o material didático oficial para as disciplinas de Engenharia de Requisitos, Lógica de Programação, Sistemas Operacionais e Arquitetura IoT.

---

## 📐 BLOCO 1: Levantamento de Requisitos

A Engenharia de Requisitos compreende o processo de descobrir, analisar, documentar e verificar os serviços e as restrições de um sistema de software.

### 📌 1. Fundamentos e Conteúdo de Aula
* **Elicitação:** Processo de descoberta de requisitos junto aos clientes e partes interessadas.
* **Análise:** Detecção de conflitos, análise de viabilidade técnica e negociação de escopo.
* **Especificação:** Documentação formal e estruturada das necessidades mapeadas do negócio.
* **Validação:** Homologação e confirmação dos requisitos junto aos envolvidos no projeto.

### 🛠️ 2. Requisitos Funcionais (RF) vs. Não Funcionais (RNF)
* **Requisitos Funcionais (RF):** Definem **o que** o sistema deve fazer (funcionalidades diretas).
  * *Exemplo:* O sistema deve permitir o cadastro de novos usuários.
* **Requisitos Não Funcionais (RNF):** Definem **como** o sistema deve operar (restrições e qualidades).
  * *Exemplo:* As páginas do sistema devem carregar em menos de 2 segundos.

### 📊 3. Diagramas na Engenharia de Requisitos
* **Diagrama de Casos de Uso (UML):** Representa os atores (usuários/sistemas externos), os casos de uso (funcionalidades) e seus relacionamentos (`<<include>>` e `<<extend>>`).
* **Diagrama de Fluxo de Dados (DFD):** Modela graficamente o fluxo de informações através de processos, entidades externas e depósitos de dados.

### 📝 4. Relatórios Técnicos (Artefatos)
* **Especificação de Requisitos de Software (SRS):** Documento contratual que detalha o escopo, a descrição geral do produto e a lista completa de RFs e RNFs.
* **Matriz de Rastreabilidade:** Tabela estruturada que conecta cada requisito à sua origem, código ou caso de teste correspondente.

### 💡 5. Técnicas de Elicitação
* **Brainstorming:** Sessão de ideação rápida dividida em *Fase de Divergência* (foco em quantidade, sem julgamentos) e *Fase de Convergência* (filtragem e priorização).
* **Prototipagem:** Construção de interfaces divididas em *Baixa Fidelidade* (desenhos em papel/wireframes), *Média Fidelidade* (telas digitais estáticas) e *Alta Fidelidade* (modelos interativos funcionais).
* **Entrevistas:** Coletas diretas divididas em *Estruturadas* (roteiro fechado), *Não Estruturadas* (conversa livre) e *Semifruturadas* (guia flexível).

---

## 🐍 BLOCO 2: Lógica de Programação em Python e Ferramentas

Introdução ao desenvolvimento de software, algoritmos, controle de versão e boas práticas de código.

### 💻 1. Python Básico e Lógica
* **Variáveis e Tipos de Dados:** Armazenamento em memória (`int`, `float`, `str`, `bool`).
* **Estruturas Condicionais:** Desvios no fluxo de execução do código (`if`, `elif`, `else`).
* **Estruturas de Repetição:** Laços e iterações de blocos de instrução (`while` e `for`).
* **Funções (`def`):** Blocos de código modulares, reaproveitáveis, com parâmetros e retornos.

### 🛠️ 2. Controle de Versão com Git
O Git opera através do controle do ciclo de vida dos arquivos em três zonas principais:
1. **Working Directory:** Pasta de trabalho local onde os arquivos são modificados.
2. **Staging Area:** Zona de preparação onde as alterações são selecionadas.
3. **Local Repository:** Banco de dados local onde os commits são armazenados de forma segura.
* **Comandos Fundamentais:** `git init`, `git status`, `git add .` e `git commit -m "mensagem"`.

### 🚀 3. Colaboração com GitHub
Plataforma em nuvem para hospedagem de repositórios remotos (*Remote Repositories*).
* **Conceitos:** *Fork* (cópia de repositório externo) e *Pull Request - PR* (solicitação de envio de código).
* **Comandos de Integração:** `git clone <url>`, `git remote add origin <url>`, `git push` e `git pull`.

### ✨ 4. Clean Code em Python
Práticas para escrita de códigos legíveis, limpos e de fácil manutenção utilizando a **PEP 8**.
* **Nomes Significativos:** Variáveis e funções devem revelar explicitamente sua real intenção.
* **Funções Pequenas:** Cada bloco funcional deve realizar apenas uma tarefa específica.
* **Código Autoexplicativo:** Priorize estruturas limpas e evite comentários óbvios no código.

### 📁 5. Projetos Práticos Sugeridos
* **Projeto 1:** Calculadora de Terminal com Histórico (foco em loops, condicionais e listas).
* **Projeto 2:** Simulador de Caixa Eletrônico - ATM (foco em validação de dados e publicação no GitHub).

---

## 🖥️ BLOCO 3: Sistemas Operacionais e CLI

Estudo da gerência de hardware por softwares básicos, administração de sistemas via terminal e segurança.

### ⚙️ 1. Fundamentos e Indicação de Sistemas Operacionais
* **Windows:** Domínio no mercado corporativo, desktops, jogos e ecossistema de desenvolvimento .NET.
* **Linux:** Padrão para servidores de nuvem, supercomputadores, infraestrutura de contêineres e segurança.
* **macOS:** Focado em desenvolvimento para o ecossistema Apple, design e edição audiovisual.

### 🐧 2. Distribuições Linux (Distros)
Compilações que unem o Kernel Linux a gerenciadores de pacotes e softwares:
* **Ubuntu / Debian:** Interfaces amigáveis, estabilidade para servidores e ampla documentação.
* **Fedora / Red Hat (RHEL):** Ambientes corporativos robustos focados em inovação de recursos.
* **Arch Linux:** Minimalista, focado em alta customização e atualizações contínuas (*Rolling Release*).
* **Kali Linux:** Suite especializada em testes de invasão e auditorias de segurança cibernética.

### 📟 3. Operação de S.O. via CLI (Interface de Linha de Comando)
A CLI oferece controle direto sobre o S.O. com consumo mínimo de recursos de hardware.
* *Listar Arquivos:* `ls` (Linux) ↔ `dir` (Windows)
* *Mudar de Diretório:* `cd` (Linux) ↔ `cd` (Windows)
* *Criar Pasta:* `mkdir` (Linux) ↔ `mkdir` (Windows)
* *Limpar Tela:* `clear` (Linux) ↔ `cls` (Windows)

### 🪟 4. Operação do Windows via CLI (CMD / PowerShell)
* **Manipulação de Pastas:** `mkdir C:\Aulas\SO`, `move arquivo.txt C:\Aulas\SO` e `del /f arquivo.txt`.
* **Variáveis de Ambiente:** `set` (exibe variáveis), `echo %USERNAME%` e `setx` (variável persistente).
* **Gerenciamento de Usuários:** `net user`, `net user Aluno1 Senha123 /add` e `net localgroup Administradores Aluno1 /add`.

### 🔒 5. Segurança Cibernética no S.O.
* **Princípio do Menor Privilégio:** Limitação de acessos; contas comuns não devem rodar como administrador.
* **Firewall e Portas:** Monitoramento e bloqueio de conexões não autorizadas de entrada e saída.
* **Correção de Vulnerabilidades:** Aplicação imediata de pacotes (*patches*) e logs de auditoria ativos.

### 📝 6. Atividades Práticas e Complementares
* **Atividade Windows (Laboratório CLI):** Criação de estruturas de pastas, criação de novo usuário e inserção deste em grupos de sistema via CMD como administrador.
* **Atividade Complementar (Pesquisa):** Análise comparativa e mitigação de falhas reais usando o banco de dados de vulnerabilidades [CVE (Common Vulnerabilities and Exposures)](https://mitre.org).

---

## 🌐 BLOCO 4: Arquitetura IoT (Internet das Coisas)

Estudo da integração de hardware embarcado com redes de comunicação locais e globais.

### 🔍 1. Dispositivos de Redes em IoT
* **Gateways IoT:** Tradutores de protocolos locais de baixa potência para redes TCP/IP baseadas na Internet.
* **Modems Celulares (NB-IoT / LTE-M):** Conectividade direta de longo alcance e baixo consumo via redes móveis.

### ⚡ 2. Ativos e Passivos de Redes
* **Ativos (Processam Dados):** Switches (LAN), Roteadores (Subredes) e Módulos de Comunicação (ESP32).
* **Passivos (Meios Físicos):** Cabos de par trançado (UTP), fibra óptica, conectores RJ-45 e antenas.

### 📡 3. Internet e suas Derivações
* **IoT (Internet das Coisas):** Conexão de objetos residenciais e cotidianos para automação e coleta de dados.
* **IIoT (Internet Industrial das Coisas):** Foco em plantas industriais, telemetria pesada e manutenção preditiva.
* **IoE (Internet of Everything):** Integração total e inteligente entre processos, dados, pessoas e coisas.

### 💻 4. Configuração do Driver ESP32
O microcontrolador necessita de drivers USB-Serial para comunicação com a máquina de desenvolvimento.
* **Chips comuns:** CP210x (Silicon Labs) ou CH340 / CH341 (clones comuns).
* **Validação:** Instalação com privilégios de administrador e verificação da porta mapeada no *Gerenciador de Dispositivos* do Windows (Portas COM e LPT).

### 📋 5. Protocolo MQTT e IoT
Protocolo leve baseado no modelo de publicação/assinatura, ideal para ambientes de baixa largura de banda.
* **Broker:** Servidor centralizador e distribuidor de pacotes de dados (Ex: Mosquitto, HiveMQ).
* **Publisher / Subscriber:** Clientes que publicam dados ou assinam tópicos estruturados (Ex: `casa/quarto/temperatura`).

### 📝 6. Modelo de Relatório Técnico (Estrutura Exigida)
1. **Capa:** Identificação dos autores, data e instituição.
2. **Introdução Teórica:** Contextualização dos hardwares e protocolos utilizados.
3. **Materiais e Métodos:** Listagem de componentes físicos e softwares utilizados.
4. **Desenvolvimento:** Esquemas eletrônicos de ligação, códigos-fonte e telas de logs do Broker MQTT.
5. **Conclusão e Referências:** Análise dos resultados obtidos e fontes bibliográficas técnicas consultadas.
