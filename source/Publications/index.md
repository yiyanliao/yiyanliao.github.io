---
title: Publications
date: 2025-05-06 17:36:01
---

<style>
  /* --- Global Styles & Resets --- */
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    line-height: 1.6;
  }

  /* --- Publication Section Title --- */
  .section-title {
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 10px;
    margin-top: 40px;
    margin-bottom: 30px;
  }

  /* --- Publication Entry Card --- */
  .publication-entry {
    display: flex; /* Use Flexbox for layout */
    align-items: flex-start; /* Align items to the top */
    margin-bottom: 40px; /* Space between entries */
    padding: 20px;
    border-radius: 12px;
    background-color: #fdfdfd;
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
    border: 1px solid #eee;
  }

  .publication-entry:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
  }

  /* --- Image Container --- */
  .publication-image-container {
    flex: 0 0 30%; /* Set width to 30% of the container */
    margin-right: 30px; /* Space between image and text */
  }

  .publication-image {
    width: 100%;
    border-radius: 8px;
    border: 1px solid #f0f0f0;
  }

  /* --- Details Container --- */
  .publication-details {
    flex: 1; /* Take up remaining space */
  }

  .publication-details a {
    text-decoration: none;
    color: #0056b3;
  }

  .publication-details a:hover {
    text-decoration: underline;
  }

  .publication-title {
    font-size: 1.25em;
    font-weight: 600;
    margin-top: 0;
    margin-bottom: 0.5em;
  }

  .publication-authors {
    font-size: 0.95em;
    color: #555;
    margin-block-start: 0.5em;
    margin-block-end: 0.5em;
  }
  
  .publication-venue {
    font-style: italic;
    color: #333;
    margin-bottom: 1em;
  }
  
  .publication-links a {
    display: inline-block;
    padding: 5px 12px;
    border: 1px solid #007bff;
    color: #007bff;
    border-radius: 20px;
    font-size: 0.9em;
    font-weight: bold;
    transition: background-color 0.2s, color 0.2s;
  }

  .publication-links a:hover {
    background-color: #007bff;
    color: white;
    text-decoration: none;
  }

  /* --- Author Toggle Styles --- */
  .toggle-authors {
    cursor: pointer;
    color: #007bff;
    font-weight: bold;
    margin-left: 4px;
  }
  
  .toggle-authors:hover {
    text-decoration: underline;
  }

</style>

<h3 class="section-title">Computer-Aided Drug Design (CADD)</h3>

<div class="publication-entry">
  <div class="publication-image-container">
    <img src="https://raw.githubusercontent.com/yiyanliao/yiyanliao.github.io/main/themes/Academia/source/img/MGTbind_TOC.png" alt="MGTbind: a comprehensive database of molecular glue ternary interactome" class="publication-image">
  </div>
  <div class="publication-details">
    <a href="https://doi.org/10.1093/nar/gkaf1075">
      <h4 class="publication-title">MGTbind: a comprehensive database of molecular glue ternary interactome</h4>
    </a>
    <p class="publication-authors">
      <span class="author-toggle-container">
        <span class="authors-short">Jintao Zhu<sup>†</sup>, <strong>Yiyan Liao</strong><sup>†</sup>, Haoyu Lin<sup>†</sup>, ..., Luhua Lai<sup>*</sup>, Jianfeng Pei<sup>*</sup></span>
        <span class="authors-full" style="display: none;">Jintao Zhu<sup>†</sup>, <strong>Yiyan Liao</strong><sup>†</sup>, Haoyu Lin<sup>†</sup>, Juan Xie, Zhichao Deng, Jinyu Han, Zhen Zhang, Jinchuan Xiao, Zhiyao Wang, Shuaipeng Zhang, Luhua Lai<sup>*</sup>, Jianfeng Pei<sup>*</sup></span>
        <span class="toggle-authors">[Show All]</span>
      </span>
    </p>
    <p class="publication-venue">Nucleic Acids Research, 2025</p>
    <div class="publication-links">
      <a href="https://doi.org/10.1093/nar/gkaf1075">Paper</a>
    </div>
  </div>
</div>

