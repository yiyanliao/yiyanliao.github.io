---
title: about
date: 2025-05-06 17:38:32
tags:
academia: true
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yiyan Liao - About</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Merriweather:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
    <style>
        /* --- General Page Styles --- */
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.7;
            background-color: #fcfcfc;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }

        /* --- Main Container --- */
        .about-container {
            width: 100%;
        }

        /* --- Header Section --- */
        .header-section {
            text-align: center;
            padding: 40px 20px;
            border-bottom: 2px solid #f0f0f0;
            margin-bottom: 40px;
        }

        .header-section h1 {
            font-size: 2.5em;
            font-weight: 700;
            margin: 0;
            color: #111;
        }

        .header-section .subtitle {
            font-size: 1.2em;
            color: #555;
            margin-top: 8px;
        }

        .header-section .affiliation {
            font-size: 1.1em;
            color: #555;
            margin-top: 4px;
        }

        .header-section .quote {
            font-family: 'Merriweather', serif;
            font-style: italic;
            font-size: 1.1em;
            color: #777;
            margin-top: 20px;
        }

        /* --- General Section Styling --- */
        .content-section {
            margin-bottom: 40px;
            background-color: #ffffff;
            border: 1px solid #eee;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        }

        .section-title {
            font-size: 1.8em;
            font-weight: 600;
            color: #000;
            border-bottom: 1px solid #e5e5e5;
            padding-bottom: 12px;
            margin-top: 0;
            margin-bottom: 25px;
        }

        ul {
            list-style-type: none;
            padding-left: 0;
        }

        li {
            margin-bottom: 15px;
            position: relative;
        }

        /* --- Section-Specific Styles --- */
        
        /* Education & Internships */
        .entry-item {
            display: flex;
            flex-direction: column;
        }
        
        .entry-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
        }

        .entry-title {
            font-size: 1.15em;
            font-weight: 600;
            color: #1a1a1a;
            margin: 0;
        }

        .entry-date {
            font-size: 0.95em;
            color: #666;
            font-weight: 500;
            flex-shrink: 0;
            margin-left: 15px;
            margin-top: 2px; /* Align with title */
        }
        
        .entry-subtitle {
            font-size: 1.05em;
            color: #555;
            margin: 4px 0 0 0;
        }
        
        .entry-link {
            font-size: 0.9em;
            color: #007bff;
            text-decoration: none;
            font-weight: 500;
        }
        
        .entry-link:hover {
            text-decoration: underline;
        }
        
        /* Academic Achievements */
        .achievement-item {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding-left: 25px; /* Space for icon */
        }
        
        .achievement-item::before {
            content: '🏅'; /* Default icon */
            position: absolute;
            left: 0;
            top: 2px;
            font-size: 1.1em;
        }
        
        .achievement-item.new::before {
            content: '🆕';
        }
        
        .achievement-item.research::before {
            content: '🔬';
        }

        .achievement-item.award::before {
            content: '🏆';
        }
        
        .achievement-item.medal::before {
            content: '🥇';
        }

        .achievement-item p {
            margin: 0;
            padding-right: 15px;
        }
        
        .achievement-text {
            font-size: 1.05em;
            color: #333;
            font-weight: 500;
        }
        
        .achievement-details {
            font-size: 0.95em;
            color: #666;
        }

        .achievement-date {
            font-size: 0.95em;
            color: #666;
            font-weight: 500;
            text-align: right;
            flex-shrink: 0;
        }
        
        /* Research Interests */
        .interests-list > li {
            font-size: 1.1em;
            font-weight: 600;
            color: #222;
            padding-left: 25px;
        }
        
        .interests-list > li::before {
            content: '🔬';
            position: absolute;
            left: 0;
            top: 1px;
        }

        .interests-list ul {
            padding-left: 20px;
            margin-top: 8px;
        }
        
        .interests-list ul li {
            font-size: 1em;
            font-weight: 400;
            color: #555;
            list-style-type: disc;
            margin-bottom: 5px;
        }
        
        /* Talk Slides */
        .talk-item {
            padding-left: 25px;
        }

        .talk-item::before {
            content: '🎤';
            position: absolute;
            left: 0;
            top: 2px;
            font-size: 1.1em;
        }
        
        .talk-title {
            font-size: 1.05em;
            font-weight: 500;
            color: #333;
            margin: 0 0 5px 0;
        }
        
        .talk-link a {
            display: inline-block;
            padding: 4px 10px;
            border: 1px solid #007bff;
            color: #007bff;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
            text-decoration: none;
            transition: background-color 0.2s, color 0.2s;
        }

        .talk-link a:hover {
            background-color: #007bff;
            color: white;
        }
        
        /* About Me */
        .about-me-list li {
            font-size: 1.05em;
            color: #333;
            padding-left: 25px;
        }
        
        .about-me-list li::before {
            position: absolute;
            left: 0;
            top: 2px;
            font-size: 1.1em;
        }

        .about-me-list li:nth-child(1)::before { content: '👤'; }
        .about-me-list li:nth-child(2)::before { content: '🎧'; }

    </style>
