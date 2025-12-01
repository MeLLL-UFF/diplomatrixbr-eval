import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
import csv
import json
import yaml

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
temp = [0.0, 0.5, 0.9]

class respostaPorCriterio(BaseModel):
  nota_1A: float
  nota_1B: float
  nota_1C: float
  numero_de_erros_gramaticais: int
  erros_gramaticais: list[str]
  feedbacks: list[str]

class respostaFinal(BaseModel):
  nota_final: float
  numero_de_erros_gramaticais: int
  erros_gramaticais: list[str]
  feedbacks: list[str]  

class respostaEmFaixa(BaseModel):
  faixa: str
  numero_de_erros_gramaticais: int
  erros_gramaticais: list[str]
  feedbacks: list[str]

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
      if prompt['id'] >= 1 and prompt['id'] <= 5:
        prompt_formatado = prompt['prompt'] + redacao
        prompt_formatado += "\n\n" + prompt['extras'] if 'extras' in prompt else ''

        print(f"Redação {numero_redacao} - Prompt {prompt['id']}")

        for i in (temp):
          for j in range(3):
            response = client.beta.chat.completions.parse(
                model="gpt-5",
                temperature=i,
                messages=[
                    {"role": "developer", "content": "Você é um corretor de redações que deverá avaliar uma redação que concorre ao cargo de diplomata brasileiro. Retorne sua resposta seguindo a estrutura passada."},
                    {"role": "user", "content": prompt_formatado},
                ],
                response_format=respostaPorCriterio
            )

            response = json.loads(response.choices[0].message.content)
            response['modelo'] = 'gpt-5'
            response['prompt'] = prompt['id']
            response['temp'] = i
            response['versao'] = j + 1
            response['essay'] = numero_redacao
            jsonGerado.append(response)

          print(f"Temperatura testada: {i}")

  with open(f'output_{response["modelo"]}.json', 'w') as file:
    json.dump(jsonGerado, file, indent=2, ensure_ascii=False)
    file.close()