<img width="1727" alt="banner-captioned" src="https://github.com/user-attachments/assets/b6d604c8-ba43-44d9-bb59-49f9a8376415" />

# Large Language Models and Provenance Metadata for Determining the Relevance of Images and Videos in News Stories

#### [Tomas Peterka]() and [Matyas Bohacek](https://www.matyasbohacek.com)

The most effective misinformation campaigns are multimodal, often combining text with images and videos taken out of context—or fabricating them entirely—to support a given narrative. Contemporary methods for detecting misinformation, whether in deepfakes or text articles, often miss the interplay between multiple modalities. Built around a large language model, the system proposed in this paper addresses these challenges. It analyzes both the article's text and the provenance metadata of included images and videos to determine whether they are relevant. We open-source the system prototype and interactive web interface.

> [See paper]() — See poster — [Contact us](mailto:maty-at-stanford-dot-edu)
> 
> _Pre-print released on arXiv_

## Getting Started


1. Clone this repo:

```shell
git clone https://github.com/matyasbohacek/media-relevance-in-news-stories.git
```

2. In the `media-relevance-in-news-stories` directory, set up a Python environment (Python 3.9 is recommended); you can create the environment from scratch or using:

```shell
conda create -n media-relevance-in-news-stories python=3.9
```

3. Install required Python dependencies using:

```shell
conda activate media-relevance-in-news-stories
pip install -r requirements.txt
```

4. Start the interactive web interface:

```shell
python -m app
```

## Features

**C2PA Provenance Extraction.** Extracts C2PA metadata from images and videos, converting it into an LLM-readable format. This functionality is implemented in `provenance_metadata.py`.

**LLM Inference.**  Provides Hugging Face-powered LLM inference, located in `llm_inference.py`. By default, the prototype uses a model from the Phi-3 family, but any LLM can be used by specifying the starting weights.

**Web Interface.** Wrapping all functionality of this prototype into an easy-to-use GUI, the `app.py` script contains the implementation of a Gradio web interface.

## Citation

```bibtex
TBD
```

## Remarks & Updates

- (**TBD Date**) The pre-print is released on arXiv.
