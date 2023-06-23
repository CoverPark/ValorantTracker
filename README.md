# ValorantTracker
A simple Valorant tracker for discord

<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.5;
            margin: 20px;
            padding: 0;
        }

        h1 {
            color: #333;
            font-size: 24px;
            margin-bottom: 10px;
        }

        h2 {
            color: #555;
            font-size: 20px;
            margin-bottom: 10px;
        }

        p {
            color: #777;
        }

        code {
            background-color: #f4f4f4;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: Consolas, monospace;
            padding: 2px 6px;
        }

        pre {
            background-color: #f4f4f4;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: Consolas, monospace;
            padding: 10px;
            white-space: pre-wrap;
        }

        .command {
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: Consolas, monospace;
            padding: 10px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>Nom du Projet</h1>

    <p>Description du projet.</p>

    <h2>Prérequis</h2>

    <p>Avant de commencer, assurez-vous d'avoir les éléments suivants installés :</p>

    <ul>
        <li>Python (version 3.11)</li>
        <li>Docker (version 24.0) <em>(uniquement si vous utilisez Docker)</em></li>
    </ul>

    <h2>Installation</h2>

    <ol>
        <li>Clonez ce dépôt de code sur votre machine locale :</li>
    </ol>

    <pre><code>git clone https://github.com/CoverPark/ValorantTracker</code></pre>

    <ol start="2">
        <li>Accédez au répertoire du projet :</li>
    </ol>

    <pre><code>cd nom_du_depot</code></pre>

    <ol start="3">
        <li>Installez les dépendances :</li>
    </ol>

    <pre><code>pip install -r requirements.txt</code></pre>

    <ol start="4">
        <li><strong>Uniquement si vous utilisez Docker :</strong> Remplacez <code>token_bot_discord</code> par votre propre token bot Discord dans le fichier <code>config.py</code>.</li>
    </ol>

    <ol start="5">
        <li><strong>Uniquement si vous utilisez Docker :</strong> Construisez l'image Docker :</li>
    </ol>

    <pre class="command"><code>docker build -t image_name:1.0.0 .</code></pre>

    <h2>Utilisation</h2>

    <ul>
        <li><strong>Si vous utilisez Docker :</strong>
            <ul>
                <li>Exécutez l'image Docker :</li>
            </ul>
        </li>
    </ul>

    <pre class="command"><code>docker run -d image_name:1.0.0</code></pre>

    <ul>
        <li><strong>Si vous n'utilisez pas Docker :</strong>
            <ul>
                <li>Remplacez <code>token_bot_discord</code> par votre propre token bot Discord dans le fichier <code>config.py</code>.</li>
                <li>Lancez l'application :</li>
            </ul>
        </li>
    </ul>

    <pre class="command"><code>py main.py</code></pre>

    <h2>Licence</h2>

    <p>ISC</p>
</body>
</html>
