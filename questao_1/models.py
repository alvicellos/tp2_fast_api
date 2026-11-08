from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM

model_id = "gpt2"
gpt2_tokenizer = AutoTokenizer.from_pretrained(model_id, clean_up_tokenization_spaces=True)

# Inicialização do modelo
gpt2_model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    device_map="auto", 
    torch_dtype="auto" 
)

def generate(model, tokenizer, prompt, max_new_tokens=80):
    
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
    **inputs,
    max_new_tokens=max_new_tokens,
    pad_token_id=tokenizer.eos_token_id
    )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def retornar(prompt):
    retorno = generate(gpt2_model, gpt2_tokenizer, prompt)
    return retorno

