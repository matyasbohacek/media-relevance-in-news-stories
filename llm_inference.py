
from huggingface_hub import InferenceClient
from constants import LLM_PROMPT, LLM_PROMPT_FOLLOWUP_CHAT


def perform_llm_article_analysis(title, body, image_caption, metadata, llm_hf_id="microsoft/Phi-3-mini-4k-instruct"):
    """
    TODO
    :param title:
    :param body:
    :param image_caption:
    :param metadata:
    :param llm_hf_id:
    :return:
    """

    prompt = LLM_PROMPT \
        .replace("$TITLE$", title) \
        .replace("$BODY$", body) \
        .replace("$IMAGE_CAPTION$", image_caption) \
        .replace("$METADATA$", metadata)

    return __perform_llm_inference(prompt, llm_hf_id=llm_hf_id)


def perform_llm_inference_chat_followup(current_reasoning, message, llm_hf_id="microsoft/Phi-3-mini-4k-instruct"):
    """
    TODO
    :param current_reasoning:
    :param message:
    :param llm_hf_id:
    :return:
    """

    prompt = LLM_PROMPT_FOLLOWUP_CHAT \
        .replace("$CURRENT_REASONING$", current_reasoning) \
        .replace("$MESSAGE$", message)

    return __perform_llm_inference(prompt, llm_hf_id=llm_hf_id)


def __perform_llm_inference(prompt, llm_hf_id="microsoft/Phi-3-mini-4k-instruct"):
    """
    TODO

    :param prompt:
    :param llm_hf_id:
    :return:
    """

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
