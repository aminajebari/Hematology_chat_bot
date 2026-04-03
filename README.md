# Hematology AI

Projet de démonstration pour la recherche et la génération assistée par récupération (RAG) appliquée à des notes d'hématologie.

## Description

Ce dépôt contient des scripts simples pour ingérer des données textuelles médicales, construire/charger une base de vecteurs (Chroma), et effectuer des requêtes / génération de réponses.

## Contenu principal

- `app.py` : point d'entrée de l'application (si présent pour démarrage web ou CLI).
- `ingest.py` : script d'ingestion des fichiers depuis `data/` vers la base de vecteurs.
- `query.py` : script d'interrogation / interface de test pour la base de connaissances.
- `rag.py` : logique RAG (récupération + génération), utilitaires d'assemblage de prompts.
- `data/` : corpus source (`hematology_notes.txt`, `hematology_qa.csv`, `training_set.csv`).
- `vector_db/` : stockage Chroma (ex. `chroma.sqlite3` et sous-dossiers de vecteurs).

## Prérequis

- Python 3.10+ recommandé
- Virtualenv ou venv
- Bibliothèques usuelles : `chromadb`, `openai` (ou autre fournisseur LLM), `langchain`, `pandas`, `tqdm`.

Si le fichier `requirements.txt` est fourni, installez-le :

```powershell
python -m venv .venv
# Windows PowerShell
& .\.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
```

Sinon, installez manuellement les dépendances principales :

```bash
pip install chromadb openai langchain pandas tiktoken tqdm
```

## Utilisation

1. Préparer les données dans le dossier `data/` (fichiers texte ou CSV).
2. Construire/mettre à jour la base de vecteurs :

```bash
python ingest.py
```

3. Interroger la base / tester RAG :

```bash
python query.py
```

4. Lancer l'application (si `app.py` implémente un serveur ou UI) :

```bash
python app.py
```

## Détails

- La base de vecteurs Chroma est stockée dans `vector_db/`.
- Adaptez les clés d'API (ex. OpenAI) via des variables d'environnement ou un fichier de configuration selon l'implémentation du projet.

## Dépannage

- Si l'ingestion échoue, vérifiez le format des fichiers dans `data/` et l'accès en écriture à `vector_db/`.
- Pour des erreurs liées aux clés d'API, exportez correctement la variable (ex. `OPENAI_API_KEY`).

## Contribuer

Signalez des problèmes via les issues et soumettez des pull requests pour des améliorations (ingestion, qualité des prompts, sécurité des données).

## License

À renseigner selon vos besoins (ex. MIT, Apache-2.0).

---

Si vous voulez, je peux :
- générer un `requirements.txt` précis en scannant les imports,
- ajouter des exemples d'usage détaillés ou des extraits de commandes pour Windows.
