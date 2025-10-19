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
    <title>About - Yiyan Liao</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Merriweather:ital,wght@0,400;1,700&display=swap" rel="stylesheet">
    
    <style>
        /* --- Basic Setup --- */
        :root {
            --primary-color: #333;
            --secondary-color: #555;
            --accent-color: #0056b3; /* A professional blue */
            --bg-color: #ffffff;
            --light-gray: #f4f4f4;
            --border-color: #ddd;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.7;
            background-color: var(--bg-color);
            color: var(--primary-color);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
        }

        .container {
            width: 100%;
            max-width: 960px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        /* --- Typography --- */
        h1, h2, h3 {
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            color: var(--primary-color);
            margin-top: 1.5em;
            margin-bottom: 0.8em;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 0.25rem;
            letter-spacing: -1px;
        }

        h2 {
            font-size: 1.75rem;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 8px;
            margin-top: 2.5rem;
        }
        
        h2::before {
            content: attr(data-icon) " ";
            font-size: 1.5rem;
            margin-right: 8px;
            vertical-align: middle;
        }

        p, li {
            font-size: 1rem;
            color: var(--secondary-color);
        }

        a {
            color: var(--accent-color);
            text-decoration: none;
            font-weight: 500;
            transition: all 0.2s ease;
        }

        a:hover {
            text-decoration: underline;
            opacity: 0.8;
        }
        
        strong {
            font-weight: 700;
            color: var(--primary-color);
        }

        /* --- Header / Hero Section --- */
        .header {
            text-align: left;
            margin-bottom: 3rem;
            padding-bottom: 2rem;
            border-bottom: 1px solid var(--border-color);
        }

        .header .subtitle {
            font-size: 1.25rem;
            font-weight: 400;
            color: var(--secondary-color);
            margin: 0;
        }

        .header .quote {
            font-family: 'Merriweather', serif;
            font-size: 1.2rem;
            font-style: italic;
            color: #777;
            margin-top: 1rem;
            border-left: 3px solid var(--accent-color);
            padding-left: 15px;
        }
        
        /* --- New Tag Style --- */
        .new-tag {
            background-color: #e6f7ff;
            color: #0056b3;
            border: 1px solid #b3d9ff;
            border-radius: 4px;
            padding: 2px 6px;
            font-size: 0.75rem;
            font-weight: 700;
            margin-right: 8px;
            vertical-align: middle;
            display: inline-block;
        }

        /* --- Main Content Layout (2-column) --- */
        .main-content {
            display: grid;
            grid-template-columns: 1fr;
            gap: 2rem 4rem;
        }

        @media (min-width: 768px) {
            .main-content {
                grid-template-columns: 3fr 1fr; /* Main content 3/4, sidebar 1/4 */
            }
            .sidebar {
                grid-row: 1 / span 2; /* Make sidebar span across all rows in its column */
                grid-column: 2;
            }
            .main-column {
                grid-column: 1;
                grid-row: 1;
            }
        }

        /* --- Section Styling --- */
        .section {
            margin-bottom: 2rem;
        }

        .section ul {
            list-style-type: none;
            padding-left: 0;
        }

        .section li {
            position: relative;
            padding-left: 1.5rem;
            margin-bottom: 1.25rem;
        }

        .section li::before {
            content: '•';
            position: absolute;
            left: 0;
            top: 0;
            color: var(--accent-color);
            font-weight: 700;
            font-size: 1.2rem;
            line-height: 1.7;
        }
        
        .list-item-title {
            display: block;
            font-weight: 700;
            font-size: 1.1rem;
            color: var(--primary-color);
            margin-bottom: 2px;
        }

        .list-item-meta {
            display: block;
            font-size: 0.9rem;
            color: #777;
            font-style: italic;
            margin-bottom: 4px;
        }
        
        .list-item-description {
            margin: 0;
            color: var(--secondary-color);
        }
        
        /* --- Specific Section: Education --- */
        #education li::before { content: '🎓'; left: -5px; }
        
        /* --- Specific Section: Achievements --- */
        #achievements li::before { content: '🏅'; left: -5px; }

        /* --- Specific Section: Internships --- */
        #internships li::before { content: '💼'; left: -5px; }
        
        /* --- Specific Section: Talks --- */
        #talks li::before { content: '🎤'; left: -5px; }
        #talks a {
            font-weight: 700;
        }

        /* --- Sidebar Sections --- */
        .sidebar .section {
            background-color: var(--light-gray);
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .sidebar h2 {
            border-bottom: none;
            font-size: 1.25rem;
            margin-top: 0;
            padding-bottom: 0;
        }
        
        .sidebar ul {
            padding-left: 1.25rem;
        }
        
        .sidebar li {
            padding-left: 0;
            margin-bottom: 0.5rem;
        }
        
        .sidebar li::before {
            position: static;
            font-size: 1rem;
            margin-right: 8px;
        }

        /* --- Footer --- */
        footer {
            text-align: center;
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid var(--border-color);
            font-size: 0.9rem;
            color: #999;
        }

    </style>
</head>
<body>

    <div class="container">
        
        <header class="header">
            <h1>Yiyan Liao</h1>
            <p class="subtitle">Undergraduate Student · Bioinformatics<br>School of Life Sciences, Peking University</p>
            <p class="quote">Be a rational poet.</p>
        </header>

        <div class="main-content">

            <main class="main-column">
                
                <section id="education" class="section">
                    <h2 data-icon="🧬">Education</h2>
                    <ul>
                        <li>
                            <span class="list-item-title">Peking University, School of Life Sciences</span>
                            <span class="list-item-meta">B.E. in Bioinformatics (2023 – Present)</span>
                        </li>
                    </ul>
                </section>

                <section id="achievements" class="section">
                    <h2 data-icon="🏅">Academic Achievements</h2>
                    <ul>
                        <li>
                            <span class="new-tag">🆕🎉</span>
                            <span class="list-item-title">2024-2025 Peking University Merit Student</span>
                            <span class="list-item-meta">Sep 2025</span>
                        </li>
                        <li>
                            <span class="new-tag">🆕🎉</span>
                            <span class="list-item-title">2024-2025 Peking University Qin Wanshun Jin Yunhui Scholarship</span>
                            <span class="list-item-meta">Sep 2025</span>
                        </li>
                        <li>
                            <span class="list-item-title">2025 Beijing Natural Science Foundation Undergraduate Research Program</span>
                            <span class="list-item-meta">Jul 2025</span>
                            <p class="list-item-description">Development and Validation of Deep Learning-Based Virtual Screening Methods for Molecular Glues</p>
                        </li>
                        <li>
                            <span class="list-item-title">33th Peking University "Challenge Cup" Interdisciplinary Student Extracurricular Academic Science and Technology Works Competition</span>
                            <span class="list-item-meta">Excellence Award (Team Leader), May 2025</span>
                        </li>
                        <li>
                            <span class="list-item-title">International Genetically Engineered Machine (iGEM) 2024</span>
                            <span class="list-item-meta">Gold Medal – Team Peking (Wet Lab Leader), Oct 2024</span>
                        </li>
                        <li>
                            <span class="list-item-title">Peking University First Prize Scholarship for Freshmen</span>
                            <span class="list-item-meta">MingDe Scholarship, Dec 2023</span>
                        </li>
                        <li>
                            <span class="list-item-title">34th International Biology Olympiad (IBO)</span>
                            <span class="list-item-meta">Gold Medal, Jul 2023</span>
                        </li>
                        <li>
                            <span class="list-item-title">31st China National Biology Olympiad (CNBO)</span>
                            <span class="list-item-meta">National Team Member, Aug 2022</span>
                        </li>
                    </ul>
                </section>

                <section id="internships" class="section">
                    <h2 data-icon="💼">Internships</h2>
                    <ul>
                        <li>
                            <span class="list-item-title">Tencent</span>
                            <span class="list-item-meta">Jun 2025 - Present</span>
                            <p class="list-item-description">Biological Large Language Models (LLMs)</p>
                        </li>
                        <li>
                            <span class="list-item-title">Moonshot AI</span>
                            <span class="list-item-meta">Reinforcement Learning Intern, Feb 2025 – Jun 2025</span>
                            <p class="list-item-description"><a href="https://www.moonshot.cn" target="_blank" rel="noopener noreferrer">moonshot.cn</a></p>
                        </li>
                    </ul>
                </section>
                
                <section id="talks" class="section">
                    <h2 data-icon="🎤">Talk Slides</h2>
                    <ul>
                        <li>
                            <span class="list-item-title">UHPB JC 2025 Autumn: Toward <em>De Novo</em> Protein Design from Natural Language</span>
                            <p class="list-item-description"><a href="https://disk.pku.edu.cn/link/AA6EFCEAA4ADB049C9A88A2D9B66949E35" target="_blank" rel="noopener noreferrer">[PowerPoint]</a></p>
                        </li>
                        <li>
                            <span class="list-item-title">UHPB Annual Symposium 2025: The computational landscape of molecular glues: MGTbind database and ternary co-folding benchmark</span>
                            <p class="list-item-description"><a href="https://disk.pku.edu.cn/link/AA292A2C4F226148A082E4F5AB790FDDC3" target="_blank" rel="noopener noreferrer">[PowerPoint]</a></p>
                        </li>
                    </ul>
                </section>

            </main>

            <aside class="sidebar">

                <section id="interests" class="section">
                    <h2 data-icon="🔬">Research Interests</h2>
                    <ul>
                        <li><strong>Computer-Aided Drug Design (CADD)</strong>
                            <ul><li>Molecular Glues (MGs)</li></ul>
                        </li>
                        <li><strong>Large Language Models (LLMs)</strong>
                            <ul><li>Reinforcement Learning (RL)</li></ul>
                        </li>
                        <li><strong>Bioinformatics</strong>
                            <ul><li>Cancer Mutation Analysis</li></ul>
                        </li>
                    </ul>
                </section>

                <section id="about-me" class="section">
                    <h2 data-icon="💡">About Me</h2>
                    <ul>
                        <li><strong>MBTI</strong>: ISTP</li>
                        <li><strong>Hobbies</strong>: Hip-hop, rock music, movies</li>
                    </ul>
                </section>

            </aside>

        </div> <footer>
            <p>&copy; 2025 Yiyan Liao. All rights reserved.</p>
        </footer>

    </div> </body>
</html>