
from huggingface_hub import InferenceClient
from constants import LLM_PROMPT


def perform_llm_inference(title, body, image_caption, metadata, llm_hf_id="microsoft/Phi-3-mini-4k-instruct"):
    prompt = LLM_PROMPT\
        .replace("$TITLE$", title)\
        .replace("$BODY$", body)\
        .replace("$IMAGE_CAPTION$", image_caption)\
        .replace("$METADATA$", metadata)

    client = InferenceClient(
        llm_hf_id,
        token="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",
    )

    response = ""
    for message in client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        stream=True,
    ):
        response += message.choices[0].delta.content

    return response