<div class="publication-entry">
  <div class="publication-image-container">
    <img src="https://raw.githubusercontent.com/yiyanliao/yiyanliao.github.io/main/themes/Academia/source/img/MGBench.png" alt="Benchmarking Cofolding Methods for Molecular Glue Ternary Structure Prediction" class="publication-image">
  </div>
  <div class="publication-details">
    <a href="https://doi.org/10.1021/acs.jcim.5c01860">
      <h4 class="publication-title">Benchmarking Cofolding Methods for Molecular Glue Ternary Structure Prediction</h4>
    </a>
    <p class="publication-authors">
      <strong>Yiyan Liao</strong><sup>†</sup>, Jintao Zhu<sup>†*</sup>, Juan Xie, Luhua Lai<sup>*</sup>, Jianfeng Pei<sup>*</sup>
    </p>
    <p class="publication-venue">Journal of Chemical Information and Modeling, 2025</p>
    <div class="publication-links">
      <a href="https://doi.org/10.1021/acs.jcim.5c01860">Paper</a>
    </div>
  </div>
</div>

<h3 class="section-title">Large Language Models (LLMs)</h3>

<div class="publication-entry">
  <div class="publication-image-container">
    <img src="https://raw.githubusercontent.com/yiyanliao/yiyanliao.github.io/main/themes/Academia/source/img/ScholarSearch.png" alt="ScholarSearch: Benchmarking Scholar" class="publication-image">
  </div>
  <div class="publication-details">
    <a href="https://arxiv.org/abs/2506.13784">
      <h4 class="publication-title">ScholarSearch: Benchmarking Scholar Searching Ability of LLMs</h4>
    </a>
    <p class="publication-authors">
      <span class="author-toggle-container">
        <span class="authors-short">Junting Zhou<sup>†</sup>, Wang Li<sup>†</sup>, <strong>Yiyan Liao</strong><sup>†</sup>, ..., Yuhan Wu<sup>*</sup>, Tong Yang<sup>*</sup></span>
        <span class="authors-full" style="display: none;">Junting Zhou<sup>†</sup>, Wang Li<sup>†</sup>, <strong>Yiyan Liao</strong><sup>†</sup>, Nengyuan Zhang, Tingjia Miao, Zhihui Qi, Yuhan Wu<sup>*</sup>, Tong Yang<sup>*</sup></span>
        <span class="toggle-authors">[Show All]</span>
      </span>
    </p>
    <p class="publication-venue">arXiv, 2025</p>
    <div class="publication-links">
      <a href="https://arxiv.org/abs/2506.13784">Paper</a>
    </div>
  </div>
</div>

<div class="publication-entry">
  <div class="publication-image-container">
    <img src="https://raw.githubusercontent.com/yiyanliao/yiyanliao.github.io/main/themes/Academia/source/img/SciDA.png" alt="SciDA: Scientific Dynamic Assessor" class="publication-image">
  </div>
  <div class="publication-details">
    <a href="https://arxiv.org/abs/2506.12909">
      <h4 class="publication-title">SciDA: Scientific Dynamic Assessor of LLMs</h4>
    </a>
    <p class="publication-authors">
      <span class="author-toggle-container">
        <span class="authors-short">Junting Zhou<sup>†</sup>, Tingjia Miao<sup>†</sup>, <strong>Yiyan Liao</strong>, ..., Yitao Liang<sup>*</sup>, Tong Yang<sup>*</sup>, Wenhao Huang<sup>*</sup>, Ge Zhang<sup>*</sup></span>
        <span class="authors-full" style="display: none;">Junting Zhou<sup>†</sup>, Tingjia Miao<sup>†</sup>, <strong>Yiyan Liao</strong>, Qichao Wang, Zhoufutu Wen, Yanqin Wang, Yunjie Huang, Ge Yan, Leqi Wang, Yucheng Xia, Hongwan Gao, Yuansong Zeng, Renjie Zheng, Chen Dun, Yitao Liang<sup>*</sup>, Tong Yang<sup>*</sup>, Wenhao Huang<sup>*</sup>, Ge Zhang<sup>*</sup></span>
        <span class="toggle-authors">[Show All]</span>
      </span>
    </p>
    <p class="publication-venue">arXiv, 2025</p>
    <div class="publication-links">
      <a href="https://arxiv.org/abs/2506.12909">Paper</a>
    </div>
  </div>
</div>

