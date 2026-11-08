# AccountMonitor

**Sistema de monitoramento de vencimento de contas e acessos, desenvolvido em Python.**

[🇧🇷 Português](README.md) | [🇺🇸 English](README.en.md)

## Sobre o projeto

O **AccountMonitor** é uma automação desenvolvida em Python para monitorar datas de expiração de contas e acessos registrados em uma planilha Excel.

O sistema realiza a leitura dos registros, verifica as datas de vencimento e identifica automaticamente as contas que estão próximas de expirar ou que já expiraram.

Quando existem registros que atendem aos critérios de alerta, o sistema envia um único relatório por e-mail, reunindo todas as ocorrências identificadas.

## Funcionalidades

- Leitura automática de registros em planilhas Excel
- Identificação de contas próximas do vencimento
- Identificação de contas já expiradas
- Alertas com antecedência de até 7 dias
- Geração de relatório consolidado por e-mail
- Integração com Gmail via SMTP
- Armazenamento de credenciais e configurações em variáveis de ambiente

## Regras de monitoramento

O sistema considera três situações:

| Situação | Comportamento |
|---|---|
| Próximo do vencimento | Alerta para contas que expiram nos próximos 7 dias |
| Vence hoje | Identificação de contas com vencimento na data atual |
| Expirado | Identificação de todas as contas com data de expiração anterior à atual |

O relatório apresenta o **login da conta**, a data de expiração e a quantidade de dias restantes ou decorridos desde o vencimento.

Por segurança, as senhas dos registros não são incluídas no e-mail.

## Tecnologias utilizadas

- **Python** — desenvolvimento da automação
- **OpenPyXL** — leitura de planilhas Excel
- **Python-dotenv** — gerenciamento de variáveis de ambiente
- **SMTP / Gmail** — envio dos relatórios por e-mail

## Estrutura do projeto

```text
AccountMonitor/
│
├── main.py
├── config.py
├── planilha.py
├── email_service.py
│
├── modelos/
│   └── molde.xlsx
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Configuração e execução

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
cd AccountMonitor
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, utilizando o `.env.example` como referência.

Configure as seguintes variáveis:

```dotenv
# Servidor E-mail
SERVER=
PORT=

# E-mails Remetente
EMAIL_SENDER=
APP_PASSWORD=

# E-mail destinatário
EMAIL_RECIPIENT=

# Planilha
SHEET_FILE=
```

**Importante:** para utilizar o Gmail, é necessário configurar uma senha de aplicativo na conta Google. Não utilize sua senha convencional.

### 5. Configure a planilha

A planilha deve conter as seguintes colunas, nesta ordem:

| Coluna | Descrição |
|---|---|
| login | Identificação da conta |
| senha | Senha da conta |
| usuário | Informação do usuário |
| data criação | Data de criação da conta |
| data expiração | Data de expiração da conta |

As datas devem estar em um formato reconhecido pelo sistema.

### 6. Execute a aplicação

```bash
python main.py
```

## Segurança

- Credenciais de e-mail armazenadas em arquivo `.env`
- Arquivo `.env` excluído do controle de versão
- Senhas dos registros não são incluídas nos relatórios enviados por e-mail
- Recomenda-se utilizar apenas dados fictícios em ambientes de teste

## Objetivo

O AccountMonitor foi desenvolvido para automatizar o acompanhamento de vencimentos, reduzir verificações manuais e facilitar o controle de contas e acessos por meio de notificações centralizadas.

---

Desenvolvido em Python.