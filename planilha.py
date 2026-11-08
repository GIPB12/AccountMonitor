
from datetime import date, datetime
from pathlib import Path
from openpyxl import load_workbook


def converter_data(valor):
    """Converte valores do Excel para datetime.date."""

    if isinstance(valor, datetime):
        return valor.date()

    if isinstance(valor, date):
        return valor

    if isinstance(valor, str):
        valor = valor.strip()

        formatos = [
            "%d/%m/%Y",
            "%d.%m.%Y",
            "%d.%m.%y",
            "%Y-%m-%d"
        ]

        for formato in formatos:
            try:
                return datetime.strptime(valor, formato).date()
            except ValueError:
                continue

    return None


def ler_planilha(caminho):
    """Lê os registros da planilha Excel."""

    caminho = Path(caminho)

    if not caminho.exists():
        raise FileNotFoundError(
            f"Planilha não encontrada: {caminho}"
        )

    workbook = load_workbook(
        caminho,
        read_only=True,
        data_only=True
    )

    try:
        planilha = workbook.active

        linhas = planilha.iter_rows(values_only=True)

        cabecalho = next(linhas, None)

        if not cabecalho:
            raise ValueError("A planilha está vazia.")

        # Identifica as colunas pelos nomes
        colunas = {}

        for indice, nome in enumerate(cabecalho):
            if nome is not None:
                nome = str(nome).strip().lower()

                colunas[nome] = indice

        obrigatorias = [
            "login",
            "data expiração"
        ]

        for coluna in obrigatorias:
            if coluna not in colunas:
                raise ValueError(
                    f"Coluna obrigatória não encontrada: {coluna}"
                )

        indice_usuario = colunas["login"]
        indice_expiracao = colunas["data expiração"]

        registros = []

        for numero_linha, linha in enumerate(linhas, start=2):

            usuario = linha[indice_usuario]
            valor_expiracao = linha[indice_expiracao]

            data_expiracao = converter_data(valor_expiracao)

            if not usuario or not data_expiracao:
                print(
                    f"Aviso: linha {numero_linha} ignorada "
                    "por falta de usuário ou data válida."
                )
                continue

            registros.append({
                "usuario": str(usuario).strip(),
                "data_expiracao": data_expiracao
            })

        return registros

    finally:
        workbook.close()


def verificar_vencimentos(registros, hoje=None):
    """Identifica contas próximas do vencimento ou expiradas."""

    hoje = hoje or date.today()

    vencimentos = []

    for registro in registros:

        data_expiracao = registro["data_expiracao"]

        dias = (data_expiracao - hoje).days

        if dias <= 7:

            if dias < 0:
                situacao = "expirado"
            elif dias == 0:
                situacao = "vence hoje"
            else:
                situacao = "proximo"

            vencimentos.append({
                "usuario": registro["usuario"],
                "data_expiracao": data_expiracao,
                "dias": dias,
                "situacao": situacao
            })

    return vencimentos
