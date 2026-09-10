# Review Sentiment Analysis

**Author:** Jace Ackerman

A sentiment analysis pipeline for Apple Watch product reviews, built around modular, single-responsibility classes and a locally-run Phi-3 model.

## Overview

This project scrapes real customer reviews for five generations of Apple Watch (Series 5–9) from eBay, runs them through a local Phi-3 language model, and visualizes sentiment trends across product versions. It was built as Project 3 in a series of assignments, extending and rewriting earlier work to follow SOLID design principles — specifically the **Single Responsibility Principle (SRP)**.

This branch (`reviewSentimentAnalysis`) contains all files required to run Project 3, including reused and refactored code from Projects 1 and 2. Only the `Project3_AI_Reviewer` folder is relevant here — `webScraping` contains legacy Project 2 code and is not used by this pipeline.

## Architecture

Every class in this project has exactly one responsibility, satisfying SRP throughout the pipeline.

**Scraping (from Project 2, already modular):**

| Class | Responsibility |
|---|---|
| `UrlManager` | Reads review page URLs from file |
| `Scraper` | Retrieves the raw HTML document |
| `Parser` | Filters the HTML for review data |
| `DataHandler` | Saves parsed review data |
| `ScrapingManager` | Integrates the scraping classes |

**Sentiment Analysis (rewritten for Project 3 to satisfy SRP):**

| Class | Responsibility |
|---|---|
| `PromptManager` | Creates prompt files from review data |
| `Phi3Interface` | Sends prompts to Phi-3 and saves responses |
| `ResponseHandler` | Counts positive, negative, and neutral responses |
| `Graph` | Builds the sentiment visualization |
| `SentimentAnalysis` | Integrates `PromptManager`, `Phi3Interface`, and `ResponseHandler` per product |
| `PerformAnalysis` | Integrates `SentimentAnalysis` and `Graph` across all five products |

Each Apple Watch generation is represented as its own `SentimentAnalysis` object, mirroring how each product was represented as a `ScrapingManager` object in Project 2.

## Prerequisites

- **Miniconda** — [installation guide](https://docs.anaconda.com/miniconda/miniconda-install/)
- **Python** — [installation guide](https://realpython.com/installing-python/)

## Setup

**1. Clone this branch only.** Do not use `main` — it contains different software.

```bash
git clone -b reviewSentimentAnalysis https://github.com/JaceAckerman/Review-Sentiment-Analysis.git
cd Review-Sentiment-Analysis/Project3_AI_Reviewer
```

Only the `Project3_AI_Reviewer` folder is needed to run this software.

**2. Create the conda environment.**

From inside `Project3_AI_Reviewer`:

```bash
conda env create -f requirements.yaml
conda clean -p
```

Conda will automatically name the environment `project3Env`.

**3. Activate the environment.**

```bash
conda activate project3Env
```

You should see `(project3Env)` appear in your terminal prompt.

## Usage

The executable accepts two command-line arguments:

```bash
python executable.py scrape     # Scrapes reviews from eBay
python executable.py analyze    # Runs sentiment analysis and generates the graph
```

### Recommended First Run

For a safe first run, scrape before analyzing so review files are populated before sentiment analysis begins:

```bash
python executable.py scrape
python executable.py analyze
```

### Running From Scratch

If prompt and response files already exist, the software will skip re-analyzing and run much faster. To force a full re-analysis:

1. Delete all content from the response files: `series5Responses.txt`, `series6Responses.txt`, `series7Responses.txt`, `series8Responses.txt`, `series9Responses.txt`
2. Delete all content from the prompt files: `series5Prompt.txt`, `series6Prompt.txt`, `series7Prompt.txt`, `series8Prompt.txt`, `series9Prompt.txt`
3. Re-run both commands:

```bash
python executable.py scrape
python executable.py analyze
```

> **Note:** Analysis can take **8+ minutes** since Phi-3 must generate a response for every review. Please be patient — the graph will display automatically once analysis completes.

## Updating With New Reviews

To incorporate newly posted reviews:

1. Run `python executable.py scrape` to refresh review files with current data.
2. Delete the prompt and response files as described above.
3. Run `python executable.py analyze` to re-run sentiment analysis on the updated dataset.

## Output

Once analysis completes, a graph comparing sentiment (positive/negative/neutral) across Apple Watch Series 5–9 is generated and displayed automatically.
