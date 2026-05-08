import os
from dotenv import load_dotenv
from pydantic import BaseModel
import json
import yaml
import requests
import argparse
import outlines

from huggingface_hub import login
import torch
import transformers

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

def main(n_iteracoes, temps, anos, lista_prompts, nome_completo_modelo, lista_redacao=None):
  url = "https://raw.githubusercontent.com/MeLLL-UFF/diplomatrixbr-gen/main/Diplomatrix.json"
  requisicao = requests.get(url)

  if requisicao.status_code == 200:
    diplomatrix = requisicao.json()
  else:
    raise ValueError("Não foi possível acessar o repositório")

  load_dotenv()

  login(token=os.getenv("HUGGINGFACE_API_KEY"))

  device = f'cuda' if torch.cuda.is_available() else 'cpu'

  model_id = "google/gemma-3-1b-it"
  hf_model = transformers.AutoModelForCausalLM.from_pretrained(model_id, device_map=device, dtype=torch.bfloat16, trust_remote_code=True)

  tokenizer = None
  try:
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
  except ValueError:
    pass

  hf_model.resize_token_embeddings(len(tokenizer))
  created_model = outlines.from_transformers(hf_model, tokenizer)

  #pipeline = transformers.pipeline(
  #  task="text-generation",
  #  trust_remote_code=True,
  #  model=model_id,
  #  # The quantization line
  #  tokenizer = tokenizer,
  #  dtype = torch.float16,
  #  device=device,
  #)

  temp = list(map(float, temps))
  num_runs = n_iteracoes # DEFINIR NÚMERO DE EXECUÇÕES POR PROMPT/TEMPERATURA
  ano = anos

  jsonGerado = []
  root_path = os.getcwd()

  path_prompts = os.path.join(root_path, "prompt_testing", "prompts.yaml")

  with open(path_prompts, 'r', encoding='utf-8') as file:
      prompts_yaml = yaml.safe_load(file)
      prompts = prompts_yaml['prompts']

  dados_candidatos = diplomatrix["Candidates_Essays"][ano]["Candidates"]
  try:
    padrao_de_resposta = diplomatrix["Candidates_Essays"][ano]["Answer_Pattern"]
    enunciado = diplomatrix["Candidates_Essays"][ano]["Question_Statement"]
  except KeyError:
    padrao_de_resposta = ""
  numero_redacao = 0

  for candidato in dados_candidatos:
    numero_redacao += 1
    if lista_redacao != None and numero_redacao not in lista_redacao:
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
          case 8 | 11 | 14:
            formato_resposta = respostaFinal
          case 9 | 12 | 15:
            formato_resposta = respostaEmFaixa

        if formato_resposta is None:
          raise ValueError("Atribua um valor a \"formato_resposta\"")

        for i in (temp):
          for j in range(num_runs):
            try:
              sample = False if i == 0.0 else True
              outputs = created_model(
                  prompt_formatado,
                  output_type=formato_resposta,
                  max_new_tokens=2048,
                  do_sample=sample,
                  temperature=i
                )
              print(sample)
              print(outputs)

            except Exception as e:
              print(outputs)
              print(f"Erro na Redação {numero_redacao} - Prompt {prompt['id']} - Temp {i} - Run {j+1}: {e}")

            response = json.loads(outputs)
            response['modelo'] = nome_completo_modelo.split("/")[-1]
            response['prompt'] = prompt['id']
            response['temp'] = float(i)
            response['versao'] = j + 1
            response['essay'] = numero_redacao
            response['ano'] = ano
            jsonGerado.append(response)
            print(f"Temperatura testada: {i}")\
            
            print(response)
""" 

    
    # Salvar resultados parciais por redação pra evitar perda de dados
    # Pode ser removido se não for necessário
    output_path = os.path.join(os.getcwd(), "prompt_testing", "essay_dump", f'redacao_{ano}_{numero_redacao}_output_{response["modelo"]}_p13-15_{num_runs}r.json')
    with open(output_path, 'w', encoding="utf-8") as file:
      json.dump(jsonGerado, file, indent=2, ensure_ascii=False)
      file.close()
  
  listtemps = ""
  for i in temp:
    listtemps += str(i) + "_"

  output_path = os.path.join(os.getcwd(), "prompt_testing", f'{listtemps}output_{response["modelo"]}_{ano}_p{lista_prompts[0]}-{lista_prompts[-1]}_{num_runs}r.json')
  with open(output_path, 'w', encoding="utf-8") as file:
    json.dump(jsonGerado, file, indent=2, ensure_ascii=False)
    file.close()
"""

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Avalia redações de um determinado ano do CACD com Sabia-3.")
  parser.add_argument("--n_iteracoes", type=int, required=True, help="Quantas iterações por redação.")
  parser.add_argument("--temps", type=str, nargs="+", required=True, help="Temperaturas usadas.")
  parser.add_argument("--anos", type=str, required=True, help="Anos avaliados.")
  parser.add_argument("--prompts", type=int, nargs="+", required=True, help="Prompts testados.")
  parser.add_argument("--nome_modelo", type=str, required=True, help="Nome do modelo a ser testado.")
  parser.add_argument("--redacoes", type=int, nargs="+", required=False, help="Redação a ser avaliada.")

  args = parser.parse_args()

  main(args.n_iteracoes, args.temps, args.anos, args.prompts, args.nome_modelo, args.redacoes)