<div class="publication-entry">
  <div class="publication-image-container">
    <img src="https://raw.githubusercontent.com/yiyanliao/yiyanliao.github.io/main/themes/Academia/source/img/supergpqa.png" alt="SuperGPQA: Scaling LLM Evaluation" class="publication-image">
  </div>
  <div class="publication-details">
    <a href="https://arxiv.org/abs/2502.14739">
      <h4 class="publication-title">SuperGPQA: Scaling LLM Evaluation across 285 Graduate Disciplines</h4>
    </a>
    <p class="publication-authors">
      <span class="author-toggle-container">
        <span class="authors-short">M-A-P Team, Xinrun Du, Yifan Yao, Kaijing Ma, ..., <strong>Yiyan Liao</strong>, ..., Jiaheng Liu<sup>*</sup>, Qunshu Lin<sup>*</sup>, Wenhao Huang<sup>*</sup>, Ge Zhang<sup>*</sup></span>
        <span class="authors-full" style="display: none;">M-A-P Team, Xinrun Du, Yifan Yao, Kaijing Ma, Bingli Wang, Tianyu Zheng, King Zhu, Minghao Liu, Yiming Liang, Xiaolong Jin, Zhenlin Wei, Chujie Zheng, Kaixin Deng, Shawn Gavin, Shian Jia, Sichao Jiang, <strong>Yiyan Liao</strong>, Rui Li, Qinrui Li, Sirun Li, Yizhi Li, Yunwen Li, David Ma, Yuansheng Ni, Haoran Que, Qiyao Wang, Zhoufutu Wen, Siwei Wu, Tyshawn Hsing, Ming Xu, Zhenzhu Yang, Zekun Moore Wang, Junting Zhou, Yuelin Bai, Xingyuan Bu, Chenglin Cai, Liang Chen, Yifan Chen, Chengtuo Cheng, Tianhao Cheng, Keyi Ding, Siming Huang, Yun Huang, Yaoru Li, Yizhe Li, Zhaoqun Li, Tianhao Liang, Chengdong Lin, Hongquan Lin, Yinghao Ma, Tianyang Pang, Zhongyuan Peng, Zifan Peng, Qige Qi, Shi Qiu, Xingwei Qu, Shanghaoran Quan, Yizhou Tan, Zili Wang, Chenqing Wang, Hao Wang, Yiya Wang, Yubo Wang, Jiajun Xu, Kexin Yang, Ruibin Yuan, Yuanhao Yue, Tianyang Zhan, Chun Zhang, Jinyang Zhang, Xiyue Zhang, Xingjian Zhang, Yue Zhang, Yongchi Zhao, Xiangyu Zheng, Chenghua Zhong, Yang Gao, Zhoujun Li, Dayiheng Liu, Qian Liu, Tianyu Liu, Shiwen Ni, Junran Peng, Yujia Qin, Wenbo Su, Guoyin Wang, Shi Wang, Jian Yang, Min Yang, Meng Cao, Xiang Yue, Zhaoxiang Zhang, Wangchunshu Zhou, Jiaheng Liu<sup>*</sup>, Qunshu Lin<sup>*</sup>, Wenhao Huang<sup>*</sup>, Ge Zhang<sup>*</sup></span>
        <span class="toggle-authors">[Show All]</span>
      </span>
    </p>
    <p class="publication-venue">NeurIPS, 2025</p>
    <div class="publication-links">
      <a href="https://arxiv.org/abs/2502.14739">Paper</a>
    </div>
  </div>
</div>

<script>
  // Add a single event listener to the document body.
  // This will catch clicks on any element, including ones added later.
  document.body.addEventListener('click', function(event) {

    // Check if the element that was clicked is a toggle button.
    if (event.target.matches('.toggle-authors')) {
      const button = event.target;
      const container = button.closest('.author-toggle-container');
      const shortList = container.querySelector('.authors-short');
      const fullList = container.querySelector('.authors-full');
    
      // If either list is not found, do nothing.
      if (!shortList || !fullList) {
        return;
      }
    
      // Check the current state.
      const isExpanded = fullList.style.display === 'inline';
    
      if (isExpanded) {
        // Collapse the list
        fullList.style.display = 'none';
        shortList.style.display = 'inline';
        button.innerText = '[Show All]';
      } else {
        // Expand the list
        shortList.style.display = 'none';
        fullList.style.display = 'inline';
        button.innerText = '[Collapse]';
      }
    }
  });
</script>