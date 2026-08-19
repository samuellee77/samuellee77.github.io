#!/usr/bin/env python3
"""Generate the project detail pages under projects/ from the write-ups in _portfolio/.

The site is plain static HTML with no build step at deploy time; this script is run by
hand whenever a write-up in _portfolio/ changes:

    python3 tools/build_projects.py

It converts each markdown source to a page that uses the shared assets/style.css,
rewrites image references to the optimised .webp variants, and wraps wide elements
(tables, plotly iframes) so they scroll inside their own box rather than the page body.
"""

import os
import re
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_portfolio")
OUT = os.path.join(ROOT, "projects")
SITE = "https://samuellee77.github.io"

# slug -> page metadata. `order` drives nothing at render time; it documents the
# ordering used on portfolio.html so the two stay easy to reconcile by eye.
PAGES = {
    "hypoevolve": dict(
        title="HypoEvolve: Benchmarking LLM-Generated Biological Hypotheses",
        short="HypoEvolve",
        desc="A genetic algorithm paired with a multi-agent LLM loop that refines biological "
             "hypotheses for drug repurposing and Type-2 Diabetes gene identification.",
        date="April 2026",
        tags=["LLM agents", "Evolutionary search", "Computational biology"],
        links=[("Poster (PDF)", "/files/hypoevolve_capstone_poster.pdf")],
    ),
    "weak2strong": dict(
        title="Weak-to-Strong: PGR Experiments on the MATH Dataset",
        short="Weak-to-Strong",
        desc="Weak-to-strong generalization in LLMs via in-context learning, measured with the "
             "Performance Gap Recovered metric on the MATH dataset.",
        date="2025",
        tags=["LLM", "Alignment"],
        links=[("Report (PDF)", "/files/weak2strong.pdf")],
    ),
    "azure-openai-chatbot": dict(
        title="Forum Bot & Chat Bot with Azure OpenAI",
        short="Azure OpenAI Bots",
        desc="A Discourse auto-reply bot and web chatbot built on a retrieval pipeline over "
             "Azure Blob Storage and Azure Search.",
        date="2023",
        tags=["RAG", "Azure", "LLM"],
        links=[("GitHub", "https://github.com/samuellee77/azure-openai-chat-forum-bot")],
    ),
    "block-blast": dict(
        title="Block Blast RL Agent with MCTS and Neural Network",
        short="Block Blast RL",
        desc="A reinforcement learning agent for Block Blast combining Monte Carlo Tree Search "
             "with a CNN policy-value model.",
        date="2025",
        tags=["Reinforcement learning", "MCTS"],
        links=[("Report (PDF)", "/files/block-blast.pdf")],
    ),
    "clickbait-classification": dict(
        title="Detecting Clickbait with RoBERTa",
        short="Clickbait Detection",
        desc="Clickbait detection with a fine-tuned RoBERTa model, compared against logistic "
             "regression and random forest TF-IDF baselines.",
        date="2025",
        tags=["NLP", "Transformers"],
        links=[("Report (PDF)", "/files/clickbait.pdf")],
    ),
    "tumor-segmentation": dict(
        title="Liver Tumor Detection with U-Net",
        short="Liver Tumor Detection",
        desc="A U-Net segmentation model for detecting liver tumors in CT scans, reaching 68% "
             "accuracy on the evaluation set.",
        date="2024",
        tags=["Medical imaging", "Segmentation"],
        links=[("Slides (PDF)", "/files/Tumor_Presentation_Final.pdf")],
    ),
    "league-analysis": dict(
        title="League of Legends Pro Game Analysis",
        short="LoL Pro Game Analysis",
        desc="An analysis of 2022 professional League of Legends match data on team side and "
             "champion picks and bans, with a fairness analysis of the resulting model.",
        date="2023",
        tags=["Data analysis", "Fairness"],
        links=[("GitHub", "https://github.com/samuellee77/league-of-legend-pro-game-analysis")],
    ),
    "comparison-classifiers": dict(
        title="Evaluating Classifier Performance Across Datasets and Partition Strategies",
        short="Classifier Comparison",
        desc="Random Forest, Logistic Regression, and SVM compared across three UCI datasets "
             "under varying train-test partitions.",
        date="2024",
        tags=["Classical ML", "Benchmarking"],
        links=[],
    ),
    "obesity-classification": dict(
        title="Classification of Obesity Levels using PCA and Random Forest",
        short="Obesity Classification",
        desc="Testing whether PCA dimensionality reduction improves a Random Forest classifier "
             "on UCI obesity-level data.",
        date="2024",
        tags=["Classical ML", "Dimensionality reduction"],
        links=[],
    ),
    "face-mask-detection": dict(
        title="Face Mask Detection",
        short="Face Mask Detection",
        desc="A CNN plus Haar-cascade face detection pipeline that flags whether a person is "
             "wearing a mask, served through Streamlit.",
        date="2022",
        tags=["Computer vision", "OpenCV"],
        links=[],
    ),
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_esc} — Hsin-Yuan (Samuel) Lee</title>
<meta name="description" content="{desc_esc}">
<link rel="canonical" href="{site}/projects/{slug}.html">

