import outlines
from transformers import AutoModelForCausalLM, AutoTokenizer

# Create model
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B"),
    AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
)

# Call it to generate text
result = model("What's the capital of Latvia?", max_new_tokens=20)
print(result) # 'Riga'