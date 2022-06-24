## spaCyTurk - trained spaCy models for Turkish

spaCyTurk is a library providing trained [spaCy](https://spacy.io) models for Turkish language.

### Available Models 

**Trained floret vectors for Turkish**

The floret vectors were trained on the deduplicated version of [OSCAR-2109](https://oscar-corpus.com/post/oscar-v21-09/) Turkish corpus. The sentence segmented (non-Turkish sentences were removed) and tokenized final corpus has a size of 30GB and 4327M tokens.

For more details, see the ***[article](https://medium.com/p/b3c516c1570f)*** describing the parameter selection and evaluation process.

>**training parameters:** model=cbow, dim=300, minn=4, maxn=6, hashCount=2, minCount=5, ws=5, neg=10, lr=0.05, epoch=5

Two models **(tr_floret_web_md, tr_floret_web_lg)** are available with bucket sizes of 50000 and 200000 respectively.

Model performances were evaluated in below downstream NLP tasks.

* Named Entity Recognition, **NER**
* Part of Speech Tagging, **POS**
* Offensive Language Identificaton, **OLI**
* Movie Sentiment Analaysis, **MSA**

| Vectors                         |  NER  |  POS  |  OLI  |  MSA  | Model Size |
| --------------------------------| ----: | ----: | ----: | ----: | ---------: |
| none                            | 90.19 | 82.60 | 61.07 | 75.63 |          - |
| fastText (~3.4M vectors/keys)   | 92.36 | 92.49 | 69.83 | 75.62 |      4.1GB |
| tr_floret_web_md (bucket 50K)   | 92.87 | 93.02 | 73.55 | 76.98 |       60MB |
| tr_floret_web_lg (bucket 200K)  | 93.05 | 93.51 | 74.00 | 77.28 |      240MB |
| BERT                            | 95.71 | 96.42 | 79.37 | 80.87 |      444MB |

**Evaluation metrics:** micro f1-score for NER, accuracy for POS, macro f1-score for OLI and MSA.

### Installation & Usage

Trained models can be installed directly from [Hugging Face Hub](https://huggingface.co/spacyturk). Alternatively, you can install `spacyturk` from [PyPI](https://pypi.org/project/spacyturk/) and download models through its API. This is the recommended way since the downloader performs version compatibility checks.
 
```bash
pip install spacyturk
```

```python
import spacyturk

# downloads the spaCyTurk model
spacyturk.download("model_name")

# info about spaCyTurk installation and models
spacyturk.info()

# load the model using spaCy
import spacy
nlp = spacy.load("model_name")
```

Alternatively, download models through CLI

```bash
# downloads the spaCyTurk model
python -m spacyturk download model_name
```
