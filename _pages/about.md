---
permalink: /
title: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
  /* Scoped, lightweight polish that plays nicely with academic-pages */
  .sl-hero {
    font-size: 1.05rem;
    line-height: 1.7;
    margin-bottom: 1.5em;
  }
  .sl-hero p { margin-bottom: 0.9em; }
  .sl-hero strong { color: #2a2a2a; }

  .sl-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45em;
    margin: 0.4em 0 1.6em;
    padding: 0;
    list-style: none;
  }
  .sl-tags li {
    background: #eef3fb;
    color: #1f4a8a;
    padding: 0.25em 0.75em;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 500;
    border: 1px solid #d9e3f3;
  }

  .sl-section-title {
    font-size: 1.15rem;
    margin: 1.6em 0 0.6em;
    padding-bottom: 0.3em;
    border-bottom: 2px solid #eaeaea;
    letter-spacing: 0.01em;
  }

  .sl-cards {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.9em;
    margin: 0.4em 0 1em;
  }
  @media (min-width: 700px) {
    .sl-cards { grid-template-columns: 1fr 1fr; }
  }
  .sl-card {
    border: 1px solid #e6e6e6;
    border-left: 4px solid #1f4a8a;
    border-radius: 6px;
    padding: 0.9em 1.1em;
    background: #fafbfd;
  }
  .sl-card h4 {
    margin: 0 0 0.15em;
    font-size: 1rem;
    line-height: 1.35;
  }
  .sl-card .sl-meta {
    color: #666;
    font-size: 0.85rem;
    margin-bottom: 0.4em;
  }
  .sl-card p { margin: 0; font-size: 0.92rem; line-height: 1.55; }

  .sl-news {
    list-style: none;
    padding: 0;
    margin: 0.4em 0 0.4em;
    border-left: 2px solid #e6e6e6;
  }
  .sl-news li {
    position: relative;
    padding: 0.35em 0 0.35em 1.1em;
    font-size: 0.95rem;
    line-height: 1.55;
  }
  .sl-news li::before {
    content: "";
    position: absolute;
    left: -6px;
    top: 0.85em;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #1f4a8a;
    border: 2px solid #fff;
  }
  .sl-news .sl-date {
    display: inline-block;
    min-width: 6.5em;
    color: #1f4a8a;
    font-weight: 600;
    font-variant-numeric: tabular-nums;
    margin-right: 0.4em;
  }

  .sl-callout {
    border-left: 4px solid #1f4a8a;
    background: #f5f8fd;
    padding: 0.9em 1.1em;
    border-radius: 0 6px 6px 0;
    margin: 1em 0 1.4em;
    font-size: 0.97rem;
  }

  .sl-contact {
    margin-top: 1em;
    font-size: 0.95rem;
    line-height: 1.7;
  }
  .sl-contact a { white-space: nowrap; }
</style>

<div class="sl-hero">
  <p>
    Hi, I'm <strong>Hsin-Yuan (Samuel) Lee</strong>, a senior at UC San Diego finishing a double major in
    <strong>Data Science</strong> and <strong>Cognitive Science</strong> (Machine Learning
    and Neural Computation), and an incoming
    <strong>M.S. in Computer Science</strong> student at <strong>UCLA</strong> this Fall.
    I work at the intersection of machine learning and cognitive science, building models
    that are both competitive <em>and</em> biologically interpretable.
  </p>
  <p>
    My research sits between <strong>multimodal learning</strong>,
    <strong>neurocomputational vision</strong>, and <strong>LLM-based scientific
    reasoning</strong>. I'm especially drawn to questions like: can we build vision systems
    that see the way humans do, and can multi-agent LLMs actually generate novel scientific
    hypotheses?
  </p>
</div>

<div class="sl-callout">
  <strong>Looking ahead.</strong> This Fall I'm heading to <strong>UCLA</strong> for an
  <strong>M.S. in Computer Science</strong>.
</div>

<h3 class="sl-section-title">Research interests</h3>
<ul class="sl-tags">
  <li>Multimodal Learning</li>
  <li>Neurocomputational Vision</li>
  <li>LLM-based Scientific Reasoning</li>
  <li>Representation Learning</li>
  <li>Human-aligned AI</li>
  <li>Embodied Agents</li>
</ul>

<h3 class="sl-section-title">Current roles</h3>
<div class="sl-cards">
  <div class="sl-card">
    <h4>Undergraduate Researcher</h4>
    <div class="sl-meta">Gary's Unbelievable Research Unit (GURU) · Prof. Garrison Cottrell · Aug 2025 – Present</div>
    <p>Building a neurocomputational vision model with fixation-based sampling and
    log-polar transforms to study the Face Inversion Effect as a window into configural
    vs. featural processing.</p>
  </div>
  <div class="sl-card">
    <h4>R&amp;D Intern</h4>
    <div class="sl-meta">Qualcomm Institute (Calit2) · Dr. Neil Smith · Aug 2025 – Present</div>
    <p>Designing a modular LLM–TTS–Animation pipeline (FastAPI + Kubernetes) that drives
    real-time 3D avatars in Unreal Engine 5 — cut response latency ~25%.</p>
  </div>
</div>

<!-- <h3 class="sl-section-title">Recent news</h3>
<ul class="sl-news">
  <li><span class="sl-date">Apr 2026</span>Committed to <strong>UCLA</strong> for an <strong>M.S. in Computer Science</strong>, starting Fall 2026.</li>
  <li><span class="sl-date">Feb 2026</span>Submitted <em>A Mechanistic Explanation for the Inverted Face Effect</em> to CogSci 2026.</li>
  <li><span class="sl-date">Jan 2026</span>Submitted <em>HypoEvolve: When Genetic Algorithms Meet Multi-Agent LLMs for Scientific Hypothesis Discovery</em> to ICML 2026.</li>
  <li><span class="sl-date">Aug 2025</span>Joined <strong>GURU</strong> (Cottrell Lab) and <strong>Qualcomm Institute / Calit2</strong> (Smith Lab) as an undergraduate researcher.</li>
  <li><span class="sl-date">Jun 2025</span>Our team finished <strong>2nd / 83</strong> in the Deep Climate Learning competition — 46% RMSE reduction vs. baseline.</li>
  <li><span class="sl-date">May 2025</span>Stepped up to <strong>Director of AI Competitions</strong> at ACM @ UCSD.</li>
</ul> -->

<h3 class="sl-section-title">Contact</h3>
<div class="sl-contact">
  Best way to reach me is by email at
  <a href="mailto:hsl023@ucsd.edu">hsl023@ucsd.edu</a>.
  You can also find me on
  <a href="https://github.com/samuellee77">GitHub</a> and
  <a href="https://www.linkedin.com/in/hsin-yuan-lee-b22653258">LinkedIn</a>
</div>