</head>
<body>

    <div class="about-container">

        <header class="header-section">
            <h1>Yiyan Liao</h1>
            <p class="subtitle">Undergraduate Student · Bioinformatics</p>
            <p class="affiliation">School of Life Sciences, Peking University</p>
            <p class="quote">Be a rational poet.</p>
        </header>

        <section class="content-section">
            <h2 class="section-title">🧬 Education</h2>
            <ul>
                <li class="entry-item">
                    <div class="entry-header">
                        <p class="entry-title">Peking University, School of Life Sciences</p>
                        <span class="entry-date">2023 – Present</span>
                    </div>
                    <p class="entry-subtitle">B.E. in Bioinformatics</p>
                </li>
            </ul>
        </section>

        <section class="content-section">
            <h2 class="section-title">🏅 Academic Achievements</h2>
            <ul>
                <li class="achievement-item new">
                    <p>
                        <span class="achievement-text">2024-2025 Peking University Merit Student</span>
                    </p>
                    <span class="achievement-date">Sep 2025</span>
                </li>
                <li class="achievement-item new">
                    <p>
                        <span class="achievement-text">2024-2025 Peking University Qin Wanshun Jin Yunhui Scholarship</span>
                    </p>
                    <span class="achievement-date">Sep 2025</span>
                </li>
                <li class="achievement-item research">
                    <p>
                        <span class="achievement-text">2025 Beijing Natural Science Foundation Undergraduate Research Program</span><br>
                        <span class="achievement-details">Development and Validation of Deep Learning-Based Virtual Screening Methods for Molecular Glues</span>
                    </p>
                    <span class="achievement-date">Jul 2025</span>
                </li>
                <li class="achievement-item award">
                    <p>
                        <span class="achievement-text">33th Peking University "Challenge Cup" Interdisciplinary Student Extracurricular Academic Science and Technology Works Competition</span><br>
                        <span class="achievement-details">Excellence Award (Team Leader)</span>
                    </p>
                    <span class="achievement-date">May 2025</span>
                </li>
                <li class="achievement-item medal">
                    <p>
                        <span class="achievement-text">International Genetically Engineered Machine (iGEM) 2024</span><br>
                        <span class="achievement-details">Gold Medal – Team Peking (Wet Lab Leader)</span>
                    </p>
                    <span class="achievement-date">Oct 2024</span>
                </li>
                <li class="achievement-item award">
                    <p>
                        <span class="achievement-text">Peking University First Prize Scholarship for Freshmen</span><br>
                        <span class="achievement-details">MingDe Scholarship</span>
                    </p>
                    <span class="achievement-date">Dec 2023</span>
                </li>
                <li class="achievement-item medal">
                    <p>
                        <span class="achievement-text">34th International Biology Olympiad (IBO)</span><br>
                        <span class="achievement-details">Gold Medal</span>
                    </p>
                    <span class="achievement-date">Jul 2023</span>
                </li>
                <li class="achievement-item medal">
                    <p>
                        <span class="achievement-text">31st China National Biology Olympiad (CNBO)</span><br>
                        <span class="achievement-details">National Team Member</span>
                    </p>
                    <span class="achievement-date">Aug 2022</span>
                </li>
            </ul>
        </section>

        <section class="content-section">
            <h2 class="section-title">🔬 Research Interests</h2>
            <ul class="interests-list">
                <li>
                    Computer-Aided Drug Design (CADD)
                    <ul>
                        <li>Molecular Glues (MGs)</li>
                    </ul>
                </li>
                <li>
                    Large Language Models (LLMs)
                    <ul>
                        <li>Reinforcement Learning (RL)</li>
                    </ul>
                </li>
                <li>
                    Bioinformatics
                    <ul>
                        <li>Cancer Mutation Analysis</li>
                    </ul>
                </li>
            </ul>
        </section>

        <section class="content-section">
            <h2 class="section-title">💼 Internships</h2>
            <ul>
                <li class="entry-item">
                    <div class="entry-header">
                        <p class="entry-title">Tencent</p>
                        <span class="entry-date">Jun 2025 - Present</span>
                    </div>
                    <p class="entry-subtitle">Biological Large Language Models (LLMs)</p>
                </li>
                <li class="entry-item">
                    <div class="entry-header">
                        <p class="entry-title">Moonshot AI</p>
                        <span class="entry-date">Feb 2025 – Jun 2025</span>
                    </div>
                    <p class="entry-subtitle">Reinforcement Learning Intern</p>
                    <a href="https://www.moonshot.cn" target="_blank" rel="noopener noreferrer" class="entry-link">moonshot.cn</a>
                </li>
            </ul>
        </section>

        <section class="content-section">
            <h2 class="section-title">🎤 Talk Slides</h2>
            <ul>
                <li class="talk-item">
                    <p class="talk-title">UHPB Annual Symposium 2025: The computational landscape of molecular glues: MGTbind database and ternary co-folding benchmark</p>
                    <div class="talk-link">
                        <a href="https://disk.pku.edu.cn/link/AA292A2C4F226148A082E4F5AB790FDDC3" target="_blank" rel="noopener noreferrer">PowerPoint</a>
                    </div>
                </li>
                <li class="talk-item">
                    <p class="talk-title">UHPB JC 2025 Autumn: Toward <i>De Novo</i> Protein Design from Natural Language</p>
                    <div class="talk-link">
                        <a href="https://disk.pku.edu.cn/link/AA6EFCEAA4ADB049C9A88A2D9B66949E35" target="_blank" rel="noopener noreferrer">PowerPoint</a>
                    </div>
                </li>
            </ul>
        </section>

        <section class="content-section">
            <h2 class="section-title">💡 About Me</h2>
            <ul class="about-me-list">
                <li><strong>MBTI</strong>: ISTP (Introverted, Sensing, Thinking, Perceiving)</li>
                <li><strong>Hobbies</strong>: Hip-hop, rock music, movies</li>
            </ul>
        </section>

    </div>

</body>
</html>