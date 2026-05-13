# 🌐 Arquitetura IoT: Dispositivos de Rede, Protocolos e Integração com ESP32

Este documento serve como material didático para as aulas de Arquitetura de Internet das Coisas (IoT), abordando desde a infraestrutura de rede básica até a comunicação com microcontroladores.

---

## 🔍 1. Pesquisa: Dispositivos de Redes em IoT
A infraestrutura de rede para IoT exige dispositivos capazes de lidar com alta densidade de conexões, baixo consumo de energia e diferentes raios de alcance.

* **Gateways IoT:** Dispositivos que traduzem protocolos locais de baixa potência (ex: Zigbee, LoRaWAN) para protocolos de internet (TCP/IP, Wi-Fi).
* **Roteadores e Access Points:** Direcionam o tráfego de dados dos módulos IoT para a rede local ou para a nuvem.
* **Modems Celulares (NB-IoT / LTE-M):** Conectam dispositivos IoT diretamente às redes de telefonia móvel para monitoramento remoto de longo alcance.

---

## ⚡ 2. Ativos e Passivos de Redes

### Ativos de Rede
Dispositivos eletroeletrônicos que manipulam, direcionam ou gerenciam ativamente os dados na rede.
* **Switches:** Direcionam os pacotes de dados especificamente para o dispositivo de destino na rede local (LAN).
* **Roteadores:** Interconectam subredes diferentes e escolhem a melhor rota para os pacotes de dados.
* **Módulos de Comunicação (ESP32, Arduino):** Processam informações e transmitem sinais de rede.

### Passivos de Rede
Componentes físicos que servem apenas como meio de transmissão ou suporte estrutural, sem processar os dados.
* **Cabos de Par Trançado (UTP/STP) e Fibra Óptica:** Meios físicos de transmissão de dados.
* **Patch Panels e Conectores (RJ-45):** Estruturas de organização de cabeamento.
* **Antenas:** Propagam as ondas eletromagnéticas no ar sem alterar o conteúdo da mensagem.

---

## 📡 3. Internet e suas Derivações: O Ecossistema IoT
A evolução da internet permitiu a ramificação da conectividade para cenários específicos:

* **Internet das Coisas (IoT):** Conexão de objetos cotidianos (eletrodomésticos, sensores domésticos) à internet para automação e coleta de dados.
* **Internet Industrial das Coisas (IIoT):** Aplicação de sensores e redes em ambientes industriais para manutenção preditiva, controle de robótica e eficiência de linhas de produção.
* **Internet de Todas as Coisas (IoE - Internet of Everything):** Conceito que une dados, processos, pessoas e coisas em uma rede inteligente integrada.

---

## 💻 4. Driver ESP32: Configuração do Ambiente
Para que o computador consiga se comunicar com a placa de desenvolvimento ESP32 via cabo USB, é necessário instalar o driver de conversão USB-Serial correto.

### Principais Chips Conversores
* **CP210x (Silicon Labs):** Muito comum em placas NodeMCU ESP32 tradicionais.
* **CH340 / CH341:** Utilizado em placas clones ou versões de baixo custo.

### Passos para Instalação e Verificação
1. Baixe o driver oficial correspondente ao chip integrado na sua placa (CP210x ou CH340).
2. Instale o arquivo executável com privilégios de administrador.
3. Conecte o ESP32 ao computador via cabo USB (certifique-se de que o cabo transmite dados e não apenas energia).
4. No Windows, abra o **Gerenciador de Dispositivos** e verifique em qual **Porta (COM e LPT)** o dispositivo foi mapeado.

---

## 📝 5. Protocolo MQTT e IoT
O **MQTT (Message Queuing Telemetry Transport)** é um protocolo de mensagens leve, baseado no modelo de publicação/assinatura, ideal para conexões de baixa largura de banda e dispositivos com recursos limitados.

### Arquitetura MQTT
* **Broker:** O servidor central que recebe todas as mensagens, filtra e distribui para os destinatários (Ex: Mosquitto, HiveMQ).
* **Publisher (Publicador):** O dispositivo (ex: ESP32 com sensor de temperatura) que envia dados para um tópico específico.
* **Subscriber (Assinante):** O dispositivo ou sistema (ex: Dashboard de monitoramento) que se inscreve em um tópico para receber dados.
* **Tópicos:** Estrutura de caminhos (Ex: `casa/quarto/temperatura`) usada para categorizar as mensagens.

---

## 📋 6. Modelo de Relatório Técnico (Atividade Prática)

Os alunos deverão entregar um relatório técnico estruturado após a realização dos laboratórios práticos.

### Estrutura Exigida
1. **Capa:** Título do experimento, nome dos alunos, data e instituição.
2. **Introdução Teórica:** Breve contextualização sobre os componentes e protocolos utilizados (ex: ESP32 e MQTT).
3. **Materiais e Métodos:** Lista de hardwares (ESP32, sensores) e softwares (Arduino IDE, Broker MQTT) utilizados.
4. **Desenvolvimento (Resultados):** Esquema de montagem do circuito, código-fonte documentado e capturas de tela das mensagens trafegando no Broker.
5. **Conclusão:** Análise crítica sobre as dificuldades encontradas e o funcionamento prático da arquitetura montada.
6. **Referências Bibliográficas:** Links e manuais técnicos utilizados como base.
