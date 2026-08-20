---
title: "HypoEvolve: Benchmarking LLM-Generated Biological Hypotheses"
excerpt: "Senior capstone project pairing a genetic algorithm with a multi-agent LLM loop to refine biological hypotheses for drug repurposing (DepMap CRISPR) and Type-2 Diabetes gene identification. Presented as a poster at the UCSD Halıcıoğlu Data Science Institute senior capstone showcase.<br/><img src='/images/hypoevolve_poster.png'>"
collection: portfolio
order: 0
---

## Overview

**HypoEvolve** is my senior capstone project (UCSD DSC 180A/B) and the project behind the
manuscript currently under review at NeurIPS 2026. It treats scientific hypothesis generation
as an **evolutionary optimization** problem: instead of a single-pass LLM prompt, a
population of candidate hypotheses is iteratively reviewed, selected, recombined, and
mutated by a multi-agent LLM loop.

> Presented as a poster at the **UCSD Halıcıoğlu Data Science Institute (HDSI) Senior
> Capstone Showcase**, Spring 2026.

Team: **Jefferson Chen, Samuel Lee** (advisors: Prof. Zhiting Hu, Dr. Zhen Wang, Jieyuan Liu).

## What the poster covers

- **Problem framing.** Single-pass LLM prompting produces one hypothesis with no systematic
  refinement — LLMs lack the *selection pressure* researchers use to keep strong ideas and
  revise weak ones.
- **Framework.** A genetic-algorithm cycle (review → selection → crossover → mutation)
  wrapped in a multi-agent loop: a **Generation Agent** proposes, a **Reflection Agent**
  critiques across a 5-stage review, an **Evolution Agent** produces offspring, and a
  **Supervisor Agent** tracks the best hypothesis across generations.
- **Fitness.** Each hypothesis is scored along three LLM-evaluated axes — **correctness
  (s_c)**, **novelty (s_n)**, and **quality (s_q)** — aggregated with learnable weights
  into a single fitness signal `f(h)`.
- **Tasks.** Two biological discovery tasks: **Drug Repurposing** validated against DepMap
  CRISPR dependency data, and **Type-2 Diabetes** associated-gene identification.

## Results

- **Drug Repurposing (31 cancer types).** HypoEvolve reaches an average DepMap score of
  **93.6%** vs. **56.3%** for vanilla single-pass prompting — a **+66%** relative
  improvement.
- **Head-to-head wins.** HypoEvolve wins **20 / 31** cancer types (65%) vs. vanilla's
  3 / 31 (10%), with 8 ties.
- **Quality tiers.** Excellent rate (fitness ≥ 0.9) jumps from **42% → 84%** between
  vanilla and HypoEvolve.
- **Learning curve.** Average best fitness climbs monotonically across generations
  (n = 34, μ ± σ), consistent with genuine selection pressure rather than noisy search.
- **T2D task.** HypoEvolve variants dominate the head-to-head ranking against LLM
  baselines and a random baseline on mean top-1 OT score.

## Key takeaways

- Evolutionary refinement yields **large, consistent gains** under *external* biological
  validation.
- Gains are achieved **without DepMap leakage** into the generation loop.
- The framework is **task-general** — it can be pointed at any discovery task where
  hypotheses can be LLM-scored along correctness / novelty / quality.

## Limitations & next steps

- Current fitness relies on LLM-based internal scoring; stronger calibration and human
  review are needed.
- Planned ablations: remove crossover, remove mutation, remove elitism to quantify each
  operator's contribution.
- Expand to additional biological research tasks beyond drug repurposing and T2D.

## Poster

![HypoEvolve capstone poster: genetic-algorithm and multi-agent LLM framework for biological hypothesis discovery, with DepMap and Type-2 Diabetes results](/images/hypoevolve_poster.png)

<embed src="/files/hypoevolve_capstone_poster.pdf" type="application/pdf" width="100%" height="800px">

[Download the poster (PDF)](/files/hypoevolve_capstone_poster.pdf)