<meta property="og:type" content="article">
<meta property="og:site_name" content="Hsin-Yuan (Samuel) Lee">
<meta property="og:title" content="{title_esc}">
<meta property="og:description" content="{desc_esc}">
<meta property="og:url" content="{site}/projects/{slug}.html">
<meta property="og:image" content="{site}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title_esc}">
<meta name="twitter:description" content="{desc_esc}">
<meta name="twitter:image" content="{site}/assets/og-image.png">

<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta name="theme-color" content="#fbf8f4" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#181612" media="(prefers-color-scheme: dark)">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,600&family=Work+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>

<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <a class="site-header__name" href="/">Samuel Lee</a>
  <nav class="site-nav" aria-label="Main">
    <a href="/">About</a>
    <a href="/portfolio.html" aria-current="page">Portfolio</a>
    <a href="/publications.html">Publications</a>
    <a href="/cv.html">CV</a>
  </nav>
</header>

<main id="main">
  <div class="wrap wrap--narrow" style="padding-top:56px; padding-bottom:80px;">

    <a class="back-link" href="/portfolio.html">&larr; All projects</a>

    <p class="eyebrow">{date}</p>
    <h1 class="page-title">{title_esc}</h1>
    <p class="lede" style="margin-bottom:24px;">{desc_esc}</p>

    <ul class="meta-row">{tags_html}</ul>
{links_html}
    <article class="prose">
{body}
    </article>

  </div>
</main>

<footer class="site-footer wrap--narrow">
  <div>© 2026 Hsin-Yuan (Samuel) Lee</div>
  <div class="site-footer__links">
    <a href="/portfolio.html">Portfolio</a>
    <a href="https://github.com/samuellee77">GitHub</a>
  </div>
</footer>

