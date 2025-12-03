# Module Gestion Entreprise

Module Odoo pour la gestion des groupes d'entreprises, des entreprises et de leurs salariés.

## Description

Ce module permet de gérer :
- **Groupes d'entreprises** : Regroupement de plusieurs entreprises sous une même entité (SIREN, siège social)
- **Entreprises** : Informations détaillées sur chaque entreprise (SIRET, adresse, contacts)
- **Salariés** : Liaison avec le module `gestion_ecole` pour gérer les personnes rattachées aux entreprises
- **Contrats** : Suivi des contrats associés à chaque entreprise

## Fonctionnalités

### Groupes d'Entreprises
- Gestion du nom, SIREN et siège social
- Vue d'ensemble des entreprises du groupe
- Compteur automatique du nombre d'entreprises

### Entreprises
- Informations complètes (nom, SIRET, adresse, téléphone, email)
- Rattachement à un groupe d'entreprises (optionnel)
- Liste des salariés avec leurs informations de contact
- Liste des contrats en cours
- Compteurs automatiques (nombre de salariés, nombre de contrats)

## Dépendances

- `base` : Module de base Odoo
- `gestion_ecole` : Module de gestion des personnes (étudiants, tuteurs, etc.)

## Installation

1. Copiez le module dans le dossier `addons` de votre instance Odoo
2. Redémarrez le serveur Odoo
3. Activez le mode développeur
4. Allez dans Apps et cliquez sur "Mettre à jour la liste des applications"
5. Recherchez "Gestion Entreprise" et installez le module

## Structure du Module

```
gestion_entreprise/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   ├── __init__.py
│   └── models.py
├── security/
│   └── ir.model.access.csv
└── views/
    └── views.xml
```

## Modèles de données

### `entreprise.groupe`
| Champ | Type | Description |
|-------|------|-------------|
| nom | Char | Nom du groupe (requis) |
| siren | Char | Numéro SIREN |
| siege_social | Char | Adresse du siège social |
| entreprise_ids | One2many | Liste des entreprises du groupe |
| entreprise_count | Integer | Nombre d'entreprises (calculé) |

### `entreprise.entreprise`
| Champ | Type | Description |
|-------|------|-------------|
| nom | Char | Nom de l'entreprise (requis) |
| siret | Char | Numéro SIRET |
| adresse | Text | Adresse complète |
| telephone | Char | Numéro de téléphone |
| email | Char | Adresse email |
| groupe_id | Many2one | Groupe d'appartenance |
| personne_ids | One2many | Liste des salariés |
| contrat_ids | One2many | Liste des contrats |
| salarie_count | Integer | Nombre de salariés (calculé) |
| contrat_count | Integer | Nombre de contrats (calculé) |

## Utilisation

1. Accédez au menu "Gestion Entreprise" depuis la barre de navigation
2. Créez d'abord vos groupes d'entreprises (si nécessaire)
3. Créez vos entreprises et rattachez-les à un groupe
4. Les salariés et contrats seront automatiquement liés depuis le module `gestion_ecole`

## Sécurité

Les droits d'accès sont configurés pour le groupe `base.group_user` (utilisateurs internes) avec tous les droits (lecture, écriture, création, suppression).

## Auteur

**MoonDev**

## Version

1.0 - Version initiale

## Licence

Propriétaire
