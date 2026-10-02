
import requests
import time
import json


# ============================================================
# CONFIGURAÇÃO
# ============================================================

TOKEN = 'Informe seu TOKEN aqui'

URL = "https://api.arquivo-nfe.com/prod/cnpj_receita"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}


# ============================================================
# CONSULTAS
#
# Parâmetros:
#   cnpj       = CNPJ obrigatório
#   qsa        = Opcional
#                0 = Não retornar QSA
#                1 = Retornar QSA
#
# O request_id será preenchido automaticamente após o envio
# da consulta, para posterior obtenção do resultado.
#
# O exemplo pode ser adaptado para recuperar os CNPJs
# diretamente de um banco de dados.
# ============================================================

consultas = [
    {
        "cnpj": "XXXXXXXXXXXXXX",
        "qsa": 0,
        "request_id": None
    },
    {
        "cnpj": "XXXXXXXXXXXXXX",
        "qsa": 1,
        "request_id": None
    },
    {
        "cnpj": "XXXXXXXXXXXXXX",
        "qsa": 0,
        "request_id": None
    }
]


# ============================================================
# FUNÇÃO PARA MONTAR OS PARÂMETROS
# ============================================================

def criar_parametros(consulta):

    cnpj = consulta.get("cnpj")

    if cnpj is None or cnpj == "":
        raise ValueError("O parâmetro cnpj é obrigatório.")

    qsa = consulta.get("qsa", 0)

    if qsa not in (0, 1):
        raise ValueError("O parâmetro qsa deve ser 0 ou 1.")

    parametros = {
        "cnpj": cnpj,
        "qsa": qsa
    }

    return parametros


# ============================================================
# ETAPA 1
# ENVIA O LOTE DE CONSULTAS
# ============================================================

print()
print("=" * 70)
print("ETAPA 1 - ENVIANDO CONSULTAS CNPJ RECEITA FEDERAL")
print("=" * 70)


for numero, consulta in enumerate(consultas, start=1):

    try:

        parametros = criar_parametros(consulta)

        print()
        print(f"Consulta {numero}")
        print(f"CNPJ: {consulta['cnpj']}")
        print(f"QSA: {parametros['qsa']}")
        print(f"Parâmetros: {parametros}")

        resposta = requests.post(
            URL,
            headers=HEADERS,
            params=parametros,
            timeout=60
        )

        print("URL enviada:")
        print(resposta.url)

        print(f"HTTP Status: {resposta.status_code}")

        # ----------------------------------------------------
        # CONVERTE A RESPOSTA PARA JSON
        # ----------------------------------------------------

        try:

            dados = resposta.json()

        except ValueError:

            print("A API não retornou um JSON válido.")
            print("Resposta bruta recebida:")
            print(resposta.text)

            continue

        # ----------------------------------------------------
        # ERRO
        # ----------------------------------------------------

        if "erro" in dados:

            print(f"ERRO: {dados['erro']}")

            if dados.get("request_id") is not None:

                consulta["request_id"] = dados["request_id"]

                print(
                    f"Request ID recebido: "
                    f"{consulta['request_id']}"
                )

            continue

        # ----------------------------------------------------
        # REQUEST_ID
        #
        # O request_id pode vir:
        #
        # 1. Diretamente na resposta:
        #    {"request_id": 26989}
        #
        # 2. Dentro de retorno:
        #    {"retorno": [{"request_id": 26989}]}
        # ----------------------------------------------------

        request_id = dados.get("request_id")

        if request_id is None:

            retorno = dados.get("retorno")

            if isinstance(retorno, list) and len(retorno) > 0:

                request_id = retorno[0].get("request_id")

        if request_id is not None:

            consulta["request_id"] = request_id

            print(
                f"Request ID recebido: {request_id}"
            )

        else:

            print(
                "A API não retornou request_id para esta consulta."
            )

    except requests.RequestException as erro:

        print(
            f"Erro de comunicação com a API: {erro}"
        )

    except ValueError as erro:

        print(
            f"Erro nos parâmetros: {erro}"
        )


# ============================================================
# ETAPA 2
# CONSULTA OS REQUEST_ID
# ============================================================

print()
print("=" * 70)
print("ETAPA 2 - CONSULTANDO OS RESULTADOS")
print("=" * 70)


# Número máximo de tentativas para cada consulta
MAX_TENTATIVAS = 5

# Tempo de espera entre as tentativas
INTERVALO = 5


for numero, consulta in enumerate(consultas, start=1):

    request_id = consulta.get("request_id")

    if request_id is None:

        print()
        print(
            f"Consulta {numero}: sem request_id. Ignorada."
        )

        continue

    print()
    print(
        f"Consulta {numero} - CNPJ: {consulta['cnpj']}"
    )
    print(
        f"Request ID: {request_id}"
    )

    resultado_obtido = False

    for tentativa in range(1, MAX_TENTATIVAS + 1):

        try:

            parametros = {
                "request_id": request_id
            }

            resposta = requests.post(
                URL,
                headers=HEADERS,
                params=parametros,
                timeout=60
            )

            print()
            print(
                f"Tentativa {tentativa}/{MAX_TENTATIVAS}"
            )

            print(f"HTTP Status: {resposta.status_code}")

            # ------------------------------------------------
            # CONVERTE A RESPOSTA PARA JSON
            # ------------------------------------------------

            try:

                dados = resposta.json()

            except ValueError:

                print(
                    "A API retornou uma resposta que não é "
                    "um JSON válido."
                )

                print("Resposta bruta recebida:")
                print(resposta.text)

                break

            info = dados.get("info", "")

            # ------------------------------------------------
            # ERRO
            # ------------------------------------------------

            if "erro" in dados:

                print(
                    f"ERRO: {dados['erro']}"
                )

                resultado_obtido = True

                break

            # ------------------------------------------------
            # AGUARDANDO RETORNO
            # ------------------------------------------------

            if (
                "Aguardando retorno" in info
                or
                "status PENDENTE" in info
            ):

                if tentativa < MAX_TENTATIVAS:

                    print(
                        "Consulta ainda em processamento."
                    )

                    print(
                        f"Nova tentativa em "
                        f"{INTERVALO} segundos."
                    )

                    time.sleep(INTERVALO)

                    continue

                else:

                    print(
                        "Não foi possível obter o retorno "
                        "dentro do limite de tentativas."
                    )

                    break

            # ------------------------------------------------
            # SUCESSO
            # ------------------------------------------------

            if info == "sucesso":

                print()
                print(
                    "CONSULTA CONCLUÍDA COM SUCESSO"
                )

                print(
                    json.dumps(
                        dados,
                        indent=4,
                        ensure_ascii=False
                    )
                )

                resultado_obtido = True

                break

            # ------------------------------------------------
            # RESPOSTA NÃO PREVISTA
            # ------------------------------------------------

            print(
                "Resposta recebida da API:"
            )

            print(
                json.dumps(
                    dados,
                    indent=4,
                    ensure_ascii=False
                )
            )

            resultado_obtido = True

            break

        except requests.RequestException as erro:

            print(
                f"Erro de comunicação com a API: {erro}"
            )

            break

        except Exception as erro:

            print(
                f"Erro inesperado: {erro}"
            )

            break

    if not resultado_obtido:

        print(
            f"CNPJ {consulta['cnpj']}: "
            "resultado ainda não obtido nesta execução."
        )


print()
print("=" * 70)
print("PROCESSAMENTO FINALIZADO")
print("=" * 70)

