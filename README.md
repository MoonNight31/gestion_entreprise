# Module Gestion Entreprise

Module Odoo 17 pour la gestion des entreprises et des relations employeur-salarié.

## 🎯 Fonctionnalités

- **Groupes d'Entreprises** : Gestion des holdings et groupes
- **Contacts Entreprise** : Gestion des sociétés avec extension res.partner
- **Salariés** : Rattachement des employés aux entreprises
- **Statistiques** : Compteurs automatiques de salariés et entreprises

## 📋 Architecture

### Extension de `res.partner` (Entreprises et Salariés)
- `groupe_id` : Many2one vers entreprise.groupe
- `siret` : SIRET de l'entreprise
- `employer_partner_id` : Many2one vers l'entreprise employeur (pour les salariés)
- `employee_ids` : One2many vers les salariés
- `salarie_count` : Compteur calculé du nombre de salariés

### Modèle `entreprise.groupe`
- `nom` : Nom du groupe
- `siren` : SIREN du groupe
- `siege_social` : Adresse du siège
- `entreprise_ids` : One2many vers les entreprises
- `entreprise_count` : Compteur calculé

## 🎨 Vues dédiées

- **Contacts Entreprise** : Vue pour les sociétés (`is_company=True`)
- **Salariés** : Vue pour les employés avec entreprise employeur
- **Groupes** : Vue avec liste des entreprises membres

## 🔄 Intégration

Ce module étend les vues de `gestion_ecole` pour ajouter :
- Champ `employer_partner_id` dans les vues personnes
- Onglet Salariés dans les vues entreprises

## 📦 Installation

1. **Prérequis** : Module `gestion_ecole` installé
2. Placer le module dans le dossier addons
3. Redémarrer Odoo : `sudo systemctl restart odoo`
4. Installer "Gestion Entreprise"

## 🔗 Dépendances

- `base` (module natif Odoo)
- `gestion_ecole` (module personnalisé)

## 👨‍💻 Auteur

MoonDev - 2025