</body>
</html>
"""


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def strip_frontmatter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def rewrite_assets(html):
    """Point image tags at the optimised .webp files and make them lazy."""
    def sub_img(m):
        src = m.group(1)
        webp = re.sub(r"\.png$", ".webp", src)
        if os.path.exists(os.path.join(ROOT, webp.lstrip("/"))):
            src = webp
        return f'src="{src}"'

    # The sources were written for a Jekyll layout nested two levels deep; from
    # /projects/*.html those relative paths no longer resolve. Make them root-relative.
    html = html.replace('src="../../files/', 'src="/files/')
    html = html.replace('href="../../files/', 'href="/files/')

    html = re.sub(r'src="([^"]+\.png)"', sub_img, html)
    html = html.replace("<img ", '<img loading="lazy" decoding="async" ')
    # Plotly figures are exported as standalone HTML documents and embedded as iframes.
    html = html.replace("<iframe", '<iframe loading="lazy" class="figure-frame"')
    return html


def rewrite_pdf_embeds(html):
    """Replace bare <embed> tags with a responsive object plus a real download link.

    <embed> for PDFs silently renders nothing on iOS Safari and on any browser with a
    PDF viewer disabled, so every embed needs a visible fallback link underneath it.
    """
    def sub(m):
        src = m.group(1)
        name = src.rsplit("/", 1)[-1]
        return (
            '<figure class="pdf-figure">\n'
            f'  <object class="pdf-embed" data="{src}" type="application/pdf">\n'
            f'    <p class="pdf-embed__fallback">This browser cannot display the embedded PDF. '
            f'<a href="{src}">Download {esc(name)}</a> instead.</p>\n'
            "  </object>\n"
            f'  <figcaption><a href="{src}">Open the full PDF &rarr;</a></figcaption>\n'
            "</figure>"
        )

    html = re.sub(r'<embed\s+src="([^"]+\.pdf)"[^>]*>', sub, html)
    # markdown wraps the standalone embed in a paragraph; unwrap so the figure is valid.
    html = re.sub(r"<p>(<figure class=\"pdf-figure\">.*?</figure>)</p>", r"\1", html, flags=re.S)
    return html


def demote_leading_labels(html):
    """Turn front-matter-style h4 labels into paragraphs.

    A couple of the sources open with lines like `#### **Authors**: ...` and
    `#### GitHub Link: ...`, using a heading purely for bold styling. Rendered as
    real h4s they sit directly under the page h1 and skip two levels, so any
    h4 appearing before the first real section heading becomes a paragraph.
    """
    first_section = min(
        (i for i in (html.find("<h2"), html.find("<h3")) if i != -1),
        default=len(html),
    )
    head, tail = html[:first_section], html[first_section:]
    head = re.sub(r"<h4[^>]*>(.*?)</h4>", r'<p class="entry__sub">\1</p>', head, flags=re.S)
    return head + tail


def wrap_wide(html):
    """Tables and iframes must scroll inside their own container, not the page body."""
    html = re.sub(r"(<table>.*?</table>)", r'<div class="scroll-x">\1</div>',
                  html, flags=re.S)
    return html


def build():
    os.makedirs(OUT, exist_ok=True)
    md = markdown.Markdown(extensions=["extra", "sane_lists", "toc"])
    written = []
    for slug, meta in PAGES.items():
        path = os.path.join(SRC, slug + ".md")
        if not os.path.exists(path):
            print("  ! missing source:", path)
            continue
        raw = strip_frontmatter(open(path, encoding="utf-8").read())
        md.reset()
        body = md.convert(raw)
        body = wrap_wide(demote_leading_labels(rewrite_pdf_embeds(rewrite_assets(body))))
        body = "\n".join("      " + ln for ln in body.splitlines())

        tags_html = "".join(f'<li class="tag">{esc(t)}</li>' for t in meta["tags"])
        links = meta["links"]
        links_html = ""
        if links:
            items = "".join(f'<a class="pill" href="{u}">{esc(t)}</a>' for t, u in links)
            links_html = f'    <div class="pub__links" style="margin:0 0 36px;">{items}</div>\n'

        html = TEMPLATE.format(
            site=SITE, slug=slug, date=esc(meta["date"]),
            title_esc=esc(meta["title"]), desc_esc=esc(meta["desc"]),
            tags_html=tags_html, links_html=links_html, body=body,
        )
        dst = os.path.join(OUT, slug + ".html")
        with open(dst, "w", encoding="utf-8") as f:
            f.write(html)
        written.append(dst)
        print(f"  wrote projects/{slug}.html  ({len(html)//1024} KB)")
    return written


if __name__ == "__main__":
    print("Building project pages from _portfolio/ ...")
    files = build()
    print(f"Done — {len(files)} pages.")
