# 📍 API d'Adresses avec Évaluation des Risques Environnementaux

Ce projet Django expose une API REST permettant de rechercher des adresses et d'afficher les risques environnementaux associés, en interrogeant l'API publique GeoRisques.

## 🚀 Fonctionnalités

- Recherche d'une adresse via une requête texte (`q`) avec suggestion géolocalisée.
- Récupération des coordonnées GPS (latitude / longitude) de l'adresse.
- Envoi d'une requête à l'API GeoRisques pour évaluer les risques à cette position.
- Enregistrement et accès aux résultats via endpoints REST.
- Gestion d'erreurs robustes et validation des entrées utilisateur.


## 🏁 Installation

1. **Cloner le projet**
   ```bash
   git clone https://github.com/hamid2amrani/api-adresses.git
   cd api-adresses
   ```

2. **Créer un environnement virtuel**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données**
   Par défaut, SQLite est utilisé. Si vous utilisez PostgreSQL :
   - Modifier `settings.py` avec vos identifiants
   - Lancer les migrations :
     ```bash
     python manage.py migrate
     ```

5. **Lancer le serveur**
   ```bash
   python manage.py runserver
   ```


## lancement du docker compose

1. **Commandes nécéssaire**
    
    ```bash
    docker compose build
    docker compose up
    
    ```
    
2. **Variables d'environnement**
  - Django :
        
        ```
        DATABASE_URL=sqlite:////data/db.sqlite
        
        ```


## 📡 API Endpoints

### 🔍 POST `/api/addresses/`

Recherche d'une adresse à partir d'une chaîne de texte.

#### Requête :
```json
{
  "q": "10 rue de Rivoli, Paris"
}
```

#### Réponse (succès) :
```json
{
  "address": "10 Rue de Rivoli, 75004 Paris",
  "latitude": 48.8556,
  "longitude": 2.3609,
  "risks": {
    "inondation": true,
    "retrait-gonflement": false,
    ...
  }
}
```

#### Réponse (erreur) :
```json
{
  "error": "Champ 'q' requis."
}
```

### 📥 GET `/api/addresses/<id>/risks/`

Affiche les résultats de risques associés à une adresse déjà enregistrée.

#### Réponse :
```json
{
  "address": "10 Rue de Rivoli, 75004 Paris",
  "risks": {
    "inondation": true,
    "radon": false
  }
}
```

## 🧪 Lancer les tests

```bash
python manage.py test
```

## 🔍 Exemple de test

```python
def test_empty_q_returns_400(self):
    response = self.client.post("/api/addresses/", {"q": ""}, format='json')
    self.assertEqual(response.status_code, 400)
    self.assertIn("error", response.json())
```

## 📄 À propos de l'API GeoRisques

Nous interrogeons l'API :
```
https://www.georisques.gouv.fr/api/v1/resultats_rapport_risque?latlon=<lon>,<lat>
```

- Plus d'infos : [Documentation officielle GeoRisques](https://www.georisques.gouv.fr)
- Attention : cette API peut retourner 404 si aucun risque n'est associé à la localisation.

## 🧑‍💻 Auteur

Projet développé par **Hamid Amrani**.
