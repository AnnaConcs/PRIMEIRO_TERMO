# 🖥️ Sistemas Operacionais, Operação via CLI e Segurança Cibernética

Este documento serve como material didático para as aulas de Fundamentos de Sistemas Operacionais, comandos em linha de comando (CLI) e práticas de segurança.

---

## ⚙️ 1. Sistemas Operacionais: Fundamentos e Indicações

Um Sistema Operacional (S.O.) é o software que gerencia o hardware do computador e provê serviços para os aplicativos de usuário.

### Indicações por Perfil de Uso
* **Windows (Microsoft):** Mercado corporativo, desktops domésticos, jogos e desenvolvimento .NET.
* **Linux (Open Source):** Servidores de nuvem, supercomputadores, contêineres e segurança.
* **macOS (Apple):** Desenvolvimento iOS, design gráfico, edição de vídeo e ecossistema integrado.

---

## 🐧 2. Distribuições Linux

O Linux não é um S.O. único, mas um núcleo (Kernel). As distribuições (Distros) combinam o kernel com softwares e gerenciadores de pacotes.

### Categorias Principais
* **Ubuntu / Debian:** Ideal para iniciantes, servidores estáveis e farta documentação.
* **Fedora / Red Hat (RHEL):** Focado em inovação tecnológica e ambientes corporativos robustos.
* **Arch Linux:** Minimalista, alta customização e modelo de atualização contínua (Rolling Release).
* **Kali Linux:** Especializado em testes de invasão e auditorias de segurança cibernética.

---

## 📟 3. Operação de S.O. via CLI (Interface de Linha de Comando)

A CLI oferece controle direto sobre o S.O., automação por scripts e consumo mínimo de recursos de hardware.

### Comandos Equivalentes (Linux vs. Windows)
* **Listar arquivos:** `ls` (Linux) ↔ `dir` (Windows)
* **Mudar de diretório:** `cd` (Linux) ↔ `cd` (Windows)
* **Criar pasta:** `mkdir` (Linux) ↔ `mkdir` (Windows)
* **Limpar tela:** `clear` (Linux) ↔ `cls` (Windows)

---

## 🪟 4. Operação do Windows via CLI: Variáveis, Pastas e Usuários

Comandos executados através do **Prompt de Comando (CMD)** ou **PowerShell** para administração do sistema.

### Manipulação de Pastas e Arquivos
* `mkdir C:\Aulas\SO`: Cria a pasta do curso no diretório raiz.
* `move arquivo.txt C:\Aulas\SO`: Move o arquivo selecionado para o destino.
* `del /f arquivo.txt`: Força a exclusão permanente de um arquivo específico.

### Gerenciamento de Variáveis de Ambiente
* `set`: Exibe todas as variáveis de ambiente locais da sessão atual.
* `echo %USERNAME%`: Exibe no terminal o nome do usuário logado no momento.
* `setx CAMINHO "C:\Ferramentas"`: Define uma variável de ambiente persistente no sistema.

### Administração de Usuários (Executar como Administrador)
* `net user`: Lista todas as contas de usuários locais criadas na máquina.
* `net user Aluno1 SenhaSegura123 /add`: Cria um novo usuário padrão no S.O.
* `net localgroup Administradores Aluno1 /add`: Eleva o usuário criado ao grupo de administradores.

---

## 🔒 5. Segurança Cibernética no S.O.

Práticas essenciais para garantir a integridade, confidencialidade e disponibilidade dos dados do sistema.

* **Princípio do Menor Privilégio:** Usuários comuns não devem rodar com direitos de administrador.
* **Firewall e Portas:** Bloqueio de conexões de rede não autorizadas de entrada e saída.
* **Atualizações (Patches):** Correção imediata de vulnerabilidades conhecidas no Kernel e softwares.
* **Logs de Auditoria:** Registro de acessos e comandos executados para análise de incidentes.

---

## 📝 6. Atividade Prática Windows (Laboratório CLI)

**Objetivo:** Executar tarefas administrativas utilizando exclusivamente o Prompt de Comando (CMD).

1. Abra o CMD como **Administrador**.
2. Crie a estrutura de pastas digitando: `mkdir C:\LabSegurança\Evidencias`
3. Crie um novo usuário local de testes chamado `AuditorTech`.
4. Adicione o usuário `AuditorTech` ao grupo local de `Usuários do Log de Desempenho`.
5. Valide se o usuário foi criado tirando um print da saída do comando `net user AuditorTech`.

---

## 🧩 7. Atividade Complementar (Pesquisa e Análise)

**Tema:** Análise Comparativa de Vulnerabilidades.

* **Tarefa:** O aluno deve pesquisar no banco de dados [CVE (Common Vulnerabilities and Exposures)](https://mitre.org) uma vulnerabilidade recente do Windows e uma do Linux.
* **Entrega:** Um mini-relatório em formato texto contendo:
  1. O código identificador da falha (Ex: CVE-2026-XXXX).
  2. O impacto gerado no sistema operacional afetado (Negação de serviço, execução remota de código).
  3. O comando ou patch utilizado para mitigar o problema encontrado.
