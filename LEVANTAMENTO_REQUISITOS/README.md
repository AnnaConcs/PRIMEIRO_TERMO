# 📚 Levantamento de Requisitos: Guia de Conteúdo Técnico

Este documento serve como material didático básico para as aulas de Engenharia de Requisitos. Ele detalha as principais técnicas, conceitos e artefatos utilizados na fase de elicitação e especificação de sistemas.

---

## 📌 1. Conteúdo de Aula: Fundamentos de Requisitos
A Engenharia de Requisitos é o processo de descobrir, analisar, documentar e verificar os serviços e as restrições de um sistema de software.

* **Elicitação:** Descoberta de requisitos junto aos clientes.
* **Análise:** Detecção de conflitos e viabilidade técnica.
* **Especificação:** Documentação formal das necessidades mapeadas.
* **Validação:** Confirmação dos requisitos com os envolvidos.

---

## 🛠️ 2. Requisitos Funcionais e Não Funcionais

### Requisitos Funcionais (RF)
Definem **o que** o sistema deve fazer. Representam as funcionalidades diretas e interações do usuário.
* **RF01:** O sistema deve permitir o cadastro de novos clientes.
* **RF02:** O sistema deve enviar um e-mail de confirmação após a compra.
* **RF03:** O usuário deve conseguir redefinir sua senha via SMS.

### Requisitos Não Funcionais (RNF)
Definem **como** o sistema deve fazer. Representam restrições, qualidades, atributos de desempenho ou segurança.
* **RNF01:** O sistema deve criptografar todas as senhas usando AES-256.
* **RNF02:** As páginas de busca devem carregar em menos de 2 segundos.
* **RNF03:** A interface deve ser responsiva para dispositivos móveis.

---

## 📊 3. Diagramas na Engenharia de Requisitos
Os diagramas traduzem a especificação textual em modelos visuais compreensíveis para desenvolvedores e clientes.

### Diagrama de Casos de Uso (UML)
* **Atores:** Entidades externas que interagem com o sistema (ex: Usuário, Administrador).
* **Casos de Uso:** Funcionalidades principais representadas por elipses (ex: Realizar Login).
* **Relacionamentos:** Linhas de associação, `<<include>>` (obrigatório) e `<<extend>>` (opcional).

### Diagrama de Fluxo de Dados (DFD)
* **Processos:** Transformações sofridas pelos dados dentro do sistema.
* **Entidades:** Origem ou destino final das informações coletadas.
* **Depósitos:** Bancos de dados ou arquivos onde as informações ficam salvas.

---

## 📝 4. Relatórios Técnicos
Artefatos formais que servem como contrato de escopo entre a equipe de desenvolvimento e o cliente.

### Documento de Especificação de Requisitos de Software (SRS)
* **Introdução:** Objetivo do sistema, escopo do projeto e definições.
* **Descrição Geral:** Perspectiva do produto, funções e restrições gerais.
* **Requisitos Específicos:** Lista detalhada de todos os RFs e RNFs mapeados.
* **Matriz de Rastreabilidade:** Tabela que conecta cada requisito à sua origem ou código.

---

## 💡 5. Técnica: Brainstorming
Sessão de ideação livre e rápida para coletar propostas e visões iniciais sobre o produto.

* **Fase de Divergência:** Foco na quantidade de ideias, sem julgamentos ou críticas.
* **Fase de Convergência:** Agrupamento, filtragem e priorização das melhores ideias coletadas.
* **Participantes:** Gerente de produto, desenvolvedores, designers e usuários finais.

---

## 🎨 6. Técnica: Prototipagem
Construção de modelos visuais do sistema para validar fluxos de navegação e interface com o usuário.

* **Baixa Fidelidade:** Desenhos em papel (wireframes) focados na estrutura da tela.
* **Média Fidelidade:** Protótipos digitais estáticos sem interações complexas de clique.
* **Alta Fidelidade:** Modelos interativos navegáveis muito próximos do produto final (ex: Figma).

---

## 👥 7. Técnica: Entrevistas
Coleta direta de dados qualitativos e quantitativos através de reuniões agendadas com os stakeholders.

* **Estruturadas:** Roteiro fechado com perguntas específicas e predefinidas.
* **Não Estruturadas:** Conversa livre baseada em tópicos gerais sobre o negócio.
* **Semiestruturadas:** Guia flexível que permite a exploração de novas respostas durante a conversa.
