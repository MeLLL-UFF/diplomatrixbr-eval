import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
import csv
import json
import yaml
import requests
import argparse

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

def main(n_iteracoes, temps, anos, lista_prompts):
  url = "https://raw.githubusercontent.com/MeLLL-UFF/diplomatrixbr-gen/main/Diplomatrix.json"
  requisicao = requests.get(url)

  if requisicao.status_code == 200:
    diplomatrix = requisicao.json()
  else:
    raise ValueError("Não foi possível acessar o repositório")

  load_dotenv()

  OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
  client = OpenAI(api_key=OPENAI_API_KEY)

  temp = temps
  num_runs = n_iteracoes
  ano = anos

  jsonGerado = []
  root_path = os.getcwd()

  path_prompts = os.path.join(root_path, "prompt_testing", "prompts.yaml")
  
  with open(path_prompts, 'r', encoding='utf-8') as file:
      prompts_yaml = yaml.safe_load(file)
      prompts = prompts_yaml['prompts']

  dados_candidatos = diplomatrix["Candidates_Essays"][ano]["Candidates"]
  numero_redacao = 0

  for candidato in dados_candidatos:
    numero_redacao += 1
    redacao = candidato["Essay"]

    for prompt in prompts:

      if prompt['id'] in lista_prompts:
        prompt_formatado = prompt['prompt'] + redacao
        prompt_formatado += "\n\n" + prompt['extras'] if 'extras' in prompt else ''

        print(f"Redação {numero_redacao} - Prompt {prompt['id']}")

        formato_resposta = None

        match prompt['id']:
          case 7 | 10:
            formato_resposta = respostaPorCriterio
          case 8 | 11:
            formato_resposta = respostaFinal
          case 9 | 12:
            formato_resposta = respostaEmFaixa

        if formato_resposta is None:
          raise ValueError("Atribua um valor a \"formato_resposta\"")

        for i in (temp):
          for j in range(num_runs):
            try:
              response = client.beta.chat.completions.parse(
                  model="gpt-5",
                  temperature=i,
                  messages=[
                      #{"role": "developer", "content": "Você é um corretor de redações que deverá avaliar uma redação que concorre ao cargo de diplomata brasileiro. Retorne sua resposta seguindo a estrutura passada."},
                      {"role": "user", "content": prompt_formatado},
                  ],
                  response_format=formato_resposta
              )

              response = json.loads(response.choices[0].message.content)
              response['modelo'] = 'gpt-5'
              response['prompt'] = prompt['id']
              response['temp'] = i
              response['versao'] = j + 1
              response['essay'] = numero_redacao
              response['ano'] = ano
              jsonGerado.append(response)
              print(f"Temperatura testada: {i}")

            except Exception as e:
              print(f"Erro na Redação {numero_redacao} - Prompt {prompt['id']} - Temp {i} - Run {j+1}: {e}")
    
    # Salvar resultados parciais por redação pra evitar perda de dados
    # Pode ser removido se não for necessário
    if jsonGerado:
        last_response = jsonGerado[-1]
        output_path = os.path.join(os.getcwd(), "prompt_testing", "essay_dump", f'redacao_{ano}_prompt{prompt["id"]}_{numero_redacao}_output_{last_response["modelo"]}_p7-12_{num_runs}r.json')
        with open(output_path, 'w', encoding="utf-8") as file:
            json.dump(jsonGerado, file, indent=2, ensure_ascii=False)
            file.close()

  if jsonGerado:
    last_response = jsonGerado[-1]
    output_path = os.path.join(os.getcwd(), "prompt_testing", f'output_{last_response["modelo"]}_p12_{num_runs}r.json')
    with open(output_path, 'w', encoding="utf-8") as file:
        json.dump(jsonGerado, file, indent=2, ensure_ascii=False)
        file.close()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Avalia redações de um determinado ano do CACD com GPT.")
  parser.add_argument("--n_iteracoes", type=int, required=True, help="Quantas iterações por redação.")
  parser.add_argument("--temps", type=float, nargs="+", required=True, help="Temperaturas usadas.")
  parser.add_argument("--anos", type=str, required=True, help="Anos avaliados.")
  parser.add_argument("--prompts", type=int, nargs="+", required=True, help="Prompts testados.")

  args = parser.parse_args()

  main(args.n_iteracoes, args.temps, args.anos, args.prompts)