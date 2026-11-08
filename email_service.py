
import smtplib
import html

from datetime import date
from email.message import EmailMessage

from config import (
    EMAIL_REMETENTE,
    EMAIL_SENHA_APP,
    EMAIL_DESTINATARIO,
    SMTP_SERVIDOR,
    SMTP_PORTA
)


def montar_email(vencimentos):
    """Monta o conteúdo HTML do relatório."""

    hoje = date.today()

    total = len(vencimentos)

    linhas = []

    for registro in vencimentos:

        usuario = html.escape(registro["usuario"])

        data = registro["data_expiracao"].strftime(
            "%d/%m/%Y"
        )

        dias = registro["dias"]
        situacao = registro["situacao"]

        if situacao == "expirado":
            status = "VENCIDO"
            descricao = f"Expirado há {abs(dias)} dias"
            cor = "#dc3545"

        elif situacao == "vence hoje":
            status = "VENCE HOJE"
            descricao = "Vence hoje"
            cor = "#fd7e14"

        else:
            status = "PRÓXIMO DO VENCIMENTO"
            descricao = f"Faltam {dias} dias"
            cor = "#d69e00"

        linhas.append(f"""
            <tr>
                <td style="padding: 12px; border-bottom: 1px solid #ddd;">
                    {usuario}
                </td>

                <td style="padding: 12px; border-bottom: 1px solid #ddd;">
                    {data}
                </td>

                <td style="padding: 12px; border-bottom: 1px solid #ddd; color: {cor};">
                    <strong>{status}</strong><br>
                    {descricao}
                </td>
            </tr>
        """)

    tabela = "\n".join(linhas)

    html_email = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333;">

        <h2>Relatório de vencimentos</h2>

        <p>
            Foram identificadas <strong>{total}</strong>
            contas próximas do vencimento ou expiradas.
        </p>

        <table style="
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        ">

            <thead>
                <tr style="background-color: #f2f2f2;">
                    <th style="padding: 12px;">Usuário</th>
                    <th style="padding: 12px;">Data de expiração</th>
                    <th style="padding: 12px;">Situação</th>
                </tr>
            </thead>

            <tbody>
                {tabela}
            </tbody>

        </table>

        <p style="margin-top: 25px; font-size: 12px; color: #777;">
            Relatório gerado automaticamente em
            {hoje.strftime("%d/%m/%Y")}.
        </p>

    </body>
    </html>
    """

    return html_email



def enviar_email(vencimentos):
    """Envia um único e-mail com todos os vencimentos."""

    import smtplib
    import ssl

    if not vencimentos:
        print("Nenhum vencimento identificado.")
        return False

    mensagem = EmailMessage()

    mensagem["Subject"] = "Alerta de vencimento de contas"
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = EMAIL_DESTINATARIO

    mensagem.set_content(
        "Foram identificadas contas próximas do vencimento "
        "ou expiradas. Consulte a versão HTML deste e-mail."
    )

    mensagem.add_alternative(
        montar_email(vencimentos),
        subtype="html"
    )

    contexto = ssl.create_default_context()

    try:
        print("Conectando ao Gmail...")

        with smtplib.SMTP(
            SMTP_SERVIDOR,
            587,
            timeout=30
        ) as servidor:

            servidor.ehlo()

            print("Iniciando conexão segura...")

            servidor.starttls(context=contexto)
            servidor.ehlo()

            print("Autenticando conta Gmail...")

            servidor.login(
                EMAIL_REMETENTE,
                EMAIL_SENHA_APP
            )

            print("Enviando mensagem...")

            servidor.send_message(mensagem)

        print("E-mail enviado com sucesso!")

        return True

    except smtplib.SMTPAuthenticationError:
        print(
            "Erro de autenticação. "
            "Verifique o e-mail e a senha de aplicativo."
        )
        return False

    except smtplib.SMTPException as erro:
        print(f"Erro SMTP: {erro}")
        return False

    except (OSError, TimeoutError) as erro:
        print(f"Erro de conexão com o Gmail: {erro}")
        return False
