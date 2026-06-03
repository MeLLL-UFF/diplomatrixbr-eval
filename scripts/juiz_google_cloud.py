import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel
import json
import yaml
import requests
import argparse
from anthropic import AnthropicVertex


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

def main(n_iteracoes, temps, anos, lista_prompts, lista_redacao=None):
  url = "https://raw.githubusercontent.com/MeLLL-UFF/diplomatrixbr-gen/main/Diplomatrix.json"
  requisicao = requests.get(url)

  if requisicao.status_code == 200:
    diplomatrix = requisicao.json()
  else:
    raise ValueError("Não foi possível acessar o repositório")

  load_dotenv()

  client = AnthropicVertex(region="global", project_id="aida-reports")

  temp = list(map(float, temps))
  num_runs = n_iteracoes
  ano = anos
  print(f"Redações do ano {ano}")

  jsonGerado = []
  root_path = os.getcwd()

  path_prompts = os.path.join(root_path, "prompt_testing", "prompts_claude.yaml")

  with open(path_prompts, 'r', encoding='utf-8') as file:
      prompts_yaml = yaml.safe_load(file)
      prompts = prompts_yaml['prompts']

  dados_candidatos = diplomatrix["Candidates_Essays"][ano]["Candidates"]
  criterios = diplomatrix["Candidates_Essays"][ano]["Criteria"]
  enunciado = diplomatrix["Candidates_Essays"][ano]["Question_Statement"]
  try:
    padrao_de_resposta = diplomatrix["Candidates_Essays"][ano]["Answer_Pattern"]
  except KeyError:
    padrao_de_resposta = ""
  numero_redacao = 0

  for candidato in dados_candidatos:
    numero_redacao += 1
    if lista_redacao is not None and numero_redacao not in lista_redacao:
      continue
    redacao = candidato["Essay"]

    for prompt in prompts:

      # DEFINIR AQUI QUAIS PROMPTS SERÃO TESTADOS
      if prompt['id'] in lista_prompts:
        prompt_formatado = prompt['prompt'].replace("{enunciado}", str(enunciado))
        prompt_formatado = prompt_formatado.replace("{padrao_resposta}", str(padrao_de_resposta)) + redacao
        prompt_formatado += "\n\n" + prompt['extras'] if 'extras' in prompt else ''

        print(f"Redação {numero_redacao} - Prompt {prompt['id']}")

        formato_resposta = None

        match prompt['id']:
          # ADICIONAR NOVOS CASOS NO SWITCH CASE CONFORME FOR INTERESSANTE
          case 7 | 10 | 13:
            formato_resposta = respostaPorCriterio
            prompt_formatado = prompt_formatado.replace("{1A}", str(criterios["1A"]))
            prompt_formatado = prompt_formatado.replace("{1B}", str(criterios["1B"]))
            prompt_formatado = prompt_formatado.replace("{1C}", str(criterios["1C"]))
            prompt_formatado = prompt_formatado.replace("{2}", str(criterios["2"]))
            max_pontos = criterios["1A"] + criterios["1B"] + criterios["1C"]
            prompt_formatado = prompt_formatado.replace("{max_pontos}", str(max_pontos))
          case 8 | 11 | 14:
            formato_resposta = respostaFinal
            pontuacao_maxima = diplomatrix["Candidates_Essays"][ano]["Maximum_Score"]
            prompt_formatado = prompt_formatado.replace("{pontuacao_maxima}", str(pontuacao_maxima))
          case 9 | 12 | 15:
            formato_resposta = respostaEmFaixa

        if formato_resposta is None:
          raise ValueError("Atribua um valor a \"formato_resposta\"")

        for i in (temp):
          for j in range(num_runs):
            try:
              model_name = "claude-opus-4-6"
              message = client.messages.parse(
                max_tokens=2048,
                messages=[{"role": "user", "content": prompt_formatado}],
                model=model_name,
                temperature=0.0,
              )

              response = json.loads(message.content[0].text)
              response['modelo'] = model_name
              response['prompt'] = prompt['id']
              response['temp'] = float(i)
              response['versao'] = j + 1
              response['essay'] = numero_redacao
              response['ano'] = ano
              jsonGerado.append(response)
              print(f"Temperatura testada: {i}")

            except Exception as e:
              print(f"Erro na Redação {numero_redacao} - Prompt {prompt['id']} - Temp {i} - Run {j+1}: {e}")

              print(f"Erro ao transformar saída em JSON\n ERRO {e}")
              dump_path = os.path.join(os.getcwd(), "prompt_testing", "essay_dump", "redacoes_unicas")
              os.makedirs(dump_path, exist_ok=True)
              dump_path = os.path.join(dump_path, f'redacao_{ano}_{numero_redacao}_output_{model_name}_p{lista_prompts[0]}-{lista_prompts[-1]}_{num_runs}r.json')
              dump_file = {}
              with open(dump_path, "w", encoding="utf-8") as file:
                dump_file['json'] = message.content[0].text
                dump_file['modelo'] = model_name
                dump_file['prompt'] = prompt['id']
                dump_file['temp'] = float(i)
                dump_file['versao'] = j + 1
                dump_file['essay'] = numero_redacao
                dump_file['ano'] = ano
                json.dump(dump_file, file, indent=2, ensure_ascii=False)
    
    # Salvar resultados parciais por redação pra evitar perda de dados
    # Pode ser removido se não for necessário
    output_path = os.path.join(os.getcwd(), "prompt_testing", "essay_dump", f'redacao_{ano}_{numero_redacao}_output_{response["modelo"]}_p{lista_prompts[0]}-{lista_prompts[-1]}_{num_runs}r.json')
    with open(output_path, 'w', encoding="utf-8") as file:
      json.dump(jsonGerado, file, indent=2, ensure_ascii=False)
      file.close()
  
  listtemps = ""
  for i in temp:
    listtemps += str(i) + "_"

  output_path = os.path.join(os.getcwd(), "prompt_testing", "outputs", model_name, f'output_{response["modelo"]}_{ano}_p{lista_prompts[0]}-{lista_prompts[-1]}_{num_runs}r.json')
  os.makedirs(os.path.join(os.getcwd(), "prompt_testing", "outputs", model_name), exist_ok=True)
  with open(output_path, 'w', encoding="utf-8") as file:
    json.dump(jsonGerado, file, indent=2, ensure_ascii=False)
    file.close()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Avalia redações de um determinado ano do CACD com Sabia.")
  parser.add_argument("--n_iteracoes", type=int, required=True, help="Quantas iterações por redação.")
  parser.add_argument("--temps", type=str, nargs="+", required=True, help="Temperaturas usadas.")
  parser.add_argument("--anos", type=str, required=True, help="Anos avaliados.")
  parser.add_argument("--prompts", type=int, nargs="+", required=True, help="Prompts testados.")
  parser.add_argument("--redacoes", type=int, nargs="+", required=False, help="Redação a ser avaliada.")

  args = parser.parse_args()

  main(args.n_iteracoes, args.temps, args.anos, args.prompts, args.redacoes)