
from config import (
    ARQUIVO_PLANILHA,
    validar_configuracoes
)

from planilha import (
    ler_planilha,
    verificar_vencimentos
)

from email_service import enviar_email


def main():

    print("=" * 45)
    print("AUTOMAÇÃO DE VENCIMENTOS")
    print("=" * 45)

    try:
        # 1. Validar configurações
        validar_configuracoes()

        print("\nVerificando configurações... OK")

        # 2. Ler planilha
        print("Lendo planilha...")

        registros = ler_planilha(ARQUIVO_PLANILHA)

        print(f"Registros encontrados: {len(registros)}")

        # 3. Verificar vencimentos
        print("Verificando datas de expiração...")

        vencimentos = verificar_vencimentos(registros)

        print(
            f"Contas identificadas: {len(vencimentos)}"
        )

        # 4. Enviar relatório
        if vencimentos:

            print("\nEnviando relatório...")

            enviar_email(vencimentos)

        else:
            print(
                "\nNenhuma conta próxima do vencimento "
                "ou expirada."
            )

        print("\nProcesso finalizado.")

    except FileNotFoundError as erro:
        print(f"\nErro: {erro}")

    except ValueError as erro:
        print(f"\nErro de configuração ou planilha: {erro}")

    except Exception as erro:
        print(f"\nErro durante a execução: {erro}")


if __name__ == "__main__":
    main()
