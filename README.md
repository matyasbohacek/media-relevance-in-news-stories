<img width="1727" alt="banner-captioned" src="https://github.com/user-attachments/assets/b6d604c8-ba43-44d9-bb59-49f9a8376415" />

# Large Language Model and Provenance Metadata for Determining Image and Video Relevance in News Stories

#### [Tomas Peterka]() and [Matyas Bohacek](https://www.matyasbohacek.com)

The most effective misinformation campaigns are multimodal, often combining text with images and videos taken out of context—or fabricating them entirely—to support a given narrative. Contemporary methods for detecting misinformation, whether in deepfakes or text articles, often miss the interplay between multiple modalities. Built around a large language model, the system proposed in this paper addresses these challenges. It analyzes both the article's text and the provenance metadata of included images and videos to determine whether they are relevant. We open-source the system prototype and interactive web interface.

> [See paper]() — See poster — [Contact us](mailto:maty-at-stanford-dot-edu)
> 
> _Pre-print released on arXiv_

## Getting Started


1. Clone this repo:

```shell
git clone https://github.com/matyasbohacek/news-article-media-provenance.git
```

2. In the `news-article-media-provenance` directory, set up a Python environment (Python 3.9 is recommended); you can create the environment from scratch or using:

```shell
conda create -n news-article-media-provenance python=3.9
```

3. Install required Python dependencies using:

```shell
pip install -r requirements.txt
```

4. Start the interactive web app:

```shell
python -m app
```

## Features

**C2PA Provenance Extraction.** TBD

**LLM Inference.** TBD

**Demo.** TBD

## Citation

```bibtex
TBD
```

## Remarks & Updates

- (**TBD Date**) The pre-print is released on arXiv.
