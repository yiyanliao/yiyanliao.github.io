---
title: about
date: 2025-05-06 17:38:32
tags:
academia: true
---

## Recent News
- [Jun 2026] Our paper [Molexar: A Unified Multimodal Molecular Foundation Model for Drug Design](https://arxiv.org/abs/2606.25865) is now on arXiv!
- [Apr 2026] I was awarded a 2026 [Caltech Summer Undergraduate Research Fellowships (SURF)](https://sfp.caltech.edu/undergraduate-research/programs/surf) award, hosted by [Prof. Anima Anandkumar](https://www.linkedin.com/in/anima-anandkumar/)! See you in Pasadena!

## Research Interests
- Computer-aided molecular glue (MG) discovery
- CLLM-based & structure-based generative drug design
- Structural geometry deep learning & modeling
- Reasoning & foundation biological large language models (LLMs)

## Selected Papers

<div class="pub">
  <div class="pub-thumb"><img src="https://raw.githubusercontent.com/yiyanliao/yiyanliao.github.io/main/themes/Academia/source/img/molexar_architecture.png" alt="Molexar"></div>
  <div class="pub-body">
    <a class="pub-title" href="https://arxiv.org/abs/2606.25865" target="_blank">Molexar: A Unified Multimodal Molecular Foundation Model for Drug Design</a>
    <p class="pub-authors">Haoyu Lin<sup>†</sup>, <strong>Yiyan Liao</strong><sup>†</sup>, Jinmei Pan, Xinliao Ling, Luhua Lai<sup>*</sup>, Jianfeng Pei<sup>*</sup></p>
    <p class="pub-venue">arXiv, 2026</p>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2606.25865" target="_blank">Paper</a>
      <a href="https://raw.githubusercontent.com/yiyanliao/yiyanliao.github.io/main/themes/Academia/source/pdf/Molexar.pdf" target="_blank">PDF</a>
    </div>
  </div>
</div>

<div class="pub">
  <div class="pub-thumb"><img src="https://raw.githubusercontent.com/yiyanliao/yiyanliao.github.io/main/themes/Academia/source/img/MGTbind_TOC.png" alt="MGTbind"></div>
  <div class="pub-body">
    <a class="pub-title" href="https://doi.org/10.1093/nar/gkaf1075" target="_blank">MGTbind: a comprehensive database of molecular glue ternary interactome</a>
    <p class="pub-authors author-toggle-container">
      <span class="authors-short">Jintao Zhu<sup>†</sup>, <strong>Yiyan Liao</strong><sup>†</sup>, Haoyu Lin<sup>†</sup>, ..., Luhua Lai<sup>*</sup>, Jianfeng Pei<sup>*</sup></span>
      <span class="authors-full" style="display: none;">Jintao Zhu<sup>†</sup>, <strong>Yiyan Liao</strong><sup>†</sup>, Haoyu Lin<sup>†</sup>, Juan Xie, Zhichao Deng, Jinyu Han, Zhen Zhang, Jinchuan Xiao, Zhiyao Wang, Shuaipeng Zhang, Luhua Lai<sup>*</sup>, Jianfeng Pei<sup>*</sup></span>
      <span class="toggle-authors">[Show All]</span>
    </p>
    <p class="pub-venue">Nucleic Acids Research, 2025</p>
    <div class="pub-links">
      <a href="https://doi.org/10.1093/nar/gkaf1075" target="_blank">Paper</a>
      <a href="https://raw.githubusercontent.com/yiyanliao/yiyanliao.github.io/main/themes/Academia/source/pdf/MGTbind.pdf" target="_blank">PDF</a>
    </div>
  </div>
</div>

<div class="pub">
  <div class="pub-thumb"><img src="https://raw.githubusercontent.com/yiyanliao/yiyanliao.github.io/main/themes/Academia/source/img/MGBench.png" alt="Benchmarking Cofolding"></div>
  <div class="pub-body">
    <a class="pub-title" href="https://doi.org/10.1021/acs.jcim.5c01860" target="_blank">Benchmarking Cofolding Methods for Molecular Glue Ternary Structure Prediction</a>
    <p class="pub-authors"><strong>Yiyan Liao</strong><sup>†</sup>, Jintao Zhu<sup>†*</sup>, Juan Xie, Luhua Lai<sup>*</sup>, Jianfeng Pei<sup>*</sup></p>
    <p class="pub-venue">Journal of Chemical Information and Modeling, 2025</p>
    <div class="pub-links">
      <a href="https://doi.org/10.1021/acs.jcim.5c01860" target="_blank">Paper</a>
      <a href="https://raw.githubusercontent.com/yiyanliao/yiyanliao.github.io/main/themes/Academia/source/pdf/benchmarking-cofolding-methods-for-molecular-glue-ternary-structure-prediction.pdf" target="_blank">PDF</a>
    </div>
  </div>
</div>

<p style="margin-top:1.4rem;"><a href="/Publications">See all publications →</a></p>

<script>
  document.body.addEventListener('click', function(event) {
    if (event.target.matches('.toggle-authors')) {
      const button = event.target;
      const container = button.closest('.author-toggle-container');
      const shortList = container.querySelector('.authors-short');
      const fullList = container.querySelector('.authors-full');
      if (!shortList || !fullList) { return; }
      const isExpanded = fullList.style.display === 'inline';
      if (isExpanded) {
        fullList.style.display = 'none';
        shortList.style.display = 'inline';
        button.innerText = '[Show All]';
      } else {
        shortList.style.display = 'none';
        fullList.style.display = 'inline';
        button.innerText = '[Collapse]';
      }
    }
  });
</script>

## Honors & Awards

### Research Grants & Fellowships
- **Caltech Summer Undergraduate Research Fellowship (SURF)**
  *Electronic Effect-Informed Generative De Novo Drug Design*, *Apr 2026*
- **Beijing Natural Science Foundation Undergraduate Research Program**
  *Development and Validation of Deep Learning-Based Virtual Screening Methods for Molecular Glues*, *Jul 2025*

### Competitions
- **Bohrium+SciMaster×OpenClaw 48-Hour AI for Science Hackathon**
  Second Prize — *GlueBind: A Deep Learning Framework for Large-Scale Molecular Glue Virtual Screening*, *Mar 2026*
- **33rd Peking University "Challenge Cup" Interdisciplinary Student Extracurricular Academic Science and Technology Works Competition**
  Excellence Award (Team Leader), *May 2025*
- **International Genetically Engineered Machine (iGEM) 2024**
  Gold Medal — Team Peking (Wet Lab Leader), *Oct 2024*
- **34th International Biology Olympiad (IBO)**
  Gold Medal (3rd globally), *Jul 2023*
- **31st China National Biology Olympiad (CNBO)**
  National Team Member, *Aug 2022*

### Scholarships & Honors
- **Outstanding Teaching Assistant Award**, School of Life Sciences, Peking University, *Jun 2026*
- **87 Excellent Research Project Scholarship**, School of Life Sciences, Peking University
  First Prize — *Computational Landscape and Structure Prediction of Molecular Glue Ternary Complexes*, *May 2026*
- **Peking University Merit Student** (2024–2025), *Sep 2025*
- **Qin Wanshun Jin Yunhui Scholarship** (2024–2025), *Sep 2025*
- **MingDe Scholarship** — First Prize Scholarship for Freshmen, *Dec 2023*

## Education
- **Peking University**, School of Life Sciences  
  *B.E. in Bioinformatics* (2023 – 2027 expected)

## Internships
- **Moonshot AI**  
  *Reinforcement Learning Intern*, Feb 2025 – Jun 2025  
  [moonshot](https://www.moonshot.cn)
- **Tencent**
  *Biological Large Language Models (LLMs) Intern*, Jun 2025 - Dec 2025
  [tencent](https://www.tencent.com/en-us/about.html)
  
## Miscellaneous
- **MBTI**: ISTP (Introverted, Sensing, Thinking, Perceiving)
- **Hobbies**: Hip-hop, rock music, movies
- **Biology Olympiad Open Access**: [Zip](https://disk.pku.edu.cn/link/AAA33D2B20BC6E4F479F26EFDE4ABBBD3C)
---


