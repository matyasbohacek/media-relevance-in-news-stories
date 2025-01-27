
import ast
import gradio as gr

from constants import EX_0, EX_1, CSS, OVERALL_ASSESSMENT_HTML_OUTPUT, OVERALL_ASSESSMENT_OUTPUT
from llm_inference import perform_llm_article_analysis, perform_llm_inference_chat_followup
from utils import clean_llm_json, pil_image_to_binary, load_image_multi_source
from provenance_metadata import extract_and_preprocess_c2pa


current_reasoning = ""


def generate_html_analysis(overall_assessment, check_one, reasoning_one, check_two, reasoning_two):

    if overall_assessment == "RELEVANT":
        assessment_class = "relevant"
        symbol = "✓"
    else:
        assessment_class = "not-relevant"
        symbol = "✗"

    reasoning_two = "There appears to be no tampering with this artifact, verified by the provenance metadata."

    html_output = OVERALL_ASSESSMENT_HTML_OUTPUT \
        .replace("$assessment_class$", overall_assessment) \
        .replace("$symbol$", symbol) \
        .replace("$check_one$", check_one) \
        .replace("$reasoning_one$", reasoning_one) \
        .replace("$check_two$", check_two) \
        .replace("$reasoning_two$", reasoning_two)

    plain_text_output = OVERALL_ASSESSMENT_OUTPUT \
        .replace("$assessment_class$", overall_assessment) \
        .replace("$check_one$", check_one) \
        .replace("$reasoning_one$", reasoning_one) \
        .replace("$check_two$", check_two) \
        .replace("$reasoning_two$", reasoning_two)
    
    return plain_text_output, html_output


def handle_chat(history, current_reasoning, message):
    """
    Handles a chat session by updating the conversation history with the user's message and generating a response using the current reasoning context.
    :param history: Conversation history
    :param current_reasoning: String that provides additional context or reasoning to the model during inference
    :param message: String, the user's latest input message
    :return: Updated history with the bot's response to the user's message
    """

    if message.strip() == "":
        return history

    response = perform_llm_inference_chat_followup(current_reasoning, message)
    history = history + [(message, "Thank you for asking! " + response)]

    return history


def main(title, body, img_url, img_file, img_caption, simplified_input, input_mode):

    if not img_url and not img_file:
        raise gr.Error("All fields must be filled!", duration=10)

    if img_url == "":
        image_used = img_file
    if img_file == "":
        image_used = img_url

    if not title or not body or not img_caption:
        raise gr.Error("All fields must be filled!", duration=10)

    else:
        metadata = extract_and_preprocess_c2pa(image_used)
        response = perform_llm_article_analysis(title, body, img_caption, metadata)
        response_structured = ast.literal_eval(clean_llm_json(response))
        return generate_html_analysis(response_structured["3-assessment"], response_structured["1-relevant"], response_structured["1-reason"], response_structured["2-relevant"], response_structured["2-reason"])


theme = gr.themes.Default(
    primary_hue=gr.themes.colors.green,
    spacing_size="md",
    radius_size="md",
    text_size="md",
    font=[gr.themes.GoogleFont("Helvetica"), "Helvetica", "sans-serif"],
    font_mono=[gr.themes.GoogleFont("IBM Plex Mono"), "IBM Plex Mono", "monospace"]
)


with gr.Blocks(theme=theme, css=CSS) as demo:
    gr.Markdown("<br>")
    gr.Markdown("# News Image")
    gr.Markdown("# Relevance Evaluator")
    gr.Markdown("Evaluate the relevance and credibility of images and videos attached to news stories.")

    with gr.Row():
        with gr.Column(scale=1):
            input_mode = gr.Radio(["Full Article", "URL (Simplified)"], label="Input Mode", value="Full Article")

            with gr.Column(visible=True) as full_input_col:
                input1 = gr.Textbox(lines=1, placeholder="Paste the article's title", label="Title")
                input2 = gr.Textbox(lines=5, placeholder="Paste the article's body", label="Body")
                with gr.Row():
                    with gr.Column(scale=1):
                        input3 = gr.Textbox(lines=2, placeholder="Paste the path or URL to the attached image or video",
                                            label="Image/Video Path/URL")
                        input5 = gr.Textbox(lines=2, placeholder="Paste the caption of the image or video",
                                            label="Image/Video Caption")
                    input4 = gr.File(show_label=False)

                with gr.Accordion("Examples", open=False):
                    gr.Examples(examples=[EX_0], inputs=[input1, input2, input3, input4, input5])

            with gr.Column(visible=False) as simplified_input_col:
                simplified_input = gr.Textbox(lines=1, placeholder="Paste the article's URL",
                                              label="URL")

            with gr.Row():
                clear = gr.ClearButton([input1, input2, input3, input4, input5, simplified_input])
                submit = gr.Button("Submit")

        with gr.Column(scale=1):
            output4 = gr.HTML()

            with gr.Column(scale=1, visible=False) as chat_module:
                chatbot = gr.Chatbot(label="Chat Interface")
                with gr.Row():
                    with gr.Column(scale=4):
                        chat_input = gr.Textbox(placeholder="Type your message here...", show_label=False)
                    with gr.Column(scale=1):
                        chat_submit = gr.Button("Send", elem_classes="chat-button")

    def toggle_visibility(mode):
        if mode == "Full Article":
            return gr.update(visible=True), gr.update(visible=False)
        else:
            return gr.update(visible=False), gr.update(visible=True)


    input_mode.change(
        fn=toggle_visibility,
        inputs=[input_mode],
        outputs=[full_input_col, simplified_input_col]
    )


    def main_wrapper(article_title, article_body, image_url, image_file, image_caption, simplified_input, input_mode):
        CURRENT_REASONING, result = main(article_title, article_body, image_url, image_file, image_caption, simplified_input, input_mode)
        return result, gr.update(visible=True)

    submit.click(main_wrapper, inputs=[input1, input2, input3, input4, input5, simplified_input, input_mode],
                 outputs=[output4, chat_module])

    chat_submit.click(
        handle_chat,
        inputs=[chatbot, current_reasoning, chat_input],
        outputs=[chatbot]
    )

demo.launch()
