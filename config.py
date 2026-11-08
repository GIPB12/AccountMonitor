
import os
from pathlib import Path
from dotenv import load_dotenv

# Diretório onde está localizado o projeto
PASTA_PROJETO = Path(__file__).resolve().parent

# Carrega as variáveis do arquivo .env
load_dotenv(PASTA_PROJETO / ".env")

# Configurações SMTP do Gmail
SMTP_SERVIDOR = os.getenv("SERVER")
SMTP_PORTA = os.getenv("PORT")

EMAIL_REMETENTE = os.getenv("EMAIL_SENDER")
EMAIL_SENHA_APP = os.getenv("APP_PASSWORD")
EMAIL_DESTINATARIO = os.getenv("EMAIL_RECIPIENT")

ARQUIVO_PLANILHA = os.getenv(
    "SHEET_FILE")


# Antecedência dos alertas
DIAS_ANTECEDENCIA = 7


def validar_configuracoes():
    """Verifica se todas as configurações obrigatórias foram preenchidas."""

    obrigatorias = {
        "EMAIL_REMETENTE": EMAIL_REMETENTE,
        "EMAIL_SENHA_APP": EMAIL_SENHA_APP,
        "EMAIL_DESTINATARIO": EMAIL_DESTINATARIO,
    }

    faltantes = [
        nome for nome, valor in obrigatorias.items()
        if not valor
    ]

    if faltantes:
        raise ValueError(
            "Configurações ausentes no arquivo .env: "
            + ", ".join(faltantes)
        )
