import os
from dotenv import load_dotenv
import csv
import json
import yaml
import time
import cohere

load_dotenv()

co = cohere.ClientV2(
  api_key = os.getenv("COHERE_API_KEY"),
  log_warning_experimental_features=False
)

temp = [0.0, 0.5, 0.9]
modelo = "command-a-03-2025" #"command-r-plus-08-2024"

respostaPorCriterio = {
  "type": "object",
  "properties": {
    "nota_1A": {
      "type": "number"
      },
    "nota_1B": {
      "type": "number"
      },
    "nota_1C": {
      "type": "number"
      },
    "numero_de_erros_gramaticais": {
      "type": "integer"
      },
    "erros_gramaticais": {
      "type": "array",
      "items": {
        "type" : "string"
        }
      },
    "feedbacks": {
      "type": "array",
      "items": {
        "type": "string"
        }
      }
  },
  "required": ["nota_1A", "nota_1B", "nota_1C", "numero_de_erros_gramaticais", "erros_gramaticais", "feedbacks"]
}

respostaFinal = {
  "type": "object",
  "properties": {
    "nota_final": {
      "type": "number"
      },
    "numero_de_erros_gramaticais": {
      "type": "integer"
      },
    "erros_gramaticais": {
      "type": "array",
      "items": {
        "type" : "string"
        }
      },
    "feedbacks": {
      "type": "array",
      "items": {
        "type": "string"
        }
      }
  },
  "required": ["nota_final", "numero_de_erros_gramaticais", "erros_gramaticais", "feedbacks"]
}

respostaEmFaixa = {
  "type": "object",
  "properties": {
    "faixa": {
      "type": "string"
      },
    "numero_de_erros_gramaticais": {
      "type": "integer"
      },
    "erros_gramaticais": {
      "type": "array",
      "items": {
        "type" : "string"
        }
      },
    "feedbacks": {
      "type": "array",
      "items": {
        "type": "string"
        }
      }
  },
  "required": ["faixa", "numero_de_erros_gramaticais", "erros_gramaticais", "feedbacks"]
}

jsonGerado = []
root_path = os.getcwd()

path_prompts = os.path.join(root_path, "prompt_testing", "prompts.yaml")
path_essays = os.path.join(root_path, "prompt_testing", "sheets", "redacoes2022.csv")

with open(path_prompts, 'r', encoding='utf-8') as file:
    prompts_yaml = yaml.safe_load(file)
    prompts = prompts_yaml['prompts']

with open(path_essays, encoding='utf-8') as arquivo_referencia:

  tabela = csv.reader(arquivo_referencia, delimiter='|')
  numero_redacao = 0

  for linha in tabela:
    numero_redacao += 1
    redacao = linha[0]

    for prompt in prompts:

      # Definir aqui intervalo de prompts a serem testados
      if prompt['id'] >= 7 and prompt['id'] <= 12:
        prompt_formatado = prompt['prompt'] + "\nRetorne em formato de JSON\n" + redacao
        prompt_formatado += "\n\n" + prompt['extras'] if 'extras' in prompt else ''

        print(f"Redação {numero_redacao} - Prompt {prompt['id']}")

        formato_resposta = None

        match prompt['id']:
          # ADICIONAR NOVOS CASOS NO SWITCH CASE CONFORME FOR INTERESSANTE
          case 7 | 10:
            formato_resposta = respostaPorCriterio
          case 8 | 11:
            formato_resposta = respostaFinal
          case 9 | 12:
            formato_resposta = respostaEmFaixa

        if formato_resposta is None:
          raise ValueError("Atribua um valor a \"formato_resposta\"")

        for i in (temp):
          for j in range(3):
            try:
              response = co.chat(
                  model=modelo,
                  temperature=i,
                  messages=[
                      {
                          "role": "user",
                          "content": prompt_formatado,
                      }
                  ],
                  response_format={
                    "type": "json_object",
                    "schema": formato_resposta
                  },
                  max_tokens=2048
              )

              response = json.loads(response.message.content[0].text)
              response['modelo'] = modelo
              response['prompt'] = prompt['id']
              response['temp'] = i
              response['versao'] = j + 1
              response['essay'] = numero_redacao
              jsonGerado.append(response)
              print(f"Temperatura testada: {i}")
            except Exception as e:
              print(f"Erro na Redação {numero_redacao} - Prompt {prompt['id']} - Temp {i} - Run {j+1}: {e}")

            # time.sleep(0.5)

  output_path = os.path.join(os.getcwd(), "prompt_testing", f'output_{response["modelo"]}.json')
  with open(output_path, 'w', encoding="utf-8") as file:
    json.dump(jsonGerado, file, indent=2, ensure_ascii=False)
    file.close()