# -*- coding: utf-8 -*-

from odoo import models, fields, api

# ========== GROUPE D'ENTREPRISES ==========
class EntrepriseGroupe(models.Model):
    _name = 'entreprise.groupe'
    _description = "Groupe d'Entreprises"
    _rec_name = 'nom'

    nom = fields.Char(string="Nom du groupe", required=True)
    siren = fields.Char(string="SIREN")
    siege_social = fields.Char(string="Siège Social")
    
    # Relations inverses
    entreprise_ids = fields.One2many('entreprise.entreprise', 'groupe_id', string="Entreprises du groupe")
    entreprise_count = fields.Integer(string="Nombre d'entreprises", compute='_compute_entreprise_count', store=True)

    @api.depends('entreprise_ids')
    def _compute_entreprise_count(self):
        for record in self:
            record.entreprise_count = len(record.entreprise_ids)


# ========== ENTREPRISE ==========
class EntrepriseEntreprise(models.Model):
    _name = 'entreprise.entreprise'
    _description = 'Entreprise'
    _rec_name = 'nom'

    nom = fields.Char(string="Nom de l'entreprise", required=True)
    siret = fields.Char(string="SIRET")
    adresse = fields.Text(string="Adresse")
    telephone = fields.Char(string="Téléphone")
    email = fields.Char(string="Email")
    
    # Relation avec le groupe
    groupe_id = fields.Many2one('entreprise.groupe', string="Groupe d'appartenance")
    
    # Relations inverses
    personne_ids = fields.One2many('school.personne', 'entreprise_id', string="Salariés")
    
    salarie_count = fields.Integer(string="Nombre de salariés", compute='_compute_salarie_count', store=True)

    @api.depends('personne_ids')
    def _compute_salarie_count(self):
        for record in self:
            record.salarie_count = len(record.personne_ids)
